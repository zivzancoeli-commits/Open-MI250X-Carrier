#!/usr/bin/env python3
"""Generate first-system mechanical envelopes from verified OCP / vendor numbers.

DO NOT FABRICATE the KiCad board. OCP signal-to-contact mapping is still BLOCKED.
Cooling height above the OAM is UNKNOWN; a planning volume is drawn and tagged.

Coordinate datum for one module (OCP v1.5 Figure 2, bottom view as drawn):
  origin = lower-left of the 102 x 165 mm PCB
  +X = right (PIN A3 side)
  +Y = toward Connector 1 (top of Figure 2)
"""

from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CAD = ROOT / "cad"
STL = CAD / "stl"
SVG = CAD / "svg"
KICAD = ROOT / "kicad_mechanical"
CSV_DIR = ROOT / "docs" / "csv"

# --- Verified: OCP Accelerator Module Design Specification v1.5 ---
# Local: 13_Reference_Docs/OCP_OAM/ocp accelerator module design specification_v1p5_Final_20220223.docx (1) (1).pdf
# SHA-256: 830729ce3018a466105f4f032aa8d236aa7e179ed031ca08139f1df4910c1824
OAM_W = 102.0  # mm, module PCB width, §5 / §6.1 / Figure 2
OAM_L = 165.0  # mm, module PCB length, §5 / §6.1 / Figure 2
OAM_T_MIN = 1.57  # mm, board thickness range §5
OAM_T_MAX = 3.20  # mm, ±10% also stated
KOZ_W = 103.0  # mm, baseboard component keep-out §6.5.2 / Figure 14
KOZ_L = 166.0  # mm
STACK_H = 5.0  # mm, Mirror Mezz Pro 218910-1115 stack height §5 / §6.2
STACK_TOL = 0.15  # mm, standoff 5 ± 0.15 §6.4.1
STIFF_H = 5.0  # mm, bottom stiffener including Mylar §5
CORNER_R = 2.0  # mm, Figure 2 4X R2
HOLE_D = 3.9  # mm, Figure 2 4X φ3.9 (M3.5 clearance; 153 mil)
HOLE_LAND_D = 8.0  # mm, Figure 2 4X φ8 MIN
HOLE_SPAN_X = 90.0  # mm, Figure 2
HOLE_SPAN_Y = 102.0  # mm, Figure 2
HOLE_EDGE_Y = 31.5  # mm, Figure 2, hole center from 165 mm end
HOLE_EDGE_X = (OAM_W - HOLE_SPAN_X) / 2.0  # 6.0 mm, implied by 102 and 90
CONN_BOX_W = 68.0  # mm, Figure 2 connector area
CONN_BOX_H = 22.0  # mm, Figure 2 connector area
CONN_TOP_FROM_END = 20.5  # mm, Figure 2, Connector 1 top from module top
CONN_INNER_GAP = 80.0  # mm, Figure 2
CONN_PITCH = 102.0  # mm, §6.1 connector-to-connector pitch (also 133.5-31.5)
NOTCH_FROM_TOP = 10.75  # mm, Figure 2 Detail A
NOTCH_LEN = 12.0  # mm
NOTCH_DEPTH = 4.0  # mm
NOTCH_R = 1.0  # mm, Figure 2 4X R1
ALIGN_PIN_D = 3.0  # mm, §6.4.2
ALIGN_PIN_LEN = 10.0  # mm from bottom of OAM PCB, §6.4.2
ALIGN_NUT_HOLE_D = 5.7  # mm, §6.5.1 / Figure 14
ALIGN_FROM_KOZ_END = 6.0  # mm, Figure 14
GASKET_PAD = (8.0, 42.0)  # mm, §6.4.3 / §6.5.3
CORNER_SQ = 10.0  # mm, Figure 14 10x10
BUMPER = 0.5  # mm each side; plastic top 103 mm §6.6 Stage 1
MATE_FORCE_N = 344.0  # N MAX, §6.2
OAM_HS_MASS_KG = 2.0  # kg MAX, §6.2
CONN_MPN = "218910-1115"

