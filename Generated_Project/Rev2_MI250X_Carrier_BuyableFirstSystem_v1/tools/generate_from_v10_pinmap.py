#!/usr/bin/env python3
"""Generate the 2-OAM v1.0-mapped stub KiCad project.

Source of pin names: 22_Pinmap_Research/extracted/OAM_v1.0_OCP_Generic_Pin_Map.csv
(xlsx wins if they disagree).

Rules:
- Do not invent AMD/OCP pin functions.
- Wire only nets named in the v1.0 map.
- TEST*/RFU/DO_NOT_USE stay unmapped (no copper / no-connect).
- PVREF is a module OUTPUT — never driven from the carrier.
- DO NOT FABRICATE. DO NOT ENERGIZE.
"""

from __future__ import annotations

import csv
import json
import re
import shutil
import uuid
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPO = Path(__file__).resolve().parents[3]
PINMAP = REPO / "22_Pinmap_Research/extracted/OAM_v1.0_OCP_Generic_Pin_Map.csv"
FOOTPRINT_SRC = ROOT / "footprints/218910-1115_candidate.kicad_mod"

SCH_VER = 20250114
PCB_VER = 20241229
SYM_VER = 20241209

# Shared carrier rails (OCP-named). Per-OAM everything else.
SHARED_RAILS = {"P48V", "P12V1", "P12V2", "P3V3", "GND"}

# Module outputs — named, must not be driven by the carrier.
MODULE_OUTPUTS = {"PVREF", "MODULE_PWRGD", "UART_TXD", "SLV_ALERT#", "PE_BIF[0]", "PE_BIF[1]",
                  "PLINK_CAP", "THERMTRIP#", "DWN_PERST#", "DWN_REFCLKP", "DWN_REFCLKN",
                  "PRSNT0#", "PRSNT1#", "I2C_D", "I2C _CLK", "SCALE_DEBUG_EN"}

UNMAPPED_EXACT = {"RFU", "DO_NOT_USE"}
UNMAPPED_PREFIXES = ("TEST",)  # TEST0–TEST14 and TEST_MODE# — AMD overlay unknown


def uid() -> str:
    return str(uuid.uuid4())


def load_pinmap() -> list[dict]:
    rows = list(csv.DictReader(PINMAP.open()))
    if len(rows) != 1376:
        raise SystemExit(f"expected 1376 named pads, got {len(rows)}")
    return rows


def is_unmapped(signal: str) -> bool:
    if signal in UNMAPPED_EXACT:
        return True
    if signal.startswith("TEST"):
        return True
    return False


def net_name(oam: int, signal: str) -> str | None:
    """Return the KiCad net for a named v1.0 signal, or None if unmapped."""
    if is_unmapped(signal):
        return None
    # KiCad net names cannot contain spaces.
    sig = signal.replace(" ", "")
    if signal in SHARED_RAILS:
        return sig
    return f"OAM{oam}_{sig}"


def classify(signal: str) -> str:
    if is_unmapped(signal):
        return "unmapped_nc"
    if signal in SHARED_RAILS:
        return "power_shared"
    if signal == "PVREF":
        return "module_output_do_not_drive"
    if signal.startswith("PCIE_"):
        return "pcie_stub"
    if signal in {"PE_REFCLKP", "PE_REFCLKN", "PERST#", "WARMRST#", "HOST_PWRGD",
                  "MODULE_PWRGD", "PWRBRK#", "PRSNT0#", "PRSNT1#", "AUX_100M_REFCLKP",
                  "AUX_100M_REFCLKN", "AUX_156M_REFCLKP", "AUX_156M_REFCLKN",
                  "DWN_PERST#", "DWN_REFCLKP", "DWN_REFCLKN"}:
        return "clock_reset"
    if signal.startswith("S") and re.match(r"S[1-7]_", signal):
        return "serdes_named_not_routed"
    if signal.startswith("MNGMT_LINK"):
        return "mgmt_link_named_not_routed"
    if signal.startswith(("CONN1_", "CONN2_")):
        return "qsfp_sideband_named_not_routed"
    if signal.startswith(("JTAG", "SMBus", "I2C", "UART", "SLV_ALERT")):
        return "mgmt_stub"
    if signal.startswith(("MODULE_ID", "LINK_CONFIG", "PE_BIF", "PLINK", "MANF",
                          "FW_RECOVERY", "PWRRDT", "THERMTRIP", "DEBUG_PORT")):
        return "ocp_sideband"
    return "named_other"


def kicad_escape(s: str) -> str:
    return s.replace("\\", "\\\\").replace('"', '\\"')


