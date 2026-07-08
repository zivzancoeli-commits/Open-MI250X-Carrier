# 13_Reference_Docs

## Purpose
This folder exists as the local evidence library for the reverse-engineering project. It collects indexes and copied references that may support mechanical, electrical, firmware, cooling, memory, and software decisions.

## Engineering Questions
- Which AMD, ROCm, OAM/OCP, Molex, cooling, firmware, memory, and application references are known?
- Which component facts are available, and which require visual confirmation?
- Which references should feed future mechanical, connector, schematic, BOM, firmware, cooling, and validation work?

## Look Elsewhere
- [ROCm](ROCm/) explains software-visible MI200/MI250X memory behavior, transfer paths, and matrix-core programming.
- [Memory_HBM](Memory_HBM/) is the local HBM reference area connected to the memory entries in the index.
- [02_AMD_Docs](../02_AMD_Docs/) tracks upstream links before references are mirrored here.
- [08_Research_Papers](../08_Research_Papers/) provides research context that should be checked against vendor references.
- [09_AI_Notes](../09_AI_Notes/) should receive extracted facts, assumptions, and open questions.

## Known Information
- `Reference_Index.rtf` names AMD architecture/datasheet/ISA references, ROCm health and validation topics, OAM/OCP references, Mirror Mezz documentation, cooling references, firmware tools, HBM references, and GPU management interfaces.
- `Component_Index.rtf` lists MP2975 as a Monolithic Power Systems digital multiphase VRM controller, believed present on MI250X, not visually confirmed, with no public datasheet.
- `README.rtf` describes planned folders for photos, KiCad, schematics, datasheets, mechanical measurements, teardowns, PCB analysis, GitHub sources, and vendor documentation.

## Open Questions
- Source URLs, document versions, and retrieval dates are mostly absent.
- Many entries in `Reference_Index.rtf` do not have matching local files.
- MP2975 presence and component details need verification.
- Planned mechanical, schematic, cooling-photo, and BOM folders do not yet exist.

## TODO
- Link each index entry to a local file or external source.
- Add provenance metadata for high-value references and mark missing documents clearly.
