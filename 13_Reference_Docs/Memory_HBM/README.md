# Memory_HBM

## Purpose
This folder exists to hold high-bandwidth-memory references that may explain the memory technology around MI250X-class accelerators. It is not yet a reliable source for carrier constraints because the only local PDF cannot be read.

## Engineering Questions
- What HBM or HBM2E references are available for memory-context research?
- Are there Samsung Flashbolt details that matter for architecture, power, or thermal notes?
- Which memory claims are supported by readable documents and which require verification?

## Look Elsewhere
- [13_Reference_Docs](../) contains the parent index listing Micron HBM2E, Samsung HBM2E, and CourtListener HBM references.
- [ROCm](../ROCm/) explains software-visible MI200/MI250X VRAM layout, managed memory, and transfer behavior.
- [09_AI_Notes](../../09_AI_Notes/) should receive verified memory, power, thermal, or architecture questions after readable sources are available.
- Planned but not present: reviewed HBM findings may eventually connect to BOM/component-database and thermal design folders.

## Known Information
- `SamsungFlashbolt.pdf` is the only local document here; Samsung Flashbolt is inferred from the filename.
- `Reference_Index.rtf` lists Micron HBM2E, Samsung HBM2E, and CourtListener HBM references, but those are not present as separate local files.
- No readable memory-interface details are available in this folder.

## Open Questions
- Exact title, revision, source URL, and publication date are not recorded.
- The other HBM references named in `Reference_Index.rtf` are absent.
- `SamsungFlashbolt.pdf` reports invalid PDF structure and needs verification.

## TODO
- Add source metadata for `SamsungFlashbolt.pdf`.
- Add notes connecting reviewed HBM facts to carrier-board constraints.
