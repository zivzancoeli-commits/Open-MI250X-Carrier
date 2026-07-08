# Mechanical

## Purpose
- Track mechanical evidence required for board outline, OAM connector placement, mounting, keepouts, and footprint creation.

## Verified
- The OAM specification link is described as useful for mechanical drawings. Source: `02_AMD_Docs/GitHub_Links.rtf`.
- OAM Specification is marked found; Mechanical Specification, Baseboard Specification, and Connector Specification are marked missing. Source: `Wanted_Documents.rtf`.
- Front, back, and connector photos are marked found; heatsink and baseboard photos are marked missing. Source: `Wanted_Documents.rtf`.
- Planned folders include photos, mechanical measurements, teardowns, and PCB analysis. Source: `13_Reference_Docs/README.rtf`.
- Mirror Mezz Datasheet, Mirror Mezz Brochure, and Mirror Mezz Product Guide are indexed. Source: `13_Reference_Docs/Reference_Index.rtf`.

## Inferred
- Mechanical work must combine OAM drawings, connector documentation, photos, and measurements because all are explicitly tracked in source indexes. Sources: `02_AMD_Docs/GitHub_Links.rtf`, `Wanted_Documents.rtf`, `13_Reference_Docs/README.rtf`.
- Mirror Mezz references may be relevant to connector mechanical stack-up because they are indexed under Molex references. Source: `13_Reference_Docs/Reference_Index.rtf`.

## Unknown
- Needs Verification: board outline, module dimensions, connector coordinates, mounting hole pattern, standoff height, keepouts, cold plate interface, and connector mating height are not available locally.
- Needs Verification: found photos referenced by `Wanted_Documents.rtf` are not stored in the repository.

## Source Documents
- `02_AMD_Docs/GitHub_Links.rtf`
- `Wanted_Documents.rtf`
- `13_Reference_Docs/README.rtf`
- `13_Reference_Docs/Reference_Index.rtf`

## Design Implications
- Do not place the OAM connector or define the board outline until mechanical and connector specifications are verified.
- Do not create final connector footprints until Mirror Mezz documents are obtained and checked.
- Photo-derived measurements must include provenance and measurement method.

## Open Questions
- What are the OAM module outline and mounting requirements?
- What is the connector stack-up and mating height?
- Where are the referenced front/back/connector photos stored?
