"""Host PCIe Gen4 x16 symbols and support-signal audit for MI250X OAM carrier.

PCIe CEM Gen4 lane naming on host slot (logical — no physical pin numbers).
OCP OAM Table 4 PET/PER naming on OAM-facing bridge (logical only).
AMD dual-GCD lane mapping remains TODO.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

OCP_SPEC = "OCP Accelerator Module Design Specification v1.5"
OCP_TABLE = "Table 4 OAM Pinouts"
PCIE_SPEC = "PCI Express Card Electromechanical Specification (CEM) Gen4"
LANE_COUNT = 16


@dataclass(frozen=True)
class PciePin:
    name: str
    electrical: str
    spec_ref: str
    description: str = ""


def _lane_pairs(prefix: str, count: int, p_electrical: str, n_electrical: str, spec_ref: str, desc: str) -> list[PciePin]:
    pins: list[PciePin] = []
    for i in range(count):
        pins.append(PciePin(f"{prefix}{i}_P", p_electrical, spec_ref, f"{desc} lane {i} (p)"))
        pins.append(PciePin(f"{prefix}{i}_N", n_electrical, spec_ref, f"{desc} lane {i} (n)"))
    return pins


def host_slot_gen4_pins() -> list[PciePin]:
    """PCIe Gen4 CEM host root-port naming — TX/RX from host perspective."""
    pins: list[PciePin] = []
    for i in range(LANE_COUNT):
        pins.append(PciePin(f"PCIE_L{i}_TX_P", "output", PCIE_SPEC, f"Host TX lane {i} (p) → OAM PERp{i}"))
        pins.append(PciePin(f"PCIE_L{i}_TX_N", "output", PCIE_SPEC, f"Host TX lane {i} (n) → OAM PERn{i}"))
        pins.append(PciePin(f"PCIE_L{i}_RX_P", "input", PCIE_SPEC, f"Host RX lane {i} (p) ← OAM PETp{i}"))
        pins.append(PciePin(f"PCIE_L{i}_RX_N", "input", PCIE_SPEC, f"Host RX lane {i} (n) ← OAM PETn{i}"))
    pins.extend(
        [
            PciePin("REFCLK_P", "input", PCIE_SPEC, "100 MHz reference clock (p) — host slot"),
            PciePin("REFCLK_N", "input", PCIE_SPEC, "100 MHz reference clock (n) — host slot"),
            PciePin("PERST#", "input", PCIE_SPEC, "PCIe reset (active low)"),
            PciePin("CLKREQ#", "passive", f"{PCIE_SPEC} — TODO", "Clock request — pin/usage TODO for OAM"),
            PciePin("WAKE#", "passive", f"{PCIE_SPEC} — TODO", "Wake — pin/usage TODO for OAM"),
        ]
    )
    return pins


def ocp_oam_host_link_pins() -> list[PciePin]:
    """OCP Table 4 host x16 SerDes — PET/PER from module perspective."""
    pins: list[PciePin] = []
    for i in range(LANE_COUNT):
        pins.append(
            PciePin(
                f"PETp{i}",
                "input",
                f"{OCP_SPEC} {OCP_TABLE}",
                f"Host link TX lane {i} (module TX → host RX); AC caps on carrier",
            )
        )
        pins.append(
            PciePin(
                f"PETn{i}",
                "input",
                f"{OCP_SPEC} {OCP_TABLE}",
                f"Host link TX lane {i} (n)",
            )
        )
        pins.append(
            PciePin(
                f"PERp{i}",
                "output",
                f"{OCP_SPEC} {OCP_TABLE}",
                f"Host link RX lane {i} (module RX ← host TX); AC caps on carrier",
            )
        )
        pins.append(
            PciePin(
                f"PERn{i}",
                "output",
                f"{OCP_SPEC} {OCP_TABLE}",
                f"Host link RX lane {i} (n)",
            )
        )
    pins.extend(
        [
            PciePin("PE_REFCLKp", "output", f"{OCP_SPEC} {OCP_TABLE}", "PCIe ref clock 100 MHz (p)"),
            PciePin("PE_REFCLKn", "output", f"{OCP_SPEC} {OCP_TABLE}", "PCIe ref clock 100 MHz (n)"),
            PciePin("PERST#", "output", f"{OCP_SPEC} {OCP_TABLE}", "CEM-compliant PCIe reset"),
            PciePin("SMBus_D", "bidirectional", f"{OCP_SPEC} {OCP_TABLE}", "SMBus data — management bridge"),
            PciePin("SMBus_CLK", "output", f"{OCP_SPEC} {OCP_TABLE}", "SMBus clock"),
            PciePin("SMB_ALERT#", "input", f"{OCP_SPEC} {OCP_TABLE}", "SMBus alert"),
            PciePin("PRESNT#", "output", f"{OCP_SPEC} {OCP_TABLE}", "Module presence detect"),
            PciePin("CLKREQ#_TODO", "passive", f"{OCP_SPEC} — TODO", "Not in OCP Table 4 — verify AMD/OAM pin map"),
            PciePin("WAKE#_TODO", "passive", f"{OCP_SPEC} — TODO", "Not in OCP Table 4 — verify AMD/OAM pin map"),
        ]
    )
    return pins


def lane_mapping_todo_notes() -> list[str]:
    return [
        "AMD MI250X dual-GCD lane map: which PET/PER lanes map to GCD0 vs GCD1 — TODO",
        "Host slot lane order vs OAM PET/PER index — TODO (no lane reversal assumed)",
        "Bifurcation: 1x x16 vs 2x x8 — TODO verify with MI250X integration guide",
        "AC coupling: OCP requires caps on carrier for PET path (module TX); values/placement TODO",
    ]


def support_signal_audit() -> dict[str, list[dict[str, str]]]:
    """PCIe support signals — present, missing, or TODO on Host PCIe sheet."""
    return {
        "present_on_sheet": [
            {"signal": "PE_REFCLKp/n", "host_name": "REFCLK_P/N", "ocp_ref": f"{OCP_SPEC} {OCP_TABLE}", "status": "Named — routed via Clocking_Reset sheet"},
            {"signal": "PERST#", "host_name": "PERST#", "ocp_ref": f"{OCP_SPEC} {OCP_TABLE}", "status": "Named — host and OAM bridge"},
            {"signal": "PETp/n[0:15]", "host_name": "PCIE_L*_RX_P/N", "ocp_ref": f"{OCP_SPEC} {OCP_TABLE}", "status": "All 16 lanes named"},
            {"signal": "PERp/n[0:15]", "host_name": "PCIE_L*_TX_P/N", "ocp_ref": f"{OCP_SPEC} {OCP_TABLE}", "status": "All 16 lanes named"},
            {"signal": "SMBus_D", "host_name": "—", "ocp_ref": f"{OCP_SPEC} {OCP_TABLE}", "status": "On OAM bridge — to Management sheet"},
            {"signal": "SMBus_CLK", "host_name": "—", "ocp_ref": f"{OCP_SPEC} {OCP_TABLE}", "status": "On OAM bridge — to Management sheet"},
            {"signal": "SMB_ALERT#", "host_name": "—", "ocp_ref": f"{OCP_SPEC} {OCP_TABLE}", "status": "On OAM bridge — to Management sheet"},
            {"signal": "PRESNT#", "host_name": "—", "ocp_ref": f"{OCP_SPEC} {OCP_TABLE}", "status": "On OAM bridge — presence detect"},
        ],
        "missing_or_todo": [
            {"signal": "CLKREQ#", "host_name": "CLKREQ#", "ocp_ref": "Not in OCP Table 4", "status": "TODO — PCIe CEM sideband; OAM pin assignment unknown"},
            {"signal": "WAKE#", "host_name": "WAKE#", "ocp_ref": "Not in OCP Table 4", "status": "TODO — PCIe CEM sideband; OAM pin assignment unknown"},
            {"signal": "PRSNT2#", "host_name": "—", "ocp_ref": "PCIe CEM optional", "status": "TODO — not required for OAM mezzanine; verify host slot"},
            {"signal": "PWRBRK#", "host_name": "—", "ocp_ref": "PCIe CEM optional", "status": "TODO — power brake; verify if host slot exposes"},
        ],
        "amd_specific_todo": [
            {"signal": "GCD lane bifurcation", "status": "TODO — 2x GCD may use x16 or 2x x8 topology"},
            {"signal": "Lane polarity / reversal", "status": "TODO — PCIe Routing Guide missing"},
            {"signal": "Dual REFCLK", "status": "TODO — AUX_100M_REFCLK on OAM Conn0 optional; MI250X requirement unknown"},
        ],
    }


def render_pcie_symbol(lib_name: str, symbol_name: str, value: str, pins: list[PciePin], unit_count: int = 8) -> str:
    pins_per_unit = (len(pins) + unit_count - 1) // unit_count
    lines = [
        f'  (symbol "{lib_name}:{symbol_name}" (pin_names (offset 1.016)) (exclude_from_sim no) (in_bom yes) (on_board yes)',
        f'    (property "Reference" "J" (at 0 0 0)',
        f'      (effects (font (size 1.27 1.27)) (justify left)))',
        f'    (property "Value" "{value}" (at 0 -2.54 0)',
        f'      (effects (font (size 1.27 1.27)) (justify left)))',
        f'    (property "Footprint" "" (at 0 0 0)',
        f'      (effects (font (size 1.27 1.27)) hide))',
        f'    (property "PhysicalPinMap" "TODO — no CEM/OAM pin numbers assigned" (at 0 -5.08 0)',
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
            lines.append(f'      (pin {pin.electrical} line (at -7.62 {y} 0) (length 2.54)')
            lines.append(f'        (name "{pin.name}" (effects (font (size 1.016 1.016))))')
            lines.append(f'        (number "{start + idx + 1}" (effects (font (size 1.016 1.016))))')
            lines.append(f"      )")
        lines.append(f"    )")
    lines.append(f"  )")
    return "\n".join(lines)


def append_host_pcie_symbols(path: Path) -> None:
    """Append Host PCIe symbols to existing MI250X-Carrier.kicad_sym library."""
    path = Path(path)
    host_pins = host_slot_gen4_pins()
    oam_pins = ocp_oam_host_link_pins()
    fragments = [
        render_pcie_symbol("MI250X-Carrier", "Host_PCIe_Slot_x16_Gen4", "PCIe_x16_Gen4_Host", host_pins),
        render_pcie_symbol("MI250X-Carrier", "OAM_PCIe_HostLink", "OAM_HostLink_PET_PER", oam_pins),
    ]
    if not path.exists():
        body = "\n".join(
            [
                '(kicad_symbol_lib (version 20241209) (generator "host_pcie")',
                '  (generator_version "1.0")',
                *fragments,
                ")",
            ]
        )
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(body + "\n")
        return
    text = path.read_text().rstrip()
    if text.endswith(")"):
        text = text[:-1].rstrip()
    text += "\n" + "\n".join(fragments) + "\n)\n"
    path.write_text(text)


def oam_lane_hierarchical_labels(side: str = "output") -> list[tuple[str, str]]:
    """PET/PER lane net names for hierarchical labels (OAM-facing)."""
    labels: list[tuple[str, str]] = []
    for i in range(LANE_COUNT):
        labels.append((f"PETp{i}", side))
        labels.append((f"PETn{i}", side))
        labels.append((f"PERp{i}", side))
        labels.append((f"PERn{i}", side))
    return labels


def host_lane_hierarchical_labels(side: str = "input") -> list[tuple[str, str]]:
    labels: list[tuple[str, str]] = []
    for i in range(LANE_COUNT):
        labels.append((f"PCIE_L{i}_TX_P", side))
        labels.append((f"PCIE_L{i}_TX_N", side))
        labels.append((f"PCIE_L{i}_RX_P", side))
        labels.append((f"PCIE_L{i}_RX_N", side))
    return labels


def support_hierarchical_labels() -> list[tuple[str, str]]:
    return [
        ("PE_REFCLKp", "bidirectional"),
        ("PE_REFCLKn", "bidirectional"),
        ("PERST_N", "bidirectional"),
        ("SMBUS_DATA", "bidirectional"),
        ("SMBUS_CLK", "bidirectional"),
        ("SMBUS_ALERT_N", "bidirectional"),
        ("PRESNT_N", "output"),
        ("CLKREQ_N_TODO", "passive"),
        ("WAKE_N_TODO", "passive"),
    ]


def root_pcie_sheet_pins(pin_x: float, start_y: float = 25.4, spacing: float = 2.54) -> list[tuple[str, str, float, float]]:
    """Hierarchical sheet pins for PET/PER lanes + PCIe support (Host ↔ OAM)."""
    pins: list[tuple[str, str, float, float]] = []
    y = start_y
    for name, ptype in oam_lane_hierarchical_labels("bidirectional"):
        pins.append((name, "bidirectional", pin_x, y))
        y += spacing
    for name, ptype in support_hierarchical_labels():
        pins.append((name, ptype, pin_x, y))
        y += spacing * 2
    return pins


def write_support_signal_doc(path: Path) -> None:
    audit = support_signal_audit()
    lines = [
        "# Host PCIe Support Signal Audit",
        "",
        f"Host PCIe Gen4 x16 sheet — {OCP_SPEC} {OCP_TABLE}; {PCIE_SPEC}.",
        "No physical connector pin numbers assigned.",
        "",
        "## Present on sheet",
        "",
        "| Signal | Host (CEM) | OCP reference | Status |",
        "|--------|------------|---------------|--------|",
    ]
    for item in audit["present_on_sheet"]:
        lines.append(
            f"| {item['signal']} | {item['host_name']} | {item['ocp_ref']} | {item['status']} |"
        )
    lines.extend(["", "## Missing or TODO", ""])
    lines.append("| Signal | Host (CEM) | OCP reference | Status |")
    lines.append("|--------|------------|---------------|--------|")
    for item in audit["missing_or_todo"]:
        lines.append(
            f"| {item['signal']} | {item['host_name']} | {item['ocp_ref']} | {item['status']} |"
        )
    lines.extend(["", "## AMD-specific TODO", ""])
    for item in audit["amd_specific_todo"]:
        lines.append(f"- **{item['signal']}**: {item['status']}")
    lines.extend(["", "## Lane mapping (host ↔ OAM)", ""])
    lines.append("| Host (CEM Gen4) | OAM (OCP Table 4) | Direction |")
    lines.append("|-----------------|-------------------|-----------|")
    lines.append("| `PCIE_Ln_TX_P/N` | `PERp/n` | Host TX → module RX |")
    lines.append("| `PCIE_Ln_RX_P/N` | `PETp/n` | Module TX → host RX |")
    lines.extend(["", "### AMD lane assignment TODO", ""])
    for note in lane_mapping_todo_notes():
        lines.append(f"- {note}")
    path.write_text("\n".join(lines) + "\n")
