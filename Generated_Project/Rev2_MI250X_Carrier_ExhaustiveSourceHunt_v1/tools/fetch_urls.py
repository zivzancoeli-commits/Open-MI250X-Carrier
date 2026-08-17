#!/usr/bin/env python3
"""HTTP fetch logger: records status, content-type, size, sha256, dest path."""
from __future__ import annotations

import hashlib
import os
import ssl
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone

UA = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Open-MI250X-Carrier-research"
)
TIMEOUT = 45
DL = os.path.join(os.path.dirname(__file__), "..", "docs", "downloads")
LOG = os.path.join(os.path.dirname(__file__), "..", "docs", "url_log", "fetch.log")
os.makedirs(DL, exist_ok=True)
os.makedirs(os.path.dirname(LOG), exist_ok=True)

CTX = ssl.create_default_context()


def fetch(url: str, dest_name: str | None = None, method: str = "GET") -> dict:
    dest = os.path.join(DL, dest_name) if dest_name else None
    req = urllib.request.Request(
        url,
        method=method,
        headers={
            "User-Agent": UA,
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.9",
        },
    )
    t0 = time.time()
    status = 0
    ctype = ""
    nbytes = 0
    err = ""
    sha = ""
    final = url
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT, context=CTX) as resp:
            status = getattr(resp, "status", 200) or 200
            ctype = resp.headers.get("Content-Type", "")
            final = resp.geturl()
            data = resp.read()
            nbytes = len(data)
            sha = hashlib.sha256(data).hexdigest()
            if dest:
                with open(dest, "wb") as f:
                    f.write(data)
    except urllib.error.HTTPError as e:
        status = e.code
        ctype = e.headers.get("Content-Type", "") if e.headers else ""
        err = str(e.reason)
        try:
            data = e.read()
            nbytes = len(data)
            if dest and data:
                with open(dest, "wb") as f:
                    f.write(data)
        except Exception:
            pass
    except Exception as e:
        status = 0
        err = f"{type(e).__name__}: {e}"
    elapsed = time.time() - t0
    rec = {
        "ts": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "status": status,
        "ctype": ctype,
        "nbytes": nbytes,
        "elapsed_s": round(elapsed, 2),
        "sha256": sha[:16] if sha else "",
        "dest": dest_name or "",
        "final": final,
        "err": err,
        "url": url,
    }
    line = (
        f"{rec['status']}|{rec['ctype']}|{rec['nbytes']}|{rec['elapsed_s']}s|"
        f"{rec['sha256']}|{rec['err']}|{url}"
        + (f" -> {dest_name}" if dest_name else "")
        + (f" final={final}" if final != url else "")
    )
    print(line, flush=True)
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(line + "\n")
    return rec


def main() -> int:
    urls = []
    for raw in sys.argv[1:]:
        if "|" in raw:
            u, n = raw.split("|", 1)
            urls.append((u, n))
        else:
            urls.append((raw, None))
    if not urls:
        return 0
    for u, n in urls:
        fetch(u, n)
        time.sleep(0.15)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