def write_classification_csv(rows: list[dict]) -> None:
    out = ROOT / "netlist/v10_pad_classification.csv"
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["connector", "pad", "v10_signal", "class", "oam0_net", "oam1_net",
                    "wired_on_stub", "notes"])
        for r in rows:
            sig = r["signal"]
            cls = classify(sig)
            n0 = net_name(0, sig) or ""
            n1 = net_name(1, sig) or ""
            wired = cls in {"power_shared", "pcie_stub", "clock_reset", "mgmt_stub",
                            "ocp_sideband", "module_output_do_not_drive"}
            note = ""
            if cls == "unmapped_nc":
                note = "Named in v1.0 but AMD overlay unknown or reserved; no copper"
            elif cls == "serdes_named_not_routed":
                note = "Named SerDes (xGMI/IF candidate). Topology AMD-unknown; pad net assigned, not routed"
            elif cls == "module_output_do_not_drive":
                note = "Module output. Never drive from carrier. Do not short OAM0 to OAM1."
            elif cls == "power_shared":
                note = "OCP-named power/ground. P48V source not yet a finished harness."
            w.writerow([r["connector"], r["pin"], sig, cls, n0, n1, "yes" if wired else "no", note])


def power_symbol(name: str) -> str:
    """Minimal power flag symbol body (embedded in schematic)."""
    pin_rot = 90 if name != "GND" else 270
    y_off = 3.556 if name != "GND" else -3.81
    return f'''(symbol "power:{name}" (power) (pin_names (offset 0)) (in_bom yes) (on_board yes)
	(property "Reference" "#PWR" (at 0 -3.81 0) (effects (font (size 1.27 1.27)) hide))
	(property "Value" "{name}" (at 0 {y_off} 0) (effects (font (size 1.27 1.27))))
	(property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
	(symbol "{name}_0_1"
		(pin power_in line (at 0 0 {pin_rot}) (length 0) (name "{name}" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
	)
)
'''


def build_conn_symbol(conn: str, rows: list[dict]) -> str:
    """One multi-unit symbol: Power, Clock/Reset/Mgmt, Host PCIe, named leftover.

    Pin number = Molex/OCP pad (A3, C1, ...). Pin name = v1.0 signal.
    Unmapped pads are omitted from the symbol (they exist on the footprint only).
    """
    by_class: dict[str, list[tuple[str, str]]] = defaultdict(list)
    for r in rows:
        if r["connector"] != conn:
            continue
        sig = r["signal"]
        cls = classify(sig)
        if cls == "unmapped_nc":
            continue
        by_class[cls].append((r["pin"], sig.replace(" ", "_")))

    # Units: 1 power, 2 clock/reset/mgmt/sideband, 3 PCIe, 4 named-not-routed
    unit_map = {
        1: ["power_shared", "module_output_do_not_drive"],
        2: ["clock_reset", "mgmt_stub", "ocp_sideband", "named_other"],
        3: ["pcie_stub"],
        4: ["serdes_named_not_routed", "mgmt_link_named_not_routed", "qsfp_sideband_named_not_routed"],
    }
    unit_titles = {
        1: "Power + PVREF (do not drive PVREF)",
        2: "Clock / reset / mgmt / OCP sideband stub",
        3: "Host PCIe x16 named pairs (stub only)",
        4: "Named SerDes/QSFP — assigned, NOT routed",
    }

    sym = f'OAM_{conn}_v10'
    lines = [
        f'(symbol "{sym}" (pin_names (offset 1.016)) (pin_numbers hide) (in_bom yes) (on_board yes)',
        f'  (property "Reference" "J" (at 0 -2.54 0) (effects (font (size 1.27 1.27))))',
        f'  (property "Value" "{sym}" (at 0 2.54 0) (effects (font (size 1.27 1.27))))',
        f'  (property "Footprint" "footprints:218910-1115_candidate" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))',
        f'  (property "Datasheet" "OAM Pin map rev 1.0.xlsx OCP Generic Pin Map" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))',
        f'  (property "ki_description" "OCP generic v1.0 {conn} 688-contact map. NOT AMD MI250X overlay. DO NOT FABRICATE." (at 0 0 0) (effects (font (size 1.27 1.27)) hide))',
        f'  (property "ki_fp_filters" "218910-1115*" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))',
    ]

    etype_for = {
        "power_shared": "power_in",
        "module_output_do_not_drive": "passive",
        "clock_reset": "passive",
        "mgmt_stub": "passive",
        "ocp_sideband": "passive",
        "named_other": "passive",
        "pcie_stub": "passive",
        "serdes_named_not_routed": "passive",
        "mgmt_link_named_not_routed": "passive",
        "qsfp_sideband_named_not_routed": "passive",
    }

    for unit, classes in unit_map.items():
        pins: list[tuple[str, str, str]] = []
        for cls in classes:
            for pad, sig in by_class.get(cls, []):
                pins.append((pad, sig, etype_for[cls]))
        # Stack extra pads that share a signal name (power).
        # Keep first of each signal visible; hide subsequent at same position.
        grouped: dict[str, list[tuple[str, str]]] = defaultdict(list)
        order = []
        for pad, sig, et in pins:
            if sig not in grouped:
                order.append((sig, et))
            grouped[sig].append((pad, et))

        n = max(len(order), 1)
        h = max(n * 2.54 + 10.16, 25.4)
        w = 50.8
        lines.append(f'  (symbol "{sym}_{unit}_1"')
        lines.append(f'    (rectangle (start {-w/2} {-h/2}) (end {w/2} {h/2})')
        lines.append(f'      (stroke (width 0.254) (type solid)) (fill (type background)))')
        y0 = h / 2 - 5.08
        for i, (sig, et) in enumerate(order):
            y = y0 - i * 2.54
            pads = grouped[sig]
            for j, (pad, pet) in enumerate(pads):
                hide = " hide" if j else ""
                # Left side
                lines.append(
                    f'    (pin {pet} line (at {-w/2 - 2.54} {y:.3f} 0) (length 2.54){hide}'
                    f' (name "{kicad_escape(sig)}" (effects (font (size 1.016 1.016))))'
                    f' (number "{pad}" (effects (font (size 1.016 1.016)))))'
                )
        lines.append("  )")
        # unit box title as property on unit 1 only is enough

    lines.append(")")
    return "\n".join(lines), unit_titles


