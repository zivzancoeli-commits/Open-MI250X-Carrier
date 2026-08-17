#!/usr/bin/env python3
"""Generate the 2-OAM v1.0-mapped FullSend research KiCad project.

Copied tree from Rev2_MI250X_Carrier_BuyableFirstSystem_v1. Production Rev2
trees are not overwritten.

Source of pin names: 22_Pinmap_Research/extracted/OAM_v1.0_OCP_Generic_Pin_Map.csv
(xlsx wins if they disagree).

Rules:
- Do not invent AMD/OCP pin functions.
- Wire only nets named in the v1.0 map.
- TEST*/RFU/DO_NOT_USE stay unmapped (no copper / no-connect).
- PVREF is a module OUTPUT — never driven from the carrier.
- P48V and GND may share inner planes because those names exist on the v1.0 map.
  Never pour P12V1 / P12V2 / P3V3 onto the P48V plane.
- 8-OAM keepout is documentation / chassis volume, not an 8-GPU electrical board.
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
	(property "Reference" "#PWR" (at 0 -3.81 0) (effects (font (size 1.27 1.27)) (hide yes)))
	(property "Value" "{name}" (at 0 {y_off} 0) (effects (font (size 1.27 1.27))))
	(property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))
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
        f'(kicad_symbol_lib (version {SYM_VER}) (generator "fullsend_research_v1")\n'
        + conn0
        + "\n"
        + conn1
        + "\n)\n"
    )
    (ROOT / "symbols/OAM_v10_mapped.kicad_sym").write_text(text)


def sch_header(title: str, comment: str) -> str:
    return f'''(kicad_sch (version {SCH_VER}) (generator "fullsend_research_v1")
	(generator_version "9.0")
	(uuid "{uid()}")
	(paper "A3")
	(title_block
		(title "{kicad_escape(title)}")
		(date "2026-08-17")
		(rev "FullSendResearch_v1")
		(comment 1 "DO NOT FABRICATE. DO NOT ENERGIZE MI250X.")
		(comment 2 "{kicad_escape(comment)}")
		(comment 3 "Pin names: OAM Pin map rev 1.0.xlsx — OCP generic, NOT AMD overlay")
		(comment 4 "r2.0 maps UNUSABLE. P3V3=2 Conn0. Full-send cart is NOT a fab decision.")
	)
'''


def write_root_sch() -> None:
    p = ROOT / "MI250X_2OAM_v10_Stub.kicad_sch"
    body = sch_header(
        "2-OAM v1.0-mapped stub (NOT fab-ready)",
        "Mechanical + power + clock + reset + PCIe stub only",
    )

    def sheet(x, y, name, rel):
        return f'''	(sheet
		(at {x} {y})
		(size 70 40)
		(exclude_from_sim no)
		(in_bom yes)
		(on_board yes)
		(dnp no)
		(stroke (width 0.1524) (type solid))
		(fill (color 0 0 0 0.0000))
		(uuid "{uid()}")
		(property "Sheetname" "{name}" (at {x + 2.54} {y - 2.54} 0)
			(effects (font (size 1.27 1.27)) (justify left bottom)))
		(property "Sheetfile" "{rel}" (at {x + 2.54} {y + 42.54} 0)
			(effects (font (size 1.27 1.27)) (justify left top)))
	)
'''

    body += f'''
	(lib_symbols
	)

	(text "DO NOT FABRICATE / DO NOT ENERGIZE\\nThis project maps OCP generic v1.0 named pads onto 2 OAM seats.\\nIt is NOT an AMD MI250X NDA overlay. It is NOT PCBWay-ready.\\nInner planes: In1=P48V, In2=GND (v1.0 named pads only). No 12V/3.3V on P48V.\\nBlockers: Molex 30V datasheet vs OCP/OEM 48-54V use; 48V harness; cooling HS;\\ndual-GCD host PCIe vs X11DPH-T Gen3; AMD TEST* straps; P12V2 on 48V modules.\\nPVREF is a MODULE OUTPUT - never drive from the carrier.\\nTEST*/RFU/DO_NOT_USE pads have no nets.\\nSerDes S1-S7 are named in v1.0 but NOT routed (AMD xGMI overlay unknown).\\n8-OAM keepout is chassis volume (UBB v1.5 417x585 mm), not 8 electrical seats."
		(at 25.4 20.32 0)
		(effects (font (size 2.54 2.54) (thickness 0.4)) (justify left top))
		(uuid "{uid()}")
	)

{sheet(25.4, 90, "00_DO_NOT_FABRICATE", "sheets/00_do_not_fabricate.kicad_sch")}
{sheet(110, 90, "01_Power_Clock_Reset", "sheets/01_power_clock_reset.kicad_sch")}
{sheet(195, 90, "02_Host_PCIe_Stub", "sheets/02_host_pcie_stub.kicad_sch")}
{sheet(25.4, 145, "03_OAM0_Connectors", "sheets/03_oam0_connectors.kicad_sch")}
{sheet(110, 145, "04_OAM1_Connectors", "sheets/04_oam1_connectors.kicad_sch")}
{sheet(195, 145, "05_Unmapped_AMD", "sheets/05_unmapped_amd.kicad_sch")}
{sheet(25.4, 200, "06_Eight_Seat_Keepout", "sheets/06_eight_seat_keepout.kicad_sch")}
)
'''
    p.write_text(body)


def write_text_sheet(rel: str, title: str, text: str) -> None:
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    escaped = kicad_escape(text).replace("\n", "\\n")
    path.write_text(
        sch_header(title, "Documentation sheet - no invented nets")
        + f'''
	(text "{escaped}"
		(at 20.32 20.32 0)
		(effects (font (size 1.5 1.5)) (justify left top))
		(uuid "{uid()}")
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
        OCP v1.5 § power: "Only five P12V power pins are mandatory when the supply power is 48V
        (16 pins), and the rest of the P12V pins can be NC." That is generic OCP, not AMD MI250X.
        Whether this specific 48 V MI250X needs P12V2 live remains AMD-unknown. Do NOT short P12V1
        to P12V2. Do NOT pour P12V onto the P48V plane.
- P3V3  Conn0 C1,C2    3.3 V up to 5 W. Required. 2 pins — matches v1.5 Table 4; r2.0 has 6.
- GND   Conn0 334 pads
- PVREF Conn0 G1,G2    MODULE OUTPUT 1.5–3.3 V, max 0.5 A. NEVER drive from carrier. Per-OAM nets.

CLOCK / RESET (Conn0 unless noted):
- PE_REFCLKP/N  F45/F46   100 MHz PCIe refclk INPUT to module. Stub only — no clock-gen IC invented.
- PERST#        D1        CEM-compliant PCIe reset, 3.3 V input.
- WARMRST#      D2        Vref. Pin list: NC for standard PCIe.
- HOST_PWRGD    H1        3.3 V input. OCP v1.5: Power Enable when P48V, P12V1/P12V2, P3V3
                          are in spec. 10k PD on the baseboard. Not sequenced in this stub.
- MODULE_PWRGD  H2        3.3 V output. Ready for PERST# deassert.
- PWRBRK#       C3        3.3 V input, CEM power brake.
- PRSNT0#       J4        Module present, 1k to GND on module. Weak PU on baseboard.
- PRSNT1#       Conn1 C63

P48V/GND inner planes exist because those nets are named on the v1.0 map. They do NOT
authorize energizing: Farnell 2189101115 still lists 30 V max; shipping SuperMicro UBB
uses 54 V on CBL-PWEX-1280 (UBB cable, not the mezz). Unresolved.

DO NOT: invent VRMs, mix Dell D3000E-S1 12 V CRPS into P48V, drive PVREF, or attach a
guessed clock chip. Never mix P48V with 12 V/3.3 V as one rail.
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
                      ("P3V3", "P3V3"), ("GND", "GND")]:
        flags.append(f'''
	(label "{net}"
		(at {x} 160 0)
		(effects (font (size 1.27 1.27)) (justify left bottom))
		(uuid "{uid()}")
	)
''')
        x += 25.4
    # hierarchical labels for clock/reset
    y = 190
    for lab in ["OAM0_PE_REFCLKP", "OAM0_PE_REFCLKN", "OAM0_PERST#", "OAM0_HOST_PWRGD",
                "OAM0_MODULE_PWRGD", "OAM0_PVREF", "OAM1_PE_REFCLKP", "OAM1_PE_REFCLKN",
                "OAM1_PERST#", "OAM1_HOST_PWRGD", "OAM1_MODULE_PWRGD", "OAM1_PVREF"]:
        flags.append(f'''
	(hierarchical_label "{lab}"
		(shape bidirectional)
		(at 30.48 {y} 0)
		(effects (font (size 1.27 1.27)) (justify left))
		(uuid "{uid()}")
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
Lane order, polarity invert, and dual-GCD (1x16 vs 2x8 vs 2x16) need the AMD overlay.
PE_BIF[1:0] on Conn1 report bifurcation; functions are OCP-named, AMD default Unknown.

Dual-GCD host PCIe (evidence, not a pin overlay):
- AMD Instinct system-acceptance: 2 GCDs per OAM, PCI 1002:740c, 4-OAM node shows 8 lspci
  endpoints (2 per OAM). Verified from retrieved HTML.
- ROCm MI250 microarchitecture: "Each GCD maintains its own PCIe x16 link to the host"
  (retrieved via research pipeline; /en/latest/ URL 404 this run, /docs-7.2.1/ was indexed).
- AMD product page / MI200 datasheet: "PCIe 4.0 x16" (singular). Do not invent PE lane split.

Host: SuperMicro X11DPH-T is PCIe Gen3 (3x x16 + 4x x8). MI250X is Gen4 and will downtrain.
Shipping SuperMicro MI250 path uses CBL-MCIO-1278S5FYB1 (4x MCIO-124p to 2x SlimSAS x8)
on an EPYC Gen4 UBB system — not a CEM card for X11DPH-T.
Commercial CEM x16 to dual SlimSAS 8i cards exist (TI CEM2SLIMSAS-EVM, ICY DOCK MB308A,
SLM-1773-8I) with redrivers; pinout is SFF-9402 storage, NOT proven as OAM host PE.
TI DS160PT801 is a real Gen4 8-lane retimer product. None of these close this carrier.

If each GCD needs x16, 2 OAMs imply 4 x16 endpoints and X11DPH-T has only 3 x16 slots.
That topology is not closed. Do not buy a PCIe switch as "the" solution this cart.
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
	(hierarchical_label "{lab}"
		(shape bidirectional)
		(at 25.4 {y:.2f} 0)
		(effects (font (size 1.016 1.016)) (justify left))
		(uuid "{uid()}")
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
	(hierarchical_label "{p}"
		(shape bidirectional)
		(at 25.4 {y} 0)
		(effects (font (size 1.27 1.27)) (justify left))
		(uuid "{uid()}")
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

Full-send shopping (host+desk+2x OAM in one cart) is a BUYING decision.
It is NOT a fab decision and NOT permission to energize OAMs.

1. 48V source identified AND harnessed to P48V pads (not Dell D3000E-S1 12V CRPS).
   Candidate brick: MEAN WELL RCP-2000-48 (Positronic PCIM34W13M400A1; sense pins 14/15).
   SuperMicro shipping UBB uses CBL-PWEX-1280 54V MicroFit 2x5 — UBB cable, not mezz.
2. Molex 218910-1115 voltage rating vs P48V still OPEN:
   Farnell sheet 30 V AC(RMS)/DC max vs OCP 44–59.5 V vs Molex marketing "supports 48V"
   vs SuperMicro AS-4124GQ-TNMI 54 V UBB. Do not invent a 12 V-to-OAM hack.
3. Connector gender/stack: hermaphroditic 2189101115 mates with itself, 5 mm stack — geometry OK;
   still confirm PIN A3 orientation on a plot before tape-out.
4. Cooling exists (OEM air HS that mates the OAM bolster). SuperMicro public PNs found:
   MCP-310-45802-0B (air shroud), MCP-240-45801-0N (stiffener), MCP-240-45809-0N (tray)
   are chassis parts, NOT a die-mating heatsink. No HPE spare HS PN retrieved.
   Do not clamp a custom cold plate on bare die.
5. AMD overlay unknowns (TEST*, dual-GCD PE mapping onto v1.0 PCIE_TX/RX pads,
   SMBus map, which S1–S7 are xGMI, P12V2 need on this 48 V module).
6. Dual NH-U14S DX-3647 vs X11DPH-T socket pitch: Unknown.
7. PCIe path: Gen3 host; commercial CEM↔SlimSAS cards exist but are SFF-9402 storage
   pinouts, not OAM host PE. Dual-GCD may be two endpoints per OAM (AMD docs).
8. HOST_PWRGD sequencing vs P48V/P12V1/P3V3 in-spec — 10k PD on baseboard (OCP);
   implement only from OCP + AMD overlay. Never drive PVREF from the carrier.

Until then this KiCad tree is a mapping artifact, not a board you send to PCBWay.
"""
    write_text_sheet("sheets/00_do_not_fabricate.kicad_sch", "DO NOT FABRICATE", text)


