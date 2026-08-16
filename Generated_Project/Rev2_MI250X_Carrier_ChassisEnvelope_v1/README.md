# Chassis Envelope v1

**Working copy only.** Production KiCad under `Rev2_MI250X_Carrier_ClockResetSchematicRepair_v2` was not modified.

This tree is the first mechanical CAD that uses **extracted OCP v1.5 Figure 2 / Figure 14 numbers** plus vendor host/cooler envelopes. It is what you open to start the two-computer box. It is **not** a fab package and it does **not** make an MI250X electrically live.

## Open these first

| File | What it is |
|---|---|
| `cad/svg/oam_module_figure2.svg` | One OAM: 102×165 PCB, holes, connectors, notch |
| `cad/svg/first_system_top.svg` | 2× MI250X now, 8× reserve, X11DPH-T host |
| `cad/first_system_envelope.scad` | Same envelopes in OpenSCAD |
| `cad/stl/` | Box STLs for any CAD tool |
| `kicad_mechanical/MI250X_2GPU_MechanicalEnvelope.kicad_pcb` | 2-GPU outline + M3.5 holes + Molex land pattern |

## Hard stops (unchanged)

- **Do not fabricate** the mechanical KiCad board.
- **Do not energize** an MI250X on it.
- OCP v1.5 **signal-to-contact map is still missing** (the unnamed §8.3 spreadsheet).
- Air-heatsink **height is unknown**. The 100 mm cooling box is a planning keep-out, not a measured OEM brick.
- Dual-CPU **socket pitch on X11DPH-T is unknown**; the two Noctua towers are placeholders.

## What this unblocks

Chassis sheet-metal / 3D printing of **bays and keep-outs**: host E-ATX, two OAM seats, later 8-OAM floor area, front-to-rear airflow. Carrier **electrical** work still waits on the pinlist.

Regenerate CAD:

```bash
python3 cad/generate_envelopes.py
```
