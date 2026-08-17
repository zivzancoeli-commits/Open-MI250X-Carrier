#!/usr/bin/env python3
"""HEAD/GET a small URL set. Log code + content-type. Do not treat 403 as dead."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path

URLS = [
    ("scs_mild_steel", "https://sendcutsend.com/materials/mild-steel/"),
    ("scs_hardware", "https://sendcutsend.com/services/hardware/"),
    ("scs_home", "https://sendcutsend.com/"),
    ("scs_guidelines", "https://sendcutsend.com/guidelines/laser-cutting/"),
    ("farnell_2189101115_pdf", "https://www.farnell.com/datasheets/3919676.pdf"),
    ("newegg_x11dph_t", "https://www.newegg.com/supermicro-mbd-x11dph-t-o-2nd-generation-intel-xeon-scalable-processors-intel-xeon-scalable-proces/p/1B4-005W-001B0"),
    ("ebay_snphvy68c", "https://www.ebay.co.uk/p/24064262136"),
    ("supermicro_dram", "https://store.supermicro.com/us_en/32gb-ddr4-2933-mem-dr432l-sl01-er29.html"),
    ("noctua_dx3647", "https://noctua.at/en/nh-u14s-dx-3647"),
    ("itcreations_d3000", "https://www.itcreations.com/product/132053"),
    ("amd_mi250x", "https://www.amd.com/en/products/accelerators/instinct/mi200/mi250x.html"),
    ("pcbway_home", "https://www.pcbway.com/"),
]


def probe(url: str) -> dict:
    cmd = [
        "curl",
        "-sS",
        "-L",
        "--max-time",
        "25",
        "-o",
        "/dev/null",
        "-D",
        "-",
        "-A",
        "Mozilla/5.0 (compatible; OpenMI250XCarrier/1.0)",
        url,
    ]
    p = subprocess.run(cmd, capture_output=True, text=True)
    headers = p.stdout
    code = None
    ctype = ""
    for line in headers.splitlines():
        if line.upper().startswith("HTTP/"):
            parts = line.split()
            if len(parts) >= 2 and parts[1].isdigit():
                code = int(parts[1])
        if line.lower().startswith("content-type:"):
            ctype = line.split(":", 1)[1].strip()
    return {
        "url": url,
        "http": code,
        "content_type": ctype,
        "curl_err": (p.stderr or "").strip()[:300],
        "ok_process": p.returncode == 0,
    }


def main() -> None:
    out_dir = Path(__file__).resolve().parent.parent / "docs"
    rows = []
    md = ["# URL log — 2026-08-17", "", "HEAD/GET via curl -L. **403/429 ≠ dead listing.**", ""]
    md.append("| Key | HTTP | Type | URL |")
    md.append("|---|---|---|---|")
    for key, url in URLS:
        rec = probe(url)
        rec["key"] = key
        rows.append(rec)
        md.append(f"| `{key}` | {rec['http']} | {rec['content_type'][:40]} | {url} |")
        print(f"{rec['http']}\t{key}\t{url}")
    md.append("")
    md.append("PCBWay home is logged only as a reminder: **do not send in-repo KiCad there.**")
    md.append("")
    (out_dir / "URL_LOG.md").write_text("\n".join(md))
    (out_dir / "url_log.json").write_text(json.dumps(rows, indent=2) + "\n")


if __name__ == "__main__":
    main()
