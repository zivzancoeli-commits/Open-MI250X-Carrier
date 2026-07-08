#!/usr/bin/env python3
"""Generate hierarchical KiCad 9 prototype carrier project for MI250X OAM.

Uses OCP OAM specification signal names where verified.
AMD-specific and pin-number mappings remain TODO.
"""

from __future__ import annotations

import json
import uuid
from pathlib import Path
from textwrap import dedent

ROOT = Path(__file__).resolve().parents[1] / "Rev1_MI250X_Carrier"
SCH_VERSION = 20250114
PRO_VERSION = 20250114


def uid() -> str:
    return str(uuid.uuid4())


def sch_header(title: str, comment1: str = "") -> list[str]:
    lines = [
        f'(kicad_sch (version {SCH_VERSION}) (generator "open-mi250x-carrier-generator")',
        "",
        f'\t(uuid "{uid()}")',
        "",
        '\t(paper "A3")',
        "",
        "\t(title_block",
        '\t\t(title "Open MI250X Carrier Rev1")',
        f'\t\t(date "2026-07-07")',
        f'\t\t(rev "0.1-prototype")',
        f'\t\t(comment 1 "{comment1}")',
        f'\t\t(comment 2 "{title}")',
        '\t\t(comment 3 "Evidence: OCP OAM Design Spec v1.5; AMD MI250X OAM")',
        '\t\t(comment 4 "AMD-specific nets marked TODO — do not route until verified")',
        "\t)",
        "",
        "\t(lib_symbols",
    ]
    return lines


def text_note(x: float, y: float, text: str, size: float = 1.27) -> str:
    escaped = text.replace('"', '\\"').replace("\n", "\\n")
    return dedent(
        f"""
        (text (at {x} {y} 0)
        \t(effects (font (size {size} {size})) (justify left top))
        \t(uuid "{uid()}")
        \t"{escaped}"
        )
    """
    ).strip()


def hierarchical_label(x: float, y: float, name: str, shape: str, size: float = 1.27) -> str:
    return dedent(
        f"""
        (hierarchical_label (at {x} {y} 0) (fields_autoplaced)
        \t(effects (font (size {size} {size})) (justify right))
        \t(uuid "{uid()}")
        \t(shape {shape})
        \t"{name}"
        )
    """
    ).strip()


def sheet_pin(x: float, y: float, name: str, pin_type: str) -> str:
    return dedent(
        f"""
        (pin "{name}" {pin_type}
        \t(at {x} {y} 0)
        \t(effects (font (size 1.27 1.27)))
        \t(uuid "{uid()}")
        )
    """
    ).strip()


def sheet_instance(x: float, y: float, w: float, h: float, name: str, file: str, pins: list[tuple[str, str, float, float]]) -> str:
    pin_lines = "\n".join(sheet_pin(px, py, pname, ptype) for pname, ptype, px, py in pins)
    return dedent(
        f"""
        (sheet (at {x} {y}) (size {w} {h}) (fields_autoplaced)
        \t(stroke (width 0.1524) (type solid))
        \t(fill (color 0 0 0 0.0000))
        \t(uuid "{uid()}")
        \t(property "Sheetname" "{name}"
        \t\t(at {x + 2.54} {y - 2.54} 0)
        \t\t(effects (font (size 1.27 1.27)) (justify left bottom))
        \t\t(uuid "{uid()}")
        \t)
        \t(property "Sheetfile" "{file}"
        \t\t(at {x + 2.54} {y + h + 2.54} 0)
        \t\t(effects (font (size 1.27 1.27)) (justify left top))
        \t\t(uuid "{uid()}")
        \t)
        {pin_lines}
        )
    """
    ).strip()


def sym_power_gnd() -> str:
    return dedent(
        f"""
        (symbol "power:+12V" (power) (pin_names (offset 0)) (in_bom yes) (on_board yes)
        \t(property "Reference" "#PWR" (at 0 -3.81 0) (effects (font (size 1.27 1.27)) hide))
        \t(property "Value" "+12V" (at 0 3.556 0) (effects (font (size 1.27 1.27))))
        \t(property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
        \t(symbol "+12V_0_1"
        \t\t(pin power_in line (at 0 0 90) (length 0) (name "+12V" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        \t)
        )
        (symbol "power:+3V3" (power) (pin_names (offset 0)) (in_bom yes) (on_board yes)
        \t(property "Reference" "#PWR" (at 0 -3.81 0) (effects (font (size 1.27 1.27)) hide))
        \t(property "Value" "+3V3" (at 0 3.556 0) (effects (font (size 1.27 1.27))))
        \t(property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
        \t(symbol "+3V3_0_1"
        \t\t(pin power_in line (at 0 0 90) (length 0) (name "+3V3" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        \t)
        )
        (symbol "power:GND" (power) (pin_names (offset 0)) (in_bom yes) (on_board yes)
        \t(property "Reference" "#PWR" (at 0 -6.35 0) (effects (font (size 1.27 1.27)) hide))
        \t(property "Value" "GND" (at 0 -3.81 0) (effects (font (size 1.27 1.27))))
        \t(property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
        \t(symbol "GND_0_1"
        \t\t(pin power_in line (at 0 0 270) (length 0) (name "GND" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        \t)
        )
        """
    ).strip()


def sym_connector(ref: str, value: str, pins: list[str]) -> str:
    pin_defs = []
    for i, pname in enumerate(pins, start=1):
        y = (i - 1) * 2.54
        pin_defs.append(
            f'(pin passive line (at -5.08 {y} 0) (length 2.54) '
            f'(name "{pname}" (effects (font (size 1.27 1.27)))) '
            f'(number "{i}" (effects (font (size 1.27 1.27)))))'
        )
    body_h = max(5.08, (len(pins) - 1) * 2.54 + 2.54)
    return dedent(
        f"""
        (symbol "{value}" (pin_names (offset 1.016)) (in_bom yes) (on_board yes)
        \t(property "Reference" "{ref}" (at 0 {body_h + 2.54} 0) (effects (font (size 1.27 1.27))))
        \t(property "Value" "{value}" (at 0 {body_h + 5.08} 0) (effects (font (size 1.27 1.27))))
        \t(property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
        \t(symbol "{value}_0_1"
        \t\t(rectangle (start -2.54 -2.54) (end 2.54 {body_h})
        \t\t\t(stroke (width 0.254) (type default))
        \t\t\t(fill (type background))
        \t\t)
        \t\t{chr(10).join(pin_defs)}
        \t)
        )
        """
    ).strip()


def sym_instance(lib_id: str, ref: str, value: str, x: float, y: float, props: dict[str, str] | None = None) -> str:
    props = props or {}
    prop_lines = [
        f'(property "Reference" "{ref}" (at {x} {y - 2.54} 0) (effects (font (size 1.27 1.27))))',
        f'(property "Value" "{value}" (at {x} {y + 2.54} 0) (effects (font (size 1.27 1.27))))',
        '(property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))',
    ]
    for k, v in props.items():
        prop_lines.append(
            f'(property "{k}" "{v}" (at {x} {y + 5.08} 0) (effects (font (size 1.27 1.27))))'
        )
    return dedent(
        f"""
        (symbol (lib_id "{lib_id}") (at {x} {y} 0) (unit 1) (exclude_from_sim no) (in_bom yes) (on_board yes) (dnp no)
        \t(uuid "{uid()}")
        \t{chr(10).join(prop_lines)}
        )
        """
    ).strip()


def write_sch(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)