# Molex 2189101115-SD sheet 2 (quarantine candidate footprint origin = pad-field centroid)
# PIN A3 in candidate is at (-29.45, +7.50). Figure 2 marks PIN A3 on the +X side.
# Rotate candidate 180° so A3 is on +X. VERIFY before any future fab.
FOOTPRINT_ROT_DEG = 180.0

# --- Verified: SuperMicro X11DPH-T product page / user manual ---
# https://www.supermicro.com/en/products/motherboard/X11DPH-T
# Manual: 13" (W) x 12" (L) (330.2 mm x 304.8 mm)
HOST_W = 330.2
HOST_L = 304.8
HOST_T = 2.4  # mm, typical server PCB; NOT measured on this board — PLANNING

# --- Vendor: Noctua NH-U14S DX-3647 (with fan) ---
# https://noctua.at/en/nh-u14s-dx-3647  (reseller tables matching Noctua DX line)
COOLER_H = 165.0
COOLER_W = 150.0
COOLER_D = 78.0  # with NF-A15

# --- Planning only (not verified MI250X / not this chassis) ---
COOLING_PLANNING_H = 100.0  # mm above module; OEM air HS height is UNKNOWN
SERVICE_MARGIN = 20.0  # mm around 2-GPU KOZ cluster
ATX_PSU = (150.0, 86.0, 140.0)  # ATX PSU form factor, not a selected CRPS
EIGHT_COLS = 4
EIGHT_ROWS = 2  # INFERRED tiling of 103 mm KOZ; not a UBB drawing


def hole_xy():
    xs = (HOLE_EDGE_X, HOLE_EDGE_X + HOLE_SPAN_X)
    ys = (HOLE_EDGE_Y, HOLE_EDGE_Y + HOLE_SPAN_Y)
    return [(x, y) for y in ys for x in xs]


def connector_centers():
    """Connector 0 (north / low Y) and Connector 1 (south / high Y) centers."""
    c0_y = CONN_TOP_FROM_END + CONN_BOX_H / 2.0  # 31.5
    c1_y = OAM_L - CONN_TOP_FROM_END - CONN_BOX_H / 2.0  # 133.5
    cx = OAM_W / 2.0
    return {"Conn0": (cx, c0_y), "Conn1": (cx, c1_y)}


def align_xy_on_module():
    """Alignment pins on module centerline.

    Figure 14 places Ø5.7 nut holes 6 mm from 166 mm KOZ ends.
    Module is 0.5 mm inset, so pin Y on the 165 mm PCB is 6.0 - 0.5 = 5.5 mm
    from each PCB end. Tagged INFERRED from KOZ-to-module inset + Figure 14.
    """
    inset = (KOZ_L - OAM_L) / 2.0
    y0 = ALIGN_FROM_KOZ_END - inset
    y1 = OAM_L - y0
    return [(OAM_W / 2.0, y0), (OAM_W / 2.0, y1)]


def write_csv():
    CSV_DIR.mkdir(parents=True, exist_ok=True)
    path = CSV_DIR / "oam_v15_figure2_coordinates.csv"
    rows = [
        ["feature", "x_mm", "y_mm", "d_or_size_mm", "status", "source"],
        ["pcb_origin_ll", 0, 0, "", "Verified", "OCP v1.5 Figure 2 datum (this file)"],
        ["pcb_ur", OAM_W, OAM_L, "", "Verified", "OCP v1.5 §5 / Figure 2 102 x 165"],
        ["koz", KOZ_W, KOZ_L, "", "Verified", "OCP v1.5 §6.5.2 103 x 166"],
        ["corner_radius", "", "", CORNER_R, "Verified", "OCP v1.5 Figure 2 4X R2"],
        ["notch_from_top", OAM_W - NOTCH_DEPTH / 2, OAM_L - NOTCH_FROM_TOP - NOTCH_LEN / 2,
         f"{NOTCH_DEPTH}x{NOTCH_LEN}", "Verified", "OCP v1.5 Figure 2 Detail A"],
    ]
    for i, (x, y) in enumerate(hole_xy(), 1):
        rows.append([f"npth_m35_{i}", x, y, HOLE_D, "Verified", "OCP v1.5 Figure 2 4X φ3.9, 90 x 102, 31.5 from end"])
    for name, (x, y) in connector_centers().items():
        rows.append([f"{name}_center", x, y, f"{CONN_BOX_W}x{CONN_BOX_H}", "Verified",
                     "OCP v1.5 Figure 2 68x22 box + 20.5/80; pitch 102 §6.1"])
    for i, (x, y) in enumerate(align_xy_on_module(), 1):
        rows.append([f"align_pin_{i}", x, y, ALIGN_PIN_D, "Inferred",
                     "OCP v1.5 Figure 14 Ø5.7 at 6 mm from KOZ end minus 0.5 mm module inset"])
    with path.open("w", newline="") as f:
        csv.writer(f).writerows(rows)
    return path