def write_symbol_lib(rows: list[dict]) -> None:
    conn0, _ = build_conn_symbol("Conn0", rows)
    conn1, _ = build_conn_symbol("Conn1", rows)
    text = (
        f'(kicad_symbol_lib (version {SYM_VER}) (generator "buyable_first_system_v1")\n'
        + conn0
        + "\n"
        + conn1
        + "\n)\n"
    )
    (ROOT / "symbols/OAM_v10_mapped.kicad_sym").write_text(text)


def sch_header(title: str, comment: str) -> str:
    return f'''(kicad_sch (version {SCH_VER}) (generator "buyable_first_system_v1")
	(uuid "{uid()}")
	(paper "A3")
	(title_block
		(title "{kicad_escape(title)}")
		(date "2026-08-17")
		(rev "BuyableFirstSystem_v1")
		(comment 1 "DO NOT FABRICATE. DO NOT ENERGIZE MI250X.")
		(comment 2 "{kicad_escape(comment)}")
		(comment 3 "Pin names: OAM Pin map rev 1.0.xlsx — OCP generic, NOT AMD overlay")
		(comment 4 "r2.0 maps UNUSABLE. P3V3=2 Conn0.")
	)
'''


def write_root_sch() -> None:
    p = ROOT / "MI250X_2OAM_v10_Stub.kicad_sch"
    body = sch_header(
        "2-OAM v1.0-mapped stub (NOT fab-ready)",
        "Mechanical + power + clock + reset + PCIe stub only",
    )
    note = (
        "DO NOT FABRICATE / DO NOT ENERGIZE\\n"
        "This project maps OCP generic v1.0 named pads onto 2 OAM seats.\\n"
        "It is NOT an AMD MI250X NDA overlay.\\n"
        "Blockers before any power: identified 48V path + harness, Molex 30V-vs-48V rating,\\n"
        "verified cooling (not a custom cold plate on bare die), dual U14S fit,\\n"
        "PCIe Gen3 host downtrain / no retimer BOM, BMC/SMBus addresses.\\n"
        "PVREF is a MODULE OUTPUT — never drive from the carrier.\\n"
        "TEST*/RFU/DO_NOT_USE pads have no nets.\\n"
        "SerDes S1–S7 are named in v1.0 but NOT routed (AMD xGMI overlay unknown)."
    )
    body += f'''
	(lib_symbols
{power_symbol("P48V")}
{power_symbol("P12V1")}
{power_symbol("P12V2")}
{power_symbol("+3V3")}
{power_symbol("GND")}
	)

	(text (at 25.4 20.32 0)
		(effects (font (size 2.54 2.54) (thickness 0.4)) (justify left top))
		(uuid "{uid()}")
		"{note}"
	)

	(sheet (at 25.4 90) (size 70 40)
		(stroke (width 0.1524) (type solid))
		(fill (color 0 0 0 0.0000))
		(uuid "{uid()}")
		(property "Sheetname" "00_DO_NOT_FABRICATE" (at 27.94 87.46 0)
			(effects (font (size 1.27 1.27)) (justify left bottom)) (uuid "{uid()}"))
		(property "Sheetfile" "sheets/00_do_not_fabricate.kicad_sch" (at 27.94 132.54 0)
			(effects (font (size 1.27 1.27)) (justify left top)) (uuid "{uid()}"))
	)
	(sheet (at 110 90) (size 70 40)
		(stroke (width 0.1524) (type solid))
		(fill (color 0 0 0 0.0000))
		(uuid "{uid()}")
		(property "Sheetname" "01_Power_Clock_Reset" (at 112.54 87.46 0)
			(effects (font (size 1.27 1.27)) (justify left bottom)) (uuid "{uid()}"))
		(property "Sheetfile" "sheets/01_power_clock_reset.kicad_sch" (at 112.54 132.54 0)
			(effects (font (size 1.27 1.27)) (justify left top)) (uuid "{uid()}"))
	)
	(sheet (at 195 90) (size 70 40)
		(stroke (width 0.1524) (type solid))
		(fill (color 0 0 0 0.0000))
		(uuid "{uid()}")
		(property "Sheetname" "02_Host_PCIe_Stub" (at 197.54 87.46 0)
			(effects (font (size 1.27 1.27)) (justify left bottom)) (uuid "{uid()}"))
		(property "Sheetfile" "sheets/02_host_pcie_stub.kicad_sch" (at 197.54 132.54 0)
			(effects (font (size 1.27 1.27)) (justify left top)) (uuid "{uid()}"))
	)
	(sheet (at 25.4 145) (size 70 40)
		(stroke (width 0.1524) (type solid))
		(fill (color 0 0 0 0.0000))
		(uuid "{uid()}")
		(property "Sheetname" "03_OAM0_Connectors" (at 27.94 142.46 0)
			(effects (font (size 1.27 1.27)) (justify left bottom)) (uuid "{uid()}"))
		(property "Sheetfile" "sheets/03_oam0_connectors.kicad_sch" (at 27.94 187.54 0)
			(effects (font (size 1.27 1.27)) (justify left top)) (uuid "{uid()}"))
	)
	(sheet (at 110 145) (size 70 40)
		(stroke (width 0.1524) (type solid))
		(fill (color 0 0 0 0.0000))
		(uuid "{uid()}")
		(property "Sheetname" "04_OAM1_Connectors" (at 112.54 142.46 0)
			(effects (font (size 1.27 1.27)) (justify left bottom)) (uuid "{uid()}"))
		(property "Sheetfile" "sheets/04_oam1_connectors.kicad_sch" (at 112.54 187.54 0)
			(effects (font (size 1.27 1.27)) (justify left top)) (uuid "{uid()}"))
	)
	(sheet (at 195 145) (size 70 40)
		(stroke (width 0.1524) (type solid))
		(fill (color 0 0 0 0.0000))
		(uuid "{uid()}")
		(property "Sheetname" "05_Unmapped_AMD" (at 197.54 142.46 0)
			(effects (font (size 1.27 1.27)) (justify left bottom)) (uuid "{uid()}"))
		(property "Sheetfile" "sheets/05_unmapped_amd.kicad_sch" (at 197.54 187.54 0)
			(effects (font (size 1.27 1.27)) (justify left top)) (uuid "{uid()}"))
	)
)
'''
    p.write_text(body)