def build_root() -> str:
    from host_pcie import root_pcie_sheet_pins

    notes = (
        "PURPOSE: Root hierarchy for single MI250X OAM prototype carrier.\\n"
        "ASSUMPTIONS: 12V input; PCIe Gen4 x16 host link; direct attach (no switch).\\n"
        "SOURCES: OCP Accelerator Module Design Specification v1.5; project AI_DESIGN_RULES.md\\n"
        "OPEN QUESTIONS: AMD MI250X rail currents; 54V/48V requirement; OAM pin spreadsheet."
    )
    pins_power = [
        ("VIN_12V", "input", 101.6, 25.4),
        ("OAM_12V", "output", 101.6, 50.8),
        ("OAM_P12V1", "output", 101.6, 76.2),
        ("OAM_P12V2", "output", 101.6, 101.6),
        ("MGMT_3V3", "output", 101.6, 127.0),
        ("LOGIC_3V3", "output", 101.6, 152.4),
        ("FAN_12V", "output", 101.6, 177.8),
        ("GND", "passive", 101.6, 203.2),
        ("OAM_EN_TODO", "output", 101.6, 228.6),
        ("OAM_PG_TODO", "input", 101.6, 254.0),
    ]
    pins_pcie = root_pcie_sheet_pins(177.8)
    pins_oam = root_pcie_sheet_pins(25.4)
    pins_mgmt = [
        ("I2C_SCL", "bidirectional", 254.0, 25.4),
        ("I2C_SDA", "bidirectional", 254.0, 50.8),
        ("PMBUS_SCL", "bidirectional", 254.0, 76.2),
        ("PMBUS_SDA", "bidirectional", 254.0, 101.6),
        ("SMBUS_CLK", "bidirectional", 254.0, 127.0),
        ("SMBUS_DATA", "bidirectional", 254.0, 152.4),
        ("SMBUS_ALERT_N", "bidirectional", 254.0, 177.8),
        ("DBG_UART_TX", "output", 254.0, 203.2),
        ("DBG_UART_RX", "input", 254.0, 228.6),
        ("TEMP_ALERT", "output", 254.0, 254.0),
        ("FAN_PWM_TODO", "passive", 254.0, 279.4),
    ]
    lines = sch_header("Root Schematic", "Hierarchical top level")
    lines.append(sym_power_gnd())
    lines.append("\t)")
    lines.append("")
    lines.append(text_note(25.4, 25.4, notes, 1.5))
    lines.append(sheet_instance(25.4, 40.64, 60.96, 80.0, "Power_System", "sheets/04_power_system.kicad_sch", pins_power))
    lines.append(sheet_instance(127.0, 40.64, 60.96, 220.0, "OAM_Interface", "sheets/02_oam_interface.kicad_sch", pins_oam + [
        ("OAM_12V", "input", 25.4, 25.4),
        ("OAM_P12V1", "input", 25.4, 50.8),
        ("OAM_P12V2", "input", 25.4, 76.2),
        ("LOGIC_3V3", "input", 25.4, 101.6),
        ("GND", "passive", 25.4, 127.0),
    ]))
    lines.append(sheet_instance(228.6, 40.64, 60.96, 220.0, "Host_PCIe", "sheets/03_host_pcie.kicad_sch", pins_pcie))
    lines.append(sheet_instance(330.2, 40.64, 60.96, 90.0, "Clocking_Reset", "sheets/05_clocking_reset.kicad_sch", [
        ("PE_REFCLKp", "bidirectional", 25.4, 25.4),
        ("PE_REFCLKn", "bidirectional", 25.4, 50.8),
        ("PERST_N", "bidirectional", 25.4, 76.2),
        ("HOST_REFCLKp", "bidirectional", 25.4, 101.6),
        ("HOST_REFCLKn", "bidirectional", 25.4, 127.0),
        ("PERST_HOST_N", "bidirectional", 25.4, 152.4),
        ("WARMRST_N_TODO", "passive", 25.4, 177.8),
        ("AUX_100M_REFCLKp_TODO", "passive", 25.4, 203.2),
        ("AUX_100M_REFCLKn_TODO", "passive", 25.4, 228.6),
        ("PERST_CONN1_N_TODO", "passive", 25.4, 254.0),
        ("MGMT_3V3", "input", 25.4, 279.4),
        ("GND", "passive", 25.4, 304.8),
        ("OAM_PG_TODO", "input", 25.4, 330.2),
    ]))
    lines.append(sheet_instance(25.4, 127.0, 60.96, 90.0, "Management", "sheets/06_management.kicad_sch", pins_mgmt + [
        ("MGMT_3V3", "input", 25.4, 25.4),
        ("GND", "passive", 25.4, 50.8),
    ]))
    from test_points_system import hierarchical_tp_inputs

    tp_pins = [(name, shape, 25.4, 25.4 + i * 12.7) for i, (name, shape) in enumerate(hierarchical_tp_inputs())]
    lines.append(sheet_instance(127.0, 127.0, 60.96, max(120.0, len(tp_pins) * 3.0), "Test_Points", "sheets/07_test_points.kicad_sch", tp_pins))
    from expansion_system import hierarchical_expansion_inputs

    exp_pins = [(name, shape, 25.4, 25.4 + i * 12.7) for i, (name, shape) in enumerate(hierarchical_expansion_inputs())]
    lines.append(sheet_instance(228.6, 127.0, 60.96, max(60.0, len(exp_pins) * 3.0), "Expansion", "sheets/08_expansion.kicad_sch", exp_pins))
    lines.append("\n\t(sheet_instances")
    lines.append('\t\t(path "/" (page "1"))')
    for i, name in enumerate(
        ["04_power_system", "02_oam_interface", "03_host_pcie", "05_clocking_reset", "06_management", "07_test_points", "08_expansion"],
        start=2,
    ):
        lines.append(f'\t\t(path "/{name.split("_", 1)[1].title().replace("_", "")}" (page "{i}"))')
    lines.append("\t)")
    lines.append("")
    lines.append(")")
    return "\n".join(lines)


def build_child(title: str, comment: str, notes: str, labels: list[tuple[float, float, str, str]]) -> str:
    lines = sch_header(title, comment)
    lines.append(sym_power_gnd())
    oam_pins = [
        "OAM_12V", "MGMT_3V3", "GND", "PE_REFCLKp", "PE_REFCLKn", "PERST_N",
        "SMBUS_CLK", "SMBUS_DATA", "OAM_PRESENT_N",
    ] + [f"PETp{i}" for i in range(16)] + [f"PETn{i}" for i in range(16)]
    lines.append(sym_connector("J", "OAM_MirrorMezz_Conn0_TODO", oam_pins[:12]))
    lines.append(sym_connector("U", "MCU_STM32G071_TODO", ["VDD", "GND", "I2C_SCL", "I2C_SDA", "UART_TX", "UART_RX"]))
    lines.append(sym_connector("U", "FRU_EEPROM_AT24C256", ["VCC", "GND", "SCL", "SDA", "WP"]))
    lines.append(sym_connector("U", "TEMP_TMP117", ["VCC", "GND", "SCL", "SDA", "ALERT"]))
    lines.append("\t)")
    lines.append("")
    lines.append(text_note(20.32, 17.78, notes, 1.4))
    for x, y, name, shape in labels:
        lines.append(hierarchical_label(x, y, name, shape))
    lines.append("")
    lines.append("\t(sheet_instances")
    lines.append(f'\t\t(path "/{title.split()[0]}" (page "1"))')
    lines.append("\t)")
    lines.append("")
    lines.append(")")
    return "\n".join(lines)