def write_eight_seat_sheet() -> None:
    text = """8-OAM / later chassis volume — NOT an 8-GPU electrical board.

This PCB has TWO electrical OAM seats. Unmapped AMD pads stay unmapped.
Do not treat 4x2 KOZ tiling as a Universal Baseboard.

Verified (OCP UBB Design Spec v1.5, retrieved via research pipeline):
- UBB PCB: 417 mm wide x 585 mm long x 3.2 mm thick.
- 8 OAM modules, 16 Mirror Mezz Pro connectors.
- 4x 54V power connectors (Amphenol 10028917-001LF) + 2x 12V (can be repurposed).
- OAM MODULE_ID[4:0] for 8x: OAM0=00000 ... OAM7=00111 (OCP table, not AMD).
- Module-to-module numeric pitch is in the spec FIGURES (not OCR'd as millimetres
  this run). Connector-to-connector pitch ON A MODULE is 102 mm (OAM v1.5 §6.1).

Inferred (do not drill from this):
- 4x2 tiling of 103 x 166 mm KOZ = 412 x 332 mm floor. That is NOT the UBB drawing.
- r2.0 UBB is 417 x 655 mm and uses r2.0 pinlists (P3V3=6) — UNUSABLE for MI250X.

Unknown:
- Public UBB schematic / gerber / AOM-MCM-Q pad overlay: NOT FOUND
  (github.com/opencomputeproject/OCP-SVR-OAI-Open_Accelerator_Infrastructure is a
  project page; no xlsx/gerber in the public tree retrieved this run).

First PCB = 2-OAM. Weld chassis bays for later 8-OAM volume using the 417 x 585 mm
UBB v1.5 envelope, not a fake 8-GPU netlist.
"""
    write_text_sheet("sheets/06_eight_seat_keepout.kicad_sch", "8-seat keepout (not electrical)", text)


