# Design Checklist

## Purpose
- Provide a source-backed checklist for schematic capture, PCB layout, prototype bring-up, and validation.

## Verified
- OAM Specification is marked found. Source: `Wanted_Documents.rtf`.
- OAM specification link is useful for mechanical drawings, connector specification, and power specification. Source: `02_AMD_Docs/GitHub_Links.rtf`.
- PCIe Routing Guide, REFCLK Guide, PMBus Controller Datasheet, VRM Datasheet, and OAM Thermal Guidelines are missing. Source: `Wanted_Documents.rtf`.
- MP2975 is believed present but not visually confirmed. Source: `13_Reference_Docs/Component_Index.rtf`.
- ROCm/HIP notes describe memory spaces, SDMA transfer behavior, `rocminfo`, and `HSA_XNACK=1`. Source: `13_Reference_Docs/ROCm/Overview.md`.

## Inferred
- Schematic capture should begin only after OAM connector, PCIe/REFCLK, power, and management unknowns are resolved because those items are listed as missing or unverified in repository references.
- PCB layout should wait for mechanical, connector, cooling, and high-speed routing constraints because local readable files do not provide those details.
- Bring-up planning can use ROCm/HIP validation clues, but these do not replace electrical design requirements. Source: `13_Reference_Docs/ROCm/Overview.md`.

## Unknown
- Needs Verification: OAM connector pinout, mechanical drawings, baseboard requirements, PCIe/REFCLK routing, and power specification.
- Needs Verification: power rails, sequencing, PMBus, telemetry, and VRM controller behavior.
- Needs Verification: cooling interface, board outline, mounting, keepouts, and connector stack-up.
- Needs Verification: firmware, management, health-check, and validation hardware requirements.

## Source Documents
- `README.md`
- `Wanted_Documents.rtf`
- `02_AMD_Docs/GitHub_Links.rtf`
- `13_Reference_Docs/Reference_Index.rtf`
- `13_Reference_Docs/Component_Index.rtf`
- `13_Reference_Docs/ROCm/Overview.md`
- `13_Reference_Docs/ROCm/README (1).md`

## Design Implications
- Before schematic capture: verify OAM connector, PCIe/REFCLK, power, management, and baseboard requirements.
- Before PCB layout: verify board outline, connector placement, high-speed routing constraints, thermal/mechanical keepouts, and footprint-critical datasheets.
- During bring-up: use `rocminfo`, XNACK status, SDMA behavior, and ROCm/HIP memory notes for software validation planning.
- Documentation hygiene: every design fact should include source path and status label.

## Open Questions
- Which missing references are mandatory for a first schematic?
- Which validation tests prove the carrier rather than only the GPU software stack?
- Which unreadable PDFs should be replaced first?