def build_oam_interface() -> str:
    from oam_mirror_mezz import OCP_SPEC, OCP_CONN_SECTION, MOLEX_MPNS, write_symbol_library

    write_symbol_library(ROOT / "symbols" / "MI250X-Carrier.kicad_sym")

    notes = dedent(
        f"""
        PURPOSE: MI250X OAM mating via 2x Molex Mirror Mezz Pro (688-pin each).
        OCP: {OCP_SPEC} {OCP_CONN_SECTION}; Table 4 OAM Pinouts.
        MPN examples: {MOLEX_MPNS} (confirm against physical MI250X module).
        CRITICAL: KiCad pin numbers are LOGICAL indices 1..688 — NOT Molex physical pads.
        Physical mapping: TODO — import OAM_Pinlist_Pinmap spreadsheet.
        Conn0 (J1): host PCIe x16, power, SMBus, presence, SerDes 1-3 per OCP §8.2.
        Conn1 (J2): 3.3V, JTAG, GPIO (AMD TODO), SerDes 4-7 per OCP §8.2.
        Do NOT route PHYS_PIN_TODO_* or GPIO_TODO_* until verified.
        """
    ).strip()

    ocp_comments = [
        (20.32, 120.0, f"OCP {OCP_SPEC} §6.2: Mezzanine connector — Molex Mirror Mezz Pro, 90 ohm, 688-pin BGA."),
        (20.32, 128.0, f"OCP §8.1: Module uses two 688-pin Mirror Mezz Pro connectors (Conn0 + Conn1)."),
        (20.32, 136.0, "OCP Table 4: PETp/n[15:0] host TX (module TX); AC coupling caps on carrier/baseboard."),
        (20.32, 144.0, "OCP Table 4: PERp/n[15:0] host RX (module RX); AC coupling on carrier/baseboard."),
        (20.32, 152.0, "OCP Table 4: PE_REFCLKp/n — 100MHz PCIe Gen5 compliant reference clock."),
        (20.32, 160.0, "OCP Table 4: PERST#, PRESNT#, SMBus_D/CLK/ALERT# on Conn0."),
        (20.32, 168.0, "OCP §8.2 Conn1: JTAG, GPIO, SerDes 4-7 — GPIO AMD-specific; do not assign."),
        (20.32, 176.0, "Physical pin numbers: TODO — OAM_Pinlist_Pinmap spreadsheet (not in repo)."),
    ]

    labels = [
        (20.0, 40.0, "OAM_12V", "input"),
        (20.0, 55.0, "OAM_P12V1", "input"),
        (20.0, 70.0, "OAM_P12V2", "input"),
        (20.0, 85.0, "LOGIC_3V3", "input"),
        (20.0, 100.0, "GND", "passive"),
    ]
    # PET/PER lanes + PCIe support — hierarchical to Host_PCIe via root
    from host_pcie import oam_lane_hierarchical_labels, support_hierarchical_labels

    y = 85.0
    for name, shape in oam_lane_hierarchical_labels("bidirectional"):
        labels.append((20.0, y, name, shape))
        y += 3.0
    for name, shape in support_hierarchical_labels():
        labels.append((20.0, y, name, shape))
        y += 5.0

    lines = sch_header("OAM Interface", "02_oam_interface")
    lines.append("\t)")
    lines.append("")
    lines.append(text_note(20.32, 17.78, notes, 1.35))
    for x, y, txt in ocp_comments:
        lines.append(text_note(x, y, txt, 1.15))
    for x, y, name, shape in labels:
        lines.append(hierarchical_label(x, y, name, shape))

    # J1 Conn0 — Molex Mirror Mezz Pro (OCP Conn0)
    lines.append(
        sym_instance_lib(
            "MI250X-Carrier:Molex_MirrorMezz_Conn0",
            "J1",
            "218910-1115",
            80.0,
            40.0,
            {
                "Datasheet": f"Molex Mirror Mezz Pro — {OCP_SPEC}",
                "MPN": "218910-1115 (alt 218916-1115)",
                "OCP_Connector": "Conn0",
                "OCP_PhysicalPinMap": "TODO — OAM_Pinlist_Pinmap",
                "Footprint": "TODO — Molex Mirror Mezz Pro 688",
            },
        )
    )
    # J2 Conn1 — Molex Mirror Mezz Pro (OCP Conn1)
    lines.append(
        sym_instance_lib(
            "MI250X-Carrier:Molex_MirrorMezz_Conn1",
            "J2",
            "218916-1115",
            180.0,
            40.0,
            {
                "Datasheet": f"Molex Mirror Mezz Pro — {OCP_SPEC}",
                "MPN": "218916-1115 (alt 218910-1115)",
                "OCP_Connector": "Conn1",
                "OCP_PhysicalPinMap": "TODO — OAM_Pinlist_Pinmap",
                "Footprint": "TODO — Molex Mirror Mezz Pro 688",
            },
        )
    )

    lines.append("")
    lines.append("\t(sheet_instances")
    lines.append('\t\t(path "/OAM_Interface" (page "1"))')
    lines.append("\t)")
    lines.append("")
    lines.append(")")
    return "\n".join(lines)


def sym_instance_lib(lib_id: str, ref: str, value: str, x: float, y: float, props: dict[str, str], dnp: bool = False) -> str:
    prop_lines = [
        f'(property "Reference" "{ref}" (at {x} {y - 2.54} 0) (effects (font (size 1.27 1.27))))',
        f'(property "Value" "{value}" (at {x} {y + 2.54} 0) (effects (font (size 1.27 1.27))))',
        '(property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))',
    ]
    for k, v in props.items():
        if k == "Footprint" and v:
            prop_lines[2] = f'(property "Footprint" "{v}" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))'
        else:
            prop_lines.append(
                f'(property "{k}" "{v}" (at {x} {y + 5.08} 0) (effects (font (size 1.27 1.27)) hide))'
            )
    dnp_flag = "yes" if dnp else "no"
    return dedent(
        f"""
        (symbol (lib_id "{lib_id}") (at {x} {y} 0) (unit 1) (exclude_from_sim no) (in_bom yes) (on_board yes) (dnp {dnp_flag})
        \t(uuid "{uid()}")
        \t{chr(10).join(prop_lines)}
        )
    """
    ).strip()


def build_host_pcie() -> str:
    from host_pcie import (
        OCP_SPEC,
        OCP_TABLE,
        PCIE_SPEC,
        LANE_COUNT,
        append_host_pcie_symbols,
        lane_mapping_todo_notes,
        oam_lane_hierarchical_labels,
        support_hierarchical_labels,
        support_signal_audit,
    )

    append_host_pcie_symbols(ROOT / "symbols" / "MI250X-Carrier.kicad_sym")

    notes = dedent(
        f"""
        PURPOSE: Host PCIe Gen4 x16 edge connector to OAM host link (PET/PER).
        HOST: {PCIE_SPEC} — PCIE_Ln_TX/RX_P/N lanes 0..{LANE_COUNT - 1}.
        OAM: {OCP_SPEC} {OCP_TABLE} — PETp/n, PERp/n lanes 0..{LANE_COUNT - 1}.
        MAPPING: Host TX (PCIE_Ln_TX) → OAM PERp/n; Host RX (PCIE_Ln_RX) ← OAM PETp/n.
        AC coupling on PET path per OCP baseboard rule — cap values TODO.
        NO physical CEM slot pins or OAM connector pins assigned on this sheet.
        AMD dual-GCD lane assignment — TODO (see lane mapping notes).
        """
    ).strip()

    ocp_comments = [
        (20.32, 95.0, f"OCP {OCP_TABLE}: PETp/n[15:0] = module TX (host RX); PERp/n[15:0] = module RX (host TX)."),
        (20.32, 103.0, f"OCP {OCP_TABLE}: PE_REFCLKp/n — 100 MHz PCIe reference clock."),
        (20.32, 111.0, f"OCP {OCP_TABLE}: PERST#, SMBus_D/CLK/ALERT#, PRESNT# on Conn0."),
        (20.32, 119.0, f"{PCIE_SPEC}: Host slot uses PCIE_Ln_TX_P/N and PCIE_Ln_RX_P/N per lane."),
        (20.32, 127.0, "CLKREQ# / WAKE#: PCIe CEM sidebands — NOT in OCP Table 4; marked TODO."),
        (20.32, 135.0, "AMD: GCD0/GCD1 lane bifurcation and lane index mapping — TODO."),
    ]

    audit = support_signal_audit()
    missing_txt = ", ".join(item["signal"] for item in audit["missing_or_todo"])
    ocp_comments.append((20.32, 143.0, f"Missing/TODO support signals: {missing_txt}"))

    lines = sch_header("Host PCIe", "03_host_pcie")
    lines.append("\t)")
    lines.append("")
    lines.append(text_note(20.32, 17.78, notes, 1.25))
    for x, y, txt in ocp_comments:
        lines.append(text_note(x, y, txt, 1.1))
    for idx, note in enumerate(lane_mapping_todo_notes()):
        lines.append(text_note(20.32, 151.0 + idx * 8.0, note, 1.05))

    # Host-facing hierarchical labels (left) — optional edge/riser hookup
    y = 40.0
    for i in range(LANE_COUNT):
        for suffix in ("TX_P", "TX_N", "RX_P", "RX_N"):
            lines.append(hierarchical_label(15.0, y, f"PCIE_L{i}_{suffix}", "bidirectional", 1.0))
            y += 2.8

    # OAM-facing hierarchical labels (right) — to OAM_Interface via root
    y = 40.0
    for name, shape in oam_lane_hierarchical_labels("output"):
        lines.append(hierarchical_label(270.0, y, name, shape, 1.0))
        y += 2.8
    for name, shape in support_hierarchical_labels():
        lines.append(hierarchical_label(270.0, y, name, shape, 1.0))
        y += 5.0

    lines.append(
        sym_instance_lib(
            "MI250X-Carrier:Host_PCIe_Slot_x16_Gen4",
            "J1",
            "PCIe_x16_Gen4_Host",
            60.0,
            45.0,
            {
                "Datasheet": PCIE_SPEC,
                "PhysicalPinMap": "TODO — host edge/riser pinout",
                "Footprint": "TODO — PCIe x16 edge or cable connector",
                "LaneCount": str(LANE_COUNT),
            },
        )
    )
    lines.append(
        sym_instance_lib(
            "MI250X-Carrier:OAM_PCIe_HostLink",
            "J2",
            "OAM_HostLink_PET_PER",
            160.0,
            45.0,
            {
                "Datasheet": f"{OCP_SPEC} {OCP_TABLE}",
                "PhysicalPinMap": "TODO — OAM Conn0 logical only",
                "Footprint": "",
                "LaneCount": str(LANE_COUNT),
            },
        )
    )

    lines.append("")
    lines.append("\t(sheet_instances")
    lines.append('\t\t(path "/Host_PCIe" (page "1"))')
    lines.append("\t)")
    lines.append("")
    lines.append(")")
    return "\n".join(lines)