def parse_footprint_pads() -> tuple[str, list[str]]:
    raw = FOOTPRINT_SRC.read_text()
    # Keep header lines until first numbered pad; we re-emit pads with nets.
    return raw, re.findall(r'\(pad "([A-Z]+\d+)" smd circle \(at ([^)]+)\) \(size ([^)]+)\) \(layers ([^)]+)\)\)', raw)


def write_pcb(rows: list[dict]) -> None:
    """4-layer 2-OAM board. P48V on In1, GND on In2. No 12V/3.3V on P48V. No signal tracks."""
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

    gnd_id = nid("GND")
    p48_id = nid("P48V")
    # UBB v1.5 >40 V internal clearance 25 mil = 0.635 mm.
    p48_clear = 0.64
    gnd_clear = 0.25

    def zone(net_id: int, net_name: str, layer: str, clearance: float, zuid: str) -> str:
        return f'''  (zone (net {net_id}) (net_name "{net_name}") (layer "{layer}") (uuid "{zuid}")
    (hatch edge 0.5)
    (priority 0)
    (connect_pads yes (clearance {clearance}))
    (min_thickness 0.25)
    (filled_areas_thickness no)
    (fill yes (thermal_gap {clearance}) (thermal_bridge_width 0.5))
    (polygon (pts (xy 2 2) (xy 244 2) (xy 244 204) (xy 2 204)))
  )'''

    # Later 8-OAM chassis volume (UBB v1.5 417x585) drawn on Dwgs.User, centered on this 246x206 board.
    ubb_x0 = (246.0 - 417.0) / 2
    ubb_y0 = (206.0 - 585.0) / 2
    koz8_x0 = (246.0 - 412.0) / 2
    koz8_y0 = (206.0 - 332.0) / 2

    pcb = f'''(kicad_pcb (version {PCB_VER}) (generator "fullsend_research_v1")
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
  (gr_text "DO NOT FABRICATE - DO NOT ENERGIZE OAMs"
    (at 123.000 10) (layer "F.SilkS")
    (effects (font (size 4.0 4.0) (thickness 0.5))))
  (gr_text "2-OAM v1.0 named nets only. Unmapped TEST/RFU/DO_NOT_USE have no net. Not PCBWay-ready."
    (at 123.000 18) (layer "F.SilkS")
    (effects (font (size 1.5 1.5) (thickness 0.2))))
  (gr_text "In1.Cu = P48V   In2.Cu = GND   P12V1/P12V2/P3V3 are NOT on the 48V plane"
    (at 123.000 198) (layer "F.SilkS")
    (effects (font (size 1.4 1.4) (thickness 0.18))))
  (gr_text "Full-send shopping is not a fab decision. Molex 30V datasheet vs OCP 48V still OPEN."
    (at 123.000 24) (layer "Cmts.User")
    (effects (font (size 1.3 1.3) (thickness 0.18))))
  (gr_rect (start 20.500 20.500) (end 122.500 185.500) (stroke (width 0.15) (type solid)) (fill none) (layer "Dwgs.User"))
  (gr_rect (start 123.500 20.500) (end 225.500 185.500) (stroke (width 0.15) (type solid)) (fill none) (layer "Dwgs.User"))
  (gr_text "OAM0 KOZ 103x166" (at 71.5 28) (layer "Dwgs.User") (effects (font (size 1.2 1.2) (thickness 0.15))))
  (gr_text "OAM1 KOZ 103x166" (at 174.5 28) (layer "Dwgs.User") (effects (font (size 1.2 1.2) (thickness 0.15))))
  (gr_rect (start {ubb_x0:.3f} {ubb_y0:.3f}) (end {ubb_x0 + 417:.3f} {ubb_y0 + 585:.3f})
    (stroke (width 0.3) (type dash)) (fill none) (layer "Dwgs.User"))
  (gr_text "LATER 8-OAM CHASSIS VOLUME: OCP UBB v1.5 417 x 585 mm (Verified). NOT this PCB. NOT 8 electrical seats."
    (at 123.000 {ubb_y0 + 8:.3f}) (layer "Dwgs.User")
    (effects (font (size 1.6 1.6) (thickness 0.2))))
  (gr_rect (start {koz8_x0:.3f} {koz8_y0:.3f}) (end {koz8_x0 + 412:.3f} {koz8_y0 + 332:.3f})
    (stroke (width 0.2) (type dash)) (fill none) (layer "Dwgs.User"))
  (gr_text "INFERRED 4x2 KOZ tiling 412 x 332 mm - do not treat as a UBB drawing"
    (at 123.000 {koz8_y0 + 8:.3f}) (layer "Dwgs.User")
    (effects (font (size 1.2 1.2) (thickness 0.15))))
{chr(10).join(hole_blocks)}
{chr(10).join(fp_blocks)}
{zone(p48_id, "P48V", "In1.Cu", p48_clear, uid())}
{zone(gnd_id, "GND", "In2.Cu", gnd_clear, uid())}
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
        "net_settings": {
            "classes": [
                {"name": "Default", "clearance": 0.2, "track_width": 0.25},
                {"name": "P48V", "clearance": 0.64, "track_width": 1.0, "nets": ["P48V"]},
                {"name": "GND", "clearance": 0.25, "track_width": 0.5, "nets": ["GND"]},
            ],
            "meta": {"version": 2},
        },
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
            ["sheets/06_eight_seat_keepout.kicad_sch", "06_Eight_Seat_Keepout"],
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
    write_eight_seat_sheet()
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
        "inner_planes": {"In1.Cu": "P48V", "In2.Cu": "GND"},
        "p12v_not_on_p48v_plane": True,
        "eight_seat_electrical": False,
        "ubb_v15_envelope_mm": [417, 585],
        "kicad_cli": "9.0.9",
    }
    (ROOT / "netlist/generation_meta.json").write_text(json.dumps(meta, indent=2) + "\n")
    print("generated", ROOT)


if __name__ == "__main__":
    main()
