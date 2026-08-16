# Host envelope v1

First compute host is the **Supermicro X11DPH-T** + two **Noctua NH-U14S DX-3647** towers. This file only records published envelopes. Socket coordinates, DIMM keep-outs, and I/O bracket depth were not taken from a board scan.

## Verified (vendor publications)

| Item | Value | Source |
|---|---|---|
| Board | Supermicro **X11DPH-T** (MBD-X11DPH-T) | Project host selection; SuperMicro product page |
| Form factor | E-ATX | SuperMicro product page |
| Board size | **12" × 13" = 304.8 × 330.2 mm** | SuperMicro product page; X11DPH-i/T/Tq user manual “13" (W) × 12" (L) (330.2 mm × 304.8 mm)” |
| DIMM slots | 16 | SuperMicro / project BOM |
| PCIe | 3× Gen3 x16, 4× Gen3 x8 | SuperMicro. MI250X is Gen4 and will downtrain. |
| CPU cooler | Noctua **NH-U14S DX-3647** (LGA3647, not LGA4189) | User cooler correction |
| Cooler envelope with fan | **150 × 78 × 165 mm** (W × D × H) | Noctua DX-3647 tables (NF-A15 installed) |
| Cooler envelope without fan | **150 × 52 × 165 mm** | Same |

Manual TDP note: X11DPH-T lists CPU TDP support **up to 165 W** in the user-manual extract. Gold 6230 is inside that class; do not assume 205 W SKUs without checking the same manual’s heatsink/chassis notes.

## Inferred / planning

| Item | Value | Tag |
|---|---|---|
| Board thickness in STL | 2.4 mm | **Planning** — not measured |
| Two-tower placement | 20 mm and 180 mm from board origin in the SCAD/SVG | **Placeholder** — CPU pitch **Unknown** |
| ATX PSU box | 150 × 86 × 140 mm | Standard ATX PSU; **not** the Dell 3 kW CRPS, **not** selected |
| 16× DIMM keep-out height | Unknown | Do not invent Optane PMem height |

## Unknown

- Exact CPU1/CPU2 center coordinates on X11DPH-T
- Whether both DX-3647 towers fit without DIMM or VRM clash (narrow vs square LGA3647 ILM)
- Rear I/O + 10GBase-T cage depth
- EPS/ATX cable volume
- Second “normal-use PC” motherboard size (not selected)

## Chassis implication

Host bay must clear **330.2 × 304.8 mm** of board plus **165 mm** tower height plus an unmeasured I/O/cable allowance. Do not freeze sheet-metal around the placeholder cooler positions.