def write_text_sheet(rel: str, title: str, text: str) -> None:
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        sch_header(title, "Documentation sheet — no invented nets")
        + f'''
	(text (at 20.32 20.32 0)
		(effects (font (size 1.5 1.5)) (justify left top))
		(uuid "{uid()}")
		"{kicad_escape(text)}"
	)
)
'''
    )


def symbol_instance_block(lib_sym: str) -> str:
    # Pull the symbol definition from the library file at generation time by
    # embedding a tiny placeholder; eeschema will resolve via sym-lib-table.
    # For a standalone open we also embed Conn0 unit-1 as a comment that the
    # library must be loaded. Hierarchical labels carry the actual nets.
    return ""


def write_power_clock_sheet() -> None:
    text = """PURPOSE: Named power / clock / reset stubs from OAM v1.0 pin map + pin list.

SHARED RAILS (OCP names, both OAMs):
- P48V  Conn0 16 pads  44–59.5 V  up to 700 W class (pin list). MI250X 500/560 W (AMD datasheet).
- P12V1 Conn0 5 pads   12 V infrastructure up to 50 W. Required.
- P12V2 Conn0 27 pads  12 V main for 12V-based OAM up to 300 W. Required for P12V-based OAM.
        Whether MI250X needs P12V2 powered is AMD-unknown. Do NOT short to P12V1 unless documented.
- P3V3  Conn0 C1,C2    3.3 V up to 5 W. Required. 2 pins — matches v1.5 Table 4; r2.0 has 6.
- GND   Conn0 334 pads
- PVREF Conn0 G1,G2    MODULE OUTPUT 1.5–3.3 V, max 0.5 A. NEVER drive from carrier. Per-OAM nets.

CLOCK / RESET (Conn0 unless noted):
- PE_REFCLKP/N  F45/F46   100 MHz PCIe refclk INPUT to module. Stub only — no clock-gen IC invented.
- PERST#        D1        CEM-compliant PCIe reset, 3.3 V input.
- WARMRST#      D2        Vref. Pin list: NC for standard PCIe.
- HOST_PWRGD    H1        3.3 V input. Pin list: Power Enable when P48V/P12V/P3V3 are in spec.
- MODULE_PWRGD  H2        3.3 V output. Ready for PERST# deassert.
- PWRBRK#       C3        3.3 V input, CEM power brake.
- PRSNT0#       J4        Module present, 1k to GND on module. Weak PU on baseboard.
- PRSNT1#       Conn1 C63

DO NOT: invent VRMs, mix 12 V CRPS into P48V, drive PVREF, pour P48V copper until
Molex 30 V datasheet vs OCP 48 V use is resolved, or attach a guessed clock chip.
"""
    write_text_sheet("sheets/01_power_clock_reset.kicad_sch", "Power / clock / reset stub", text)

    # Add power flags so the sheet is a real schematic, not only a note.
    path = ROOT / "sheets/01_power_clock_reset.kicad_sch"
    existing = path.read_text().rstrip()
    if existing.endswith(")"):
        existing = existing[:-1]
    flags = []
    x = 30.48
    for name, net in [("P48V", "P48V"), ("P12V1", "P12V1"), ("P12V2", "P12V2"),
                      ("+3V3", "P3V3"), ("GND", "GND")]:
        flags.append(f'''
	(symbol (lib_id "power:{name}") (at {x} 160 0) (unit 1)
		(in_bom yes) (on_board yes) (dnp no)
		(uuid "{uid()}")
		(property "Reference" "#PWR{name.replace('+','')}" (at {x} 155 0)
			(effects (font (size 1.27 1.27)) hide) (uuid "{uid()}"))
		(property "Value" "{name}" (at {x} 165 0)
			(effects (font (size 1.27 1.27))) (uuid "{uid()}"))
		(pin "1" (uuid "{uid()}"))
	)
	(label (at {x} 165.1 0)
		(effects (font (size 1.27 1.27)) (justify left bottom))
		(uuid "{uid()}")
		"{net}"
	)
''')
        x += 25.4
    # hierarchical labels for clock/reset
    y = 190
    for lab in ["OAM0_PE_REFCLKP", "OAM0_PE_REFCLKN", "OAM0_PERST#", "OAM0_HOST_PWRGD",
                "OAM0_MODULE_PWRGD", "OAM0_PVREF", "OAM1_PE_REFCLKP", "OAM1_PE_REFCLKN",
                "OAM1_PERST#", "OAM1_HOST_PWRGD", "OAM1_MODULE_PWRGD", "OAM1_PVREF"]:
        flags.append(f'''
	(hierarchical_label (at 30.48 {y} 0)
		(effects (font (size 1.27 1.27)) (justify left))
		(uuid "{uid()}")
		(shape bidirectional)
		"{lab}"
	)
''')
        y += 5.08
    path.write_text(existing + "\n" + "".join(flags) + "\n)\n")


