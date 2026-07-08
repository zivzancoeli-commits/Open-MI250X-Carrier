# Clock Architecture

## Purpose
- Track clocking evidence and missing REFCLK requirements before schematic capture.

## Verified
- REFCLK Guide is listed as missing under PCIe. Source: `Wanted_Documents.rtf`.
- `Clocking.md` exists, but contains no visible plain Markdown engineering content. Source: `09_AI_Notes/Clocking.md`.

## Inferred
- REFCLK is a schematic-capture research topic because it is explicitly listed as missing. Source: `Wanted_Documents.rtf`.
- Clocking is intended as a design-note category because `Clocking.md` already exists in `09_AI_Notes`.

## Unknown
- Needs Verification: reference clock frequency, topology, source, fanout, jitter budget, AC coupling, termination, and enable/reset relationships are not documented locally.
- Needs Verification: local readable files do not confirm whether the carrier requires only PCIe REFCLK or additional management, fabric, or board-level clocks.
- Needs Verification: no clock tree, schematic fragment, or timing requirement is present.

## Source Documents
- `Wanted_Documents.rtf`
- `09_AI_Notes/Clocking.md`

## Design Implications
- Do not select clock generators, buffers, or routing constraints until REFCLK requirements are sourced.
- Tie clock requirements to `03_PCIe_Interface.md` once PCIe and connector references are verified.
- Mark all clocking assumptions as Needs Verification until sourced.

## Open Questions
- What REFCLK frequency and topology are required?
- Are additional clocks needed beyond PCIe REFCLK?
- What jitter and routing constraints apply?
