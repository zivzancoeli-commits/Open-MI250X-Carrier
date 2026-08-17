# What the 2-OAM stub actually wires

Source: `22_Pinmap_Research/extracted/OAM_v1.0_OCP_Generic_Pin_Map.csv`  
Authority if mismatch: `downloads/OAM_Pin_map_rev_1.0.xlsx` sheet **OCP Generic Pin Map**.

This is OCP **generic v1.0**, not an AMD MI250X overlay. P3V3 = **2 pads on Conn0** (C1, C2) — matches v1.5 Table 4; r2.0 (P3V3=6) is UNUSABLE.

## Wired on the stub (named nets)

| Class | Nets | What the carrier does in this tree |
|---|---|---|
| Shared power | `P48V`, `P12V1`, `P12V2`, `P3V3`, `GND` | Same net on both OAMs. **No VRM. No 12→48 converter. No P48V plane pour.** |
| Per-OAM module output | `OAMn_PVREF`, `OAMn_MODULE_PWRGD`, … | Named, **not driven**. Do not short OAM0 PVREF to OAM1. |
| Clock / reset | `OAMn_PE_REFCLKP/N`, `PERST#`, `HOST_PWRGD`, `WARMRST#`, `PWRBRK#`, `PRSNTn#` | Hierarchical labels only. **No clock generator IC.** |
| Host PCIe names | `OAMn_PCIE_TXnP/N`, `OAMn_PCIE_RXnP/N` (n=0..15) | Hierarchical labels only. **No CEM pin mapping.** |
| Mgmt stub | `OAMn_SMBus_SLV_*`, `I2C_*`, `UART_*` | Named. **No BMC, no invented addresses.** |

### P48V pads (Conn0 only) — Verified from xlsx

H59, K59, H60, K60, H61, J61, K61, L61, H62, J62, K62, L62, H63, J63, H64, J64 (16).

### P3V3 — Verified

Conn0 C1, C2.

### PE_REFCLK — Verified

Conn0 F45 `PE_REFCLKP`, F46 `PE_REFCLKN`.

### PERST# — Verified

Conn0 D1.

## Named but not routed

SerDes `S1_*` … `S7_*` (and management-link / QSFP-DD sidebands). Pad nets exist so the footprint is not blank; **no tracks, no inter-OAM mesh.** AMD overlay required to know which links are xGMI.

## Unmapped (no net, no copper)

`TEST0`–`TEST14`, `TEST_MODE#`, `RFU`, `DO_NOT_USE`.

See `netlist/v10_pad_classification.csv` and sheet `05_unmapped_amd`.

## PCB

- Outline 246 × 206 mm copied from the chassis-envelope 2-GPU mechanical board (20 mm service margin, **planning**).
- Two 103 × 166 mm KOZ seats, Figure 2 M3.5 φ3.9 mm holes, Molex land patterns.
- **4 copper layers.** Inners reserved. **No signal tracks. No P48V pour.**
- Unmapped pads are present geometrically and have **empty net**.

## Connector gender (Verified, not guessed)

Farnell datasheet for **2189101115**: Mirror Mezz Pro **hermaphroditic**, mated height **5.00 mm**, **Mates With 2189101115**.

Carrier buy: **4×** 218910-1115 (2 OAMs × 2 connectors). Modules already carry the mating half. Do not buy 218916 unless a non-5 mm stack is documented. Tape-and-reel pack quantity is 150 at the factory — buy cut-tape/each if a distributor will sell singles.

## Do not “Update PCB from Schematic”

Pad nets were written from the CSV onto the footprint instances. A schematic-to-PCB update would risk wiping unmapped-empty pads or inventing connections.
