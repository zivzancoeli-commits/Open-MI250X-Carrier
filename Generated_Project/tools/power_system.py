"""Power architecture symbols and rail audit for MI250X OAM carrier Rev1 prototype.

Carrier-side rails only. OAM module internal rails and AMD sequencing are TODO.
OCP Conn0/Conn1 power signal names used where verified (v1.5 §8.2, Table 4).
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

OCP_SPEC = "OCP Accelerator Module Design Specification v1.5"
OCP_POWER_SECTION = "§8.2 Conn0/Conn1 power"


@dataclass(frozen=True)
class PowerPin:
    name: str
    electrical: str
    description: str = ""


@dataclass(frozen=True)
class PowerBlock:
    symbol_name: str
    value: str
    reference_prefix: str
    pins: list[PowerPin]
    mpn_example: str
    notes: str


def power_blocks() -> list[PowerBlock]:
    """Prototype carrier power blocks — realistic architecture, ratings TODO."""
    return [
        PowerBlock(
            "Pwr_12V_Input",
            "12V_Input",
            "J",
            [
                PowerPin("VIN+", "power_in", "12V input positive"),
                PowerPin("VIN-", "power_in", "Return / chassis GND"),
                PowerPin("GND", "power_in", "Local power ground"),
            ],
            "MPN_TODO — 2-pin screw terminal or ATX peripheral",
            "System 12V harness per 20_System_BOM/Power.md planning goal",
        ),
        PowerBlock(
            "Pwr_Input_Protection",
            "Input_Protect",
            "D",
            [
                PowerPin("VIN", "passive", "Before fuse"),
                PowerPin("VOUT", "passive", "After TVS to fuse"),
                PowerPin("GND", "power_in", "Protection return"),
            ],
            "SMBJ15A or equiv — rating TODO after 12V current known",
            "Reverse polarity + transient clamp — values TODO",
        ),
        PowerBlock(
            "Pwr_Fuse",
            "Fuse_12V_In",
            "F",
            [
                PowerPin("IN", "passive", "Input side"),
                PowerPin("OUT", "passive", "Output side"),
            ],
            "MPN_TODO — blade fuse holder + fuse",
            "Input overcurrent — rating TODO (AMD 12V draw unknown)",
        ),
        PowerBlock(
            "Pwr_BulkCap_12V",
            "Bulk_12V",
            "C",
            [
                PowerPin("VIN", "passive", "12V rail"),
                PowerPin("GND", "power_in", "Return"),
            ],
            "2x 470µF/25V polymer + 100nF — values TODO",
            "Input bulk + HF bypass at entry",
        ),
        PowerBlock(
            "Pwr_HotSwap_12V",
            "HotSwap_12V",
            "U",
            [
                PowerPin("VIN", "power_in", "12V in"),
                PowerPin("VOUT", "power_out", "Switched 12V out"),
                PowerPin("EN", "input", "Enable — tie to sequencer TODO"),
                PowerPin("PG", "output", "Power good — to MCU TODO"),
                PowerPin("GND", "power_in", "Return"),
            ],
            "TPS25942ARVCR or equiv — SOA TODO",
            "eFuse / hot-swap / inrush limit for OAM 12V path",
        ),
        PowerBlock(
            "Pwr_OAM_Seq_TODO",
            "OAM_Seq_AMD_TODO",
            "U",
            [
                PowerPin("VIN_12V", "power_in", "12V input"),
                PowerPin("OAM_EN", "output", "Module enable — AMD timing TODO"),
                PowerPin("OAM_PG", "input", "Module power good — AMD TODO"),
                PowerPin("P12V1_EN", "output", "OCP P12V1 enable — sequencing TODO"),
                PowerPin("P12V2_EN", "output", "OCP P12V2 enable — sequencing TODO"),
                PowerPin("GND", "power_in", "Return"),
            ],
            "AMD sequencing TBD — do not implement without rail table",
            "Placeholder for AMD/OAM power-up order; nets unconnected until verified",
        ),
        PowerBlock(
            "Pwr_48V_TODO",
            "P48V_OAM_TODO",
            "U",
            [
                PowerPin("VIN_48V", "passive", "48V/54V input — not routed Rev1"),
                PowerPin("P48V_OUT", "passive", "To OAM P48V — NC until AMD confirms"),
                PowerPin("GND", "power_in", "Return"),
            ],
            "NC Rev1 — OCP P48V on Conn0",
            "MI250X may require 48V/54V; 12V-only prototype defers this rail",
        ),
        PowerBlock(
            "Pwr_LDO_3V3_Mgmt",
            "LDO_3V3_Mgmt",
            "U",
            [
                PowerPin("VIN", "power_in", "12V in"),
                PowerPin("VOUT", "power_out", "3.3V management out"),
                PowerPin("EN", "input", "Enable"),
                PowerPin("GND", "power_in", "Return"),
            ],
            "AP2112K-3.3TRG1 or TPS7A0333 — load current TODO",
            "MCU, FRU EEPROM, temp sensor, SMBus pull-ups, debug UART",
        ),
        PowerBlock(
            "Pwr_LDO_3V3_Logic",
            "LDO_3V3_Logic",
            "U",
            [
                PowerPin("VIN", "power_in", "12V in"),
                PowerPin("VOUT", "power_out", "3.3V logic / OAM aux out"),
                PowerPin("EN", "input", "Enable — may follow OAM_EN TODO"),
                PowerPin("GND", "power_in", "Return"),
            ],
            "AP2112K-3.3TRG1 or separate regulator — OAM load TODO",
            "OCP P3V3 Conn0 + P3V3_CONN1; separate domain from management",
        ),
        PowerBlock(
            "Pwr_Fan_12V",
            "Fan_12V_Dist",
            "J",
            [
                PowerPin("VIN", "power_in", "12V from input bus"),
                PowerPin("FAN+", "power_out", "Fan supply positive"),
                PowerPin("FAN-", "power_out", "Fan return"),
                PowerPin("GND", "power_in", "Local GND"),
            ],
            "4-pin PWM fan header ×1 — count TODO",
            "Carrier cooling fans; isolated fuse F_FAN; PWM from MCU on mgmt sheet",
        ),
        PowerBlock(
            "Pwr_Fuse_Fan",
            "Fuse_Fan_12V",
            "F",
            [
                PowerPin("IN", "passive", "From 12V bus"),
                PowerPin("OUT", "passive", "To fan distribution"),
            ],
            "MPN_TODO — low-current fuse",
            "Fan rail protection — rating TODO",
        ),
        PowerBlock(
            "Pwr_Bus_12V_OAM",
            "Bus_12V_OAM",
            "N",
            [
                PowerPin("P12V1", "power_out", "OCP P12V1 logical net"),
                PowerPin("P12V2", "power_out", "OCP P12V2 logical net"),
                PowerPin("GND", "power_in", "Return"),
            ],
            "Copper pour / bus bar — layout TODO",
            "OCP defines P12V1 + P12V2; may be common source until pin map confirms split",
        ),
    ]


def hierarchical_power_outputs() -> list[tuple[str, str]]:
    return [
        ("OAM_12V", "output"),
        ("OAM_P12V1", "output"),
        ("OAM_P12V2", "output"),
        ("MGMT_3V3", "output"),
        ("LOGIC_3V3", "output"),
        ("FAN_12V", "output"),
        ("GND", "passive"),
        ("OAM_EN_TODO", "output"),
        ("OAM_PG_TODO", "input"),
    ]


def hierarchical_power_input() -> list[tuple[str, str]]:
    return [("VIN_12V", "input")]


def missing_power_rails() -> dict[str, list[dict[str, str]]]:
    """Rails not implemented or not verified for Rev1 prototype."""
    return {
        "oam_connector_rails_todo": [
            {
                "rail": "P48V",
                "ocp_name": "P48V",
                "voltage": "48V / 54V (OCP)",
                "status": "NOT ROUTED Rev1 — 12V-only input; may be required for MI250X",
                "source": f"{OCP_SPEC} Table 4 Conn0",
            },
            {
                "rail": "P12V1",
                "ocp_name": "P12V1",
                "voltage": "12V",
                "status": "Logical net OAM_P12V1 — current/pin fanout TODO",
                "source": f"{OCP_SPEC} Table 4 Conn0",
            },
            {
                "rail": "P12V2",
                "ocp_name": "P12V2",
                "voltage": "12V",
                "status": "Logical net OAM_P12V2 — split vs P12V1 TODO",
                "source": f"{OCP_SPEC} Table 4 Conn0",
            },
            {
                "rail": "P3V3",
                "ocp_name": "P3V3",
                "voltage": "3.3V",
                "status": "Carrier LOGIC_3V3 planned — load current TODO",
                "source": f"{OCP_SPEC} Table 4 Conn0",
            },
            {
                "rail": "P3V3_CONN1",
                "ocp_name": "P3V3_CONN1",
                "voltage": "3.3V",
                "status": "May share LOGIC_3V3 — Conn1 pin assignment TODO",
                "source": f"{OCP_SPEC} Table 4 Conn1",
            },
            {
                "rail": "PVREF",
                "ocp_name": "PVREF / PVREF_CONN1",
                "voltage": "Reference output from module",
                "status": "Module output — not a carrier supply rail",
                "source": f"{OCP_SPEC} Table 4",
            },
        ],
        "amd_unknown_rails": [
            {"rail": "Standby / auxiliary", "status": "TODO — no AMD rail table in repo"},
            {"rail": "Module internal VRM inputs", "status": "TODO — on-module; MP2975 candidate unverified"},
            {"rail": "Sequencing enables (all)", "status": "TODO — OAM_EN, P12V1_EN, P12V2_EN timing unknown"},
            {"rail": "Power Good thresholds", "status": "TODO — OAM_PG behavior unknown"},
            {"rail": "12V current per rail", "status": "TODO — fuse/hot-swap SOA cannot be sized"},
            {"rail": "54V vs 48V nominal", "status": "TODO — confirm MI250X OAM input requirement"},
        ],
        "carrier_rails_missing_ratings": [
            {"rail": "VIN_12V", "status": "Input connector MPN and max current TODO"},
            {"rail": "MGMT_3V3", "status": "LDO selected — load budget TODO"},
            {"rail": "LOGIC_3V3", "status": "LDO selected — OAM 3.3V load TODO"},
            {"rail": "FAN_12V", "status": "Fan count, current, PWM control TODO"},
        ],
    }


def placeholders_identified() -> list[str]:
    """Every placeholder removed or retained on Power System sheet."""
    return [
        "REMOVED: OAM_MirrorMezz_Conn0_TODO (wrong sheet)",
        "REMOVED: MCU_STM32G071_TODO (belongs on Management)",
        "REMOVED: FRU_EEPROM_AT24C256 (belongs on Management)",
        "REMOVED: TEMP_TMP117 (belongs on Management)",
        "REMOVED: Generic text-only J_PWR / U_LDO blocks",
        "ADDED: J1 12V input connector block",
        "ADDED: D1 input protection (TVS) — rating TODO",
        "ADDED: F1 input fuse — rating TODO",
        "ADDED: CB1 bulk capacitors — values TODO",
        "ADDED: U1 hot-swap/eFuse TPS25942 class — SOA TODO",
        "ADDED: U2 OAM sequencer AMD_TODO — sequencing not implemented",
        "ADDED: U3 P48V block — explicitly NC Rev1",
        "ADDED: U4 LDO 3.3V management",
        "ADDED: U5 LDO 3.3V logic/OAM",
        "ADDED: F2 fan fuse — rating TODO",
        "ADDED: J2 fan 12V distribution header",
        "ADDED: N1 OAM 12V bus P12V1/P12V2 logical split",
    ]


def render_power_block_symbol(lib_name: str, block: PowerBlock) -> str:
    pins = block.pins
    lines = [
        f'  (symbol "{lib_name}:{block.symbol_name}" (pin_names (offset 1.016)) (exclude_from_sim no) (in_bom yes) (on_board yes)',
        f'    (property "Reference" "{block.reference_prefix}" (at 0 0 0)',
        f'      (effects (font (size 1.27 1.27)) (justify left)))',
        f'    (property "Value" "{block.value}" (at 0 -2.54 0)',
        f'      (effects (font (size 1.27 1.27)) (justify left)))',
        f'    (property "Footprint" "" (at 0 0 0)',
        f'      (effects (font (size 1.27 1.27)) hide))',
        f'    (property "MPN_Example" "{block.mpn_example}" (at 0 -5.08 0)',
        f'      (effects (font (size 1.27 1.27)) hide))',
        f'    (property "Notes" "{block.notes}" (at 0 -7.62 0)',
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


def append_power_symbols(path: Path) -> None:
    path = Path(path)
    fragments = [render_power_block_symbol("MI250X-Carrier", b) for b in power_blocks()]
    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            "(kicad_symbol_lib (version 20241209) (generator \"power_system\")\n"
            + "\n".join(fragments)
            + "\n)\n"
        )
        return
    text = path.read_text()
    if "Pwr_12V_Input" in text:
        return
    text = text.rstrip()
    if text.endswith(")"):
        text = text[:-1].rstrip()
    path.write_text(text + "\n" + "\n".join(fragments) + "\n)\n")


def write_missing_rails_doc(path: Path) -> None:
    data = missing_power_rails()
    lines = [
        "# Missing Power Rails — Verification Required",
        "",
        f"Rev1 prototype carrier. OCP reference: {OCP_SPEC} {OCP_POWER_SECTION}.",
        "AMD MI250X rail table not in repository — do not size or sequence from guesses.",
        "",
        "## Placeholders replaced on Power System sheet",
        "",
    ]
    for item in placeholders_identified():
        lines.append(f"- {item}")
    lines.extend(["", "## OCP connector rails — status", ""])
    lines.append("| Rail | OCP name | Voltage | Status | Source |")
    lines.append("|------|----------|---------|--------|--------|")
    for item in data["oam_connector_rails_todo"]:
        lines.append(
            f"| {item['rail']} | {item['ocp_name']} | {item['voltage']} | {item['status']} | {item['source']} |"
        )
    lines.extend(["", "## AMD / module rails — unknown", ""])
    for item in data["amd_unknown_rails"]:
        lines.append(f"- **{item['rail']}**: {item['status']}")
    lines.extend(["", "## Carrier rails — architecture present, ratings TODO", ""])
    for item in data["carrier_rails_missing_ratings"]:
        lines.append(f"- **{item['rail']}**: {item['status']}")
    lines.extend(
        [
            "",
            "## Power domains on sheet",
            "",
            "| Domain | Components | Hierarchical output |",
            "|--------|------------|---------------------|",
            "| 12V input | J1, D1, F1, CB1 | VIN_12V (in) |",
            "| OAM 12V | U1 hot-swap, U2 seq TODO, N1 bus | OAM_12V, OAM_P12V1, OAM_P12V2 |",
            "| 48V OAM | U3 P48V TODO | Not routed (NC Rev1) |",
            "| 3.3V management | U4 LDO | MGMT_3V3 |",
            "| 3.3V logic/OAM | U5 LDO | LOGIC_3V3 |",
            "| Fan 12V | F2, J2 | FAN_12V |",
            "| Sequencing | U2 OAM_Seq_AMD_TODO | OAM_EN_TODO, OAM_PG_TODO |",
        ]
    )
    path.write_text("\n".join(lines) + "\n")