def write_pcie_sheet() -> None:
    text = """PURPOSE: Host PCIe stub using ONLY v1.0 names PCIE_TXnP/N and PCIE_RXnP/N (n=0..15).

OCP pin list (module POV):
- PETp/n = module TX, host RX. AC caps on motherboard/carrier.
- PERp/n = module RX, host TX. AC caps on motherboard/carrier.

This sheet does NOT map those pairs onto a CEM x16 connector pinout.
Lane order, polarity invert, and dual-GCD (1x16 vs 2x8) need the AMD overlay.
PE_BIF[1:0] on Conn1 report bifurcation; functions are OCP-named, AMD default Unknown.

Host: Supermicro X11DPH-T is PCIe Gen3 (3x x16 + 4x x8). MI250X is Gen4 and will downtrain.
No retimer/switch BOM is closed from pinmap+host. Do not buy a PCIe switch for this stub.

X11DPH-T has two physical x16 slots that could eventually take two CEM adapters —
that adapter does not exist in this repository and is not invented here.
"""
    write_text_sheet("sheets/02_host_pcie_stub.kicad_sch", "Host PCIe stub", text)
    path = ROOT / "sheets/02_host_pcie_stub.kicad_sch"
    existing = path.read_text().rstrip()[:-1]
    labels = []
    y = 140
    for oam in (0, 1):
        for n in range(16):
            for pn in ("P", "N"):
                for txrx in ("TX", "RX"):
                    lab = f"OAM{oam}_PCIE_{txrx}{n}{pn}"
                    labels.append(f'''
	(hierarchical_label (at 25.4 {y:.2f} 0)
		(effects (font (size 1.016 1.016)) (justify left))
		(uuid "{uid()}")
		(shape bidirectional)
		"{lab}"
	)
''')
                    y += 3.81
                    if y > 250:
                        y = 140
    path.write_text(existing + "".join(labels) + "\n)\n")


def write_oam_connector_sheet(oam: int, rel: str) -> None:
    text = f"""OAM{oam} connector instances.

Footprint: Molex 218910-1115 candidate (geometry). Hermaphroditic — mates with itself
(Farnell 2189101115: Mates With 2189101115; mated height 5.00 mm).

Pad nets are assigned on the PCB from the v1.0 CSV. Schematic shows hierarchical
ports for the stub (power / clock / reset / PCIe / mgmt). SerDes S1–S7 are named
on the PCB and left unrouted.

MODULE_ID[4:0]: OCP pin list says weak PU on module; 1k to GND on baseboard for 0,
leave open for 1. This stub does NOT place those resistors — population is a later
step after AMD overlay. Default (all open) is all-1s.

LINK_CONFIG[4:0]: same OCP rule; leave open this stub (AMD topology unknown).
"""
    write_text_sheet(rel, f"OAM{oam} connectors", text)
    path = ROOT / rel
    existing = path.read_text().rstrip()[:-1]
    ports = [
        "P48V", "P12V1", "P12V2", "P3V3", "GND",
        f"OAM{oam}_PVREF", f"OAM{oam}_PE_REFCLKP", f"OAM{oam}_PE_REFCLKN",
        f"OAM{oam}_PERST#", f"OAM{oam}_HOST_PWRGD", f"OAM{oam}_MODULE_PWRGD",
        f"OAM{oam}_WARMRST#", f"OAM{oam}_PWRBRK#", f"OAM{oam}_PRSNT0#",
        f"OAM{oam}_SMBus_SLV_D", f"OAM{oam}_SMBus_SLV_CLK",
    ]
    y = 150
    extra = []
    for p in ports:
        extra.append(f'''
	(hierarchical_label (at 25.4 {y} 0)
		(effects (font (size 1.27 1.27)) (justify left))
		(uuid "{uid()}")
		(shape bidirectional)
		"{p}"
	)
''')
        y += 5.08
    path.write_text(existing + "".join(extra) + "\n)\n")