def build_power() -> str:
    from power_system import (
        OCP_SPEC,
        OCP_POWER_SECTION,
        append_power_symbols,
        hierarchical_power_input,
        hierarchical_power_outputs,
        missing_power_rails,
    )

    append_power_symbols(ROOT / "symbols" / "MI250X-Carrier.kicad_sym")

    notes = dedent(
        f"""
        PURPOSE: Prototype MI250X carrier power — separated domains per engineering architecture.
        DOMAINS: (1) 12V input  (2) OAM 12V + sequencing TODO  (3) 3.3V management
        (4) 3.3V logic/OAM aux  (5) Fan 12V  — 48V P48V explicitly NC Rev1.
        OCP: {OCP_SPEC} {OCP_POWER_SECTION}; Table 4 P12V1/2, P3V3, P48V.
        AMD: Rail currents, enables, Power Good, startup order — TODO (no rail table in repo).
        NO OAM connector power pin numbers assigned.
        """
    ).strip()

    domain_comments = [
        (20.32, 88.0, "DOMAIN 1 — 12V INPUT: J1 connector → D1 TVS → F1 fuse → CB1 bulk."),
        (20.32, 96.0, "DOMAIN 2 — OAM 12V: U1 hot-swap/eFuse → U2 AMD sequencer TODO → N1 P12V1/P12V2 bus."),
        (20.32, 104.0, f"OCP P48V (48V/54V): U3 block NC Rev1 — energize only after AMD rail table confirms."),
        (20.32, 112.0, "DOMAIN 3 — 3.3V MGMT: U4 LDO → MCU/FRU/sensors/SMBus (Management sheet)."),
        (20.32, 120.0, "DOMAIN 4 — 3.3V LOGIC: U5 LDO → OCP P3V3 Conn0 + P3V3_CONN1 (OAM Interface)."),
        (20.32, 128.0, "DOMAIN 5 — FAN 12V: F2 fuse → J2 fan header; PWM control on Management sheet."),
        (20.32, 136.0, "SEQUENCING: U2 OAM_Seq_AMD_TODO — all enable/PG timing unconnected until AMD docs."),
    ]

    lines = sch_header("Power System", "04_power_system")
    lines.append("\t)")
    lines.append("")
    lines.append(text_note(20.32, 17.78, notes, 1.2))
    for x, y, txt in domain_comments:
        lines.append(text_note(x, y, txt, 1.05))

    missing = missing_power_rails()
    p48 = next(r for r in missing["oam_connector_rails_todo"] if r["rail"] == "P48V")
    lines.append(text_note(20.32, 144.0, f"MISSING RAIL: {p48['rail']} — {p48['status']}", 1.05))

    for name, shape in hierarchical_power_input():
        lines.append(hierarchical_label(15.0, 40.0, name, shape))
    y = 40.0
    for name, shape in hierarchical_power_outputs():
        lines.append(hierarchical_label(300.0, y, name, shape))
        y += 8.0

    # Component placement — left to right signal flow
    placement = [
        ("Pwr_12V_Input", "J1", "12V_Input", 35.0, 55.0, {"MPN": "MPN_TODO — 12V input connector"}),
        ("Pwr_Input_Protection", "D1", "Input_Protect", 60.0, 55.0, {"MPN": "SMBJ15A — rating TODO"}),
        ("Pwr_Fuse", "F1", "Fuse_12V_In", 85.0, 55.0, {"MPN": "MPN_TODO — fuse rating after AMD 12V current"}),
        ("Pwr_BulkCap_12V", "CB1", "Bulk_12V", 110.0, 55.0, {}),
        ("Pwr_HotSwap_12V", "U1", "HotSwap_12V", 140.0, 55.0, {"MPN": "TPS25942ARVCR — SOA TODO"}),
        ("Pwr_OAM_Seq_TODO", "U2", "OAM_Seq_AMD_TODO", 170.0, 55.0, {"Status": "AMD sequencing TODO — do not route"}),
        ("Pwr_Bus_12V_OAM", "N1", "Bus_12V_OAM", 200.0, 55.0, {}),
        ("Pwr_48V_TODO", "U3", "P48V_OAM_TODO", 140.0, 95.0, {"Status": "NC Rev1 — P48V not routed"}),
        ("Pwr_LDO_3V3_Mgmt", "U4", "LDO_3V3_Mgmt", 230.0, 45.0, {"MPN": "AP2112K-3.3TRG1 — load TODO"}),
        ("Pwr_LDO_3V3_Logic", "U5", "LDO_3V3_Logic", 230.0, 85.0, {"MPN": "AP2112K-3.3TRG1 — OAM load TODO"}),
        ("Pwr_Fuse_Fan", "F2", "Fuse_Fan_12V", 265.0, 55.0, {"MPN": "MPN_TODO — fan fuse"}),
        ("Pwr_Fan_12V", "J2", "Fan_12V_Dist", 290.0, 55.0, {"MPN": "4-pin PWM fan header"}),
    ]
    for sym, ref, val, x, y, props in placement:
        lines.append(
            sym_instance_lib(
                f"MI250X-Carrier:{sym}",
                ref,
                val,
                x,
                y,
                props,
            )
        )

    lines.append("")
    lines.append("\t(sheet_instances")
    lines.append('\t\t(path "/Power_System" (page "1"))')
    lines.append("\t)")
    lines.append("")
    lines.append(")")
    return "\n".join(lines)


