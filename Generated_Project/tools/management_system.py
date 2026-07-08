"""Management subsystem symbols for MI250X OAM carrier Rev1.

Distinguishes verified prototype requirements from optional features.
AMD-specific addresses, GPIO, and module-side management remain TODO.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

OCP_SPEC = "OCP Accelerator Module Design Specification v1.5"
OCP_TABLE = "Table 4 OAM Pinouts"


@dataclass(frozen=True)
class MgmtPin:
    name: str
    electrical: str
    description: str = ""


@dataclass(frozen=True)
class MgmtBlock:
    symbol_name: str
    value: str
    reference_prefix: str
    pins: list[MgmtPin]
    mpn_example: str
    notes: str
    category: str  # verified | optional | amd_todo


def management_blocks() -> list[MgmtBlock]:
    return [
        MgmtBlock(
            "Mgmt_MCU_STM32G071",
            "STM32G071_MCU",
            "U",
            [
                MgmtPin("VDD", "power_in", "3.3V from MGMT_3V3"),
                MgmtPin("GND", "power_in", "Return"),
                MgmtPin("NRST", "input", "Reset — pull-up + button optional"),
                MgmtPin("I2C1_SCL", "bidirectional", "FRU EEPROM + local sensors bus"),
                MgmtPin("I2C1_SDA", "bidirectional", "FRU EEPROM + local sensors bus"),
                MgmtPin("I2C2_SCL", "bidirectional", "PMBus + SMBus bridge bus"),
                MgmtPin("I2C2_SDA", "bidirectional", "PMBus + SMBus bridge bus"),
                MgmtPin("UART_TX", "output", "Debug UART TX → J_DBG"),
                MgmtPin("UART_RX", "input", "Debug UART RX ← J_DBG"),
                MgmtPin("SWDIO", "bidirectional", "SWD debug"),
                MgmtPin("SWCLK", "input", "SWD clock"),
                MgmtPin("TEMP_ALERT", "input", "From TMP117 ALERT#"),
                MgmtPin("SMBUS_ALERT", "input", "From OAM SMB_ALERT# via level shifter"),
            ],
            "STM32G071GBU6 — prototype placeholder; AMD fw expectations TODO",
            "Central management MCU — user prototype requirement",
            "verified",
        ),
        MgmtBlock(
            "Mgmt_FRU_EEPROM",
            "FRU_EEPROM",
            "U",
            [
                MgmtPin("VCC", "power_in", "3.3V"),
                MgmtPin("GND", "power_in", "Return"),
                MgmtPin("SCL", "bidirectional", "I2C1_SCL"),
                MgmtPin("SDA", "bidirectional", "I2C1_SDA"),
                MgmtPin("WP", "input", "Write protect — strap TODO"),
                MgmtPin("A0", "input", "I2C address bit 0 — strap TODO"),
                MgmtPin("A1", "input", "I2C address bit 1 — strap TODO"),
                MgmtPin("A2", "input", "I2C address bit 2 — strap TODO"),
            ],
            "AT24C256C-SSHL-T or AT24C512 — IPMI FRU format TODO",
            "Carrier board identification / FRU — user prototype requirement",
            "verified",
        ),
        MgmtBlock(
            "Mgmt_I2C_Pullups",
            "I2C_Pullups",
            "R",
            [
                MgmtPin("I2C1_SCL", "passive", "2.2k–4.7k to 3.3V — value TODO"),
                MgmtPin("I2C1_SDA", "passive", "2.2k–4.7k to 3.3V"),
                MgmtPin("I2C2_SCL", "passive", "PMBus/SMBus pull-ups — value TODO"),
                MgmtPin("I2C2_SDA", "passive", "PMBus/SMBus pull-ups"),
                MgmtPin("VDD", "power_in", "MGMT_3V3"),
            ],
            "4x resistor pack — values per bus capacitance",
            "I2C open-drain pull-ups on carrier management buses",
            "verified",
        ),
        MgmtBlock(
            "Mgmt_PMBus_PassThrough",
            "PMBus_Interface",
            "U",
            [
                MgmtPin("PMBUS_SCL", "bidirectional", "To expansion / module telemetry path"),
                MgmtPin("PMBUS_SDA", "bidirectional", "To expansion / module telemetry path"),
                MgmtPin("MCU_SCL", "bidirectional", "MCU I2C2_SCL"),
                MgmtPin("MCU_SDA", "bidirectional", "MCU I2C2_SDA"),
                MgmtPin("GND", "power_in", "Return"),
            ],
            "Pass-through + ESD — isolator optional; module addresses AMD TODO",
            "PMBus path for power telemetry — user prototype requirement; device map unknown",
            "verified",
        ),
        MgmtBlock(
            "Mgmt_SMBus_LevelShift",
            "SMBus_OAM_Bridge",
            "U",
            [
                MgmtPin("SCL_MCU", "bidirectional", "MCU-side 3.3V SMBus clock"),
                MgmtPin("SDA_MCU", "bidirectional", "MCU-side 3.3V SMBus data"),
                MgmtPin("SCL_OAM", "bidirectional", "OAM SMBus_CLK — OCP Table 4"),
                MgmtPin("SDA_OAM", "bidirectional", "OAM SMBus_D — OCP Table 4"),
                MgmtPin("ALERT_OAM", "input", "OAM SMB_ALERT#"),
                MgmtPin("VCCA", "power_in", "3.3V MCU side"),
                MgmtPin("VCCB", "power_in", "OAM I/O voltage TODO (3.3V or 1.8V)"),
                MgmtPin("GND", "power_in", "Return"),
            ],
            "PCA9306 or TXS0102 — OAM SMBus voltage TODO",
            f"OCP {OCP_TABLE} SMBus on Conn0 — verified signal category",
            "verified",
        ),
        MgmtBlock(
            "Mgmt_Temp_TMP117",
            "Temp_Sensor",
            "U",
            [
                MgmtPin("VCC", "power_in", "3.3V"),
                MgmtPin("GND", "power_in", "Return"),
                MgmtPin("SCL", "bidirectional", "I2C1_SCL"),
                MgmtPin("SDA", "bidirectional", "I2C1_SDA"),
                MgmtPin("ALERT", "output", "Open-drain alert → MCU TEMP_ALERT"),
                MgmtPin("ADDR", "input", "Address strap — TODO"),
            ],
            "TMP117AIDRVR — I2C address strap TODO",
            "Board temperature monitoring — user prototype requirement",
            "verified",
        ),
        MgmtBlock(
            "Mgmt_UART_Debug",
            "Debug_UART",
            "J",
            [
                MgmtPin("TX", "output", "UART TX to header pin 1"),
                MgmtPin("RX", "input", "UART RX from header pin 2"),
                MgmtPin("GND", "power_in", "Header pin 3 ground"),
            ],
            "1×3 2.54 mm header — 3.3V UART, no RTS/CTS",
            "Debug UART bring-up — user prototype requirement",
            "verified",
        ),
        MgmtBlock(
            "Mgmt_I2C_Exp_Connector",
            "I2C_Expansion",
            "J",
            [
                MgmtPin("SCL", "bidirectional", "Carrier I2C to Expansion sheet"),
                MgmtPin("SDA", "bidirectional", "Carrier I2C to Expansion sheet"),
                MgmtPin("GND", "power_in", "Return"),
            ],
            "2×1 or 4-pin header — expansion bus",
            "Local I2C to Expansion sheet — user prototype / Rev2 hooks",
            "verified",
        ),
        MgmtBlock(
            "Mgmt_I2C_Mux_DNP",
            "I2C_Mux_Optional",
            "U",
            [
                MgmtPin("SCL_IN", "bidirectional", "From MCU"),
                MgmtPin("SDA_IN", "bidirectional", "From MCU"),
                MgmtPin("SCL_OUT0", "bidirectional", "Channel 0 — DNP Rev1"),
                MgmtPin("SDA_OUT0", "bidirectional", "Channel 0"),
                MgmtPin("GND", "power_in", "Return"),
            ],
            "PCA9548A DNP — multi-module I2C expansion Rev2+",
            "Optional I2C mux for 2/4/8 OAM — not populated Rev1",
            "optional",
        ),
        MgmtBlock(
            "Mgmt_Fan_PWM_TODO",
            "Fan_PWM_Optional",
            "U",
            [
                MgmtPin("PWM_OUT", "output", "To fan header — FAN_12V on Power sheet"),
                MgmtPin("TACH_IN", "input", "Fan tachometer — optional"),
                MgmtPin("GND", "power_in", "Return"),
            ],
            "MCU GPIO or DNP — fan control optional Rev1",
            "Carrier fan PWM/tach — optional until thermal plan defined",
            "optional",
        ),
        MgmtBlock(
            "Mgmt_AMD_SMBus_TODO",
            "AMD_SMBus_Map_TODO",
            "U",
            [
                MgmtPin("SMBUS_CLK", "passive", "OAM SMBus — device addresses TODO"),
                MgmtPin("SMBUS_DATA", "passive", "OAM SMBus — device addresses TODO"),
                MgmtPin("GND", "power_in", "Return"),
            ],
            "NC — do not assign addresses until AMD/OAM map verified",
            "AMD module SMBus device map — addresses, voltage, ownership TODO",
            "amd_todo",
        ),
        MgmtBlock(
            "Mgmt_AMD_PMBus_TODO",
            "AMD_PMBus_Map_TODO",
            "U",
            [
                MgmtPin("PMBUS_SCL", "passive", "Module VRM telemetry — MP2975 candidate"),
                MgmtPin("PMBUS_SDA", "passive", "PMBus addresses/commands TODO"),
                MgmtPin("GND", "power_in", "Return"),
            ],
            "NC — MP2975 unverified; no PMBus datasheet in repo",
            "AMD module-internal PMBus — do not invent addresses",
            "amd_todo",
        ),
        MgmtBlock(
            "Mgmt_AMD_GPIO_TODO",
            "AMD_Mgmt_GPIO_TODO",
            "U",
            [
                MgmtPin("GPIO_00", "passive", "OAM Conn1 GPIO — function TODO"),
                MgmtPin("GPIO_01", "passive", "OAM Conn1 GPIO — function TODO"),
                MgmtPin("GND", "power_in", "Return"),
            ],
            "NC — 16× GPIO on Conn1; AMD integration guide required",
            "AMD-specific management GPIO — do not route",
            "amd_todo",
        ),
    ]


def verified_requirements() -> list[dict[str, str]]:
    return [
        {"item": "SMBus on OAM Conn0", "source": f"{OCP_SPEC} {OCP_TABLE}", "note": "SMBus_D, SMBus_CLK, SMB_ALERT# — OCP verified category"},
        {"item": "FRU EEPROM on carrier", "source": "User prototype requirement", "note": "Board identification; IPMI format TODO"},
        {"item": "Management MCU", "source": "User prototype requirement", "note": "I2C×2, UART; STM32G071 placeholder"},
        {"item": "I2C local bus", "source": "User prototype requirement", "note": "FRU + temp sensor + expansion"},
        {"item": "PMBus interface", "source": "User prototype requirement", "note": "Telemetry path; module devices AMD TODO"},
        {"item": "Temperature sensor", "source": "User prototype requirement", "note": "Carrier board temp — TMP117 class"},
        {"item": "Debug UART", "source": "User prototype requirement", "note": "3.3V 3-pin header"},
    ]


def optional_features() -> list[dict[str, str]]:
    return [
        {"item": "I2C mux PCA9548", "note": "DNP Rev1 — multi-OAM expansion Rev2+"},
        {"item": "Fan PWM/tach", "note": "Optional until thermal/fan plan defined"},
        {"item": "BMC / IPMI host interface", "note": "Not in prototype scope — no verified requirement"},
        {"item": "Voltage/current monitors", "note": "INA226 etc. — not in user MVP list"},
        {"item": "Module firmware update path", "note": "Indexed in repo but wiring unknown"},
    ]


def amd_management_todo() -> list[dict[str, str]]:
    return [
        {"signal": "OAM SMBus device addresses", "status": "TODO — scan procedure and map unknown"},
        {"signal": "OAM SMBus I/O voltage", "status": "TODO — level shifter VCCB may be 1.8V"},
        {"signal": "PMBus module addresses (MP2975?)", "status": "TODO — candidate only, not verified"},
        {"signal": "PMBus commands / telemetry registers", "status": "TODO — no datasheet in repo"},
        {"signal": "Conn1 GPIO management functions", "status": "TODO — AMD-specific"},
        {"signal": "Module vs carrier management ownership", "status": "TODO — BMC/MCU on module unknown"},
        {"signal": "FRU fields for MI250X compatibility", "status": "TODO — custom carrier format"},
        {"signal": "Firmware update / JTAG wiring", "status": "TODO — not on Management sheet Rev1"},
    ]


def hierarchical_mgmt_inputs() -> list[tuple[str, str]]:
    return [
        ("MGMT_3V3", "input"),
        ("GND", "passive"),
        ("SMBUS_CLK", "bidirectional"),
        ("SMBUS_DATA", "bidirectional"),
        ("SMBUS_ALERT_N", "bidirectional"),
    ]


def hierarchical_mgmt_outputs() -> list[tuple[str, str]]:
    return [
        ("I2C_SCL", "bidirectional"),
        ("I2C_SDA", "bidirectional"),
        ("PMBUS_SCL", "bidirectional"),
        ("PMBUS_SDA", "bidirectional"),
        ("DBG_UART_TX", "output"),
        ("DBG_UART_RX", "input"),
        ("TEMP_ALERT", "output"),
        ("FAN_PWM_TODO", "passive"),
    ]


def placeholders_identified() -> list[str]:
    return [
        "REMOVED: OAM_MirrorMezz_Conn0_TODO (wrong sheet)",
        "REMOVED: Embedded lib-only MCU/FRU/TEMP stubs without architecture",
        "REMOVED: Aggregate DBG_UART / I2C_FRU hierarchical labels",
        "ADDED: U1 STM32G071 management MCU with I2C1/I2C2/UART/SWD",
        "ADDED: U2 AT24C256 FRU EEPROM with address straps",
        "ADDED: R1 I2C pull-up network",
        "ADDED: U3 PMBus pass-through interface",
        "ADDED: U4 SMBus level shifter (OCP → MCU)",
        "ADDED: U5 TMP117 temperature sensor",
        "ADDED: J1 debug UART 3-pin header",
        "ADDED: J2 I2C expansion connector",
        "ADDED: U6 I2C mux DNP (optional)",
        "ADDED: U7 fan PWM optional block",
        "ADDED: U8–U10 AMD SMBus/PMBus/GPIO TODO blocks (NC)",
    ]


def render_mgmt_block(lib_name: str, block: MgmtBlock) -> str:
    pins = block.pins
    lines = [
        f'  (symbol "{lib_name}:{block.symbol_name}" (pin_names (offset 1.016)) (exclude_from_sim no) (in_bom yes) (on_board yes)',
        f'    (property "Reference" "{block.reference_prefix}" (at 0 0 0)',
        f'      (effects (font (size 1.27 1.27)) (justify left)))',
        f'    (property "Value" "{block.value}" (at 0 -2.54 0)',
        f'      (effects (font (size 1.27 1.27)) (justify left)))',
        f'    (property "Category" "{block.category}" (at 0 -5.08 0)',
        f'      (effects (font (size 1.27 1.27)) hide))',
        f'    (property "MPN_Example" "{block.mpn_example}" (at 0 -7.62 0)',
        f'      (effects (font (size 1.27 1.27)) hide))',
        f'    (property "Notes" "{block.notes}" (at 0 -10.16 0)',
        f'      (effects (font (size 1.27 1.27)) hide))',
        f'    (symbol "{block.symbol_name}_0_1"',
        f"      (pin_numbers hide)",
        f"      (pin_names (offset 1.016))",
        f"      (exclude_from_sim no)",
        f"      (in_bom yes)",
        f"      (on_board yes)",
    ]
    body_h = max(5.08, (len(pins) - 1) * 2.54 + 2.54)
    lines.append(f'      (rectangle (start -5.08 -2.54) (end 0 {body_h})')
    lines.append(f"        (stroke (width 0.254) (type default))")
    lines.append(f"        (fill (type background))")
    lines.append(f"      )")
    for idx, pin in enumerate(pins):
        y = idx * 2.54
        lines.append(f'      (pin {pin.electrical} line (at -7.62 {y} 0) (length 2.54)')
        lines.append(f'        (name "{pin.name}" (effects (font (size 1.016 1.016))))')
        lines.append(f'        (number "{idx + 1}" (effects (font (size 1.016 1.016))))')
        lines.append(f"      )")
    lines.append(f"    )")
    lines.append(f"  )")
    return "\n".join(lines)


def append_management_symbols(path: Path) -> None:
    path = Path(path)
    if path.exists() and "Mgmt_MCU_STM32G071" in path.read_text():
        return
    fragments = [render_mgmt_block("MI250X-Carrier", b) for b in management_blocks()]
    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            "(kicad_symbol_lib (version 20241209) (generator \"management_system\")\n"
            + "\n".join(fragments)
            + "\n)\n"
        )
        return
    text = path.read_text().rstrip()
    if text.endswith(")"):
        text = text[:-1].rstrip()
    path.write_text(text + "\n" + "\n".join(fragments) + "\n)\n")


def write_management_audit_doc(path: Path) -> None:
    lines = [
        "# Management Sheet — Requirements Audit",
        "",
        f"OCP reference: {OCP_SPEC} {OCP_TABLE} (SMBus on Conn0).",
        "",
        "## Verified prototype requirements",
        "",
        "| Item | Source | Notes |",
        "|------|--------|-------|",
    ]
    for item in verified_requirements():
        lines.append(f"| {item['item']} | {item['source']} | {item['note']} |")
    lines.extend(["", "## Optional features (not required for Rev1 MVP)", ""])
    for item in optional_features():
        lines.append(f"- **{item['item']}**: {item['note']}")
    lines.extend(["", "## AMD-specific management — TODO (do not route)", ""])
    for item in amd_management_todo():
        lines.append(f"- **{item['signal']}**: {item['status']}")
    lines.extend(["", "## Architecture blocks on sheet", ""])
    lines.append("| Ref | Block | Category |")
    lines.append("|-----|-------|----------|")
    placement = [
        ("U1", "Mgmt_MCU_STM32G071", "verified"),
        ("U2", "Mgmt_FRU_EEPROM", "verified"),
        ("R1", "Mgmt_I2C_Pullups", "verified"),
        ("U3", "Mgmt_PMBus_PassThrough", "verified"),
        ("U4", "Mgmt_SMBus_LevelShift", "verified"),
        ("U5", "Mgmt_Temp_TMP117", "verified"),
        ("J1", "Mgmt_UART_Debug", "verified"),
        ("J2", "Mgmt_I2C_Exp_Connector", "verified"),
        ("U6", "Mgmt_I2C_Mux_DNP", "optional"),
        ("U7", "Mgmt_Fan_PWM_TODO", "optional"),
        ("U8", "Mgmt_AMD_SMBus_TODO", "amd_todo"),
        ("U9", "Mgmt_AMD_PMBus_TODO", "amd_todo"),
        ("U10", "Mgmt_AMD_GPIO_TODO", "amd_todo"),
    ]
    for ref, sym, cat in placement:
        lines.append(f"| {ref} | {sym} | {cat} |")
    lines.extend(["", "## Placeholders replaced", ""])
    for item in placeholders_identified():
        lines.append(f"- {item}")
    path.write_text("\n".join(lines) + "\n")
