"""Expansion subsystem placeholders for MI250X OAM carrier Rev1.

Interface planning only — no multi-module implementation on Rev1.
All expansion logic symbols are DNP (do not populate).
Only nets that exist elsewhere in the hierarchical schematic are used.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

OCP_SPEC = "OCP Accelerator Module Design Specification v1.5"
OCP_TABLE = "Table 4 OAM Pinouts"
PCIE_SPEC = "PCI Express Card Electromechanical Specification (CEM) Gen4"


@dataclass(frozen=True)
class ExpPin:
    name: str
    electrical: str
    description: str = ""


@dataclass(frozen=True)
class ExpBlock:
    symbol_name: str
    value: str
    reference_prefix: str
    pins: list[ExpPin]
    mpn_example: str
    notes: str
    dnp: bool = True


def expansion_topology() -> list[dict[str, str]]:
    """Documented scale-out path — electrical details TODO until one-module verified."""
    return [
        {
            "revision": "Rev1",
            "modules": "1",
            "pcie": "Direct Host_PCIe x16 → OAM_Interface (no switch populated)",
            "power": "Single OAM_12V domain from Power_System",
            "mgmt": "Management J2 I2C → Expansion sheet interface only",
        },
        {
            "revision": "Rev2",
            "modules": "2",
            "pcie": "PCIe switch DNP placeholder — upstream from host, downstream to slot 1 + slot 2",
            "power": "OAM_12V bus bar pads DNP — per-module hot-swap AMD TODO",
            "mgmt": "I2C mux DNP — per-module SMBus/FRU addressing AMD TODO",
        },
        {
            "revision": "Rev3",
            "modules": "4",
            "pcie": "Switch topology and lane bifurcation TODO — host upstream width unknown",
            "power": "Distributed 12V — current budget and sequencing TODO",
            "mgmt": "Multi-drop SMBus arbitration TODO",
        },
        {
            "revision": "Rev4",
            "modules": "8",
            "pcie": "Multi-switch or retimer fabric TODO — no verified topology in repo",
            "power": "Chassis-level distribution TODO",
            "mgmt": "BMC/IPMI scale-out TODO",
        },
    ]


def pcie_switch_integration() -> dict[str, list[dict[str, str]]]:
    """Future PCIe switch placement — planning only; no switch MPN selected."""
    return {
        "rev1_bypass": [
            {
                "path": "Host_PCIe J3 (PCIE_Ln_TX/RX) ↔ OAM_Interface PET/PER",
                "note": "Rev1 direct path — U1 switch DNP, footprint only",
            },
            {
                "path": "Clocking_Reset Y1/U1 → PE_REFCLKp/n → OAM_Interface",
                "note": "Rev1 single refclk fanout — Expansion U3 REFCLK fanout DNP for multi-module",
            },
            {
                "path": "Clocking_Reset U2 → PERST_N → OAM_Interface",
                "note": "Rev1 single reset — Expansion U4 PERST fanout DNP for additional slots",
            },
        ],
        "future_switch_ports": [
            {
                "port": "UPSTREAM",
                "nets": "PCIE_L0..15_TX_P/N, PCIE_L0..15_RX_P/N (from Host_PCIe)",
                "note": "Host root complex — lane count and bifurcation AMD TODO",
            },
            {
                "port": "DOWNSTREAM_0",
                "nets": "PETp0..15, PETn0..15, PERp0..15, PERn0..15 (to OAM slot 1 / existing OAM_Interface)",
                "note": "Rev1 active module — bypass switch in direct mode or wire to port 0 when populated",
            },
            {
                "port": "DOWNSTREAM_1",
                "nets": "Same PET/PER naming — OAM slot 2 DNP connector J2",
                "note": "Second Mirror Mezz — footprint DNP; full pin map on OAM_Interface sheet pattern",
            },
            {
                "port": "DOWNSTREAM_2..3",
                "nets": "PET/PER logical groups — slots 3–4 DNP",
                "note": "Rev3 planning — mechanical and thermal TODO",
            },
            {
                "port": "REFCLK_IN",
                "nets": "PE_REFCLKp, PE_REFCLKn",
                "note": "100 MHz HCSL from Clocking_Reset — switch refclk fanout requirements TODO",
            },
            {
                "port": "PERST_IN",
                "nets": "PERST_N",
                "note": "PCIe reset — per-port PERST_OUTn from switch or separate fanout DNP",
            },
            {
                "port": "PRESNT_IN / PRESNT_OUTn",
                "nets": "PRESNT_N per slot",
                "note": "Module presence — Host_PCIe bridge today; per-slot presence TODO",
            },
            {
                "port": "CLKREQ_N / WAKE_N",
                "nets": "CLKREQ_N_TODO, WAKE_N_TODO",
                "note": "Not in OCP Table 4 — not routed Rev1; switch sideband support unknown",
            },
        ],
        "open_questions": [
            "Switch vs retimer vs redriver — no verified requirement for 1× MI250X (see 15_Reverse_Engineering/05_PCIe.md)",
            "AMD MI250X dual-GCD lane map affects downstream port width — TODO",
            "Host upstream: x16 vs bifurcated x8/x8 for dual module — TODO",
            "AC coupling on PET path per OCP — per-port cap placement when switch inserted — TODO",
            "Switch reference clock jitter budget vs OCP PE_REFCLK — REFCLK guide missing",
            "Switch power rail (3.3V / 1.8V / 12V) — not on Power_System Rev1",
            "Firmware/OS enumeration with switch — software topology TODO",
        ],
    }


def expansion_blocks() -> list[ExpBlock]:
    """All blocks DNP — placeholders and interface planning only."""
    return [
        ExpBlock(
            "Exp_PCIe_Switch_DNP",
            "PCIe_Switch_DNP",
            "U",
            [
                ExpPin("UPSTREAM", "passive", "Logical — Host_PCIe PCIE_Ln_TX/RX (not routed Rev1)"),
                ExpPin("DOWNSTREAM_0", "passive", "Logical — OAM slot 1 PET/PER (Rev1 bypass)"),
                ExpPin("DOWNSTREAM_1", "passive", "Logical — OAM slot 2 PET/PER DNP"),
                ExpPin("DOWNSTREAM_2", "passive", "Logical — slot 3 DNP"),
                ExpPin("DOWNSTREAM_3", "passive", "Logical — slot 4 DNP"),
                ExpPin("REFCLK_IN", "passive", "PE_REFCLKp/n from Clocking_Reset"),
                ExpPin("PERST_IN", "passive", "PERST_N from reset distribution"),
                ExpPin("REFCLK_OUT0", "passive", "Per-port refclk — fanout TODO"),
                ExpPin("REFCLK_OUT1", "passive", "Per-port refclk — fanout TODO"),
                ExpPin("PERST_OUT0", "passive", "Per-port reset — fanout TODO"),
                ExpPin("PERST_OUT1", "passive", "Per-port reset — fanout TODO"),
                ExpPin("GND", "power_in", "Return"),
            ],
            "MPN TODO — candidate category only; see 18_Component_Research/08_PCIe_Retimers.md",
            "PCIe Gen4 switch fabric for 2/4/8 OAM — DNP Rev1; footprint reserved",
            dnp=True,
        ),
        ExpBlock(
            "Exp_OAM_Slot2_DNP",
            "OAM_Slot2_DNP",
            "J",
            [
                ExpPin("OAM_12V", "passive", "From OAM_12V bus bar — Power_System domain"),
                ExpPin("LOGIC_3V3", "passive", "OAM P3V3 — LOGIC_3V3 from Power_System"),
                ExpPin("GND", "power_in", "Return"),
                ExpPin("PE_REFCLKp", "passive", f"OCP {OCP_TABLE}"),
                ExpPin("PE_REFCLKn", "passive", f"OCP {OCP_TABLE}"),
                ExpPin("PERST_N", "passive", f"OCP {OCP_TABLE} PERST#"),
                ExpPin("PRESNT_N", "passive", f"OCP {OCP_TABLE} PRESNT#"),
                ExpPin("SMBUS_CLK", "passive", f"OCP {OCP_TABLE} SMBus_CLK"),
                ExpPin("SMBUS_DATA", "passive", f"OCP {OCP_TABLE} SMBus_D"),
            ],
            "Molex Mirror Mezz Pro — same class as OAM_Interface J1/J2; DNP Rev1",
            "Second OAM module connector placeholder — 688-pin map not expanded on this sheet",
            dnp=True,
        ),
        ExpBlock(
            "Exp_Power_Bus_DNP",
            "OAM_12V_BusBar_DNP",
            "J",
            [
                ExpPin("OAM_12V_IN", "passive", "From Power_System N1 OAM_12V bus"),
                ExpPin("SLOT2_12V", "passive", "Tap to slot 2 — DNP"),
                ExpPin("SLOT3_12V", "passive", "Tap to slot 3 — DNP"),
                ExpPin("SLOT4_12V", "passive", "Tap to slot 4 — DNP"),
                ExpPin("GND", "power_in", "Return"),
            ],
            "Bus bar or heavy copper pour pads — rating TODO",
            "12V distribution taps for additional OAM modules — DNP Rev1",
            dnp=True,
        ),
        ExpBlock(
            "Exp_I2C_Mux_DNP",
            "I2C_Mux_Exp_DNP",
            "U",
            [
                ExpPin("SCL_IN", "bidirectional", "I2C_SCL from Management J2"),
                ExpPin("SDA_IN", "bidirectional", "I2C_SDA from Management J2"),
                ExpPin("SCL_OUT0", "bidirectional", "Module 0 / carrier sensors — active Rev1 path"),
                ExpPin("SDA_OUT0", "bidirectional", "Module 0 / carrier sensors"),
                ExpPin("SCL_OUT1", "bidirectional", "Module 2 management — DNP"),
                ExpPin("SDA_OUT1", "bidirectional", "Module 2 management — DNP"),
                ExpPin("GND", "power_in", "Return"),
            ],
            "PCA9548A class — DNP; note Management U6 is upstream optional mux",
            "Expansion-side I2C fanout for per-module management — DNP Rev1",
            dnp=True,
        ),
        ExpBlock(
            "Exp_REFCLK_Fanout_DNP",
            "PE_REFCLK_Fanout_DNP",
            "U",
            [
                ExpPin("REFCLK_IN_P", "passive", "PE_REFCLKp from Clocking_Reset"),
                ExpPin("REFCLK_IN_N", "passive", "PE_REFCLKn from Clocking_Reset"),
                ExpPin("REFCLK_OUT0_P", "passive", "To OAM slot 1 — Rev1 direct from U1 buffer"),
                ExpPin("REFCLK_OUT0_N", "passive", "To OAM slot 1"),
                ExpPin("REFCLK_OUT1_P", "passive", "To OAM slot 2 — DNP"),
                ExpPin("REFCLK_OUT1_N", "passive", "To OAM slot 2 — DNP"),
                ExpPin("GND", "power_in", "Return"),
            ],
            "LMK00101 / PCIe clock buffer class — DNP",
            "Multi-module PE_REFCLK fanout when switch populated — DNP Rev1",
            dnp=True,
        ),
        ExpBlock(
            "Exp_PERST_Fanout_DNP",
            "PERST_Fanout_DNP",
            "U",
            [
                ExpPin("PERST_IN", "passive", "PERST_N from Clocking_Reset U2"),
                ExpPin("PERST_OUT0", "passive", "To OAM slot 1"),
                ExpPin("PERST_OUT1", "passive", "To OAM slot 2 — DNP"),
                ExpPin("PERST_OUT2", "passive", "To slot 3 — DNP"),
                ExpPin("PERST_OUT3", "passive", "To slot 4 — DNP"),
                ExpPin("GND", "power_in", "Return"),
            ],
            "Reset buffer / gate array — DNP",
            "Per-module PERST# distribution — AMD sequencing TODO",
            dnp=True,
        ),
        ExpBlock(
            "Exp_Mgmt_I2C_Interface",
            "I2C_Exp_Interface",
            "J",
            [
                ExpPin("SCL", "bidirectional", "I2C_SCL ← Management J2"),
                ExpPin("SDA", "bidirectional", "I2C_SDA ← Management J2"),
                ExpPin("GND", "power_in", "Return"),
            ],
            "2-pin or 4-pin header — matches Management J2",
            "Rev1 active interface hook — not expansion logic; connects Management to Expansion sheet",
            dnp=False,
        ),
    ]


def hierarchical_expansion_inputs() -> list[tuple[str, str]]:
    """Nets brought into Expansion sheet via root hierarchy — all exist on other sheets."""
    return [
        ("I2C_SCL", "bidirectional"),
        ("I2C_SDA", "bidirectional"),
        ("OAM_12V", "input"),
        ("MGMT_3V3", "input"),
        ("GND", "passive"),
        ("PE_REFCLKp", "input"),
        ("PE_REFCLKn", "input"),
        ("PERST_N", "input"),
    ]


def placeholders_identified() -> list[str]:
    return [
        "REMOVED: OAM_MirrorMezz_Conn0_TODO (belongs on OAM_Interface sheet)",
        "REMOVED: MCU_STM32G071_TODO / FRU_EEPROM / TEMP_TMP117 (belong on Management sheet)",
        "REMOVED: build_child() generic stubs",
        "ADDED: U1 PCIe switch DNP — footprint + integration planning",
        "ADDED: J2 OAM slot 2 connector DNP — key OCP nets only",
        "ADDED: J3 OAM_12V bus bar DNP — multi-module power taps",
        "ADDED: U2 I2C mux DNP — per-module management fanout",
        "ADDED: U3 REFCLK fanout DNP, U4 PERST fanout DNP",
        "ADDED: J1 I2C interface from Management (Rev1 hook)",
        "DOCUMENTED: PCIe switch upstream/downstream/refclk/reset — docs/expansion_planning.md",
    ]


def render_exp_block(lib_name: str, block: ExpBlock) -> str:
    pins = block.pins
    dnp_str = "yes" if block.dnp else "no"
    lines = [
        f'  (symbol "{lib_name}:{block.symbol_name}" (pin_names (offset 1.016)) (exclude_from_sim no) (in_bom yes) (on_board yes)',
        f'    (property "Reference" "{block.reference_prefix}" (at 0 0 0)',
        f'      (effects (font (size 1.27 1.27)) (justify left)))',
        f'    (property "Value" "{block.value}" (at 0 -2.54 0)',
        f'      (effects (font (size 1.27 1.27)) (justify left)))',
        f'    (property "DNP" "{dnp_str}" (at 0 -5.08 0)',
        f'      (effects (font (size 1.27 1.27)) hide))',
        f'    (property "MPN_Example" "{block.mpn_example}" (at 0 -7.62 0)',
        f'      (effects (font (size 1.27 1.27)) hide))',
        f'    (property "Notes" "{block.notes}" (at 0 -10.16 0)',
        f'      (effects (font (size 1.27 1.27)) hide))',
        f'    (symbol "{block.symbol_name}_0_1"',
        f"      (pin_numbers hide)",
        f"      (exclude_from_sim no)",
        f"      (in_bom yes)",
        f"      (on_board yes)",
        f'      (rectangle (start -2.54 -2.54) (end 0 {2.54 * max(len(pins) - 1, 1)})',
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


def append_expansion_symbols(path: Path) -> None:
    path = Path(path)
    if path.exists() and "Exp_PCIe_Switch_DNP" in path.read_text():
        return
    fragments = [render_exp_block("MI250X-Carrier", b) for b in expansion_blocks()]
    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            "(kicad_symbol_lib (version 20241209) (generator \"expansion_system\")\n"
            + "\n".join(fragments)
            + "\n)\n"
        )
        return
    text = path.read_text().rstrip()
    if text.endswith(")"):
        text = text[:-1].rstrip()
    path.write_text(text + "\n" + "\n".join(fragments) + "\n)\n")


def write_expansion_planning_doc(path: Path) -> None:
    topo = expansion_topology()
    sw = pcie_switch_integration()
    lines = [
        "# Expansion Planning — Rev1 MI250X OAM Carrier",
        "",
        "Interface planning only. **All expansion logic is DNP on Rev1.**",
        "No switch MPN, lane bifurcation, or multi-module power sequencing is implemented.",
        "",
        "## Revision scale-out path",
        "",
        "| Revision | Modules | PCIe | Power | Management |",
        "|----------|---------|------|-------|------------|",
    ]
    for t in topo:
        lines.append(f"| {t['revision']} | {t['modules']} | {t['pcie']} | {t['power']} | {t['mgmt']} |")

    lines.extend(["", "## Rev1 active interface (not DNP)", ""])
    lines.append("- **I2C_SCL / I2C_SDA** — Management sheet J2 → Expansion sheet J1 (carrier/expansion I2C hook)")
    lines.append("- All other Expansion sheet symbols are **DNP** — footprint and planning only")

    lines.extend(["", "## PCIe switch integration (future — U1 DNP)", ""])
    lines.append("Rev1 bypasses the switch: Host_PCIe connects directly to OAM_Interface.")
    lines.append("")
    lines.append("### Rev1 direct paths (active today)")
    for item in sw["rev1_bypass"]:
        lines.append(f"- **{item['path']}** — {item['note']}")
    lines.extend(["", "### Future switch port map (logical — not routed Rev1)", ""])
    for port in sw["future_switch_ports"]:
        lines.append(f"- **{port['port']}**: nets `{port['nets']}` — {port['note']}")

    lines.extend(["", "### PCIe switch open questions", ""])
    for q in sw["open_questions"]:
        lines.append(f"- {q}")

    lines.extend(["", "## Expansion sheet placeholders (all DNP except J1)", ""])
    lines.append("| Ref | Symbol | Value | DNP | Notes |")
    lines.append("|-----|--------|-------|-----|-------|")
    ref_map = {"Exp_PCIe_Switch_DNP": "U1", "Exp_OAM_Slot2_DNP": "J2", "Exp_Power_Bus_DNP": "J3",
               "Exp_I2C_Mux_DNP": "U2", "Exp_REFCLK_Fanout_DNP": "U3", "Exp_PERST_Fanout_DNP": "U4",
               "Exp_Mgmt_I2C_Interface": "J1"}
    for block in expansion_blocks():
        ref = ref_map.get(block.symbol_name, block.reference_prefix)
        dnp = "no" if not block.dnp else "yes"
        lines.append(f"| {ref} | {block.symbol_name} | {block.value} | {dnp} | {block.notes} |")

    lines.extend(["", "## Hierarchical nets on Expansion sheet", ""])
    for name, shape in hierarchical_expansion_inputs():
        lines.append(f"- `{name}` ({shape})")

    lines.extend(["", "## Placeholders replaced", ""])
    for p in placeholders_identified():
        lines.append(f"- {p}")
    path.write_text("\n".join(lines) + "\n")