def build_clocking() -> str:
    from clocking_reset import (
        OCP_SPEC,
        OCP_TABLE,
        append_clock_symbols,
        hierarchical_clock_inputs,
        hierarchical_clock_outputs,
        pcie_clock_tree_architecture,
        reset_signals,
    )

    append_clock_symbols(ROOT / "symbols" / "MI250X-Carrier.kicad_sym")

    notes = dedent(
        f"""
        PURPOSE: PCIe reference clock (OCP PE_REFCLKp/n) and reset distribution.
        OCP: {OCP_SPEC} {OCP_TABLE} — PE_REFCLK 100 MHz PCIe Gen5 compliant.
        CLOCK TREE: Y1 oscillator → U1 PCIe buffer → OAM PE_REFCLKp/n (+ host fanout).
        ALT: Host REFCLK passthrough via J1 (Mode B) — select after REFCLK guide.
        RESET: PERST# (OCP) via U2; WARMRST#/AUX_100M/PERST_Conn1 — TODO blocks NC.
        AMD: Reset release vs OAM_PG, SSC, dual-GCD clocks — TODO (not invented).
        """
    ).strip()

    tree_lines = pcie_clock_tree_architecture()
    comments = [
        (20.32, 88.0, f"OCP {OCP_TABLE}: PE_REFCLKp + PE_REFCLKn — official OAM naming (not REFCLK or PE_REFCLK aggregate)."),
        (20.32, 96.0, "CLOCK TREE Mode A: Y1 → U1 buffer CLK0 → OAM; CLK1 → host slot (if carrier sources)."),
        (20.32, 104.0, "CLOCK TREE Mode B: J1 host REFCLK in → U1 → OAM (Y1 DNP)."),
        (20.32, 112.0, "R1 termination/coupling at PE_REFCLK receivers — values per REFCLK Guide (TODO)."),
        (20.32, 120.0, f"RESET: PERST# (OCP Conn0) → net PERST_N; U6 gates release on OAM_PG_TODO (AMD timing TODO)."),
        (20.32, 128.0, "TODO clocks: U3 AUX_100M_REFCLK; no AMD-specific clocks assigned."),
    ]
    for i, line in enumerate(tree_lines[:4]):
        comments.append((20.32, 136.0 + i * 8.0, line))

    lines = sch_header("Clocking Reset", "05_clocking_reset")
    lines.append("\t)")
    lines.append("")
    lines.append(text_note(20.32, 17.78, notes, 1.15))
    for x, y, txt in comments:
        lines.append(text_note(x, y, txt, 1.0))

    resets = reset_signals()
    todo_resets = ", ".join(r["signal"] for r in resets["ocp_todo_not_routed"])
    lines.append(text_note(20.32, 168.0, f"Reset TODO (OCP): {todo_resets}", 1.0))

    y = 40.0
    for name, shape in hierarchical_clock_inputs():
        lines.append(hierarchical_label(15.0, y, name, shape))
        y += 10.0
    y = 40.0
    for name, shape in hierarchical_clock_outputs():
        lines.append(hierarchical_label(300.0, y, name, shape))
        y += 10.0

    placement = [
        ("Clk_Osc_100M_PE_REFCLK", "Y1", "100MHz_PE_REFCLK", 50.0, 55.0, {"MPN": "100 MHz HCSL — MPN TODO"}),
        ("Clk_Buffer_PCIe", "U1", "PCIe_ClkBuffer", 90.0, 55.0, {"MPN": "LMK00101 class — MPN TODO"}),
        ("Clk_Term_PE_REFCLK", "R1", "PE_REFCLK_Term", 130.0, 55.0, {}),
        ("Clk_HOST_REFCLK_IN", "J1", "Host_REFCLK_In", 50.0, 95.0, {"Status": "Mode B host passthrough"}),
        ("Rst_PERST_Dist", "U2", "PERST_Distribution", 170.0, 55.0, {}),
        ("Clk_AUX_100M_TODO", "U3", "AUX_100M_REFCLK_TODO", 90.0, 95.0, {"Status": "NC — OCP optional"}),
        ("Rst_WARMRST_TODO", "U4", "WARMRST_TODO", 130.0, 95.0, {"Status": "NC — OCP optional"}),
        ("Rst_PERST_CONN1_TODO", "U5", "PERST_Conn1_TODO", 170.0, 95.0, {"Status": "NC — verify pin map"}),
        ("Rst_Seq_Gate_TODO", "U6", "Reset_Seq_AMD_TODO", 210.0, 55.0, {"Status": "AMD sequencing TODO"}),
    ]
    for sym, ref, val, x, y, props in placement:
        lines.append(sym_instance_lib(f"MI250X-Carrier:{sym}", ref, val, x, y, props))

    lines.append("")
    lines.append("\t(sheet_instances")
    lines.append('\t\t(path "/Clocking_Reset" (page "1"))')
    lines.append("\t)")
    lines.append("")
    lines.append(")")
    return "\n".join(lines)


def build_management() -> str:
    from management_system import (
        OCP_SPEC,
        OCP_TABLE,
        append_management_symbols,
        hierarchical_mgmt_inputs,
        hierarchical_mgmt_outputs,
        optional_features,
        verified_requirements,
    )

    append_management_symbols(ROOT / "symbols" / "MI250X-Carrier.kicad_sym")

    notes = dedent(
        f"""
        PURPOSE: Carrier management — MCU, FRU, I2C, PMBus, SMBus bridge, temp, debug UART.
        VERIFIED: User prototype requirements + OCP {OCP_TABLE} SMBus on Conn0.
        OPTIONAL: I2C mux (DNP), fan PWM — marked on sheet; not required Rev1 MVP.
        AMD TODO: Module SMBus/PMBus addresses, GPIO, FRU format — U8–U10 blocks NC.
        """
    ).strip()

    comments = [
        (20.32, 88.0, "VERIFIED: U1 MCU, U2 FRU EEPROM, U5 temp, J1 UART, U4 OCP SMBus bridge."),
        (20.32, 96.0, f"OCP {OCP_TABLE}: SMBus_D, SMBus_CLK, SMB_ALERT# via U4 level shifter."),
        (20.32, 104.0, "VERIFIED: U3 PMBus path — module device addresses AMD TODO (U9 block NC)."),
        (20.32, 112.0, "OPTIONAL: U6 I2C mux DNP; U7 fan PWM DNP until thermal plan."),
        (20.32, 120.0, "AMD TODO: U8 SMBus map, U9 PMBus map, U10 GPIO — do not route."),
        (20.32, 128.0, "I2C1: FRU + TMP117. I2C2: PMBus + SMBus MCU side. J2: Expansion sheet."),
    ]

    lines = sch_header("Management", "06_management")
    lines.append("\t)")
    lines.append("")
    lines.append(text_note(20.32, 17.78, notes, 1.15))
    for x, y, txt in comments:
        lines.append(text_note(x, y, txt, 1.0))

    lines.append(text_note(20.32, 136.0, "VERIFIED REQ: " + "; ".join(v["item"] for v in verified_requirements()[:4]) + "...", 0.95))
    lines.append(text_note(20.32, 144.0, "OPTIONAL: " + "; ".join(o["item"] for o in optional_features()[:3]), 0.95))

    y = 40.0
    for name, shape in hierarchical_mgmt_inputs():
        lines.append(hierarchical_label(15.0, y, name, shape))
        y += 10.0
    y = 40.0
    for name, shape in hierarchical_mgmt_outputs():
        lines.append(hierarchical_label(300.0, y, name, shape))
        y += 10.0

    placement = [
        ("Mgmt_MCU_STM32G071", "U1", "STM32G071_MCU", 70.0, 55.0, {"MPN": "STM32G071GBU6", "Category": "verified"}),
        ("Mgmt_FRU_EEPROM", "U2", "FRU_EEPROM", 70.0, 100.0, {"MPN": "AT24C256C", "Category": "verified"}),
        ("Mgmt_I2C_Pullups", "R1", "I2C_Pullups", 110.0, 55.0, {"Category": "verified"}),
        ("Mgmt_PMBus_PassThrough", "U3", "PMBus_Interface", 140.0, 55.0, {"Category": "verified"}),
        ("Mgmt_SMBus_LevelShift", "U4", "SMBus_OAM_Bridge", 170.0, 55.0, {"MPN": "PCA9306", "Category": "verified"}),
        ("Mgmt_Temp_TMP117", "U5", "Temp_Sensor", 110.0, 100.0, {"MPN": "TMP117AIDRVR", "Category": "verified"}),
        ("Mgmt_UART_Debug", "J1", "Debug_UART", 200.0, 100.0, {"Category": "verified"}),
        ("Mgmt_I2C_Exp_Connector", "J2", "I2C_Expansion", 230.0, 55.0, {"Category": "verified"}),
        ("Mgmt_I2C_Mux_DNP", "U6", "I2C_Mux_Optional", 200.0, 55.0, {"DNP": "Rev1", "Category": "optional"}),
        ("Mgmt_Fan_PWM_TODO", "U7", "Fan_PWM_Optional", 230.0, 100.0, {"DNP": "Rev1", "Category": "optional"}),
        ("Mgmt_AMD_SMBus_TODO", "U8", "AMD_SMBus_Map_TODO", 140.0, 100.0, {"Status": "NC — AMD TODO", "Category": "amd_todo"}),
        ("Mgmt_AMD_PMBus_TODO", "U9", "AMD_PMBus_Map_TODO", 170.0, 100.0, {"Status": "NC — AMD TODO", "Category": "amd_todo"}),
        ("Mgmt_AMD_GPIO_TODO", "U10", "AMD_Mgmt_GPIO_TODO", 260.0, 55.0, {"Status": "NC — AMD TODO", "Category": "amd_todo"}),
    ]
    for sym, ref, val, x, y, props in placement:
        lines.append(sym_instance_lib(f"MI250X-Carrier:{sym}", ref, val, x, y, props))

    lines.append("")
    lines.append("\t(sheet_instances")
    lines.append('\t\t(path "/Management" (page "1"))')
    lines.append("\t)")
    lines.append("")
    lines.append(")")
    return "\n".join(lines)


