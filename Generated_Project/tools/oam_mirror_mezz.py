"""Molex Mirror Mezz Pro connector symbols per OCP OAM Specification v1.5.

Physical Mirror Mezz pin numbers are NOT assigned here.
KiCad pin numbers are logical indices only; OCP physical mapping is TODO.
"""

from __future__ import annotations

from dataclasses import dataclass

OCP_SPEC = "OCP Accelerator Module Design Specification v1.5"
OCP_TABLE = "Table 4 OAM Pinouts"
OCP_CONN_SECTION = "§8.1–8.3"
MOLEX_MPNS = "218910-1115, 218916-1115"
PIN_COUNT = 688


@dataclass(frozen=True)
class OcpPin:
    name: str
    electrical: str  # KiCad pin electrical type
    ocp_ref: str
    description: str = ""


def _diff_pair(prefix: str, count: int, electrical: str, ocp_ref: str, desc: str) -> list[OcpPin]:
    pins: list[OcpPin] = []
    for i in range(count):
        pins.append(OcpPin(f"{prefix}p{i}", electrical, ocp_ref, f"{desc} (p lane {i})"))
        pins.append(OcpPin(f"{prefix}n{i}", electrical, ocp_ref, f"{desc} (n lane {i})"))
    return pins


def conn0_ocp_pins() -> list[OcpPin]:
    """OCP Table 4 signals assigned to Connector 0 (logical names only)."""
    pins: list[OcpPin] = []

    # Power — OCP Table 4; physical fanout count TODO (spreadsheet)
    for sig, desc in [
        ("P48V", "48V/54V main input power"),
        ("P12V1", "12V input power rail 1"),
        ("P12V2", "12V input power rail 2"),
        ("P3V3", "3.3V auxiliary (Conn0 presence per Table 4)"),
        ("PVREF", "Sideband I/O reference output from module"),
    ]:
        pins.append(OcpPin(sig, "power_in", f"{OCP_SPEC} {OCP_TABLE}", desc))

    # Host PCIe — §8.2 Conn0 x16 SerDes
    pins.extend(_diff_pair("PET", 16, "output", f"{OCP_SPEC} {OCP_TABLE}", "Host link TX (module TX, host RX); AC caps on carrier"))
    pins.extend(_diff_pair("PER", 16, "input", f"{OCP_SPEC} {OCP_TABLE}", "Host link RX (module RX, host TX); AC caps on carrier"))

    # Inter-accelerator SerDes 1–3 on Conn0
    for n in (1, 2, 3):
        pins.extend(
            _diff_pair(
                f"SERDES_{n}T",
                16,
                "output",
                f"{OCP_SPEC} {OCP_TABLE}",
                f"SerDes link {n} TX (inter-module)",
            )
        )
        pins.extend(
            _diff_pair(
                f"SERDES_{n}R",
                16,
                "input",
                f"{OCP_SPEC} {OCP_TABLE}",
                f"SerDes link {n} RX (inter-module)",
            )
        )

    # Clock / reset
    pins.extend(
        [
            OcpPin("PE_REFCLKp", "input", f"{OCP_SPEC} {OCP_TABLE}", "PCIe reference clock 100MHz (p)"),
            OcpPin("PE_REFCLKn", "input", f"{OCP_SPEC} {OCP_TABLE}", "PCIe reference clock 100MHz (n)"),
            OcpPin("PERST#", "input", f"{OCP_SPEC} {OCP_TABLE}", "CEM-compliant PCIe reset"),
            OcpPin("AUX_100M_REFCLKp", "input", f"{OCP_SPEC} {OCP_TABLE}", "Auxiliary 100MHz ref clock (p) — optional"),
            OcpPin("AUX_100M_REFCLKn", "input", f"{OCP_SPEC} {OCP_TABLE}", "Auxiliary 100MHz ref clock (n) — optional"),
            OcpPin("WARMRST#", "input", f"{OCP_SPEC} {OCP_TABLE}", "Warm reset"),
        ]
    )

    # Management / presence — OCP Table 4 Conn0
    for sig, etype, desc in [
        ("SMBus_D", "bidirectional", "I2C/SMBus data (open-drain)"),
        ("SMBus_CLK", "input", "I2C/SMBus clock"),
        ("SMB_ALERT#", "output", "SMBus alert"),
        ("PRESNT#", "input", "Module presence detect"),
    ]:
        pins.append(OcpPin(sig, etype, f"{OCP_SPEC} {OCP_TABLE}", desc))

    # GND — single logical pin; physical return pin count TODO per spreadsheet
    pins.append(
        OcpPin(
            "GND",
            "power_in",
            f"{OCP_SPEC} {OCP_TABLE}",
            "Ground returns — multiple physical pins TODO (pin map spreadsheet)",
        )
    )

    return pins


