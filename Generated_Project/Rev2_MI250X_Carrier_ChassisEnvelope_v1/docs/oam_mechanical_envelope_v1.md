# OAM mechanical envelope v1

**Date:** 2026-08-15  
**Tree:** `Generated_Project/Rev2_MI250X_Carrier_ChassisEnvelope_v1`  
**Mode:** extract + CAD envelopes. No production schematic/PCB edits. **Do not fabricate.**

## Sources

| Document | Local path | Use |
|---|---|---|
| OCP Accelerator Module Design Specification **v1.5** | `13_Reference_Docs/OCP_OAM/ocp accelerator module design specification_v1p5_Final_20220223.docx (1) (1).pdf` SHA-256 `830729ce3018a466105f4f032aa8d236aa7e179ed031ca08139f1df4910c1824` | Module / KOZ / stack / hardware |
| Rendered Figure 2, 3/4, 8/9, 14 | `docs/figures/` | Hole and connector coordinates that are drawing-only in the PDF |
| Molex 2189101115-SD | Pin-map audit vendor download | 688-pad land pattern (signals still BLOCKED) |

`15_Reverse_Engineering/06_Mechanical.md` still lists these as Unknown because it was written before this extraction. This file is the current mechanical source.

## Verified (OCP v1.5 text + Figure 2 / 14)

Datum for one module: **Figure 2 bottom view**, origin at lower-left of the 102×165 mm PCB, +X to the PIN A3 side, +Y toward Connector 1 (top of the drawing).

| Item | Value | Source |
|---|---|---|
| Module PCB | **102 × 165 mm** | §5, §6.1, Figure 2 |
| Corner radius | **4× R2** | Figure 2 |
| Board thickness | **1.57–3.20 mm ± 10%** | §5 |
| Connector-to-connector pitch | **102 mm** | §6.1 |
| Connectors | 2× Molex Mirror Mezz Pro **218910-1115** | §5, §6.2 |
| Stack / standoff height | **5 mm ± 0.15 mm** | §5, §6.2, §6.4.1 |
| Bottom stiffener height (incl. Mylar) | **5 ± 0.15 mm** | §5 |
| Connector land box | **68 × 22 mm** each | Figure 2 |
| Connector 1 top from module top | **20.5 mm** | Figure 2 |
| Gap between connector inner edges | **80 mm** | Figure 2 |
| Connector 0 / 1 centers (this datum) | **(51.0, 31.5)** and **(51.0, 133.5) mm** | Arithmetic from Figure 2; pitch 102 mm matches §6.1 |
| Four NPTH | **φ 3.9 mm** (153 mil), **φ 8 mm MIN** land | Figure 2 |
| Hole span | **90 × 102 mm** | Figure 2 |
| Hole center from 165 mm end | **31.5 mm** | Figure 2 |
| Hole center from 102 mm side | **6.0 mm** | (102−90)/2; consistent with Figure 14 6.5 mm from 103 mm KOZ |
| Notch (Detail A) | **12 × 4 mm**, starts **10.75 mm** from top, **4× R1** | Figure 2 |
| PIN A3 | Marked on **+X / right** of both connectors in Figure 2 bottom view | Figure 2 |
| Baseboard component KOZ | **103 × 166 mm** | §6.5.2, Figure 14 |
| Stage-1 bumper | **0.5 mm** each side (plastic top 103 mm) | §6.6 |
| Alignment pins | **φ 3 mm**, **10 mm** from PCB bottom | §6.4.2 PEM TPS-3mm-8 or equivalent |
| Baseboard SMT nut holes | **φ 5.7 mm**, **3.6 mm** nut ID | §6.5.1, Figure 14 |
| Alignment holes vs 166 mm KOZ | **6 mm** from each KOZ end (**154 mm** CTC) | Figure 14 |
| EMI gasket pads | **8 × 42 mm** (gasket 6×40×1 mm) | §6.4.3 / §6.5.3 |
| Corner squares | **10 × 10 mm** | Figure 14 / §6.5 |
| Four long screws | **M3.5** into bolster, diagonal torque | §6.7.2 |
| Mate force | **0.50 N/pin MAX**, **344 N** total MAX | §6.2 |
| OAM + heatsink mass | **2 kg MAX** | §6.2 |
| Air recommendation | TDP **≤ 450 W** for the reference 8× shadowed layout | §6.7 / §7.5.3 |
| 1 RU liquid die stack | Bottom-stiffener lower surface to die top **≤ 13 mm** | §7.5.3 |
| High-power input | **44–59.5 V**, up to **700 W** class | §5 (MI250X is 500/560 W — see thermal audit) |

CSV: `docs/csv/oam_v15_figure2_coordinates.csv`

## Inferred

| Item | Basis | Do not treat as |
|---|---|---|
| 8-GPU floor **412 × 332 mm** | 4×2 tiling of the **103 × 166 mm** KOZ, plus §6.6 0.5 mm bumpers | A Universal Baseboard drawing. No UBB DXF was extracted. |
| Alignment pin Y on the **165 mm** PCB = **5.5 mm** from each end | Figure 14 6 mm from 166 mm KOZ minus 0.5 mm inset | Independent Figure 2 callout (Figure 2 does not dimension the pins) |
| Candidate footprint rotation **180°** | Figure 2 PIN A3 on +X; quarantine footprint has A3 at **x = −29.45 mm** | Proven module↔baseboard silk orientation until overlay-checked on a plot |

## Unknown / blocked

| Item | Why it is still blocked |
|---|---|
| OCP §8.3 pinlist spreadsheet | PDF says “separated spreadsheet”; file not in repo |
| AMD MI250X package / TIM / cold-plate ICD | Not in public datasheet used here |
| OEM air-heatsink **height** | Photos exist under `07_Photos/04_Cooling/`; not measured, not used as dimensions |
| OAM contribution **DXF / 3D** package | Spec points to a contribution package that is not local |
| Figure 9 stiffener hole-span vs Figure 2 | Figure 2 is **required**. Do not override the 90×102 mm M3.5 pattern with a conflicting read of Figure 9 |

## PCB implication

The 688-pad Molex candidate footprint is **geometry-proven** and is placed on the 2-GPU mechanical board at the Figure 2 centers. **No OCP nets are assigned.** Production `218910-1115.kicad_mod` (165 blank pads) was not modified.