def build_test_points() -> str:
    from test_points_system import (
        append_test_point_symbols,
        debug_headers,
        hierarchical_tp_inputs,
        pcie_debug_signals,
        power_rail_test_points,
    )

    append_test_point_symbols(ROOT / "symbols" / "MI250X-Carrier.kicad_sym")

    notes = dedent(
        f"""
        PURPOSE: Bring-up test points and debug headers per AI_DESIGN_RULES.md.
        POWER: TP on every primary rail from Power_System (limits TODO).
        PCIe: TP on sidebands only (PE_REFCLKp/n, PERST_N, PRESNT_N) — NOT on PET/PER HS lanes.
        MGMT: SMBus/PMBus TPs; J1 I2C debug header; UART TPs (header on Management J1).
        CHECKLIST: docs/bringup_checklist.md — gated per 08_Bringup.md.
        """
    ).strip()

    comments = [
        (20.32, 88.0, "POWER TPs: VIN_12V, OAM_12V, OAM_P12V1/2, MGMT_3V3, LOGIC_3V3, FAN_12V, GND."),
        (20.32, 96.0, "PCIe TPs: PE_REFCLKp/n, PERST_N, PRESNT_N — scope/LA only."),
        (20.32, 104.0, "HS lanes PET/PER: NO stub TPs — probe at Mirror Mezz or host edge."),
        (20.32, 112.0, "SMBus/PMBus: TP_SMBUS_*, TP_PMBUS_* — module addresses AMD TODO."),
        (20.32, 120.0, "J1 I2C_DBG: SCL, SDA, 3V3, GND — expansion I2C bus."),
        (20.32, 128.0, "UART: TP_UART_TX/RX; primary header Management sheet J1."),
    ]

    lines = sch_header("Test Points", "07_test_points")
    lines.append("\t)")
    lines.append("")
    lines.append(text_note(20.32, 17.78, notes, 1.1))
    for x, y, txt in comments:
        lines.append(text_note(x, y, txt, 1.0))

    y = 40.0
    for name, shape in hierarchical_tp_inputs():
        lines.append(hierarchical_label(15.0, y, name, shape, 1.0))
        y += 6.0

    # Power rail TPs
    x_tp = 80.0
    y_tp = 45.0
    for rail in power_rail_test_points():
        lines.append(
            sym_instance_lib(
                "MI250X-Carrier:Tp_Signal",
                rail["tp"].replace("TP_", "TP"),
                rail["net"],
                x_tp,
                y_tp,
                {"Net": rail["net"], "Limit": rail["limit"]},
            )
        )
        y_tp += 12.0

    # PCIe sideband TPs
    x_tp = 120.0
    y_tp = 45.0
    for sig in pcie_debug_signals()["suitable_for_tp"]:
        lines.append(
            sym_instance_lib(
                "MI250X-Carrier:Tp_Signal",
                sig["tp"].replace("TP_", "TP"),
                sig["net"],
                x_tp,
                y_tp,
                {"Net": sig["net"]},
            )
        )
        y_tp += 12.0

    # Management TPs
    mgmt_tps = [
        ("TP_SMBUS_CLK", "SMBUS_CLK"),
        ("TP_SMBUS_DATA", "SMBUS_DATA"),
        ("TP_SMBUS_ALERT", "SMBUS_ALERT_N"),
        ("TP_PMBUS_SCL", "PMBUS_SCL"),
        ("TP_PMBUS_SDA", "PMBUS_SDA"),
        ("TP_UART_TX", "DBG_UART_TX"),
        ("TP_UART_RX", "DBG_UART_RX"),
    ]
    x_tp = 160.0
    y_tp = 45.0
    for ref, net in mgmt_tps:
        lines.append(sym_instance_lib("MI250X-Carrier:Tp_Signal", ref.replace("TP_", "TP"), net, x_tp, y_tp, {"Net": net}))
        y_tp += 12.0

    # I2C debug header
    lines.append(
        sym_instance_lib(
            "MI250X-Carrier:Dbg_Header_I2C",
            "J1",
            "I2C_Debug_4pin",
            200.0,
            55.0,
            {"Pins": debug_headers()[0]["pins"]},
        )
    )

    lines.append("")
    lines.append("\t(sheet_instances")
    lines.append('\t\t(path "/Test_Points" (page "1"))')
    lines.append("\t)")
    lines.append("")
    lines.append(")")
    return "\n".join(lines)


def build_expansion() -> str:
    from expansion_system import (
        OCP_TABLE,
        append_expansion_symbols,
        expansion_topology,
        hierarchical_expansion_inputs,
        pcie_switch_integration,
    )

    append_expansion_symbols(ROOT / "symbols" / "MI250X-Carrier.kicad_sym")

    notes = dedent(
        f"""
        PURPOSE: Multi-MI250X expansion interface planning — NOT implemented Rev1.
        REV1: Direct Host_PCIe → OAM_Interface; Management J2 I2C → J1 here only.
        DNP: U1 PCIe switch, J2 slot-2 OAM, J3 power bus, U2 I2C mux, U3/U4 clk/rst fanout.
        PCIe SWITCH: See docs/expansion_planning.md — upstream/downstream/refclk/reset port map.
        SCALE: Rev2 dual / Rev3 quad / Rev4 oct — topology and MPN all TODO.
        """
    ).strip()

    topo = expansion_topology()
    sw = pcie_switch_integration()

    comments = [
        (20.32, 88.0, f"REV1 ACTIVE: J1 I2C from Management J2 — only populated interface."),
        (20.32, 96.0, f"REV1 BYPASS: Host_PCIe x16 direct to OAM_Interface — U1 switch DNP."),
        (20.32, 104.0, f"DNP U1: PCIe switch — upstream PCIE_Ln_TX/RX; downstream PET/PER per slot."),
        (20.32, 112.0, f"DNP J2: OAM slot 2 Mirror Mezz — {OCP_TABLE} key nets only."),
        (20.32, 120.0, "DNP J3: OAM_12V bus bar taps for modules 2–4."),
        (20.32, 128.0, "DNP U2: I2C mux per-module mgmt; U3 REFCLK fanout; U4 PERST fanout."),
        (20.32, 136.0, f"FUTURE: {topo[1]['revision']} {topo[1]['modules']} modules — {topo[1]['pcie'][:70]}..."),
        (20.32, 144.0, "OPEN: " + sw["open_questions"][0][:85] + "..."),
    ]

    lines = sch_header("Expansion", "08_expansion")
    lines.append("\t)")
    lines.append("")
    lines.append(text_note(20.32, 17.78, notes, 1.1))
    for x, y, txt in comments:
        lines.append(text_note(x, y, txt, 1.0))

    y = 40.0
    for name, shape in hierarchical_expansion_inputs():
        lines.append(hierarchical_label(15.0, y, name, shape, 1.0))
        y += 8.0

    placement = [
        ("Exp_Mgmt_I2C_Interface", "J1", "I2C_Exp_Interface", 55.0, 50.0, {"Category": "rev1_active"}, False),
        ("Exp_PCIe_Switch_DNP", "U1", "PCIe_Switch_DNP", 100.0, 50.0, {"DNP": "Rev1", "Status": "footprint only"}, True),
        ("Exp_I2C_Mux_DNP", "U2", "I2C_Mux_Exp_DNP", 145.0, 50.0, {"DNP": "Rev1"}, True),
        ("Exp_REFCLK_Fanout_DNP", "U3", "PE_REFCLK_Fanout_DNP", 190.0, 50.0, {"DNP": "Rev1"}, True),
        ("Exp_PERST_Fanout_DNP", "U4", "PERST_Fanout_DNP", 235.0, 50.0, {"DNP": "Rev1"}, True),
        ("Exp_OAM_Slot2_DNP", "J2", "OAM_Slot2_DNP", 100.0, 110.0, {"DNP": "Rev1"}, True),
        ("Exp_Power_Bus_DNP", "J3", "OAM_12V_BusBar_DNP", 145.0, 110.0, {"DNP": "Rev1"}, True),
    ]
    for sym, ref, val, x, y_pos, props, dnp in placement:
        lines.append(sym_instance_lib(f"MI250X-Carrier:{sym}", ref, val, x, y_pos, props, dnp=dnp))

    lines.append("")
    lines.append("\t(sheet_instances")
    lines.append('\t\t(path "/Expansion" (page "1"))')
    lines.append("\t)")
    lines.append("")
    lines.append(")")
    return "\n".join(lines)


