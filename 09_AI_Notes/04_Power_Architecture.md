# Power Architecture

## Purpose
- Track power-related evidence for OAM power input, VRM control, PMBus research, and missing power specifications.

## Verified
- The OAM specification link is noted as useful for power specification. Source: `02_AMD_Docs/GitHub_Links.rtf`.
- PMBus Controller Datasheet and VRM Datasheet are listed as missing. Source: `Wanted_Documents.rtf`.
- MP2975 is named as a component. Source: `13_Reference_Docs/Component_Index.rtf`.
- MP2975 manufacturer is Monolithic Power Systems (MPS). Source: `13_Reference_Docs/Component_Index.rtf`.
- MP2975 function is digital multiphase VRM controller. Source: `13_Reference_Docs/Component_Index.rtf`.
- MP2975 is believed present on MI250X but not visually confirmed. Source: `13_Reference_Docs/Component_Index.rtf`.
- No public MP2975 datasheet is currently available in the repository. Source: `13_Reference_Docs/Component_Index.rtf`.

## Inferred
- PMBus is a power-management research topic because the missing document list explicitly asks for a PMBus controller datasheet. Source: `Wanted_Documents.rtf`.
- MP2975 identification could affect BOM, telemetry, sequencing, enable, and fault handling because it is listed as a digital multiphase VRM controller. Source: `13_Reference_Docs/Component_Index.rtf`.

## Unknown
- Needs Verification: actual power rails, voltages, sequencing, current requirements, connectors, fusing, hot-plug behavior, and telemetry signals are not available in readable local files.
- Needs Verification: MP2975 presence requires visual or documentary confirmation.
- Needs Verification: MP2975 register maps and electrical requirements are not available here.

## Source Documents
- `02_AMD_Docs/GitHub_Links.rtf`
- `Wanted_Documents.rtf`
- `13_Reference_Docs/Component_Index.rtf`
- `13_Reference_Docs/Reference_Index.rtf`

## Design Implications
- Do not choose regulators, connectors, or rail sequencing until OAM power specifications are verified.
- Treat MP2975 as a candidate component, not a confirmed BOM item.
- Keep PMBus assumptions out of schematic labels until supported by a readable datasheet or confirmed board evidence.

## Open Questions
- What rails and sequencing does the MI250X OAM require?
- Is MP2975 actually present on the hardware?
- What PMBus addresses, telemetry, and fault behavior are required?
