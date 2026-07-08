"""Test points and bring-up access for MI250X OAM carrier Rev1.

Only nets that exist in the hierarchical schematic are listed.
No invented signals. Pass/fail limits remain TODO per 15_Reverse_Engineering/08_Bringup.md.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

OCP_SPEC = "OCP Accelerator Module Design Specification v1.5"
OCP_TABLE = "Table 4 OAM Pinouts"


@dataclass(frozen=True)
class TpPin:
    name: str
    electrical: str
    description: str = ""


@dataclass(frozen=True)
class TpBlock:
    symbol_name: str
    value: str
    reference_prefix: str
    pins: list[TpPin]
    notes: str


def power_rail_test_points() -> list[dict[str, str]]:
    """Primary carrier rails — names from Power_System hierarchical outputs."""
    return [
        {"net": "VIN_12V", "tp": "TP_VIN_12V", "source": "Power_System J1 input", "limit": "TODO — AMD/input spec"},
        {"net": "OAM_12V", "tp": "TP_OAM_12V", "source": "Power_System N1 bus", "limit": "TODO — MI250X 12V draw"},
        {"net": "OAM_P12V1", "tp": "TP_OAM_P12V1", "source": f"OCP {OCP_TABLE} P12V1 logical", "limit": "TODO"},
        {"net": "OAM_P12V2", "tp": "TP_OAM_P12V2", "source": f"OCP {OCP_TABLE} P12V2 logical", "limit": "TODO"},
        {"net": "MGMT_3V3", "tp": "TP_MGMT_3V3", "source": "Power_System U4 LDO", "limit": "3.3V nominal — tolerance TODO"},
        {"net": "LOGIC_3V3", "tp": "TP_LOGIC_3V3", "source": "Power_System U5 LDO → OAM P3V3", "limit": "TODO — OAM load unknown"},
        {"net": "FAN_12V", "tp": "TP_FAN_12V", "source": "Power_System J2 fan rail", "limit": "TODO"},
        {"net": "GND", "tp": "TP_GND", "source": "Power return — multiple locations", "limit": "0V reference"},
    ]


def pcie_debug_signals() -> dict[str, list[dict[str, str]]]:
    """PCIe-related signals in this project — suitable vs not for solder test points."""
    return {
        "suitable_for_tp": [
            {
                "net": "PE_REFCLKp",
                "tp": "TP_PE_REFCLKp",
                "source": f"OCP {OCP_TABLE} — Clocking_Reset Y1/U1",
                "note": "100 MHz diff (p) — scope probe; keep stub short",
            },
            {
                "net": "PE_REFCLKn",
                "tp": "TP_PE_REFCLKn",
                "source": f"OCP {OCP_TABLE} — Clocking_Reset Y1/U1",
                "note": "100 MHz diff (n) — scope probe",
            },
            {
                "net": "PERST_N",
                "tp": "TP_PERST_N",
                "source": f"OCP {OCP_TABLE} PERST# — Clocking_Reset U2",
                "note": "Active-low PCIe reset — logic analyzer",
            },
            {
                "net": "PRESNT_N",
                "tp": "TP_PRESNT_N",
                "source": f"OCP {OCP_TABLE} PRESNT# — Host_PCIe bridge",
                "note": "Module presence — logic level TODO",
            },
        ],
        "not_suitable_stub_tp": [
            {
                "net": "PETp0..15 / PETn0..15",
                "source": f"OCP {OCP_TABLE} host link TX",
                "note": "High-speed differential — no stub TPs; probe at Mirror Mezz or host edge only",
            },
            {
                "net": "PERp0..15 / PERn0..15",
                "source": f"OCP {OCP_TABLE} host link RX",
                "note": "High-speed differential — SI probe at connector, not solder TP",
            },
            {
                "net": "PCIE_Ln_TX/RX_*",
                "source": "Host_PCIe sheet — PCIe CEM Gen4",
                "note": "Host slot lanes — same as above",
            },
            {
                "net": "CLKREQ_N_TODO",
                "source": "Host_PCIe — not in OCP Table 4",
                "note": "TODO — not routed; no TP until verified",
            },
            {
                "net": "WAKE_N_TODO",
                "source": "Host_PCIe — not in OCP Table 4",
                "note": "TODO — not routed",
            },
        ],
    }


def management_debug_access() -> list[dict[str, str]]:
    return [
        {
            "bus": "SMBus (OAM)",
            "nets": "SMBUS_CLK, SMBUS_DATA, SMBUS_ALERT_N",
            "tp": "TP_SMBUS_CLK, TP_SMBUS_DATA, TP_SMBUS_ALERT_N",
            "source": f"OCP {OCP_TABLE} — Management U4",
        },
        {
            "bus": "PMBus",
            "nets": "PMBUS_SCL, PMBUS_SDA",
            "tp": "TP_PMBUS_SCL, TP_PMBUS_SDA",
            "source": "Management U3 — module addresses AMD TODO",
        },
        {
            "bus": "I2C expansion",
            "nets": "I2C_SCL, I2C_SDA",
            "header": "J_I2C_DBG (4-pin)",
            "source": "Management J2 → Expansion sheet",
        },
        {
            "bus": "Debug UART",
            "nets": "DBG_UART_TX, DBG_UART_RX",
            "header": "J_UART_DBG on Management J1 (primary)",
            "tp": "TP_UART_TX, TP_UART_RX",
            "source": "Management U1 — 3.3V UART",
        },
    ]


def debug_headers() -> list[dict[str, str]]:
    return [
        {
            "ref": "J1",
            "name": "J_I2C_DBG",
            "pins": "1=SCL, 2=SDA, 3=MGMT_3V3, 4=GND",
            "nets": "I2C_SCL, I2C_SDA",
            "location": "Test_Points sheet",
            "note": "Carrier/expansion I2C — 2.2k pull-ups on Management R1",
        },
        {
            "ref": "J2",
            "name": "J_UART_DBG",
            "pins": "1=TX, 2=RX, 3=GND",
            "nets": "DBG_UART_TX, DBG_UART_RX",
            "location": "Management sheet J1 (primary); TPs here for probe",
            "note": "3.3V UART — match Management J1 pinout",
        },
    ]


def hierarchical_tp_inputs() -> list[tuple[str, str]]:
    """Nets brought into Test_Points sheet via root hierarchy."""
    rails = [r["net"] for r in power_rail_test_points()]
    pcie = [s["net"] for s in pcie_debug_signals()["suitable_for_tp"]]
    mgmt = [
        "SMBUS_CLK",
        "SMBUS_DATA",
        "SMBUS_ALERT_N",
        "PMBUS_SCL",
        "PMBUS_SDA",
        "I2C_SCL",
        "I2C_SDA",
        "DBG_UART_TX",
        "DBG_UART_RX",
    ]
    return [(n, "input" if n != "GND" else "passive") for n in rails + pcie + mgmt]


def test_point_blocks() -> list[TpBlock]:
    blocks = [
        TpBlock(
            "Tp_Signal",
            "TestPoint",
            "TP",
            [TpPin("SIGNAL", "passive", "Net under test")],
            "1.0 mm or 0.5 mm round TP per AI_DESIGN_RULES.md",
        ),
        TpBlock(
            "Dbg_Header_I2C",
            "I2C_Debug_4pin",
            "J",
            [
                TpPin("SCL", "bidirectional", "I2C_SCL"),
                TpPin("SDA", "bidirectional", "I2C_SDA"),
                TpPin("VCC", "power_in", "MGMT_3V3"),
                TpPin("GND", "power_in", "Return"),
            ],
            "2.54 mm × 4 header — expansion/carrier I2C debug",
        ),
    ]
    return blocks


def bringup_checklist() -> list[dict[str, str]]:
    """Gated checklist — limits TODO; aligned with 15_Reverse_Engineering/08_Bringup.md."""
    return [
        {"phase": "0", "step": "Evidence gate", "action": "Confirm OAM pin map, rail table, REFCLK guide before energizing", "stop": "STOP if Wanted_Documents still missing"},
        {"phase": "1", "step": "Unpowered check", "action": "Visual inspect; GND continuity at TP_GND; no short VIN→GND", "stop": "STOP on short — limits TODO"},
        {"phase": "1", "step": "Power — input", "action": "Apply current-limited VIN_12V; measure TP_VIN_12V", "stop": "STOP — pass/fail voltage TODO"},
        {"phase": "1", "step": "Power — management", "action": "Verify TP_MGMT_3V3, TP_LOGIC_3V3 with VIN present", "stop": "STOP if not ~3.3V nominal (tolerance TODO)"},
        {"phase": "1", "step": "Power — OAM rails", "action": "Measure TP_OAM_12V, TP_OAM_P12V1, TP_OAM_P12V2 after hot-swap enable", "stop": "STOP — sequencing AMD TODO; do not enable OAM until documented"},
        {"phase": "1", "step": "Power — fan", "action": "Measure TP_FAN_12V if fan rail enabled", "stop": "Optional Rev1"},
        {"phase": "2", "step": "Clock", "action": "Scope TP_PE_REFCLKp/n — expect 100 MHz diff per OCP Table 4", "stop": "STOP — amplitude/jitter limits TODO (REFCLK Guide missing)"},
        {"phase": "2", "step": "Reset idle", "action": "Verify TP_PERST_N asserted (low) before release", "stop": "STOP — polarity/timing TODO"},
        {"phase": "3", "step": "UART", "action": "Connect to Management J1 / probe TP_UART_TX/RX — MCU console if firmware present", "stop": "STOP if no firmware — expected Rev1"},
        {"phase": "3", "step": "I2C scan", "action": "Use J_I2C_DBG — scan for FRU EEPROM (U2) and TMP117 (U5) addresses", "stop": "STOP — addresses TODO; do not assume"},
        {"phase": "3", "step": "SMBus", "action": "Probe TP_SMBUS_CLK/DATA — OAM module not installed or level shifter U4 only", "stop": "STOP — OAM SMBus addresses AMD TODO"},
        {"phase": "3", "step": "PMBus", "action": "Probe TP_PMBUS_SCL/SDA — module telemetry AMD TODO", "stop": "STOP — no invented addresses"},
        {"phase": "3", "step": "Temperature", "action": "Read TMP117 via I2C if address verified", "stop": "STOP — limit thresholds TODO"},
        {"phase": "4", "step": "Presence", "action": "Check TP_PRESNT_N with module seated", "stop": "STOP — logic level TODO"},
        {"phase": "4", "step": "PERST release", "action": "Release PERST# per AMD timing TODO after PE_REFCLK valid + OAM_PG", "stop": "STOP — sequencing not documented"},
        {"phase": "4", "step": "PCIe enumerate", "action": "Host BIOS/OS link training — no stub TPs on PET/PER lanes", "stop": "STOP on training failure — lane map TODO"},
        {"phase": "5", "step": "ROCm", "action": "After successful enumeration: rocminfo / driver load per 08_Bringup.md", "stop": "Software validation only — not hardware proof"},
    ]


def placeholders_identified() -> list[str]:
    return [
        "REMOVED: OAM_MirrorMezz_Conn0_TODO (wrong sheet)",
        "REMOVED: MCU/FRU/TEMP embedded stubs",
        "REMOVED: Only 4 hierarchical labels (VIN, OAM_12V, PE_REFCLKp/n)",
        "ADDED: TP per primary rail (8 nets from Power_System)",
        "ADDED: PCIe sideband TPs (PE_REFCLKp/n, PERST_N, PRESNT_N)",
        "ADDED: SMBus + PMBus TPs",
        "ADDED: UART probe TPs + I2C debug header J1",
        "ADDED: Documented unsuitable HS lane TPs (PET/PER)",
    ]


def render_tp_block(lib_name: str, block: TpBlock) -> str:
    pins = block.pins
    lines = [
        f'  (symbol "{lib_name}:{block.symbol_name}" (pin_names (offset 1.016)) (exclude_from_sim no) (in_bom yes) (on_board yes)',
        f'    (property "Reference" "{block.reference_prefix}" (at 0 0 0)',
        f'      (effects (font (size 1.27 1.27)) (justify left)))',
        f'    (property "Value" "{block.value}" (at 0 -2.54 0)',
        f'      (effects (font (size 1.27 1.27)) (justify left)))',
        f'    (property "Notes" "{block.notes}" (at 0 -5.08 0)',
        f'      (effects (font (size 1.27 1.27)) hide))',
        f'    (symbol "{block.symbol_name}_0_1"',
        f"      (pin_numbers hide)",
        f"      (exclude_from_sim no)",
        f"      (in_bom yes)",
        f"      (on_board yes)",
        f'      (rectangle (start -2.54 -2.54) (end 0 2.54)',
        f"        (stroke (width 0.254) (type default))",
        f"        (fill (type background))",
        f"      )",
    ]
    for idx, pin in enumerate(pins):
        y = idx * 2.54
        lines.append(f'      (pin {pin.electrical} line (at -5.08 {y} 0) (length 2.54)')
        lines.append(f'        (name "{pin.name}" (effects (font (size 1.016 1.016))))')
        lines.append(f'        (number "{idx + 1}" (effects (font (size 1.016 1.016))))')
        lines.append(f"      )")
    lines.append(f"    )")
    lines.append(f"  )")
    return "\n".join(lines)


def append_test_point_symbols(path: Path) -> None:
    path = Path(path)
    if path.exists() and "Tp_Signal" in path.read_text():
        return
    fragments = [render_tp_block("MI250X-Carrier", b) for b in test_point_blocks()]
    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            "(kicad_symbol_lib (version 20241209) (generator \"test_points_system\")\n"
            + "\n".join(fragments)
            + "\n)\n"
        )
        return
    text = path.read_text().rstrip()
    if text.endswith(")"):
        text = text[:-1].rstrip()
    path.write_text(text + "\n" + "\n".join(fragments) + "\n)\n")


def write_bringup_checklist_doc(path: Path) -> None:
    pcie = pcie_debug_signals()
    lines = [
        "# Bring-Up Checklist — Rev1 MI250X OAM Carrier",
        "",
        "Gated procedure per `15_Reverse_Engineering/08_Bringup.md`.",
        "**Pass/fail voltage, current, and timing limits are TODO** — do not energize OAM module until AMD rail table exists.",
        "",
        "## Power rails — test points required",
        "",
        "| Net | Test point | Source | Pass/fail limit |",
        "|-----|------------|--------|-----------------|",
    ]
    for r in power_rail_test_points():
        lines.append(f"| {r['net']} | {r['tp']} | {r['source']} | {r['limit']} |")
    lines.extend(["", "## PCIe — suitable for debug (test points on sheet)", ""])
    for s in pcie["suitable_for_tp"]:
        lines.append(f"- **{s['net']}** (`{s['tp']}`) — {s['note']}")
    lines.extend(["", "## PCIe — NOT suitable for stub test points", ""])
    for s in pcie["not_suitable_stub_tp"]:
        lines.append(f"- **{s['net']}** — {s['note']}")
    lines.extend(["", "## Debug headers", ""])
    for h in debug_headers():
        lines.append(f"- **{h['name']}** ({h['ref']}): {h['pins']} — nets: {h['nets']}. {h['note']}")
    lines.extend(["", "## Management debug access", ""])
    for m in management_debug_access():
        hdr = m.get("header", m.get("tp", ""))
        lines.append(f"- **{m['bus']}**: {m['nets']} — {hdr} ({m['source']})")
    lines.extend(["", "## Numbered bring-up checklist", ""])
    lines.append("| Phase | Step | Action | Stop condition |")
    lines.append("|-------|------|--------|----------------|")
    for item in bringup_checklist():
        lines.append(f"| {item['phase']} | {item['step']} | {item['action']} | {item['stop']} |")
    lines.extend(["", "## Placeholders replaced on Test_Points sheet", ""])
    for p in placeholders_identified():
        lines.append(f"- {p}")
    path.write_text("\n".join(lines) + "\n")
