#!/usr/bin/env python3
"""Find out which Z.ai models a plan actually covers, and what a minimal call costs.

This is the one executable artifact in the bundle, and it exists because `rungs.md` is the one
file allowed to name a model. A rung mapping written from a vendor's pricing page is a guess.
This turns it into a measurement that can be re-run and dated.

Run it from a machine with egress to `api.z.ai`. Many agent sessions run behind an allowlist
that does not include it, in which case the call is refused before it leaves the box; that is
a network fact about where you ran it, not a fact about the plan.

**The key is read from the environment and never printed, never written, never passed as an
argument.** An argument lands in shell history, which is the same leak one step removed.
`describe_key` reports the key's shape without ever emitting a character of it, which is what
catches the common failure: a whole shell assignment pasted into a masked prompt.

    export ZAI_API_KEY=...          # not typed into a chat window, not committed
    python3 tools/probe_models.py
    python3 tools/probe_models.py --models GLM-4.6,Web-Reader
    python3 tools/probe_models.py --surface anthropic   # the coding plan
    python3 tools/probe_models.py --base https://open.bigmodel.cn/api/paas/v4

Adapting it to another vendor is an edit to SURFACES and DEFAULT_MODELS and nothing else.

What it answers, per model: does the plan cover it, what does the endpoint return, how long
does it take, and how many tokens does the smallest possible exchange actually bill. That last
column is the point. The architecture's premise is that capability is spent per decision and
cost per token, and none of it has been measured.

Standard library only. A check that needs an install is a check someone skips.

Exit codes: 0 at least one model answered, 1 none did, 2 configuration.
"""
import argparse
import base64
import hashlib
import hmac
import json
import os
import ssl
import sys
import time
import urllib.error
import urllib.request

# Two products, not two hostnames. The open platform is pay-as-you-go and bills against a
# balance. The coding plan is Anthropic-shaped and carries its own quota. Same key, same model
# names, different meter, and the advanced models answer only on the second. A 429 saying
# "insufficient balance" on one surface says nothing about the other.
SURFACES = {
    "openai": {
        "base": "https://api.z.ai/api/paas/v4",
        "path": "/chat/completions",
        "auth": lambda key: {"Authorization": f"Bearer {key}"},
        "body": lambda model: {"model": model, "max_tokens": 8, "temperature": 0,
                               "messages": [{"role": "user", "content": PROMPT}]},
    },
    "anthropic": {
        "base": "https://api.z.ai/api/anthropic",
        "path": "/v1/messages",
        "auth": lambda key: {"x-api-key": key, "anthropic-version": "2023-06-01"},
        "body": lambda model: {"model": model, "max_tokens": 8,
                               "messages": [{"role": "user", "content": PROMPT}]},
    },
}
DEFAULT_BASE = SURFACES["openai"]["base"]
BASES = [SURFACES["openai"]["base"], "https://open.bigmodel.cn/api/paas/v4"]

# The rungs this architecture leans on, cheapest first. Order is deliberate: if the fetch
# rung alone works, that is already the largest saving in the architecture.
DEFAULT_MODELS = [
    # fetch: retrieval that returns facts and makes no decisions
    "Web-Reader", "Search-Prime", "Search-Prime-Claude",
    # build: executes a complete specification
    "GLM-4.5-Flash", "GLM-4.5-Air", "GLM-4.6", "GLM-4.7-Flash",
    # judgment: decides, emits little
    "GLM-4.7", "GLM-5", "GLM-5.2",
]

PROMPT = "Reply with the single word: ok"


