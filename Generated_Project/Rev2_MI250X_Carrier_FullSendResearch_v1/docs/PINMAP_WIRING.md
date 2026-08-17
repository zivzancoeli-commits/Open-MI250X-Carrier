# What the 2-OAM FullSend stub actually wires

Source: `22_Pinmap_Research/extracted/OAM_v1.0_OCP_Generic_Pin_Map.csv`  
Authority: `downloads/OAM_Pin_map_rev_1.0.xlsx` sheet **OCP Generic Pin Map**.

OCP **generic v1.0**, not an AMD overlay. P3V3 = **2 pads on Conn0** (C1, C2). r2.0 is UNUSABLE.

## Planes (this copy vs the buy-pack stub)

| Layer | Net | Why |
|---|---|---|
| In1.Cu | **P48V** | Named on v1.0 map (16 Conn0 pads). **Does not** authorize 48 V in the Molex 30 V sheet. |
| In2.Cu | **GND** | Named. |
| F.Cu / B.Cu | signal (no tracks) | Unmapped pads have empty net. |
| — | P12V1 / P12V2 / P3V3 | **Not** poured on In1. Never mix with P48V. |

Zones use ~0.64 mm clearance on P48V (OCP UBB v1.5 >40 V internal 25 mil). Molex pad pitch still produces DRC clearance hits — another reason this is not fab-ready.

## Wired (named nets)

Same classes as PR #2: shared `P48V` `P12V1` `P12V2` `P3V3` `GND`; per-OAM PVREF (do not drive); clock/reset including HOST_PWRGD / PWRBRK#; host PCIe names; mgmt stubs. SerDes S1–S7 named, **not routed**. TEST*/RFU/DO_NOT_USE **unmapped**.

P48V pads Conn0: H59, K59, H60, K60, H61, J61, K61, L61, H62, J62, K62, L62, H63, J63, H64, J64.

## 8-seat keepout

Dwgs.User dashed **417 × 585 mm** = OCP UBB v1.5 (Verified). Dashed **412 × 332 mm** = Inferred 4×2 KOZ (not a UBB). Electrical seats remain **two**.

## Connector

Hermaphroditic **2189101115** mates with itself, 5.00 mm. Buy **4×** for the carrier.

## Do not “Update PCB from Schematic”

Pad nets were written from the CSV. A schematic update would risk wiping unmapped-empty pads.