def conn1_ocp_pins() -> list[OcpPin]:
    """OCP Table 4 signals assigned to Connector 1 (logical names only)."""
    pins: list[OcpPin] = []

    pins.append(OcpPin("P3V3_CONN1", "power_in", f"{OCP_SPEC} {OCP_TABLE}", "3.3V power pins on Conn1"))
    pins.append(OcpPin("PVREF_CONN1", "power_in", f"{OCP_SPEC} {OCP_TABLE}", "PVREF on Conn1 if applicable — verify spreadsheet"))

    # Inter-accelerator / optional host SerDes 4–7 on Conn1 per §8.2
    for n in (4, 5, 6, 7):
        pins.extend(
            _diff_pair(
                f"SERDES_{n}T",
                16,
                "output",
                f"{OCP_SPEC} {OCP_TABLE}",
                f"SerDes link {n} TX (Conn1)",
            )
        )
        pins.extend(
            _diff_pair(
                f"SERDES_{n}R",
                16,
                "input",
                f"{OCP_SPEC} {OCP_TABLE}",
                f"SerDes link {n} RX (Conn1)",
            )
        )

    # JTAG — OCP Table 4 Conn1 category
    for sig, etype, desc in [
        ("JTAG0_TRST", "input", "JTAG test reset"),
        ("JTAG0_TMS", "input", "JTAG test mode select"),
        ("JTAG0_TCK", "input", "JTAG test clock"),
        ("JTAG0_TDI", "input", "JTAG test data in"),
        ("JTAG0_TDO", "output", "JTAG test data out"),
    ]:
        pins.append(OcpPin(sig, etype, f"{OCP_SPEC} {OCP_TABLE}", desc))

    pins.append(OcpPin("PERST#_CONN1", "input", f"{OCP_SPEC} {OCP_TABLE}", "PERST# on Conn1 if routed — verify spreadsheet"))

    # GPIO — count and functions AMD-specific; do not invent names
    for i in range(16):
        pins.append(
            OcpPin(
                f"GPIO_TODO_{i:02d}",
                "bidirectional",
                f"{OCP_SPEC} {OCP_TABLE} — AMD-specific TODO",
                "GPIO function undefined until OAM pin map + AMD integration guide",
            )
        )

    pins.append(
        OcpPin(
            "GND_CONN1",
            "power_in",
            f"{OCP_SPEC} {OCP_TABLE}",
            "Ground returns Conn1 — multiple physical pins TODO",
        )
    )

    return pins


def pad_to_688(named: list[OcpPin], connector: str) -> list[OcpPin]:
    """Fill remaining connector positions with explicit TODO placeholders."""
    result = list(named)
    todo_start = len(result) + 1
    for i in range(todo_start, PIN_COUNT + 1):
        result.append(
            OcpPin(
                f"PHYS_PIN_TODO_{i:03d}",
                "passive",
                f"{OCP_SPEC} — physical pin map TODO",
                f"{connector}: reserved/NC/vendor/unknown until OAM_Pinlist_Pinmap spreadsheet",
            )
        )
    return result


def all_conn0_pins() -> list[OcpPin]:
    return pad_to_688(conn0_ocp_pins(), "Conn0")


def all_conn1_pins() -> list[OcpPin]:
    return pad_to_688(conn1_ocp_pins(), "Conn1")


def remaining_unknown_summary() -> dict[str, list[str]]:
    """Categorize pins still requiring verification."""
    c0 = all_conn0_pins()
    c1 = all_conn1_pins()
    return {
        "physical_pin_mapping_all": [
            f"All {PIN_COUNT} Conn0 KiCad pin indices → Molex BGA pad numbers (OAM_Pinlist_Pinmap spreadsheet)",
            f"All {PIN_COUNT} Conn1 KiCad pin indices → Molex BGA pad numbers (OAM_Pinlist_Pinmap spreadsheet)",
        ],
        "conn0_todo_placeholder_pins": [p.name for p in c0 if p.name.startswith("PHYS_PIN_TODO_")],
        "conn1_todo_placeholder_pins": [p.name for p in c1 if p.name.startswith("PHYS_PIN_TODO_")],
        "conn1_gpio_todo": [p.name for p in c1 if p.name.startswith("GPIO_TODO_")],
        "power_physical_fanout": [
            "P48V — number of physical pins and current per pin",
            "P12V1, P12V2 — physical pin assignment and grouping",
            "P3V3 / P3V3_CONN1 — physical pins",
            "PVREF / PVREF_CONN1 — physical pins and load",
            "GND / GND_CONN1 — all return pin positions",
        ],
        "amd_specific": [
            "GPIO_TODO_00..15 — function, direction, voltage",
            "MI250X dual-GCD PCIe lane mapping to PET/PER",
            "Whether 54V/48V (P48V) required for MI250X on 12V-only carrier",
            "PMBus visibility on OAM connector vs module-internal only",
        ],
        "optional_ocp_signals": [
            "AUX_100M_REFCLKp/n — required for MI250X?",
            "WARMRST# — required for MI250X?",
            "PERST#_CONN1 — used on MI250X?",
            "SERDES_1..7 — required for single-module Rev1 (likely NC)",
        ],
        "mechanical": [
            "Confirm Molex MPN 218910-1115 vs 218916-1115 for target MI250X module",
            "Mirror Mezz Pro footprint and board-to-board stack-up",
        ],
    }


