"""Clocking and reset architecture for MI250X OAM carrier Rev1.

OCP OAM Table 4 naming for PE_REFCLKp/n (100 MHz PCIe reference clock).
AMD-specific and unverified clocks marked TODO — not invented.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

OCP_SPEC = "OCP Accelerator Module Design Specification v1.5"
OCP_TABLE = "Table 4 OAM Pinouts"
PCIE_CLK_SPEC = "PCI-SIG PCIe REFCLK specification (100 MHz HCSL/LP-HCSL)"


@dataclass(frozen=True)
class ClkPin:
    name: str
    electrical: str
    description: str = ""


@dataclass(frozen=True)
class ClkBlock:
    symbol_name: str
    value: str
    reference_prefix: str
    pins: list[ClkPin]
    mpn_example: str
    notes: str


def clock_blocks() -> list[ClkBlock]:
    return [
        ClkBlock(
            "Clk_Osc_100M_PE_REFCLK",
            "100MHz_PE_REFCLK",
            "Y",
            [
                ClkPin("VDD", "power_in", "3.3V supply from MGMT_3V3"),
                ClkPin("GND", "power_in", "Return"),
                ClkPin("OE", "input", "Output enable — tie high or MCU TODO"),
                ClkPin("PE_REFCLKp", "output", "OCP PE_REFCLKp — 100 MHz diff (p)"),
                ClkPin("PE_REFCLKn", "output", "OCP PE_REFCLKn — 100 MHz diff (n)"),
            ],
            "MPN_TODO — 100 MHz HCSL/LP-HCSL oscillator (e.g. Si510 class)",
            f"Primary REFCLK source; OCP {OCP_TABLE} PE_REFCLK 100 MHz PCIe Gen5 compliant",
        ),
        ClkBlock(
            "Clk_Buffer_PCIe",
            "PCIe_ClkBuffer",
            "U",
            [
                ClkPin("CLK_INp", "input", "Differential clock in (p)"),
                ClkPin("CLK_INn", "input", "Differential clock in (n)"),
                ClkPin("CLK0p", "output", "Fanout 0 (p) — to OAM PE_REFCLK"),
                ClkPin("CLK0n", "output", "Fanout 0 (n)"),
                ClkPin("CLK1p", "output", "Fanout 1 (p) — to host REFCLK TODO"),
                ClkPin("CLK1n", "output", "Fanout 1 (n)"),
                ClkPin("OE", "input", "Output enable"),
                ClkPin("VDD", "power_in", "3.3V"),
                ClkPin("GND", "power_in", "Return"),
            ],
            "MPN_TODO — 1:2 PCIe clock buffer (e.g. LMK00101, 9DB8014)",
            "Standard PCIe clock tree fanout when oscillator drives OAM + host slot",
        ),
        ClkBlock(
            "Clk_Term_PE_REFCLK",
            "PE_REFCLK_Term",
            "R",
            [
                ClkPin("PE_REFCLKp", "passive", "Near receiver"),
                ClkPin("PE_REFCLKn", "passive", "Near receiver"),
                ClkPin("GND", "power_in", "Return"),
            ],
            "49.9Ω series + 100nF AC coupling per PCIe SI guide — values TODO",
            "Termination / coupling per PCIe REFCLK routing rules — REFCLK Guide missing",
        ),
        ClkBlock(
            "Clk_HOST_REFCLK_IN",
            "Host_REFCLK_In",
            "J",
            [
                ClkPin("REFCLKp", "input", "Host slot REFCLK in (p) — alternate topology"),
                ClkPin("REFCLKn", "input", "Host slot REFCLK in (n)"),
                ClkPin("GND", "power_in", "Return"),
            ],
            "Passthrough from host — use if host supplies REFCLK (Mode B)",
            "Alternate clock tree: host-sourced REFCLK passed to OAM; select vs Y1 after REFCLK guide",
        ),
        ClkBlock(
            "Clk_AUX_100M_TODO",
            "AUX_100M_REFCLK_TODO",
            "U",
            [
                ClkPin("AUX_100M_REFCLKp", "passive", "OCP optional auxiliary clock (p)"),
                ClkPin("AUX_100M_REFCLKn", "passive", "OCP optional auxiliary clock (n)"),
                ClkPin("GND", "power_in", "Return"),
            ],
            "NC — OCP AUX_100M_REFCLK optional; MI250X requirement TODO",
            f"{OCP_TABLE} AUX_100M_REFCLK — do not implement until verified",
        ),
        ClkBlock(
            "Rst_PERST_Dist",
            "PERST_Distribution",
            "U",
            [
                ClkPin("PERST_IN", "input", "PERST# from host slot (active low)"),
                ClkPin("PERST_OUT", "output", "PERST# to OAM Conn0 (OCP PERST#)"),
                ClkPin("VDD", "power_in", "3.3V"),
                ClkPin("GND", "power_in", "Return"),
            ],
            "MPN_TODO — PERST# buffer/level shifter if required",
            f"OCP {OCP_TABLE} PERST# — CEM-compliant PCIe reset distribution",
        ),
        ClkBlock(
            "Rst_WARMRST_TODO",
            "WARMRST_TODO",
            "U",
            [
                ClkPin("WARMRST_IN", "passive", "Source TODO"),
                ClkPin("WARMRST_OUT", "passive", "OCP WARMRST# to OAM — NC until verified"),
                ClkPin("GND", "power_in", "Return"),
            ],
            "NC — OCP WARMRST# optional; AMD timing TODO",
            f"{OCP_TABLE} WARMRST# — warm reset; not routed Rev1",
        ),
        ClkBlock(
            "Rst_PERST_CONN1_TODO",
            "PERST_Conn1_TODO",
            "U",
            [
                ClkPin("PERST_CONN1", "passive", "OCP PERST#_CONN1 — usage TODO"),
                ClkPin("GND", "power_in", "Return"),
            ],
            "NC — verify OAM pin map for Conn1 PERST#",
            f"{OCP_TABLE} PERST# on Conn1 if routed",
        ),
        ClkBlock(
            "Rst_Seq_Gate_TODO",
            "Reset_Seq_AMD_TODO",
            "U",
            [
                ClkPin("OAM_PG", "input", "Power good from Power sheet — TODO"),
                ClkPin("PERST_GATE", "output", "Gated PERST# — AMD timing TODO"),
                ClkPin("GND", "power_in", "Return"),
            ],
            "AMD reset release vs Power Good — sequencing TODO",
            "Do not connect until AMD rail table + reset timing documented",
        ),
    ]


def reset_signals() -> dict[str, list[dict[str, str]]]:
    """Every reset-related signal — present, TODO, or out-of-scope."""
    return {
        "present_on_sheet": [
            {
                "signal": "PERST#",
                "ocp_name": "PERST#",
                "net": "PERST_N",
                "connector": "Conn0",
                "status": "Distributed via U2 — OCP CEM-compliant PCIe reset",
                "source": f"{OCP_SPEC} {OCP_TABLE}",
            },
        ],
        "ocp_todo_not_routed": [
            {
                "signal": "WARMRST#",
                "ocp_name": "WARMRST#",
                "net": "WARMRST_N_TODO",
                "connector": "Conn0",
                "status": "TODO — optional OCP warm reset; AMD requirement unknown",
                "source": f"{OCP_SPEC} {OCP_TABLE}",
            },
            {
                "signal": "PERST# (Conn1)",
                "ocp_name": "PERST#_CONN1",
                "net": "PERST_CONN1_N_TODO",
                "connector": "Conn1",
                "status": "TODO — verify if used on MI250X",
                "source": f"{OCP_SPEC} {OCP_TABLE}",
            },
        ],
        "jtag_not_pcie_reset": [
            {
                "signal": "JTAG0_TRST",
                "ocp_name": "JTAG0_TRST",
                "net": "—",
                "connector": "Conn1",
                "status": "JTAG test reset — Management/debug sheet, not Clocking",
                "source": f"{OCP_SPEC} {OCP_TABLE}",
            },
        ],
        "sequencing_related_todo": [
            {
                "signal": "OAM_PG",
                "ocp_name": "—",
                "net": "OAM_PG_TODO",
                "status": "Power Good gates PERST# release — AMD timing TODO",
                "source": "Power System sheet U2",
            },
            {
                "signal": "OAM_EN",
                "ocp_name": "—",
                "net": "OAM_EN_TODO",
                "status": "Module enable — not a reset; sequencing on Power sheet",
                "source": "Power System sheet",
            },
        ],
        "not_reset_sidebands": [
            {"signal": "CLKREQ#", "status": "Clock request — Host PCIe sheet TODO, not reset"},
            {"signal": "WAKE#", "status": "Wake — Host PCIe sheet TODO, not reset"},
            {"signal": "PRESNT#", "status": "Presence detect — not reset"},
        ],
    }


def unknown_clocks() -> list[dict[str, str]]:
    return [
        {
            "clock": "AUX_100M_REFCLKp/n",
            "ocp_ref": f"{OCP_SPEC} {OCP_TABLE}",
            "status": "TODO — optional OCP auxiliary 100 MHz; U3 block NC",
        },
        {
            "clock": "AMD GCD-specific REFCLK",
            "ocp_ref": "Not in OCP base table",
            "status": "TODO — do not invent; dual-GCD clocking unknown",
        },
        {
            "clock": "Spread-spectrum REFCLK",
            "ocp_ref": "REFCLK Guide missing",
            "status": "TODO — SSC requirement for MI250X unknown",
        },
        {
            "clock": "SerDes reference clocks (SERDES 1–7)",
            "ocp_ref": f"{OCP_SPEC} {OCP_TABLE}",
            "status": "TODO — inter-module links; N/A single-module Rev1",
        },
        {
            "clock": "Host vs carrier REFCLK ownership",
            "ocp_ref": "REFCLK Guide missing",
            "status": "TODO — Mode A (carrier Y1) vs Mode B (host passthrough)",
        },
    ]


def pcie_clock_tree_architecture() -> list[str]:
    """Standard PCIe clock tree — suggested topology for Rev1 prototype."""
    return [
        "MODE A (carrier-generated) — default Rev1 suggestion:",
        "  MGMT_3V3 → Y1 (100 MHz HCSL) → PE_REFCLKp/n → U1 clock buffer",
        "    ├─ CLK0 → R_TERM → OAM Conn0 PE_REFCLKp/n (OCP naming)",
        "    └─ CLK1 → host slot REFCLKp/n (if carrier sources host clock)",
        "MODE B (host-sourced) — alternate if baseboard provides REFCLK:",
        "  Host REFCLKp/n → J_HOST_CLK IN → U1 buffer → OAM PE_REFCLKp/n",
        "  Y1 DNP or not populated",
        "COMMON:",
        "  - 100 MHz ±300 ppm per PCIe; OCP cites PCIe Gen5-compliant PE_REFCLK",
        "  - Point-to-point differential; 85Ω or 100Ω per REFCLK Guide (TODO)",
        "  - PERST# asserted during power-up; release after PE_REFCLK stable + PG (AMD TODO)",
        "  - CLKREQ# couples to clock power-management — Host PCIe sheet (not Clocking)",
    ]


def hierarchical_clock_outputs() -> list[tuple[str, str]]:
    return [
        ("PE_REFCLKp", "bidirectional"),
        ("PE_REFCLKn", "bidirectional"),
        ("PERST_N", "bidirectional"),
        ("WARMRST_N_TODO", "passive"),
        ("AUX_100M_REFCLKp_TODO", "passive"),
        ("AUX_100M_REFCLKn_TODO", "passive"),
        ("PERST_CONN1_N_TODO", "passive"),
    ]


def hierarchical_clock_inputs() -> list[tuple[str, str]]:
    return [
        ("HOST_REFCLKp", "bidirectional"),
        ("HOST_REFCLKn", "bidirectional"),
        ("PERST_HOST_N", "bidirectional"),
        ("MGMT_3V3", "input"),
        ("GND", "passive"),
        ("OAM_PG_TODO", "input"),
    ]


def placeholders_identified() -> list[str]:
    return [
        "REMOVED: OAM_MirrorMezz_Conn0_TODO (wrong sheet)",
        "REMOVED: MCU / FRU / TEMP (wrong sheet)",
        "REMOVED: Generic Y1 text note without components",
        "ADDED: Y1 100 MHz oscillator — OCP PE_REFCLKp/n output naming",
        "ADDED: U1 PCIe clock buffer — standard fanout tree",
        "ADDED: R1 PE_REFCLK termination network — values TODO",
        "ADDED: J1 host REFCLK input — alternate Mode B topology",
        "ADDED: U2 PERST# distribution block",
        "ADDED: U3 AUX_100M_REFCLK TODO — OCP optional, NC",
        "ADDED: U4 WARMRST# TODO — OCP optional, NC",
        "ADDED: U5 PERST# Conn1 TODO — NC",
        "ADDED: U6 reset sequencing gate AMD TODO — NC",
    ]


def render_clk_block(lib_name: str, block: ClkBlock) -> str:
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


def append_clock_symbols(path: Path) -> None:
    path = Path(path)
    if path.exists() and "Clk_Osc_100M_PE_REFCLK" in path.read_text():
        return
    fragments = [render_clk_block("MI250X-Carrier", b) for b in clock_blocks()]
    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            "(kicad_symbol_lib (version 20241209) (generator \"clocking_reset\")\n"
            + "\n".join(fragments)
            + "\n)\n"
        )
        return
    text = path.read_text().rstrip()
    if text.endswith(")"):
        text = text[:-1].rstrip()
    path.write_text(text + "\n" + "\n".join(fragments) + "\n)\n")


def write_clocking_reset_doc(path: Path) -> None:
    resets = reset_signals()
    lines = [
        "# Clocking & Reset — Signal Audit",
        "",
        f"OCP reference: {OCP_SPEC} {OCP_TABLE}.",
        f"PE_REFCLK uses OCP naming: **PE_REFCLKp** / **PE_REFCLKn** (100 MHz PCIe reference).",
        "",
        "## Standard PCIe clock tree (suggested Rev1)",
        "",
    ]
    for line in pcie_clock_tree_architecture():
        lines.append(line)
    lines.extend(["", "## Reset signals — present on sheet", ""])
    lines.append("| Signal | OCP name | Net | Connector | Status |")
    lines.append("|--------|----------|-----|-----------|--------|")
    for item in resets["present_on_sheet"]:
        lines.append(
            f"| {item['signal']} | {item['ocp_name']} | {item['net']} | {item['connector']} | {item['status']} |"
        )
    lines.extend(["", "## Reset signals — OCP TODO (not routed)", ""])
    for item in resets["ocp_todo_not_routed"]:
        lines.append(
            f"- **{item['signal']}** (`{item['net']}`) — {item['status']} ({item['connector']})"
        )
    lines.extend(["", "## JTAG (not PCIe reset)", ""])
    for item in resets["jtag_not_pcie_reset"]:
        lines.append(f"- **{item['signal']}** — {item['status']}")
    lines.extend(["", "## Sequencing-related (not pure reset)", ""])
    for item in resets["sequencing_related_todo"]:
        lines.append(f"- **{item['signal']}** (`{item['net']}`) — {item['status']}")
    lines.extend(["", "## Not reset — PCIe sidebands", ""])
    for item in resets["not_reset_sidebands"]:
        lines.append(f"- **{item['signal']}** — {item['status']}")
    lines.extend(["", "## Unknown / TODO clocks", ""])
    lines.append("| Clock | OCP / source | Status |")
    lines.append("|-------|--------------|--------|")
    for item in unknown_clocks():
        lines.append(f"| {item['clock']} | {item['ocp_ref']} | {item['status']} |")
    lines.extend(["", "## Placeholders replaced", ""])
    for item in placeholders_identified():
        lines.append(f"- {item}")
    path.write_text("\n".join(lines) + "\n")