def write_unmapped_sheet(rows: list[dict]) -> None:
    unmapped = sorted({(r["connector"], r["pin"], r["signal"]) for r in rows if is_unmapped(r["signal"])})
    lines = [
        "Pads explicitly UNMAPPED on this stub (no net, no copper).",
        "They are named in the v1.0 generic map but are reserved, do-not-use, or TEST pins",
        "whose AMD MI250X function is Unknown. Do not invent pullups or straps.",
        "",
    ]
    for conn, pad, sig in unmapped:
        lines.append(f"{conn} {pad:4s}  {sig}")
    write_text_sheet("sheets/05_unmapped_amd.kicad_sch", "Unmapped / AMD-unknown pads", "\n".join(lines))


def write_do_not_fab_sheet() -> None:
    text = """GATE LIST — all must be closed before fabrication or applying power to an MI250X.

1. 48V source identified AND harnessed to P48V pads (not Dell D3000E-S1 12V CRPS).
2. Molex 218910-1115 voltage rating vs P48V (Farnell sheet 30 V max vs OCP 44–59.5 V) resolved.
3. Connector gender/stack: hermaphroditic 2189101115 mates with itself, 5 mm stack — geometry OK;
   still confirm PIN A3 orientation on a plot before tape-out.
4. Cooling exists (OEM air HS or documented liquid). Do not clamp a custom cold plate on bare die.
   Chassis must leave replaceable cooling. Air-heatsink height is still Unknown.
5. AMD overlay unknowns listed (TEST*, dual-GCD PCIe, SMBus map, P12V2 need, xGMI S1–S7).
6. Dual NH-U14S DX-3647 vs X11DPH-T socket pitch: Unknown. Do not freeze sheet metal on placeholders.
7. PCIe path: Gen3 host, no verified CEM adapter, no retimer BOM. Enumeration not closed.
8. HOST_PWRGD sequencing vs P48V/P12V1/P3V3 in-spec — implement only from OCP + AMD overlay.

Until then this KiCad tree is a mapping artifact, not a board you send to a fab.
"""
    write_text_sheet("sheets/00_do_not_fabricate.kicad_sch", "DO NOT FABRICATE", text)


def parse_footprint_pads() -> tuple[str, list[str]]:
    raw = FOOTPRINT_SRC.read_text()
    # Keep header lines until first numbered pad; we re-emit pads with nets.
    return raw, re.findall(r'\(pad "([A-Z]+\d+)" smd circle \(at ([^)]+)\) \(size ([^)]+)\) \(layers ([^)]+)\)\)', raw)


