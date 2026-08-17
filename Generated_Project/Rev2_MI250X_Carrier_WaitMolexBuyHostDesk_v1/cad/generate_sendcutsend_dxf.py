#!/usr/bin/env python3
"""Generate SendCutSend-ready 1:1 mm DXFs for chassis sheet (not OAM pins).

Units: millimetres ($INSUNITS=4). Closed LWPOLYLINE outlines + CIRCLE holes.
No text (SendCutSend wants outlines only). Orientation: 6x6 mm notch at 0,0.

Does NOT contain:
  - OAM M3.5 NPTH pattern
  - Molex 218910-1115 pads
  - SuperMicro/ATX motherboard standoff holes (not OCR'd; drill after board in hand)
  - Fan / I/O / GPU-duct cutouts (height and I/O shield Unknown)
"""

from __future__ import annotations

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / "dxf"
NOTCH = 6.0  # mm, lower-left orientation clip
FLANGE_HOLE_D = 4.5  # mm; SendCutSend resizes if you pick M4 PEM in the app
EDGE = 15.0  # mm, hole center to outer edge (conservative vs typical M4 K)


def dxf_header() -> str:
    return "\n".join(
        [
            "0",
            "SECTION",
            "2",
            "HEADER",
            "9",
            "$ACADVER",
            "1",
            "AC1009",
            "9",
            "$INSUNITS",
            "70",
            "4",
            "9",
            "$MEASUREMENT",
            "70",
            "1",
            "0",
            "ENDSEC",
            "0",
            "SECTION",
            "2",
            "TABLES",
            "0",
            "TABLE",
            "2",
            "LAYER",
            "70",
            "1",
            "0",
            "LAYER",
            "2",
            "0",
            "70",
            "0",
            "62",
            "7",
            "6",
            "CONTINUOUS",
            "0",
            "ENDTAB",
            "0",
            "ENDSEC",
            "0",
            "SECTION",
            "2",
            "ENTITIES",
        ]
    )


def dxf_footer() -> str:
    return "\n".join(["0", "ENDSEC", "0", "EOF", ""])


def closed_poly(pts: list[tuple[float, float]]) -> str:
    """R12 POLYLINE (widely accepted by SendCutSend DXF parsers)."""
    lines = [
        "0",
        "POLYLINE",
        "8",
        "0",
        "66",
        "1",
        "70",
        "1",
    ]
    for x, y in pts:
        lines += [
            "0",
            "VERTEX",
            "8",
            "0",
            "10",
            f"{x:.4f}",
            "20",
            f"{y:.4f}",
            "30",
            "0.0",
        ]
    lines += ["0", "SEQEND", "8", "0"]
    return "\n".join(lines)


def circle(cx: float, cy: float, d: float) -> str:
    r = d / 2.0
    return "\n".join(
        [
            "0",
            "CIRCLE",
            "8",
            "0",
            "10",
            f"{cx:.4f}",
            "20",
            f"{cy:.4f}",
            "30",
            "0.0",
            "40",
            f"{r:.4f}",
        ]
    )


def notched_rect(w: float, h: float, notch: float = NOTCH) -> list[tuple[float, float]]:
    """CCW outline with a square clip at (0,0) so the part is not rotationally ambiguous."""
    return [
        (notch, 0.0),
        (w, 0.0),
        (w, h),
        (0.0, h),
        (0.0, notch),
        (notch, notch),
    ]


def flange_holes(w: float, h: float, extra: list[tuple[float, float]] | None = None):
    pts = [
        (EDGE, EDGE),
        (w - EDGE, EDGE),
        (w - EDGE, h - EDGE),
        (EDGE, h - EDGE),
    ]
    if w >= 300:
        pts.append((w / 2.0, EDGE))
        pts.append((w / 2.0, h - EDGE))
    if h >= 300:
        pts.append((EDGE, h / 2.0))
        pts.append((w - EDGE, h / 2.0))
    if extra:
        pts.extend(extra)
    # unique
    seen = set()
    out = []
    for p in pts:
        key = (round(p[0], 3), round(p[1], 3))
        if key not in seen:
            seen.add(key)
            out.append(p)
    return out


