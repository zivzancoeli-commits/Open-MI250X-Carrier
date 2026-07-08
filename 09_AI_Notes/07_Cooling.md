# Cooling

## Purpose
- Track thermal and cooling evidence needed for mechanical constraints, board placement, and prototype validation.

## Verified
- OAM Thermal Guidelines are listed as missing. Source: `Wanted_Documents.rtf`.
- Front, back, and connector photos are marked found; heatsink and baseboard photos are marked missing. Source: `Wanted_Documents.rtf`.
- Cooling references indexed include Cold Plate Requirements, Cold Plate Development, Rack Manifold, Reservoir & Pumping Unit, Water Cooling, Glycol Cooling, and Immersion Cooling. Source: `13_Reference_Docs/Reference_Index.rtf`.
- A planned photos area is described for PCB, heatsink, package, connectors, and related images. Source: `13_Reference_Docs/README.rtf`.
- `Cooling.md` exists, but contains no visible plain Markdown engineering content. Source: `09_AI_Notes/Cooling.md`.

## Inferred
- Cooling design depends on OAM thermal guidelines and physical evidence because thermal guidelines and photos are explicitly tracked. Source: `Wanted_Documents.rtf`.
- Cold plate and liquid-cooling references may become relevant because they are indexed, but their contents are not present locally. Source: `13_Reference_Docs/Reference_Index.rtf`.

## Unknown
- Needs Verification: MI250X OAM thermal design power, cold plate interface, mounting force, keepouts, heatsink geometry, coolant requirements, and sensor locations are not documented locally.
- Needs Verification: no thermal photos or drawings are present in the repository.

## Source Documents
- `Wanted_Documents.rtf`
- `13_Reference_Docs/Reference_Index.rtf`
- `13_Reference_Docs/README.rtf`
- `09_AI_Notes/Cooling.md`

## Design Implications
- Do not set keepouts, mounting assumptions, or cooling interface constraints until thermal and mechanical sources are verified.
- Cross-check cooling requirements with `04_Power_Architecture.md`.
- Treat any heatsink or cold-plate assumptions as Needs Verification until photos or guidelines are available.

## Open Questions
- What thermal interface and cooling method are required?
- What heatsink or cold plate geometry applies?
- Where are the found photos referenced in `Wanted_Documents.rtf`?