def write_pcb(rows: list[dict]) -> None:
    """4-layer mechanical+mapped board. No signal tracks. No P48V plane pour."""
    raw, pads = parse_footprint_pads()
    # placements copied from ChassisEnvelope 2-GPU board (Verified Figure 2 centers + 20 mm margin).
    seats = [
        # (oam, conn, ref, x, y, rot)
        (0, "Conn0", "J0_Conn0", 71.500, 154.000, 180),
        (0, "Conn1", "J0_Conn1", 71.500, 52.000, 180),
        (1, "Conn0", "J1_Conn0", 174.500, 154.000, 180),
        (1, "Conn1", "J1_Conn1", 174.500, 52.000, 180),
    ]
    holes = [
        ("H01", 26.500, 154.000), ("H02", 116.500, 154.000),
        ("H03", 26.500, 52.000), ("H04", 116.500, 52.000),
        ("H11", 129.500, 154.000), ("H12", 219.500, 154.000),
        ("H13", 129.500, 52.000), ("H14", 219.500, 52.000),
    ]

    pad_sig = {(r["connector"], r["pin"]): r["signal"] for r in rows}

    nets: dict[str, int] = {}
    def nid(name: str) -> int:
        if name not in nets:
            nets[name] = len(nets) + 1
        return nets[name]

    # Pre-register shared rails so numbers are stable.
    for n in ["GND", "P48V", "P12V1", "P12V2", "P3V3"]:
        nid(n)

    fp_blocks = []
    for oam, conn, ref, x, y, rot in seats:
        pad_lines = [
            '    (pad "" np_thru_hole circle (at -31.5000 -9.5000) (size 1.80 1.80) (drill 1.80) (layers "*.Cu" "*.Mask"))',
            '    (pad "" np_thru_hole circle (at 31.5000 -9.5000) (size 1.80 1.80) (drill 1.80) (layers "*.Cu" "*.Mask"))',
        ]
        for pad, at, size, layers in pads:
            sig = pad_sig.get((conn, pad))
            extra = ""
            if sig:
                n = net_name(oam, sig)
                if n:
                    extra = f' (net {nid(n)} "{n}")'
            pad_lines.append(
                f'    (pad "{pad}" smd circle (at {at}) (size {size}) (layers {layers}){extra})'
            )
        fp_blocks.append(f'''  (footprint "footprints:218910-1115_candidate" (layer "F.Cu") (at {x} {y} {rot})
    (descr "v1.0 mapped geometry candidate — DO NOT FABRICATE")
    (property "Reference" "{ref}" (at 0 -14) (layer "F.SilkS") (effects (font (size 1.2 1.2) (thickness 0.15))))
    (property "Value" "218910-1115" (at 0 14) (layer "F.Fab") (effects (font (size 1 1) (thickness 0.15))))
    (property "Sheetfile" "MI250X_2OAM_v10_Stub.kicad_sch" (at 0 0) (layer "F.Fab") (effects (font (size 1 1)) hide))
    (fp_text user "OAM{oam} {conn} v1.0 names; unmapped pads have no net" (at 0 0) (layer "Cmts.User")
      (effects (font (size 0.8 0.8) (thickness 0.1))))
{chr(10).join(pad_lines)}
  )''')

    net_decls = "\n".join(f'  (net {i} "{name}")' for name, i in sorted(nets.items(), key=lambda kv: kv[1]))
    hole_blocks = []
    for ref, hx, hy in holes:
        hole_blocks.append(
            f'''  (footprint "NPTH_3.9_Fig2" (layer "F.Cu") (at {hx} {hy})
    (property "Reference" "{ref}" (at 0 -4) (layer "F.Fab") (effects (font (size 1 1) (thickness 0.15))))
    (property "Value" "NPTH_3.9" (at 0 4) (layer "F.Fab") (effects (font (size 0.8 0.8) (thickness 0.12))))
    (pad "" np_thru_hole circle (at 0 0) (size 8.00 8.00) (drill 3.90) (layers "*.Cu" "*.Mask"))
  )'''
        )

    pcb = f'''(kicad_pcb (version {PCB_VER}) (generator "buyable_first_system_v1")
  (general (thickness 1.6))
  (paper "A3")
  (layers
    (0 "F.Cu" signal)
    (1 "In1.Cu" power)
    (2 "In2.Cu" power)
    (31 "B.Cu" signal)
    (37 "F.SilkS" user)
    (36 "B.SilkS" user)
    (39 "F.Mask" user)
    (38 "B.Mask" user)
    (41 "Cmts.User" user)
    (40 "Dwgs.User" user)
    (44 "Edge.Cuts" user)
    (45 "F.CrtYd" user)
    (49 "F.Fab" user)
  )
  (setup
    (pad_to_mask_clearance 0)
    (stackup
      (layer "F.Cu" (type "copper") (thickness 0.035))
      (layer "dielectric 1" (type "core") (thickness 0.2) (material "FR4") (epsilon_r 4.5) (loss_tangent 0.02))
      (layer "In1.Cu" (type "copper") (thickness 0.035))
      (layer "dielectric 2" (type "core") (thickness 1.065) (material "FR4") (epsilon_r 4.5) (loss_tangent 0.02))
      (layer "In2.Cu" (type "copper") (thickness 0.035))
      (layer "dielectric 3" (type "core") (thickness 0.2) (material "FR4") (epsilon_r 4.5) (loss_tangent 0.02))
      (layer "B.Cu" (type "copper") (thickness 0.035))
    )
  )
{net_decls}
  (gr_rect (start 0 0) (end 246.000 206.000)
    (stroke (width 0.2) (type solid)) (fill none) (layer "Edge.Cuts"))
  (gr_text "DO NOT FABRICATE — 2-OAM v1.0 named-net stub — no P48V pour — no signal tracks on unmapped pads"
    (at 123.000 8) (layer "Cmts.User")
    (effects (font (size 2.0 2.0) (thickness 0.25))))
  (gr_text "4-layer: F.Cu / In1 / In2 / B.Cu. Inners reserved; P48V copper NOT poured (Molex 30V vs OCP 48V open)."
    (at 123.000 14) (layer "Cmts.User")
    (effects (font (size 1.4 1.4) (thickness 0.2))))
  (gr_rect (start 20.500 20.500) (end 122.500 185.500) (stroke (width 0.15) (type solid)) (fill none) (layer "Dwgs.User"))
  (gr_rect (start 123.500 20.500) (end 225.500 185.500) (stroke (width 0.15) (type solid)) (fill none) (layer "Dwgs.User"))
{chr(10).join(hole_blocks)}
{chr(10).join(fp_blocks)}
)
'''
    (ROOT / "MI250X_2OAM_v10_Stub.kicad_pcb").write_text(pcb)

    # Human netlist
    nl = ROOT / "netlist/named_nets.csv"
    with nl.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["net", "oam", "connector", "pads"])
        grouped = defaultdict(list)
        for r in rows:
            for oam in (0, 1):
                n = net_name(oam, r["signal"])
                if n:
                    grouped[(n, oam, r["connector"])].append(r["pin"])
        for (n, oam, conn), plist in sorted(grouped.items()):
            w.writerow([n, oam, conn, " ".join(plist)])


