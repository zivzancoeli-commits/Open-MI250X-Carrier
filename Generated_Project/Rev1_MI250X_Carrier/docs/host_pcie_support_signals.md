# Host PCIe Support Signal Audit

Host PCIe Gen4 x16 sheet — OCP Accelerator Module Design Specification v1.5 Table 4 OAM Pinouts; PCI Express Card Electromechanical Specification (CEM) Gen4.
No physical connector pin numbers assigned.

## Present on sheet

| Signal | Host (CEM) | OCP reference | Status |
|--------|------------|---------------|--------|
| PE_REFCLKp/n | REFCLK_P/N | OCP Accelerator Module Design Specification v1.5 Table 4 OAM Pinouts | Named — routed via Clocking_Reset sheet |
| PERST# | PERST# | OCP Accelerator Module Design Specification v1.5 Table 4 OAM Pinouts | Named — host and OAM bridge |
| PETp/n[0:15] | PCIE_L*_RX_P/N | OCP Accelerator Module Design Specification v1.5 Table 4 OAM Pinouts | All 16 lanes named |
| PERp/n[0:15] | PCIE_L*_TX_P/N | OCP Accelerator Module Design Specification v1.5 Table 4 OAM Pinouts | All 16 lanes named |
| SMBus_D | — | OCP Accelerator Module Design Specification v1.5 Table 4 OAM Pinouts | On OAM bridge — to Management sheet |
| SMBus_CLK | — | OCP Accelerator Module Design Specification v1.5 Table 4 OAM Pinouts | On OAM bridge — to Management sheet |
| SMB_ALERT# | — | OCP Accelerator Module Design Specification v1.5 Table 4 OAM Pinouts | On OAM bridge — to Management sheet |
| PRESNT# | — | OCP Accelerator Module Design Specification v1.5 Table 4 OAM Pinouts | On OAM bridge — presence detect |

## Missing or TODO

| Signal | Host (CEM) | OCP reference | Status |
|--------|------------|---------------|--------|
| CLKREQ# | CLKREQ# | Not in OCP Table 4 | TODO — PCIe CEM sideband; OAM pin assignment unknown |
| WAKE# | WAKE# | Not in OCP Table 4 | TODO — PCIe CEM sideband; OAM pin assignment unknown |
| PRSNT2# | — | PCIe CEM optional | TODO — not required for OAM mezzanine; verify host slot |
| PWRBRK# | — | PCIe CEM optional | TODO — power brake; verify if host slot exposes |

## AMD-specific TODO

- **GCD lane bifurcation**: TODO — 2x GCD may use x16 or 2x x8 topology
- **Lane polarity / reversal**: TODO — PCIe Routing Guide missing
- **Dual REFCLK**: TODO — AUX_100M_REFCLK on OAM Conn0 optional; MI250X requirement unknown

## Lane mapping (host ↔ OAM)

| Host (CEM Gen4) | OAM (OCP Table 4) | Direction |
|-----------------|-------------------|-----------|
| `PCIE_Ln_TX_P/N` | `PERp/n` | Host TX → module RX |
| `PCIE_Ln_RX_P/N` | `PETp/n` | Module TX → host RX |

### AMD lane assignment TODO

- AMD MI250X dual-GCD lane map: which PET/PER lanes map to GCD0 vs GCD1 — TODO
- Host slot lane order vs OAM PET/PER index — TODO (no lane reversal assumed)
- Bifurcation: 1x x16 vs 2x x8 — TODO verify with MI250X integration guide
- AC coupling: OCP requires caps on carrier for PET path (module TX); values/placement TODO
