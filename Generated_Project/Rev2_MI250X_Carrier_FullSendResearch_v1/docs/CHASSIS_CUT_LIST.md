# Chassis cut-list v1 — dual chamber (desk PC + compute)

**Date:** 2026-08-17  
**Intent:** mild-steel square tube frame + 16–18 ga CRS skins, user-welded. Front-to-rear airflow, **replaceable cooling**.  
**This is not a fab drawing.** Lengths below are envelopes. Add kerf, weld shrinkage, and your tube size (not selected).

Sources:

- `Generated_Project/Rev2_MI250X_Carrier_ChassisEnvelope_v1/docs/oam_mechanical_envelope_v1.md`
- `.../docs/host_envelope_v1.md`
- `.../docs/first_system_layout_v1.md`
- SuperMicro X11DPH-T product page (board 12" × 13")
- OCP OAM Design Spec v1.5 Figure 2 / §6.5.2

---

## Verified envelopes (use these)

| Item | Size | Source |
|---|---|---|
| OAM module PCB | **102 × 165 mm**, 4× R2 | OCP v1.5 §5 / Figure 2 |
| Baseboard KOZ per module | **103 × 166 mm** | OCP v1.5 §6.5.2 / Figure 14 |
| Connector stack / standoff | **5 mm ± 0.15 mm** | OCP v1.5 §5, §6.2, §6.4.1 |
| M3.5 clearance | **φ 3.9 mm**, 90 × 102 mm hole span, 31.5 mm from 165 mm end, 6.0 mm from 102 mm side | Figure 2 |
| Connector land box | **68 × 22 mm**, pitch **102 mm** | Figure 2 / §6.1 |
| Alignment pins | **φ 3 mm**, PEM TPS-3mm-8 or equivalent (spec) | §6.4.2 |
| Baseboard SMT nut | **φ 5.7 mm**, 3.6 mm nut ID | §6.5.1 |
| Four long screws | **M3.5** into bolster | §6.7.2 |
| Mate force | 0.50 N/pin MAX, **344 N** total MAX | §6.2 |
| OAM + HS mass | **2 kg MAX** | §6.2 |
| Host board | X11DPH-T **330.2 × 304.8 mm** (13" × 12" E-ATX) | SuperMicro |
| CPU cooler | NH-U14S DX-3647 **150 × 78 × 165 mm** with fan | Noctua DX-3647 tables |
| Cooler without fan | 150 × 52 × 165 mm | Same |

## Inferred (do not drill 8-GPU holes from this)

| Item | Size | Basis |
|---|---|---|
| 2-GPU KOZ cluster | **206 × 166 mm** | 2 × 103 mm along module width |
| 8-GPU floor reserve | **412 × 332 mm** | 4×2 tiling of 103 × 166. **Not** a UBB drawing. |
| Carrier PCB this stub | **246 × 206 mm** | Envelope 2-GPU board + 20 mm service margin (**planning**) |
| Alignment pin Y on 165 mm PCB | 5.5 mm from each end | Figure 14 6 mm from 166 mm KOZ minus 0.5 mm inset |
| Desk board | mATX class (ASUS PRIME B550M-A AC combo is mATX) | Exact mm **not measured**; typical mATX **244 × 244 mm** is **Inferred** |
| ATX PSU box | 150 × 86 × 140 mm | Standard ATX; **not** Dell 3 kW CRPS |

## Unknown (leave extra metal)

- OEM GPU heatsink **height** (100 mm cooling box is a hole to argue about)
- X11DPH-T CPU1/CPU2 centers — dual U14S may collide with DIMMs
- Rear 10GBase-T cage + I/O depth
- EPS/ATX cable volume
- CRPS goldfinger depth if you later use Dell 12 V shelves
- Desk GPU (RX 470) dual-slot length (~240 mm class, **not measured**)

---

## Dual-chamber layout (planning)

```
FRONT (intake)                                              REAR (exhaust)
+------------------------------+  +-------------------------------+
| COMPUTE                      |  | HOST (X11DPH-T)               |
| 2× OAM now  206 × 166 KOZ    |  | 330.2 × 304.8 board           |
| 8× reserve  412 × 332 (inf.) |  | 2× DX-3647 165 mm H (pitch ?) |
| cooling volume height UNKNOWN|  | I/O + cables unmeasured       |
+------------------------------+  +-------------------------------+
| DESK (B550M mATX + 5500)     |  | desk ATX PSU + optional RX470 |
+------------------------------+  +-------------------------------+
```

Airflow goal (BOM intent, not OAM qualification): front-to-rear, positive pressure, skins removable for a later liquid loop. **Do not weld a cold-plate boss onto the die.**

