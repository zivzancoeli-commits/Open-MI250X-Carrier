# Full-send research v1 — 2× MI250X OAM (NOT fab-ready)

**Copied tree.** Production KiCad under other `Rev2_*` folders was not modified.

**DO NOT FABRICATE. DO NOT ENERGIZE an MI250X on this board.**

A full-send **shopping cart** (host + desk + 2× OAM + Molex + a 48 V brick) is a **buying** decision. It is **not** a PCBWay decision and **not** permission to apply P48V.

This folder advances the v1.0-mapped 2-OAM stub:

- Inner copper: **In1.Cu = P48V**, **In2.Cu = GND** because those names exist on the OCP generic v1.0 map. **P12V1 / P12V2 / P3V3 are not on the 48 V plane.**
- Silk: `DO NOT FABRICATE - DO NOT ENERGIZE OAMs`.
- 8-OAM **keepout** is chassis volume (OCP UBB v1.5 **417 × 585 mm**), not eight electrical seats.
- Unmapped `TEST*` / `RFU` / `DO_NOT_USE` pads still have **no net**.

KiCad **9.0.9** CLI ran ERC and DRC here. The user’s Mac KiCad **10.0.4** can open these files. The board is **not** PCBWay-ready.

## Open these first

| File | What it is |
|---|---|
| [`docs/FULL_SEND_SHOPPING.md`](docs/FULL_SEND_SHOPPING.md) | One cart: A will POST / B sits unused / C do not buy |
| [`docs/BLOCKERS_REMAINING.md`](docs/BLOCKERS_REMAINING.md) | Why PCBWay + plug-in is still forbidden |
| [`docs/RESEARCH_REPORT.md`](docs/RESEARCH_REPORT.md) | Seven research questions, quotes, Verified/Inferred/Unknown |
| [`docs/KICAD_INSTALL.md`](docs/KICAD_INSTALL.md) | How `kicad-cli` got onto this image |
| [`docs/URL_FETCH_LOG.txt`](docs/URL_FETCH_LOG.txt) | HTTP codes for URLs actually retrieved |
| `MI250X_2OAM_v10_Stub.kicad_pro` | KiCad 9 project (4-layer, 2 seats) |

## Regenerate (do not hand-edit pad nets)

```bash
python3 Generated_Project/Rev2_MI250X_Carrier_FullSendResearch_v1/tools/generate_from_v10_pinmap.py
```

If the CSV and the xlsx disagree, **the xlsx wins** (`22_Pinmap_Research/downloads/OAM_Pin_map_rev_1.0.xlsx`).

PR #1 pin map and PR #2 buy-pack are already on `main` (PR #2 merged; PR #1 files are in `22_Pinmap_Research/`). This branch copies forward; it does not overwrite those trees in place.