def stl_box(path: Path, sx, sy, sz, ox=0.0, oy=0.0, oz=0.0):
    """ASCII STL axis-aligned box. Size sx,sy,sz; origin at min corner."""
    x0, y0, z0 = ox, oy, oz
    x1, y1, z1 = ox + sx, oy + sy, oz + sz
    faces = [
        ((0, 0, -1), (x0, y0, z0), (x1, y0, z0), (x1, y1, z0), (x0, y1, z0)),
        ((0, 0, 1), (x0, y0, z1), (x0, y1, z1), (x1, y1, z1), (x1, y0, z1)),
        ((0, -1, 0), (x0, y0, z0), (x0, y0, z1), (x1, y0, z1), (x1, y0, z0)),
        ((0, 1, 0), (x0, y1, z0), (x1, y1, z0), (x1, y1, z1), (x0, y1, z1)),
        ((-1, 0, 0), (x0, y0, z0), (x0, y1, z0), (x0, y1, z1), (x0, y0, z1)),
        ((1, 0, 0), (x1, y0, z0), (x1, y0, z1), (x1, y1, z1), (x1, y1, z0)),
    ]
    lines = ["solid envelope"]
    for n, a, b, c, d in faces:
        for tri in ((a, b, c), (a, c, d)):
            lines.append(f"  facet normal {n[0]} {n[1]} {n[2]}")
            lines.append("    outer loop")
            for p in tri:
                lines.append(f"      vertex {p[0]:.4f} {p[1]:.4f} {p[2]:.4f}")
            lines.append("    endloop")
            lines.append("  endfacet")
    lines.append("endsolid envelope")
    path.write_text("\n".join(lines) + "\n")


def write_stls():
    STL.mkdir(parents=True, exist_ok=True)
    stl_box(STL / "oam_module_pcb.stl", OAM_W, OAM_L, OAM_T_MAX)
    stl_box(STL / "oam_baseboard_koz.stl", KOZ_W, KOZ_L, 0.4)
    stl_box(STL / "oam_connector_stack.stl", CONN_BOX_W, CONN_BOX_H, STACK_H)
    two_w, two_l = 2 * KOZ_W, KOZ_L
    stl_box(STL / "two_gpu_koz_cluster.stl", two_w, two_l, 0.4)
    eight_w, eight_l = EIGHT_COLS * KOZ_W, EIGHT_ROWS * KOZ_L
    stl_box(STL / "eight_gpu_koz_reserve.stl", eight_w, eight_l, 0.4)
    stl_box(STL / "host_x11dph_t.stl", HOST_W, HOST_L, HOST_T)
    stl_box(STL / "noctua_nh_u14s_dx3647.stl", COOLER_W, COOLER_D, COOLER_H)
    stl_box(STL / "cooling_planning_volume_UNKNOWN_height.stl",
            two_w, two_l, COOLING_PLANNING_H)


def svg_rect(x, y, w, h, fill, stroke="#222", sw=0.4, opacity=1.0, extra=""):
    return (f'<rect x="{x:.3f}" y="{y:.3f}" width="{w:.3f}" height="{h:.3f}" '
            f'fill="{fill}" fill-opacity="{opacity}" stroke="{stroke}" '
            f'stroke-width="{sw}" {extra}/>')


def svg_circle(x, y, r, fill="none", stroke="#222", sw=0.35):
    return (f'<circle cx="{x:.3f}" cy="{y:.3f}" r="{r:.3f}" fill="{fill}" '
            f'stroke="{stroke}" stroke-width="{sw}"/>')


