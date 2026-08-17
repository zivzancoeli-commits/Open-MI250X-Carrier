# KiCad 9.0.9 CLI reports (not a fab sign-off)

- `erc.json` / `erc_cli.txt` — hierarchical ERC. This run: **378** violations (`label_dangling`, `hier_label_mismatch`, `multiple_net_names`). Expected for a named-net stub.
- `drc.json` / `drc_cli.txt` — PCB DRC. This run: **12** violations (8× P48V clearance vs 0.64 mm rule on 0.4 mm pad pitch; 4× lib_footprint_mismatch) and **499** unconnected items (no tracks).
- SVG plots of silk, edge, drawings, In1 (P48V zone outline), In2 (GND zone outline).

**DO NOT FABRICATE.**