def zhipu_jwt(key):
    """Sign an id.secret key as a JWT, which is how this vendor's platform has historically
    authenticated. Returns None when the key is not in id.secret shape.

    This is a hypothesis the probe tests, not a documented fact about the current API. If the
    `jwt` auth style is the one that answers, that is the finding.
    """
    if key.count(".") != 1:
        return None
    kid, secret = key.split(".", 1)
    if not kid or not secret:
        return None
    now_ms = int(time.time() * 1000)
    def seg(obj):
        raw = json.dumps(obj, separators=(",", ":")).encode()
        return base64.urlsafe_b64encode(raw).rstrip(b"=")
    signing_input = seg({"alg": "HS256", "sign_type": "SIGN"}) + b"." + seg(
        {"api_key": kid, "exp": now_ms + 3600 * 1000, "timestamp": now_ms})
    sig = hmac.new(secret.encode(), signing_input, hashlib.sha256).digest()
    return (signing_input + b"." + base64.urlsafe_b64encode(sig).rstrip(b"=")).decode()


def auth_headers(style, key):
    """The three ways this key could plausibly be presented. None means not applicable."""
    if style == "bearer":
        return {"Authorization": f"Bearer {key}"}
    if style == "raw":
        return {"Authorization": key}
    if style == "jwt":
        tok = zhipu_jwt(key)
        return {"Authorization": f"Bearer {tok}"} if tok else None
    raise ValueError(style)


def describe_key(key):
    """Say what shape the key is without printing any of it."""
    classes = []
    if any(c.isupper() for c in key): classes.append("upper")
    if any(c.islower() for c in key): classes.append("lower")
    if any(c.isdigit() for c in key): classes.append("digit")
    if any(c in "-_" for c in key): classes.append("dash/underscore")
    other = sorted({c for c in key if not (c.isalnum() or c in "-_.")})
    parts = key.split(".")
    shape = (f"{len(parts)} dot-separated parts of lengths {[len(x) for x in parts]}"
             if len(parts) > 1 else "no dot")
    return (f"{len(key)} chars, {shape}, contains {'+'.join(classes) or 'nothing recognised'}"
            + (f", unexpected characters {other}" if other else ""))


def call(base, model, key, timeout, style="bearer", surface="openai"):
    """One minimal exchange. Returns (verdict, detail, seconds, tokens)."""
    spec = SURFACES[surface]
    body = json.dumps(spec["body"](model)).encode()
    if surface == "openai":
        hdrs = auth_headers(style, key)
        if hdrs is None:
            return "n/a", "key is not in id.secret shape, jwt not applicable", 0.0, None
    else:
        hdrs = dict(spec["auth"](key))
    hdrs["Content-Type"] = "application/json"
    req = urllib.request.Request(
        f"{base}{spec['path']}", data=body, method="POST", headers=hdrs)
    start = time.monotonic()
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=ssl.create_default_context()) as r:
            payload = json.load(r)
        elapsed = time.monotonic() - start
        usage = payload.get("usage") or {}
        try:
            if surface == "openai":
                total = usage.get("total_tokens")
                text = payload["choices"][0]["message"]["content"].strip()[:24]
            else:
                inp, out = usage.get("input_tokens"), usage.get("output_tokens")
                total = (inp + out) if (inp is not None and out is not None) else None
                text = "".join(b.get("text", "") for b in payload.get("content", [])
                               if b.get("type") == "text").strip()[:24]
        except (KeyError, IndexError, TypeError, AttributeError):
            total, text = None, "(unexpected response shape)"
        return "ok", text, elapsed, total
    except urllib.error.HTTPError as e:
        elapsed = time.monotonic() - start
        raw = e.read(2000).decode("utf-8", "replace")
        msg = raw
        try:
            err = json.loads(raw)
            # Providers disagree on shape. Try the common ones, then fall back to the body,
            # because an empty detail column is worse than an ugly one.
            for path in (("error", "message"), ("error", "msg"), ("msg",), ("message",)):
                cur = err
                for k in path:
                    cur = cur.get(k) if isinstance(cur, dict) else None
                if isinstance(cur, str) and cur.strip():
                    msg = cur
                    break
        except json.JSONDecodeError:
            pass
        if not msg.strip():
            msg = f"(empty body, {len(raw)} bytes)"
        # 400 from this vendor is usually a rejected key rather than a bad request.
        # 404 on a name that exists in the console usually means a different endpoint:
        # search and reader products commonly do not sit on chat/completions.
        verdict = {400: "rejected", 401: "auth", 403: "not on plan",
                   404: "wrong endpoint", 429: "rate limited",
                   # A 500 against a valid key on a model the plan reaches usually means the
                   # product is not chat-shaped: search and retrieval endpoints take a
                   # different body and error inside rather than rejecting cleanly.
                   500: "not chat-shaped"}.get(e.code, f"http {e.code}")
        # This vendor returns 429 for an unfunded model as well as for throttling, and the two
        # mean opposite things: one clears by waiting, the other never does.
        if e.code == 429 and ("balance" in msg.lower() or "recharge" in msg.lower()):
            verdict = "no balance"
        return verdict, " ".join(msg.split())[:120], elapsed, None
    except urllib.error.URLError as e:
        return "unreachable", f"{e.reason}", time.monotonic() - start, None
    except (TimeoutError, OSError) as e:
        return "unreachable", str(e)[:90], time.monotonic() - start, None


