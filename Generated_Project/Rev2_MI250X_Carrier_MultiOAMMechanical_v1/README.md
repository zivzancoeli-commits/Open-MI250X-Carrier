# MI250X 8-seat mechanical carrier (v1)

**Do not fabricate. Do not apply power. Pads are unmapped.**

KiCad 10 project created with the Cursor KiCad MCP. Outline is a 4×2 OAM keep-out floor (OCP v1.5 KOZ 103×166 mm, plus 20 mm margin → **452×372 mm**, 4 copper layers).

| What is on the board | Status |
|---|---|
| 8 seats of M3.5 clearance holes (stock `MountingHole_3.7mm`; OCP Figure 2 is **φ3.9 mm**) | Mechanical candidate |
| 2 seats of Molex **218910-1115** land patterns (688 pads, numbered, **no OCP signal names**) | Geometry candidate |
| Seats 3–8 connector pairs | Not placed (same pad map still BLOCKED) |
| P48V / PCIe / REFCLK / PERST / SMBus nets | **Not routed** — pinlist missing |

Production schematics were not modified. This is a copied tree.

## Pin map

The carrier cannot invent AMD/OCP assignments. See `docs/pin_mapping.md`.