---

## Square-tube members (Inferred planning — pick a tube, then recut)

Tube size is **not selected**. Use these as **minimum clear inside** lengths, then add 2× wall + weld tabs.

Assume for quoting a **25 mm (1")** square tube (common; **not verified as the user’s stock**):

| ID | Qty | Cut length (Inferred) | Faces | Why |
|---|---|---|---|---|
| A | 4 | **≥ 500 mm** | compute bay width | 412 mm 8-GPU reserve + ~80 mm duct/structure |
| B | 4 | **≥ 450 mm** | compute bay depth | 332 mm 8-GPU + intake/exhaust plenum |
| C | 4 | **≥ 400 mm** | host bay width | 330.2 mm board + ~70 mm cable/IO |
| D | 4 | **≥ 380 mm** | host bay depth | 304.8 mm board + I/O unknown — **add more if 10G cage is deep** |
| E | 4 | **≥ 280 mm** | desk bay | mATX 244 mm + PSU/cables |
| F | 8 | **height TBD** | verticals | Must clear **165 mm** U14S + board + feet, **and** GPU cooling height **Unknown**. Do **not** freeze under 300 mm until HS is measured. |
| G | 4 | cross braces | as fitted | Keep 8-GPU floor as a **removable** tray, not a welded hole pattern. |

**Do not** drill the 8× M3.5 OAM pattern into the chassis. That pattern lives on the **carrier PCB** (φ3.9 mm NPTH). Chassis only needs tray rails / standoffs for a 246 × 206 mm (2-GPU) card now, with room to swap a larger tray later.

---

## CRS skins (16–18 ga) — Inferred panel sizes

| Panel | Qty | Approx blank | Notes |
|---|---|---|---|
| Compute front intake | 1 | ≥ A × F | Fan holes later; don’t punch GPU-specific ducts until HS height is known |
| Compute rear | 1 | ≥ A × F | Exhaust; leave liquid pass-through knockouts **blank** |
| Compute top/bottom | 2 | ≥ A × B | Removable. Bottom = tray rails, not a welded cold plate |
| Host rear I/O | 1 | ≥ C × F | Cut **after** measuring the X11DPH-T I/O shield; standard ATX I/O is **not** this board |
| Host / desk sides | 4 | as fitted | 16–18 ga CRS |
| Divider wall | 1 | full height × depth | Separates desk 12 V from compute 48 V. **Never** share P48V with desk/host 12 V. |

I/O shield for X11DPH-T is a server I/O plate (VGA + 2× 10GBase-T + USB). **Unknown** exact cut. Trace the board.

---

## Hardware to buy with the chassis (not OAM power)

| Item | Qty | Status |
|---|---|---|
| M3.5 socket-cap screws (OCP §6.7.2) | 8 now (2 OAMs × 4), 32 if you pre-buy 8-GPU | Length **Unknown** (bolster stack). Buy a mixed M3.5 × 8/10/12/16 mm assortment, stainless. |
| M3.5 nuts / PEM-style | match screws | Spec nut ID 3.6 mm on baseboard SMT nut |
| 5 mm standoffs / bolster | 8 now | Height **Verified** 5 mm ± 0.15 mm as the **connector stack**, not necessarily the screw length |
| φ 3 mm alignment pins | 4 now (2 per OAM) | OCP PEM TPS-3mm-8 or equivalent |
| EMI gasket 6 × 40 × 1 mm | 8 pads spec / 2-GPU | OCP §6.4.3 — buy only if you are building the KOZ pads |
| Chassis fans (12 V PWM) | 2–4 | Airflow for the **box**, not a qualified GPU HS. Size after bay height is known. |
| Rubber feet / casters | as wanted | 2 kg max per OAM+HS; 2-GPU + host is still a heavy weldment |

---

## Power isolation (chassis rule)

- Host 12 V (ATX/EPS, or Dell 12 V CRPS **if** you later have a breakout) stays in the **host** bay.
- Desk 12 V stays in the **desk** bay.
- Future **48 V** GPU feed stays in the **compute** bay with its own inlet.
- **Never** mix P48V with 12 V / 3.3 V. **Never** drive PVREF from the carrier or from a bench PSU “3.3 V rail.”

---

## Full-send addendum (2026-08-17)

OCP **UBB Design Spec v1.5** public text: 8-OAM board **417 mm × 585 mm × 3.2 mm**. Use that as the **later 8-OAM chassis volume**, not as this PCB. Do not drill from the Inferred 4×2 KOZ **412 × 332 mm**. r2.0 UBB (417 × 655 mm) is the wrong generation.

No public UBB gerber was found this run.