def svg_text(x, y, text, size=3.2):
    return (f'<text x="{x:.3f}" y="{y:.3f}" font-size="{size}" '
            f'font-family="Helvetica,Arial,sans-serif">{text}</text>')


def write_svg_module():
    SVG.mkdir(parents=True, exist_ok=True)
    pad = 12
    # SVG Y-down: flip Figure 2 Y so Connector 1 stays visually at top
    def fy(y):
        return pad + (OAM_L - y)

    w = OAM_W + 2 * pad
    h = OAM_L + 2 * pad + 18
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:.1f} {h:.1f}" '
        f'width="{w*4:.0f}" height="{h*4:.0f}">',
        '<title>OAM v1.5 Figure 2 envelope — not a fabrication drawing</title>',
        svg_rect(pad, pad, OAM_W, OAM_L, "#e8f0e4", "#1b5e20", 0.6),
        svg_text(pad + 2, pad + 8, "102 x 165 mm PCB  |  OCP v1.5 Fig 2  |  DO NOT FAB"),
    ]
    # connectors
    c = connector_centers()
    for name, (cx, cy) in c.items():
        x = pad + cx - CONN_BOX_W / 2
        y = fy(cy) - CONN_BOX_H / 2
        parts.append(svg_rect(x, y, CONN_BOX_W, CONN_BOX_H, "#bbdefb", "#0d47a1", 0.5))
        parts.append(svg_text(x + 2, y + 8, f"{name}  {CONN_MPN}  PIN A3 → +X"))
    for x, y in hole_xy():
        parts.append(svg_circle(pad + x, fy(y), HOLE_D / 2, stroke="#b71c1c", sw=0.5))
        parts.append(svg_circle(pad + x, fy(y), HOLE_LAND_D / 2, stroke="#ef9a9a", sw=0.25))
    for x, y in align_xy_on_module():
        parts.append(svg_circle(pad + x, fy(y), ALIGN_PIN_D / 2, stroke="#6a1b9a", sw=0.4))
    # notch (right side, near Connector 1 / top)
    nx = pad + OAM_W - NOTCH_DEPTH
    ny = fy(OAM_L - NOTCH_FROM_TOP) 
    # fy of top-of-notch Y=OAM_L-10.75 is near pad; notch extends toward smaller Y (down in fig, up in svg wait)
    # Notch occupies Y = [OAM_L-10.75-12, OAM_L-10.75] = [142.25, 154.25]
    n_y_svg = fy(OAM_L - NOTCH_FROM_TOP)
    n_h = NOTCH_LEN
    parts.append(svg_rect(nx, n_y_svg, NOTCH_DEPTH, n_h, "#fff", "#333", 0.4))
    parts.append(svg_text(pad + 2, pad + OAM_L + 10,
                          "Holes 90 x 102 mm, 31.5 from ends, φ3.9  |  Conn pitch 102  |  notch 12 x 4"))
    parts.append("</svg>")
    path = SVG / "oam_module_figure2.svg"
    path.write_text("\n".join(parts) + "\n")
    return path