def build_project() -> dict:
    return {
        "board": {
            "design_settings": {
                "defaults": {
                    "board_outline_line_width": 0.1,
                    "copper_line_width": 0.2,
                    "copper_text_size_h": 1.5,
                    "copper_text_size_v": 1.5,
                    "copper_text_thickness": 0.3,
                },
                "diff_pair_dimensions": [],
                "drc_exclusions": [],
                "meta": {"version": 2},
                "rule_severities": {},
                "track_widths": [0.2, 0.5, 1.0, 2.0],
                "via_dimensions": [],
            },
            "layer_presets": [],
        },
        "boards": [],
        "cvpcb": {"equivalence_files": []},
        "erc": {
            "erc_exclusions": [],
            "meta": {"version": 0},
            "pin_map": [
                [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
            ],
        },
        "libraries": {
            "pinned_footprint_libs": [],
            "pinned_symbol_libs": [],
        },
        "meta": {
            "filename": "MI250X_Carrier_Rev1.kicad_pro",
            "version": 3,
        },
        "net_settings": {
            "classes": [
                {
                    "bus_width": 12,
                    "clearance": 0.2,
                    "diff_pair_gap": 0.25,
                    "diff_pair_via_gap": 0.25,
                    "diff_pair_width": 0.2,
                    "line_style": 0,
                    "microvia_diameter": 0.3,
                    "microvia_drill": 0.1,
                    "name": "Default",
                    "pcb_color": "rgba(0, 0, 0, 0.000)",
                    "priority": 2147483647,
                    "schematic_color": "rgba(0, 0, 0, 0.000)",
                    "track_width": 0.2,
                    "via_diameter": 0.6,
                    "via_drill": 0.3,
                    "wire_width": 6,
                }
            ],
            "meta": {"version": 4},
            "net_colors": None,
            "netclass_assignments": None,
            "netclass_patterns": [],
        },
        "pcbnew": {"last_paths": {"gencad": "", "idf": "", "netlist": "", "plot": "", "pos_files": "", "specctra_dsn": "", "step": "", "svg": "", "vrml": ""}, "page_layout_descr_file": ""},
        "schematic": {
            "annotate_start_num": 1,
            "drawing": {"dashed_lines_dash_length_ratio": 12, "dashed_lines_gap_length_ratio": 3, "default_line_thickness": 6, "default_text_size": 50, "field_names": [], "intersheets_ref_own_page": False, "intersheets_ref_prefix": "", "intersheets_ref_short": False, "intersheets_ref_suffix": "", "junction_size_choice": 3, "label_size_ratio": 0.375, "operating_point_overlay_i_precision": 3, "operating_point_overlay_i_range": "~A", "operating_point_overlay_v_precision": 3, "operating_point_overlay_v_range": "~V", "overbar_offset_ratio": 1.23, "pin_symbol_size": 25, "text_offset_ratio": 0.15},
            "legacy_lib_dir": "",
            "legacy_lib_list": [],
            "meta": {"version": 1},
            "net_format_name": "",
            "page_layout_descr_file": "",
            "plot_directory": "",
            "space_save_all": False,
            "spice_current_sheet_as_root": False,
            "spice_external_command": "spice \"%I\"",
            "spice_model_current_sheet_as_root": True,
            "spice_save_all_currents": False,
            "spice_save_all_dissipations": False,
            "spice_save_all_voltages": False,
            "subpart_first_id": 65,
            "subpart_id_separator": 0,
        },
        "sheets": [
            ["root", ""],
            ["02_oam_interface", "sheets/02_oam_interface.kicad_sch"],
            ["03_host_pcie", "sheets/03_host_pcie.kicad_sch"],
            ["04_power_system", "sheets/04_power_system.kicad_sch"],
            ["05_clocking_reset", "sheets/05_clocking_reset.kicad_sch"],
            ["06_management", "sheets/06_management.kicad_sch"],
            ["07_test_points", "sheets/07_test_points.kicad_sch"],
            ["08_expansion", "sheets/08_expansion.kicad_sch"],
        ],
        "text_variables": {
            "PROJECT": "Open MI250X Carrier Rev1",
            "TARGET": "AMD Instinct MI250X OAM x1",
            "OCP_SPEC": "OCP Accelerator Module Design Specification v1.5",
        },
    }


def write_docs() -> None:
    docs = ROOT / "docs"
    docs.mkdir(parents=True, exist_ok=True)
    (docs / "sources.md").write_text(
        dedent(
            """
            # Source Documents

            ## Verified (used in this prototype)

            | Source | Used for |
            |--------|----------|
            | [OCP Accelerator Module Design Specification v1.5](https://www.opencompute.org/documents/ocp-accelerator-module-design-specification-v1p5-final-20220223-docx-1-pdf) | Mirror Mezz Pro connectors; host x16 SerDes; PE_REFCLK 100MHz; 12V/54V power on Conn0; SMBus; AC coupling on baseboard |
            | AMD ROCm Overview (`13_Reference_Docs/ROCm/Overview.md`) | MI250X is OCP OAM; 2 GCD; 128 GB; two software-visible devices |
            | `AI_DESIGN_RULES.md` | KiCad 9; no invented OAM pins; test points; sheet documentation |

            ## Not locally available (TODO)

            - OAM_Pinlist_Pinmap spreadsheet (physical pin numbers)
            - PCIe Routing Guide
            - REFCLK Guide (supplemental)
            - AMD MI250X power rail table
            - PMBus/VRM datasheet for module telemetry
            """
        ).strip()
        + "\n"
    )
    (docs / "assumptions.md").write_text(
        dedent(
            """
            # Prototype Assumptions

            These are **user-requested prototype features** or **engineering placeholders**, not verified AMD requirements.

            1. **12V-only input** — OCP Conn0 also defines 54V/48V; prototype defers 54V until AMD rail table confirms need.
            2. **Carrier-hosted FRU EEPROM** — User requirement; OCP does not mandate carrier FRU for minimal boot.
            3. **STM32G071 management MCU** — Placeholder for I2C/PMBus/UART; part not verified against AMD firmware expectations.
            4. **Direct PCIe x16** — No switch/retimer on Rev1; expansion sheet reserves DNP switch.
            5. **3.3V management rail** — OCP Conn1 includes 3.3V pins; LDO from 12V input assumed.
            """
        ).strip()
        + "\n"
    )
    (docs / "open_questions.md").write_text(
        dedent(
            """
            # Open Questions / TODO

            ## OAM connector (P0)

            - [ ] Import OAM_Pinlist_Pinmap spreadsheet — assign physical Mirror Mezz pin numbers
            - [ ] Confirm Molex MPN 218910-1115 vs 218916-1115 for MI250X module revision
            - [ ] Classify AMD-specific GPIO/sidebands not in OCP Table 4

            ## Power (P0)

            - [ ] MI250X 12V current, sequencing, enable/PG signals
            - [ ] 54V/48V pin requirement for MI250X — energize or NC?
            - [ ] PMBus addresses for module VRM telemetry

            ## PCIe (P0)

            - [ ] MI250X lane map: 1x16 vs 2x8 per GCD
            - [ ] CLKREQ# / WAKE# pin assignments
            - [ ] Host slot on X11DPH-T

            ## Management (P1)

            - [ ] SMBus voltage level and pull-ups on OAM
            - [ ] FRU EEPROM contents and IPMI compatibility
            - [ ] Whether AMD firmware tools require carrier-side storage

            ## Mechanical / thermal (P1)

            - [ ] Connector footprint and stack-up from Molex drawing
            - [ ] Heatsink retention and TDP limits
            """
        ).strip()
        + "\n"
    )
    (docs / "oam_signal_map.md").write_text(
        dedent(
            """
            # OAM Signal Map (Logical — OCP Verified Names)

            Physical pin numbers: **TODO** — see OAM_Pinlist_Pinmap spreadsheet.

            ## Connector hardware (OCP verified)

            | Item | Value | Source |
            |------|-------|--------|
            | Connector family | Molex Mirror Mezz Pro | OCP OAM v1.5 §6.2 |
            | Quantity | 2 × 688-pin | OCP OAM v1.5 §8.1 |
            | MPN (examples) | 218910-1115, 218916-1115 | OCP OAM v1.5 |
            | Impedance | 90 Ω ± 5% nominal | OCP OAM v1.5 |

            ## Conn0 — host link (OCP verified categories)

            | Signal | Direction (module) | Notes |
            |--------|-------------------|-------|
            | PETp/n[15:0] | Output (module TX) | AC coupling on baseboard/carrier |
            | PERp/n[15:0] | Input (module RX) | Host TX → module RX |
            | PE_REFCLKp/n | Input | 100 MHz, PCIe Gen5 compliant per OCP Table 4 |
            | PERST# | — | PCIe reset sideband |
            | SMBus | — | Management |
            | OAM_PRESENT# / PRESNT# | — | Presence detect |
            | 12V / 54V/48V power | Input | Prototype: 12V only — 54V TODO |
            | GND | — | Multiple return pins |

            ## Conn1 (partial — OCP verified categories)

            | Signal | Notes |
            |--------|-------|
            | 3.3V power | Management/aux |
            | JTAG | — |
            | GPIO | AMD-specific usage **TODO** |
            | Additional SerDes | Inter-accelerator — N/A single module Rev1 |

            ## AMD-specific (TODO — do not assign)

            - All GPIO functions on Conn1
            - Dual-GCD PCIe topology
            - Module-internal PMBus device map
            """
        ).strip()
        + "\n"
    )


def main() -> None:
    ROOT.mkdir(parents=True, exist_ok=True)
    (ROOT / "sheets").mkdir(exist_ok=True)

    write_sch(ROOT / "MI250X_Carrier_Rev1.kicad_sch", build_root())
    write_sch(ROOT / "sheets/02_oam_interface.kicad_sch", build_oam_interface())
    write_sch(ROOT / "sheets/03_host_pcie.kicad_sch", build_host_pcie())
    write_sch(ROOT / "sheets/04_power_system.kicad_sch", build_power())
    write_sch(ROOT / "sheets/05_clocking_reset.kicad_sch", build_clocking())
    write_sch(ROOT / "sheets/06_management.kicad_sch", build_management())
    write_sch(ROOT / "sheets/07_test_points.kicad_sch", build_test_points())
    write_sch(ROOT / "sheets/08_expansion.kicad_sch", build_expansion())

    (ROOT / "MI250X_Carrier_Rev1.kicad_pro").write_text(json.dumps(build_project(), indent=2) + "\n")

    (ROOT / "sym-lib-table").write_text(
        dedent(
            """
            (sym_lib_table
              (version 7)
              (lib (name "MI250X-Carrier")(type "KiCad")(uri "${KIPRJMOD}/symbols/MI250X-Carrier.kicad_sym")(options "")(descr "Prototype carrier symbols"))
            )
            """
        ).strip()
        + "\n"
    )
    (ROOT / "fp-lib-table").write_text(
        dedent(
            """
            (fp_lib_table
              (version 7)
              (lib (name "MI250X-Carrier")(type "KiCad")(uri "${KIPRJMOD}/footprints")(options "")(descr "Prototype footprints — TODO"))
            )
            """
        ).strip()
        + "\n"
    )

    write_docs()
    write_remaining_unknown_pins()
    from host_pcie import write_support_signal_doc
    from power_system import write_missing_rails_doc

    write_support_signal_doc(ROOT / "docs" / "host_pcie_support_signals.md")
    write_missing_rails_doc(ROOT / "docs" / "missing_power_rails.md")
    from clocking_reset import write_clocking_reset_doc

    write_clocking_reset_doc(ROOT / "docs" / "clocking_reset_audit.md")
    from management_system import write_management_audit_doc

    write_management_audit_doc(ROOT / "docs" / "management_audit.md")
    from test_points_system import write_bringup_checklist_doc

    write_bringup_checklist_doc(ROOT / "docs" / "bringup_checklist.md")
    from expansion_system import write_expansion_planning_doc

    write_expansion_planning_doc(ROOT / "docs" / "expansion_planning.md")
    print(f"Generated KiCad project at {ROOT}")


def write_remaining_unknown_pins() -> None:
    from oam_mirror_mezz import remaining_unknown_summary, all_conn0_pins, all_conn1_pins

    summary = remaining_unknown_summary()
    c0_todo = [p.name for p in all_conn0_pins() if p.name.startswith("PHYS_PIN_TODO_")]
    c1_todo = [p.name for p in all_conn1_pins() if p.name.startswith("PHYS_PIN_TODO_")]

    lines = [
        "# Remaining Unknown Pins — Verification Required",
        "",
        "Generated from OAM Interface sheet connector symbols.",
        "KiCad logical pin indices **are not** Molex physical pad numbers.",
        "",
        f"**Conn0 (J1):** {len(c0_todo)} `PHYS_PIN_TODO_*` placeholder pins",
        f"**Conn1 (J2):** {len(c1_todo)} `PHYS_PIN_TODO_*` placeholder pins",
        "",
        "## 1. Physical pin mapping (blocks all routing)",
        "",
    ]
    for item in summary["physical_pin_mapping_all"]:
        lines.append(f"- {item}")

    lines.extend(["", "## 2. Power — logical OCP names without physical fanout", ""])
    for item in summary["power_physical_fanout"]:
        lines.append(f"- {item}")

    lines.extend(["", "## 3. AMD-specific / vendor-specific", ""])
    for item in summary["amd_specific"]:
        lines.append(f"- {item}")

    lines.extend(["", "## 4. Optional OCP signals — confirm for MI250X", ""])
    for item in summary["optional_ocp_signals"]:
        lines.append(f"- {item}")

    lines.extend(["", "## 5. Conn1 GPIO placeholders", ""])
    for name in summary["conn1_gpio_todo"]:
        lines.append(f"- `{name}` — function/direction/voltage TODO")

    lines.extend(["", "## 6. Mechanical", ""])
    for item in summary["mechanical"]:
        lines.append(f"- {item}")

    lines.extend(
        [
            "",
            "## 7. Conn0 `PHYS_PIN_TODO_*` indices (logical KiCad pin numbers)",
            "",
            f"Count: {len(c0_todo)}. Replace each with OCP spreadsheet signal after import.",
            "",
            "<details><summary>Full Conn0 TODO list</summary>",
            "",
        ]
    )
    for name in c0_todo:
        lines.append(f"- `{name}`")
    lines.extend(["", "</details>", "", "## 8. Conn1 `PHYS_PIN_TODO_*` indices", ""])
    for name in c1_todo:
        lines.append(f"- `{name}`")

    (ROOT / "docs" / "remaining_unknown_pins.md").write_text("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