def write_project() -> None:
    (ROOT / "fp-lib-table").write_text(
        '(fp_lib_table\n  (lib (name "footprints")(type "KiCad")(uri "${KIPRJMOD}/footprints")(options "")(descr "Molex 218910-1115 geometry candidate"))\n)\n'
    )
    (ROOT / "sym-lib-table").write_text(
        '(sym_lib_table\n  (lib (name "OAM_v10_mapped")(type "KiCad")(uri "${KIPRJMOD}/symbols/OAM_v10_mapped.kicad_sym")(options "")(descr "v1.0 OCP generic named pads"))\n)\n'
    )
    pro = {
        "board": {
            "design_settings": {
                "defaults": {
                    "board_outline_line_width": 0.1,
                    "copper_line_width": 0.2,
                    "courtyard_line_width": 0.05,
                    "silk_line_width": 0.12,
                },
                "rules": {},
                "track_widths": [0.2, 0.5, 1.0],
                "via_dimensions": [{"diameter": 0.6, "drill": 0.3}],
            }
        },
        "boards": [],
        "cvpcb": {"equivalence_files": []},
        "libraries": {"pinned_footprint_libs": [], "pinned_symbol_libs": []},
        "meta": {"filename": "MI250X_2OAM_v10_Stub.kicad_pro", "version": 3},
        "net_settings": {"classes": [], "meta": {"version": 0}},
        "pcbnew": {"last_paths": {"netlist": "", "plot": ""}, "page_layout_descr_file": ""},
        "schematic": {"annotate_start_num": 0},
        "sheets": [
            ["MI250X_2OAM_v10_Stub.kicad_sch", "Root"],
            ["sheets/00_do_not_fabricate.kicad_sch", "00_DO_NOT_FABRICATE"],
            ["sheets/01_power_clock_reset.kicad_sch", "01_Power_Clock_Reset"],
            ["sheets/02_host_pcie_stub.kicad_sch", "02_Host_PCIe_Stub"],
            ["sheets/03_oam0_connectors.kicad_sch", "03_OAM0_Connectors"],
            ["sheets/04_oam1_connectors.kicad_sch", "04_OAM1_Connectors"],
            ["sheets/05_unmapped_amd.kicad_sch", "05_Unmapped_AMD"],
        ],
        "text_variables": {
            "DO_NOT_FABRICATE": "true",
            "PINMAP": "OAM Pin map rev 1.0.xlsx OCP Generic Pin Map",
        },
    }
    (ROOT / "MI250X_2OAM_v10_Stub.kicad_pro").write_text(json.dumps(pro, indent=2) + "\n")


def write_ipc_netlist(rows: list[dict]) -> None:
    """Simple pad-to-net list (not a fab netlist)."""
    lines = [
        "# Open-MI250X 2-OAM v1.0 named-net stub",
        "# NOT a fabrication netlist. Unmapped pads omitted.",
        "# Format: ref.pad  net",
    ]
    for oam, conn, ref in [
        (0, "Conn0", "J0_Conn0"), (0, "Conn1", "J0_Conn1"),
        (1, "Conn0", "J1_Conn0"), (1, "Conn1", "J1_Conn1"),
    ]:
        for r in rows:
            if r["connector"] != conn:
                continue
            n = net_name(oam, r["signal"])
            if n:
                lines.append(f"{ref}.{r['pin']}\t{n}")
    (ROOT / "netlist/MI250X_2OAM_v10_Stub.net").write_text("\n".join(lines) + "\n")


def main() -> None:
    rows = load_pinmap()
    write_classification_csv(rows)
    write_symbol_lib(rows)
    write_project()
    write_root_sch()
    write_do_not_fab_sheet()
    write_power_clock_sheet()
    write_pcie_sheet()
    write_oam_connector_sheet(0, "sheets/03_oam0_connectors.kicad_sch")
    write_oam_connector_sheet(1, "sheets/04_oam1_connectors.kicad_sch")
    write_unmapped_sheet(rows)
    write_pcb(rows)
    write_ipc_netlist(rows)
    meta = {
        "pinmap_csv": str(PINMAP.relative_to(REPO)),
        "named_pads": len(rows),
        "unmapped_signal_names": sorted({r["signal"] for r in rows if is_unmapped(r["signal"])}),
        "shared_rails": sorted(SHARED_RAILS),
        "do_not_fabricate": True,
        "layers": 4,
        "oam_seats": 2,
        "connectors_per_seat": 2,
        "molex_mpn": "218910-1115",
        "molex_mates_with": "2189101115 (hermaphroditic, self-mating)",
        "p3v3_count_conn0": sum(1 for r in rows if r["connector"] == "Conn0" and r["signal"] == "P3V3"),
    }
    (ROOT / "netlist/generation_meta.json").write_text(json.dumps(meta, indent=2) + "\n")
    print("generated", ROOT)


if __name__ == "__main__":
    main()
