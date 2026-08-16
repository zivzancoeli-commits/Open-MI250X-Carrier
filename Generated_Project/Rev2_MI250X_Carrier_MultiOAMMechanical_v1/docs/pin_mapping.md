# How to get a real MI250X OAM pin map

MI250X uses **OAM v1.x (688 contacts)**. Do not use `OAI-OAM_Pinlist_Pinmap_r2.0` (different rail counts, e.g. P3V3).

## Documents that actually assign pins

1. **OCP OAM Design Specification v1.5** — PDF Table 4 is pin *counts* only. The named pinlist is a **separated spreadsheet** (§8.3). Request the v1.5 package (or v1.0/v1.1 zip with `OAM_Pin_list_Rev1.0`) from the OCP OAI workgroup / Groups.io. Wiki: https://www.opencompute.org/wiki/Server/OAI
2. **AMD Instinct MI250X OAM hardware integration / baseboard guide** — typically NDA.
3. **A donor Universal Baseboard (UBB) or OEM tray** (HPE/Cray/OCP) — continuity from a known-good board is more useful than GPUs alone.

Public GitHub `opencomputeproject/OCP-SVR-OAI-Open_Accelerator_Infrastructure` is a project page, not the v1.5 xlsx.

## Buying MI250X modules does not let you invent a custom pin map

The module already has a **fixed** AMD/OCP map. The carrier must match it. You cannot reassign PCIe lanes, REFCLK, PERST, or 48 V onto other pads and expect the GPU to work.

Unpowered continuity on a purchased module can **cluster** large shorted groups (likely GND or P48V) and you can compare *counts* to v1.5 Table 4. That does **not** give lane order, clocks, reset, or SMBus. Do not apply 48 V to guessed pins.

Buying OAMs helps mechanical fit and maybe power-net clustering. It does **not** replace the spreadsheet for a first safe electrical carrier. A donor UBB is the better purchase if the goal is reverse-mapping.