def diagnose(key, timeout):
    """A 401 with a plausible key is a question, not an answer. Three things could be wrong and
    only one of them is 'the key is bad', so test all three rather than assuming."""
    print("\n" + "=" * 78)
    print("AUTH SWEEP")
    print(f"key shape: {describe_key(key)}\n")
    print(f"{'surface':<38} {'auth style':<11} {'verdict':<13} detail")
    print("-" * 78)
    probe_model = "GLM-4.5-Flash"
    hits = []
    attempts = [(b, s, "openai") for b in BASES for s in ("bearer", "raw", "jwt")]
    attempts.append((SURFACES["anthropic"]["base"], "bearer", "anthropic"))
    for base, style, surface in attempts:
        verdict, detail, _secs, _tok = call(base, probe_model, key, timeout, style, surface)
        host = base.split("//", 1)[1].split("/", 1)[0]
        label = style if surface == "openai" else f"{surface}/x-api-key"
        print(f"{host:<38} {label:<11} {verdict:<13} {detail[:60]}")
        if verdict not in ("auth", "rejected", "unreachable", "n/a"):
            hits.append((base, style, verdict))
    print()
    if hits:
        base, style, verdict = hits[0]
        print(f"Something other than an auth failure came back from {base}")
        print(f"with auth style '{style}' ({verdict}). That combination is the one to use:")
        print(f"    python3 probe_zai_models.py --base {base}")
        if style != "bearer":
            print(f"    (and the '{style}' auth style, which this script currently hardcodes")
            print("     for the main table. Tell Claude which style answered.)")
    else:
        print("Every surface and every auth style refused. That narrows it to the key itself:")
        print("  * issued on a different surface than either of the two tried")
        print("  * not yet activated, or its plan not yet started")
        print("  * copied from a console field that truncates or adds an invisible character")
        print("Check the key's shape line above against what the console shows it should be.")
    print("=" * 78)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--surface", choices=sorted(SURFACES), default="openai",
                    help="which product to bill against. 'openai' is the pay-as-you-go open "
                         "platform; 'anthropic' is the coding plan, which carries its own quota "
                         "and is where the advanced models answer. Default openai")
    ap.add_argument("--base", help="override the surface's default API base")
    ap.add_argument("--models", help="comma-separated. Default is the rung shortlist")
    ap.add_argument("--timeout", type=float, default=45.0)
    ap.add_argument("--diagnose", action="store_true",
                    help="on auth failure, sweep both API surfaces and all three auth styles "
                         "against one cheap model, and report the key's shape")
    args = ap.parse_args(argv)

    key = os.environ.get("ZAI_API_KEY")
    if not key:
        print("CONFIG ERROR ZAI_API_KEY is not set in this shell.")
        print("  export ZAI_API_KEY=...   then run this again.")
        print("  Do not pass it as an argument: it would land in shell history.")
        return 2

    # A key that is obviously wrong should cost zero calls, not ten. The first run of this
    # script spent ten requests proving that a one-character key is a one-character key.
    # A key that carries shell syntax is a pasted command, not a key. This costs zero calls
    # and is the failure that actually happened: an assignment line pasted into a prompt,
    # which then authenticated as itself, forever, against every surface and auth style.
    shell = sorted({c for c in key if c in ' \t"\'$=`;|'})
    if shell:
        print(f"CONFIG ERROR ZAI_API_KEY contains {shell}, which no API key does.")
        print("  Those are shell characters. The value is almost certainly a whole command")
        print("  rather than the key inside it. Paste only the key: the id.secret string on")
        print("  its own, no $env:, no equals sign, no surrounding quotes.")
        print("")
        print('      $env:ZAI_API_KEY = Read-Host "Z.ai key"')
        print("      # at the prompt, paste ONLY the key, then Enter")
        print("")
        print("  Verify with:  $env:ZAI_API_KEY.Length")
        print(f"  Current value: {describe_key(key)}")
        return 2

    stripped = key.strip()
    if len(stripped) < 16 or stripped != key:
        print(f"CONFIG ERROR ZAI_API_KEY is {len(key)} characters"
              f"{' and has surrounding whitespace' if stripped != key else ''}.")
        print("  That is not a usable key. The usual cause on Windows is a masked prompt")
        print("  that did not accept the paste. Set it with a plain Read-Host instead:")
        print("")
        print('      $env:ZAI_API_KEY = Read-Host "Z.ai key"')
        print("")
        print("  The value is not written to PowerShell history; only the command line is.")
        print("  To keep it masked, convert the SecureString properly:")
        print("")
        print('      $s = Read-Host "Z.ai key" -AsSecureString')
        print("      $env:ZAI_API_KEY = " +
              "[System.Net.NetworkCredential]::new('', $s).Password")
        print("")
        print("  Then check it took, without printing it:  $env:ZAI_API_KEY.Length")
        return 2

    base = args.base or SURFACES[args.surface]["base"]
    models = [m.strip() for m in args.models.split(",")] if args.models else DEFAULT_MODELS
    print(f"surface {args.surface}   base {base}{SURFACES[args.surface]['path']}")
    print(f"key present, {len(key)} chars, not shown\n")
    print(f"{'model':<21} {'verdict':<13} {'secs':>5} {'tok':>5}  detail")
    print("-" * 78)

    answered = 0
    for m in models:
        verdict, detail, secs, tokens = call(base, m, key, args.timeout,
                                             surface=args.surface)
        # 529 is this vendor saying "overloaded, try later". One retry confirms whether it is
        # transient. One, not a loop: a second failure is a real answer, not bad luck.
        if verdict == "http 529":
            time.sleep(2)
            verdict, detail, secs, tokens = call(base, m, key, args.timeout,
                                                 surface=args.surface)
            if verdict == "http 529":
                verdict, detail = "overloaded", "still overloaded after one retry"
        if verdict == "ok":
            answered += 1
        tok = str(tokens) if tokens is not None else "-"
        head, tail = detail[:62].rstrip(), detail[62:].strip()
        print(f"{m:<21} {verdict:<13} {secs:>5.2f} {tok:>5}  {head}")
        if tail:
            print(f"{'':<47}{tail}")

    print()
    if not answered:
        print("No model answered. Read the pattern rather than any single row:")
        print("  every row unreachable  ->  network or egress policy, not the plan")
        print("  every row rejected/auth ->  see the sweep below")
        print("  every row not on plan  ->  the key is valid and the plan covers none of these")
        print("  a mix                  ->  the key works; the verdicts are real answers")
        diagnose(key, args.timeout)
        return 1
    print(f"{answered} of {len(models)} answered. Record the result in registry.md, dated,")
    print("and put the covered names into the rung-to-model mapping rather than into contracts.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