def render_kicad_symbol(lib_name: str, symbol_name: str, value: str, pins: list[OcpPin], unit_count: int = 8) -> str:
    """Render one symbol into KiCad sym library S-expression fragment."""
    pins_per_unit = (len(pins) + unit_count - 1) // unit_count
    lines = [
        f'  (symbol "{lib_name}:{symbol_name}" (pin_names (offset 1.016)) (exclude_from_sim no) (in_bom yes) (on_board yes)',
        f'    (property "Reference" "J" (at 0 0 0)',
        f'      (effects (font (size 1.27 1.27)) (justify left)))',
        f'    (property "Value" "{value}" (at 0 -2.54 0)',
        f'      (effects (font (size 1.27 1.27)) (justify left)))',
        f'    (property "Footprint" "" (at 0 0 0)',
        f'      (effects (font (size 1.27 1.27)) hide))',
        f'    (property "Datasheet" "Molex Mirror Mezz Pro — {OCP_SPEC} {OCP_CONN_SECTION}" (at 0 -5.08 0)',
        f'      (effects (font (size 1.27 1.27)) hide))',
        f'    (property "MPN" "{MOLEX_MPNS}" (at 0 -7.62 0)',
        f'      (effects (font (size 1.27 1.27)) hide))',
        f'    (property "OCP_PhysicalPinMap" "TODO — OAM_Pinlist_Pinmap spreadsheet" (at 0 -10.16 0)',
        f'      (effects (font (size 1.27 1.27)) hide))',
        f'    (property "PinCount" "{PIN_COUNT}" (at 0 -12.7 0)',
        f'      (effects (font (size 1.27 1.27)) hide))',
    ]

    for unit in range(1, unit_count + 1):
        start = (unit - 1) * pins_per_unit
        chunk = pins[start : start + pins_per_unit]
        if not chunk:
            continue
        body_h = max(5.08, (len(chunk) - 1) * 2.54 + 2.54)
        lines.append(f'    (symbol "{symbol_name}_{unit-1}_{unit}"')
        lines.append(f"      (pin_numbers hide)")
        lines.append(f"      (pin_names (offset 1.016))")
        lines.append(f'      (exclusive false)')
        lines.append(f"      (unit {unit})")
        lines.append(f"      (exclude_from_sim no)")
        lines.append(f"      (in_bom yes)")
        lines.append(f"      (on_board yes)")
        lines.append(f'      (rectangle (start -5.08 -2.54) (end 0 {body_h})')
        lines.append(f"        (stroke (width 0.254) (type default))")
        lines.append(f"        (fill (type background))")
        lines.append(f"      )")
        for idx, pin in enumerate(chunk):
            y = idx * 2.54
            etype = pin.electrical
            lines.append(
                f'      (pin {etype} line (at -7.62 {y} 0) (length 2.54)'
            )
            lines.append(
                f'        (name "{pin.name}" (effects (font (size 1.016 1.016))))'
            )
            lines.append(
                f'        (number "{start + idx + 1}" (effects (font (size 1.016 1.016))))'
            )
            lines.append(f'      )')
        lines.append(f"    )")

    lines.append(f"  )")
    return "\n".join(lines)


def write_symbol_library(path) -> None:
    from pathlib import Path

    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    c0 = all_conn0_pins()
    c1 = all_conn1_pins()
    body = "\n".join(
        [
            '(kicad_symbol_lib (version 20241209) (generator "oam_mirror_mezz")',
            "  (generator_version \"1.0\")",
            render_kicad_symbol("MI250X-Carrier", "Molex_MirrorMezz_Conn0", "218910-1115_Conn0", c0),
            render_kicad_symbol("MI250X-Carrier", "Molex_MirrorMezz_Conn1", "218916-1115_Conn1", c1),
            ")",
        ]
    )
    path.write_text(body + "\n")
