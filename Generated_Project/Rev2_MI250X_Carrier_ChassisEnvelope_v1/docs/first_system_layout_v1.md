# First-system layout v1

Target: **one custom chassis**, two computers, first compute config **2× MI250X OAM**. Later: same floor reserved for **8×**.

Airflow intent from `20_System_BOM/Cooling.md`: front-to-rear, positive pressure, replaceable cooling. That is a **goal**, not an OAM qualification.

## Bays

```
FRONT  (intake)                                         REAR
+---------------------------+  +---------------------+
| 2× OAM (first)            |  | X11DPH-T            |
| 206 × 166 mm KOZ          |  | 330.2 × 304.8 mm    |
|                           |  | 2× DX-3647 165 mm H |
| 8× reserve drawn around it|  | PSU / I/O unknown   |
| 412 × 332 mm (INFERRED)   |  |                     |
+---------------------------+  +---------------------+
        compute                          host
```

A second desk-PC bay is **Unknown** until that motherboard is chosen. Leave volume; do not draw a fake ATX layout as verified.

## 2-GPU now

- Two **103 × 166 mm** keep-outs side by side (verified KOZ tiled along the 102 mm module width).
- Each seat: Figure 2 holes + two 218910-1115 land patterns.
- Carrier board in `kicad_mechanical/` adds a **20 mm** service margin (**planning**).
- Cooling **above** the module: **Unknown**. STL `cooling_planning_volume_UNKNOWN_height.stl` is 100 mm so the chassis has a hole to argue about — not an OEM brick.

OCP §7.5.3 observed ~**450 W** air limit on a shadowed 8× tray. MI250X is **500 W / 560 W peak**. User BOM still says air first. Chassis must keep liquid plumbing **replaceable** later. Do not clamp a custom cold plate onto a bare die (thermal audit).

## 8-GPU later

**412 × 332 mm** = 4 columns × 2 rows of the 103×166 mm KOZ. That is **inferred from tiling**, not from an OCP Universal Baseboard drawing. Do not drill an 8-GPU hole pattern from this number.

## Power / do-not-buy (unchanged)

- Host can POST on a normal EPS/ATX PSU.
- Dell D3000E-S1 3 kW units are **12 V CRPS**, not 48 V GPU power.
- Final PSU waits on chassis (`20_System_BOM/Power.md`).
- Do not buy or energize MI250X until a verified P48V path **and** a real cooler exist.

## What to do next (mechanical)

1. Open `cad/svg/first_system_top.svg` and the OpenSCAD file; iterate bay walls.
2. Measure an OEM air HS from `07_Photos/04_Cooling/` **with a scale** if you own that cooler — then replace the 100 mm planning height.
3. Get X11DPH-T CPU coordinates from SuperMicro’s board file / a caliper on the board.
4. Keep carrier electrical blocked until the OCP v1.5 pinlist spreadsheet is in hand.