def write_svg_system():
    """2-GPU cluster + 8-GPU reserve + host board, top view, planning layout."""
    gap = 30.0
    two_w, two_l = 2 * KOZ_W, KOZ_L
    eight_w, eight_l = EIGHT_COLS * KOZ_W, EIGHT_ROWS * KOZ_L
    ox, oy = 20.0, 20.0
    host_x = ox + eight_w + gap
    width = host_x + HOST_W + 20
    height = max(eight_l, HOST_L + COOLER_D) + 50
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width:.1f} {height:.1f}" '
        f'width="{width:.0f}" height="{height:.0f}">',
        "<title>First-system envelopes — 2 GPU now, 8 GPU reserve, host E-ATX</title>",
        svg_text(ox, 14, "PLANNING TOP VIEW  |  8-GPU KOZ tiling is INFERRED from 103 mm keep-out, not a UBB drawing"),
        svg_rect(ox, oy, eight_w, eight_l, "#fff3e0", "#e65100", 0.8, 0.35),
        svg_text(ox + 4, oy + 14, f"8x OAM reserve {eight_w:.0f} x {eight_l:.0f} mm (4x2 x 103x166 KOZ) INFERRED"),
        svg_rect(ox, oy, two_w, two_l, "#e3f2fd", "#1565c0", 0.9, 0.85),
        svg_text(ox + 4, oy + 28, f"2x OAM first config {two_w:.0f} x {two_l:.0f} mm  (2 x 103 mm KOZ)"),
    ]
    for col in range(EIGHT_COLS):
        for row in range(EIGHT_ROWS):
            x = ox + col * KOZ_W
            y = oy + row * KOZ_L
            parts.append(svg_rect(x, y, KOZ_W, KOZ_L, "none", "#ef6c00" if (col, row) != (0, 0) and (col, row) != (1, 0) else "#1565c0", 0.35))
            if row == 0 and col < 2:
                parts.append(svg_rect(x + 0.5, y + 0.5, OAM_W, OAM_L, "#c8e6c9", "#2e7d32", 0.4, 0.7))
                parts.append(svg_text(x + 4, y + 20, f"OAM{col}"))
    parts.append(svg_rect(host_x, oy, HOST_W, HOST_L, "#f3e5f5", "#6a1b9a", 0.8, 0.8))
    parts.append(svg_text(host_x + 4, oy + 14, f"X11DPH-T E-ATX {HOST_W} x {HOST_L} mm VERIFIED SuperMicro"))
    parts.append(svg_rect(host_x + 20, oy + 40, COOLER_W, COOLER_D, "#ce93d8", "#4a148c", 0.5, 0.9))
    parts.append(svg_text(host_x + 24, oy + 56, f"NH-U14S DX-3647 {COOLER_W}x{COOLER_D}x{COOLER_H} vendor"))
    parts.append(svg_rect(host_x + 180, oy + 40, COOLER_W, COOLER_D, "#ce93d8", "#4a148c", 0.5, 0.9))
    parts.append(svg_text(host_x + 184, oy + 56, "2nd cooler — CPU pitch UNKNOWN"))
    parts.append(svg_text(ox, oy + eight_l + 18,
                          "Airflow intent: front→rear. Cooling height above OAM = UNKNOWN (100 mm STL is planning only)."))
    parts.append(svg_text(ox, oy + eight_l + 32,
                          "Do not energize MI250X. Connector land pattern exists; OCP pin map does not."))
    parts.append("</svg>")
    path = SVG / "first_system_top.svg"
    path.write_text("\n".join(parts) + "\n")
    return path


def write_openscad():
    path = CAD / "first_system_envelope.scad"
    path.write_text(f"""// First-system mechanical envelopes.
// Generated by generate_envelopes.py — numbers cited in docs/oam_mechanical_envelope_v1.md
// NOT a fabrication or cooling-qualification model.

oam_w = {OAM_W};
oam_l = {OAM_L};
oam_t = {OAM_T_MAX};
koz_w = {KOZ_W};
koz_l = {KOZ_L};
stack_h = {STACK_H};
two_w = 2*koz_w;
eight_w = {EIGHT_COLS}*koz_w;
eight_l = {EIGHT_ROWS}*koz_l;
host_w = {HOST_W};
host_l = {HOST_L};
cooler_w = {COOLER_W};
cooler_d = {COOLER_D};
cooler_h = {COOLER_H};
cooling_planning_h = {COOLING_PLANNING_H}; // UNKNOWN real HS height

module oam_pcb() color([0.55,0.75,0.45]) cube([oam_w, oam_l, oam_t]);
module koz() color([0.2,0.4,0.8,0.25]) cube([koz_w, koz_l, 0.4]);

module two_gpu() {{
    for (i=[0:1]) translate([i*koz_w, 0, 0]) {{
        koz();
        translate([0.5, 0.5, stack_h]) oam_pcb();
    }}
    color([1,0.6,0.1,0.2]) translate([0,0,stack_h+oam_t])
        cube([two_w, koz_l, cooling_planning_h]);
}}

module eight_reserve() color([1,0.5,0,0.12]) cube([eight_w, eight_l, 0.4]);

module host() {{
    color([0.6,0.3,0.7]) cube([host_w, host_l, 2.4]);
    // CPU-to-CPU pitch UNKNOWN — coolers shown as placeholders, not socket-accurate
    color([0.45,0.15,0.6,0.7]) translate([20, 40, 2.4]) cube([cooler_w, cooler_d, cooler_h]);
    color([0.45,0.15,0.6,0.7]) translate([180, 40, 2.4]) cube([cooler_w, cooler_d, cooler_h]);
}}

eight_reserve();
two_gpu();
translate([eight_w + 30, 0, 0]) host();
""")
    return path


