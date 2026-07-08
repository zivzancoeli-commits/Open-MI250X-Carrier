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