def write_dxf(name: str, w: float, h: float, holes: list[tuple[float, float]], meta: dict) -> dict:
    ents = [closed_poly(notched_rect(w, h))]
    for x, y in holes:
        ents.append(circle(x, y, FLANGE_HOLE_D))
    (OUT / name).write_text(dxf_header() + "\n" + "\n".join(ents) + "\n" + dxf_footer())
    rec = {
        "file": name,
        "outer_mm": [w, h],
        "units": "mm",
        "orientation_notch_mm": NOTCH,
        "flange_hole_d_mm": FLANGE_HOLE_D,
        "flange_holes_xy_mm": [[round(x, 3), round(y, 3)] for x, y in holes],
        **meta,
    }
    return rec


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    parts = []

    # 1. Host tray — X11DPH-T 330.2 x 304.8 mm Verified + 15 mm each side Planning.
    w, h = 360.2, 334.8
    parts.append(
        write_dxf(
            "01_host_tray_x11dph_t.dxf",
            w,
            h,
            flange_holes(w, h),
            {
                "qty": 1,
                "material": "SendCutSend A1008 mild steel 0.059 in (1.50 mm) — nearest 16 ga",
                "verified_payload_mm": [330.2, 304.8],
                "verified_source": "SuperMicro X11DPH-T 13 in x 12 in (330.2 mm x 304.8 mm)",
                "do_not": "No motherboard standoff holes. ATX Figure 3 millimetres not extracted; SuperMicro extra E-ATX holes Unknown. Drill after the board is in hand.",
            },
        )
    )

    # 2. Desk tray — mATX class Inferred 244 x 244 + margin. B550M SKU not unique.
    w, h = 280.0, 280.0
    parts.append(
        write_dxf(
            "02_desk_tray_matx_class.dxf",
            w,
            h,
            flange_holes(w, h),
            {
                "qty": 1,
                "material": "SendCutSend A1008 mild steel 0.059 in (1.50 mm)",
                "inferred_payload_mm": [244.0, 244.0],
                "inferred_source": "Typical microATX; ASUS PRIME B550M-A AC was an example combo, not a locked unique board.",
                "do_not": "No mATX standoff holes. Drill after the desk board is in hand.",
            },
        )
    )

    # 3. Compute tray — 2-OAM KOZ 206 x 166 Verified tiling; planning carrier 246 x 206 + 20 mm flange.
    w, h = 286.0, 246.0
    parts.append(
        write_dxf(
            "03_compute_tray_2oam.dxf",
            w,
            h,
            flange_holes(w, h),
            {
                "qty": 1,
                "material": "SendCutSend A1008 mild steel 0.059 in (1.50 mm)",
                "verified_koz_2gpu_mm": [206.0, 166.0],
                "verified_source": "Two 103 x 166 mm OCP v1.5 KOZs tiled on module width",
                "planning_carrier_mm": [246.0, 206.0],
                "do_not": "No OAM M3.5 NPTH, no Molex land pattern, no 8-GPU 412x332 hole grid. SendCutSend has no M3.5 PEM.",
            },
        )
    )

    # 4. 12 V / 48 V divider — extra metal; trim after bay height is known.
    w, h = 500.0, 450.0
    parts.append(
        write_dxf(
            "04_divider_12v_48v.dxf",
            w,
            h,
            flange_holes(w, h),
            {
                "qty": 1,
                "material": "SendCutSend A1008 mild steel 0.059 in (1.50 mm)",
                "note": "Trim to welded-tube inside after height is known (GPU HS height Unknown; U14S is 165 mm).",
                "do_not": "Do not put P48V and ATX 12 V on the same side of this wall.",
            },
        )
    )

    # 5-7. Blank skins — no fan/I/O punches.
    for name, w, h, qty, note in [
        (
            "05_skin_compute_front.dxf",
            520.0,
            500.0,
            1,
            "Compute intake face. Cut-list A>=500, F TBD. No fan holes.",
        ),
        (
            "06_skin_compute_top.dxf",
            520.0,
            470.0,
            1,
            "Compute top/bottom candidate. Cut-list A>=500 x B>=450. Removable; not a cold plate.",
        ),
        (
            "07_skin_host_rear.dxf",
            420.0,
            500.0,
            1,
            "Host rear. Cut I/O after tracing the X11DPH-T shield (server I/O, not ATX 158.75 x 44.45 mm).",
        ),
    ]:
        parts.append(
            write_dxf(
                name,
                w,
                h,
                flange_holes(w, h),
                {
                    "qty": qty,
                    "material": "SendCutSend A1008 mild steel 0.059 in (1.50 mm)",
                    "note": note,
                    "do_not": "No GPU ducts, no ATX I/O aperture, no OAM holes.",
                },
            )
        )

    manifest = {
        "generator": "generate_sendcutsend_dxf.py",
        "vendor": "https://sendcutsend.com/",
        "upload": "https://sendcutsend.com/  (DXF, 1:1 mm)",
        "material_page": "https://sendcutsend.com/materials/mild-steel/",
        "hardware_page": "https://sendcutsend.com/services/hardware/",
        "max_part_in": [36, 46],
        "tolerance_in": 0.005,
        "pem_note": "Metric PEM nuts in SCS catalog: M3, M4, M5, M6 — not M3.5. Optional: add M4 nuts on the 4.5 mm holes in the app (holes auto-resize).",
        "forbidden": [
            "PCBWay / any PCB fab of in-repo KiCad",
            "Energize OAMs",
            "OAM M3.5 pattern on these DXFs",
        ],
        "parts": parts,
    }
    (HERE / "MANIFEST.json").write_text(json.dumps(manifest, indent=2) + "\n")
    print(f"Wrote {len(parts)} DXFs to {OUT}")


if __name__ == "__main__":
    main()
