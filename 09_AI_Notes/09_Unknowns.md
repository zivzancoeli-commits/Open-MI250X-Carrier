# Unknowns

## Purpose
- Consolidate missing, unverifiable, or undocumented information that must be resolved before schematic capture, PCB layout, prototype bring-up, or validation.

## Verified
- Undocumented behavior should be tracked as open questions rather than assumptions. Source: `README.md`.
- Missing wanted documents include Mechanical Specification, Baseboard Specification, Connector Specification, ROCm Documentation, Server Integration Guides, PCIe Routing Guide, REFCLK Guide, PMBus Controller Datasheet, VRM Datasheet, OAM Thermal Guidelines, heatsink photos, and baseboard photos. Source: `Wanted_Documents.rtf`.
- MP2975 is believed present on MI250X but not visually confirmed. Source: `13_Reference_Docs/Component_Index.rtf`.
- MP2975 public datasheet is not available in the repository. Source: `13_Reference_Docs/Component_Index.rtf`.
- `Understanding_Data_Movement.pdf`, `MI200_Memory_Space.pdf`, and `SamsungFlashbolt.pdf` report invalid PDF structure when read locally. Source: repository PDF read attempts.

## Inferred
- OAM connector pinout, power pins, mechanical stack-up, and baseboard integration are likely blockers for schematic capture because the corresponding specifications are listed as missing. Source: `Wanted_Documents.rtf`.
- PCIe lane mapping, REFCLK routing, reset/sideband signals, and routing constraints are likely blockers because PCIe Routing Guide and REFCLK Guide are missing. Source: `Wanted_Documents.rtf`.
- Power sequencing, rails, telemetry, PMBus registers, and VRM placement are likely blockers because PMBus and VRM datasheets are missing. Source: `Wanted_Documents.rtf`.

## Unknown
- Needs Verification: whether found photos listed in `Wanted_Documents.rtf` exist outside this repository.
- Needs Verification: whether indexed references in `13_Reference_Docs/Reference_Index.rtf` have been downloaded or reviewed elsewhere.
- Needs Verification: whether MI250X carrier bring-up requires firmware tooling, management interfaces, or validation flows not yet captured.

## Source Documents
- `README.md`
- `Wanted_Documents.rtf`
- `13_Reference_Docs/Component_Index.rtf`
- `13_Reference_Docs/Reference_Index.rtf`
- `08_Research_Papers/01_Architecture/Understanding_Data_Movement.pdf` (Needs Verification: invalid PDF structure)
- `13_Reference_Docs/ROCm/MI200_Memory_Space.pdf` (Needs Verification: invalid PDF structure)
- `13_Reference_Docs/Memory_HBM/SamsungFlashbolt.pdf` (Needs Verification: invalid PDF structure)

## Design Implications
- Do not promote unknowns into schematic labels, footprints, constraints, or BOM entries.
- Resolve connector, power, clock, PCIe, mechanical, cooling, and management unknowns before PCB layout.
- Replace or repair unreadable PDFs before using them as evidence.

## Open Questions
- Where are the found photos referenced by `Wanted_Documents.rtf`?
- Which missing specifications are required before schematic capture?
- Can the indexed but absent references be recovered or linked?