def write_kicad():
    """Mechanical-only 2-GPU carrier outline + holes. DO NOT FABRICATE."""
    KICAD.mkdir(parents=True, exist_ok=True)
    (KICAD / "footprints").mkdir(exist_ok=True)
    margin = SERVICE_MARGIN
    board_w = 2 * KOZ_W + 2 * margin
    board_h = KOZ_L + 2 * margin
    # KiCad Y increases down; place KOZ cluster at (margin, margin)
    lines = [
        '(kicad_pcb (version 20241229) (generator chassis_envelope_v1)',
        '  (general (thickness 1.6))',
        '  (paper "A3")',
        '  (layers',
        '    (0 "F.Cu" signal)',
        '    (31 "B.Cu" signal)',
        '    (37 "F.SilkS" user)',
        '    (36 "B.SilkS" user)',
        '    (39 "F.Mask" user)',
        '    (38 "B.Mask" user)',
        '    (41 "Cmts.User" user)',
        '    (40 "Dwgs.User" user)',
        '    (44 "Edge.Cuts" user)',
        '    (45 "F.CrtYd" user)',
        '    (49 "F.Fab" user)',
        '  )',
        '  (setup (pad_to_mask_clearance 0))',
        f'  (gr_rect (start 0 0) (end {board_w:.3f} {board_h:.3f})',
        '    (stroke (width 0.2) (type solid)) (fill none) (layer "Edge.Cuts"))',
        f'  (gr_text "MECHANICAL ENVELOPE ONLY — DO NOT FABRICATE — OCP v1.5 pin map BLOCKED"',
        f'    (at {board_w/2:.3f} 8) (layer "Cmts.User")',
        '    (effects (font (size 2.5 2.5) (thickness 0.3))))',
    ]
    cons = connector_centers()
    holes = hole_xy()
    for m in range(2):
        ox = margin + m * KOZ_W + 0.5  # 0.5 mm KOZ-to-module inset
        oy = margin + 0.5
        # module outline
        lines.append(
            f'  (gr_rect (start {ox:.3f} {oy:.3f}) (end {ox+OAM_W:.3f} {oy+OAM_L:.3f})'
            f' (stroke (width 0.15) (type solid)) (fill none) (layer "Dwgs.User"))')
        lines.append(
            f'  (gr_rect (start {margin + m*KOZ_W:.3f} {margin:.3f}) '
            f'(end {margin + (m+1)*KOZ_W:.3f} {margin+KOZ_L:.3f})'
            f' (stroke (width 0.12) (type dash)) (fill none) (layer "F.CrtYd"))')
        for i, (hx, hy) in enumerate(holes, 1):
            x, y = ox + hx, oy + (OAM_L - hy)  # flip Y to KiCad
            lines.append(
                f'  (footprint "NPTH_3.9_Fig2" (layer "F.Cu") (at {x:.3f} {y:.3f})'
                f' (descr "OCP v1.5 Figure 2 M3.5 clearance")'
                f' (property "Reference" "H{m}{i}" (at 0 -4) (layer "F.Fab")'
                f' (effects (font (size 1 1) (thickness 0.15))))'
                f' (property "Value" "NPTH_3.9" (at 0 4) (layer "F.Fab")'
                f' (effects (font (size 0.8 0.8) (thickness 0.12))))'
                f' (pad "" np_thru_hole circle (at 0 0) (size {HOLE_LAND_D:.2f} {HOLE_LAND_D:.2f}) '
                f'(drill {HOLE_D:.2f}) (layers "*.Cu" "*.Mask")))')
        for name, (cx, cy) in cons.items():
            x, y = ox + cx, oy + (OAM_L - cy)
            ref = f"J{m}_{name}"
            lines.append(
                f'  (footprint "footprints:218910-1115_candidate" (layer "F.Cu") '
                f'(at {x:.3f} {y:.3f} {FOOTPRINT_ROT_DEG:.0f})'
                f' (property "Reference" "{ref}" (at 0 -14) (layer "F.SilkS")'
                f' (effects (font (size 1.2 1.2) (thickness 0.15))))'
                f' (property "Value" "{CONN_MPN}" (at 0 14) (layer "F.Fab")'
                f' (effects (font (size 1 1) (thickness 0.15)))))')
    lines.append(")")
    pcb = KICAD / "MI250X_2GPU_MechanicalEnvelope.kicad_pcb"
    pcb.write_text("\n".join(lines) + "\n")
    pro = KICAD / "MI250X_2GPU_MechanicalEnvelope.kicad_pro"
    pro.write_text("""{
  "board": { "3dviewports": [], "design_settings": {} },
  "boards": [],
  "cvpcb": { "equivalence_files": [] },
  "libraries": { "pinned_footprint_libs": [], "pinned_symbol_libs": [] },
  "meta": { "filename": "MI250X_2GPU_MechanicalEnvelope.kicad_pro", "version": 3 },
  "net_settings": { "classes": [], "meta": { "version": 0 } },
  "pcbnew": { "last_paths": { "gencad": "", "idf": "", "netlist": "", "plot": "", "specctra_dsn": "", "step": "", "vrml": "" }, "page_layout_descr_file": "" },
  "schematic": { "annotate_start_num": 0 },
  "sheets": [ [ "MI250X_2GPU_MechanicalEnvelope.kicad_sch", "Root" ] ],
  "text_variables": {}
}
""")
    (KICAD / "fp-lib-table").write_text(
        '(fp_lib_table\n  (lib (name "footprints")(type "KiCad")'
        '(uri "${KIPRJMOD}/footprints")(options "")(descr "Molex 218910-1115 quarantine candidate"))\n)\n'
    )
    sch = KICAD / "MI250X_2GPU_MechanicalEnvelope.kicad_sch"
    sch.write_text("""(kicad_sch (version 20250114) (generator chassis_envelope_v1)
  (uuid 11111111-2222-3333-4444-555555555555)
  (paper "A4")
  (title_block
    (title "MI250X 2-GPU mechanical envelope")
    (comment 1 "DO NOT FABRICATE — OCP v1.5 pin map not assigned")
  )
  (lib_symbols)
)
""")
    return pcb


