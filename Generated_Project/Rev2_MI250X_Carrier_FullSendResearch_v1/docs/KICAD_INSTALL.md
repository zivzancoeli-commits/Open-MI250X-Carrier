# KiCad install in this cloud environment

**Date:** 2026-08-17  
**Result:** **Succeeded.** `kicad-cli --version` → **9.0.9** (`/usr/bin/kicad-cli`, package `kicad 9.0.9~ubuntu24.04.1`).

The user locally has **KiCad 10.0.4**. This tree uses schematic version `20250114` and PCB version `20241229` (KiCad 9). KiCad 10 can open that. Do not assume a KiCad 10-only feature was used.

## What was tried

| Method | Result |
|---|---|
| `apt-get install kicad-cli` on stock Ubuntu 24.04 | **Failed.** No `kicad-cli` package name; universe has `kicad` 7.0.11 but was not the first success. |
| `snapd` | **Failed to configure.** `fuse3` left unconfigured; snapd depends on it. Did not block later apt. |
| Official PPA `ppa:kicad/kicad-9.0-releases` | **Worked.** Candidate `9.0.9~ubuntu24.04.1`. `apt-get install kicad` installed CLI + footprints/symbols/3d. apt still printed fuse3/snapd errors; kicad itself configured. |
| Flatpak / AppImage / conda / KiCad 10 official .deb | **Not needed** after 9.0.9 CLI was present. |

Confirm on a later image:

```bash
kicad-cli --version
kicad-cli sch erc --help
kicad-cli pcb drc --help
```

## What KiCad was used for (this tree)

- Regenerated s-expr schematic + PCB from `tools/generate_from_v10_pinmap.py` (v1.0 CSV nets only).
- `kicad-cli sch erc` on the hierarchical project.
- `kicad-cli pcb drc` on the 4-layer 2-OAM board.
- `kicad-cli pcb export svg` of silk / edge / drawings / In1 / In2.

Reports: `docs/kicad_reports/`. **ERC/DRC numbers are not a fab sign-off.** See `BLOCKERS_REMAINING.md`.
