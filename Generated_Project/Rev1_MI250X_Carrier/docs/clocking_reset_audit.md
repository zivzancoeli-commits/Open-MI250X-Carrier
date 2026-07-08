# Clocking & Reset — Signal Audit

OCP reference: OCP Accelerator Module Design Specification v1.5 Table 4 OAM Pinouts.
PE_REFCLK uses OCP naming: **PE_REFCLKp** / **PE_REFCLKn** (100 MHz PCIe reference).

## Standard PCIe clock tree (suggested Rev1)

MODE A (carrier-generated) — default Rev1 suggestion:
  MGMT_3V3 → Y1 (100 MHz HCSL) → PE_REFCLKp/n → U1 clock buffer
    ├─ CLK0 → R_TERM → OAM Conn0 PE_REFCLKp/n (OCP naming)
    └─ CLK1 → host slot REFCLKp/n (if carrier sources host clock)
MODE B (host-sourced) — alternate if baseboard provides REFCLK:
  Host REFCLKp/n → J_HOST_CLK IN → U1 buffer → OAM PE_REFCLKp/n
  Y1 DNP or not populated
COMMON:
  - 100 MHz ±300 ppm per PCIe; OCP cites PCIe Gen5-compliant PE_REFCLK
  - Point-to-point differential; 85Ω or 100Ω per REFCLK Guide (TODO)
  - PERST# asserted during power-up; release after PE_REFCLK stable + PG (AMD TODO)
  - CLKREQ# couples to clock power-management — Host PCIe sheet (not Clocking)

## Reset signals — present on sheet

| Signal | OCP name | Net | Connector | Status |
|--------|----------|-----|-----------|--------|
| PERST# | PERST# | PERST_N | Conn0 | Distributed via U2 — OCP CEM-compliant PCIe reset |

## Reset signals — OCP TODO (not routed)

- **WARMRST#** (`WARMRST_N_TODO`) — TODO — optional OCP warm reset; AMD requirement unknown (Conn0)
- **PERST# (Conn1)** (`PERST_CONN1_N_TODO`) — TODO — verify if used on MI250X (Conn1)

## JTAG (not PCIe reset)

- **JTAG0_TRST** — JTAG test reset — Management/debug sheet, not Clocking

## Sequencing-related (not pure reset)

- **OAM_PG** (`OAM_PG_TODO`) — Power Good gates PERST# release — AMD timing TODO
- **OAM_EN** (`OAM_EN_TODO`) — Module enable — not a reset; sequencing on Power sheet

## Not reset — PCIe sidebands

- **CLKREQ#** — Clock request — Host PCIe sheet TODO, not reset
- **WAKE#** — Wake — Host PCIe sheet TODO, not reset
- **PRESNT#** — Presence detect — not reset

## Unknown / TODO clocks

| Clock | OCP / source | Status |
|-------|--------------|--------|
| AUX_100M_REFCLKp/n | OCP Accelerator Module Design Specification v1.5 Table 4 OAM Pinouts | TODO — optional OCP auxiliary 100 MHz; U3 block NC |
| AMD GCD-specific REFCLK | Not in OCP base table | TODO — do not invent; dual-GCD clocking unknown |
| Spread-spectrum REFCLK | REFCLK Guide missing | TODO — SSC requirement for MI250X unknown |
| SerDes reference clocks (SERDES 1–7) | OCP Accelerator Module Design Specification v1.5 Table 4 OAM Pinouts | TODO — inter-module links; N/A single-module Rev1 |
| Host vs carrier REFCLK ownership | REFCLK Guide missing | TODO — Mode A (carrier Y1) vs Mode B (host passthrough) |

## Placeholders replaced

- REMOVED: OAM_MirrorMezz_Conn0_TODO (wrong sheet)
- REMOVED: MCU / FRU / TEMP (wrong sheet)
- REMOVED: Generic Y1 text note without components
- ADDED: Y1 100 MHz oscillator — OCP PE_REFCLKp/n output naming
- ADDED: U1 PCIe clock buffer — standard fanout tree
- ADDED: R1 PE_REFCLK termination network — values TODO
- ADDED: J1 host REFCLK input — alternate Mode B topology
- ADDED: U2 PERST# distribution block
- ADDED: U3 AUX_100M_REFCLK TODO — OCP optional, NC
- ADDED: U4 WARMRST# TODO — OCP optional, NC
- ADDED: U5 PERST# Conn1 TODO — NC
- ADDED: U6 reset sequencing gate AMD TODO — NC