def write_meta():
    meta = {
        "tree": "Generated_Project/Rev2_MI250X_Carrier_ChassisEnvelope_v1",
        "do_not_fabricate": True,
        "oam_spec": "OCP Accelerator Module Design Specification v1.5",
        "oam_sha256": "830729ce3018a466105f4f032aa8d236aa7e179ed031ca08139f1df4910c1824",
        "connector_mpn": CONN_MPN,
        "production_pcb_untouched": True,
        "ocp_signal_map": "BLOCKED",
        "verified_mm": {
            "oam_pcb": [OAM_W, OAM_L],
            "koz": [KOZ_W, KOZ_L],
            "hole_span": [HOLE_SPAN_X, HOLE_SPAN_Y],
            "hole_from_end": HOLE_EDGE_Y,
            "hole_diameter": HOLE_D,
            "connector_box": [CONN_BOX_W, CONN_BOX_H],
            "connector_pitch": CONN_PITCH,
            "stack_height": STACK_H,
            "host_eatx": [HOST_W, HOST_L],
            "cooler_with_fan": [COOLER_W, COOLER_D, COOLER_H],
        },
        "unknown": [
            "OEM air heatsink height (photos exist, not measured)",
            "X11DPH-T CPU-to-CPU pitch",
            "OCP v1.5 pinlist spreadsheet",
            "AMD MI250X package / cold-plate ICD",
        ],
    }
    path = ROOT / "docs" / "envelope_meta.json"
    path.write_text(json.dumps(meta, indent=2) + "\n")
    return path


def main():
    write_csv()
    write_stls()
    write_svg_module()
    write_svg_system()
    write_openscad()
    write_kicad()
    write_meta()
    print("Wrote envelopes under", ROOT)


if __name__ == "__main__":
    main()
