# 09_AI_Notes

## Purpose
This folder exists to turn source documents into engineering knowledge. It should hold verified facts, open questions, and assumptions before those items influence reverse engineering, schematics, layout, or validation.

## Engineering Questions
- Which reference facts have been verified and are safe to use?
- Which topics still need evidence: architecture, clocking, cooling, management, PCIe, power, or firmware behavior?
- What unknowns must be resolved before schematic or PCB work?
- Which design ideas are unsupported and should remain separate from facts?

## Look Elsewhere
- [13_Reference_Docs](../13_Reference_Docs/) is the source library for facts that should be distilled here.
- [13_Reference_Docs/ROCm](../13_Reference_Docs/ROCm/) should feed architecture, PCIe, management, and validation notes with software-visible behavior.
- [13_Reference_Docs/Memory_HBM](../13_Reference_Docs/Memory_HBM/) should feed memory, power, or thermal questions after readable sources are available.
- [08_Research_Papers/01_Architecture](../08_Research_Papers/01_Architecture/) should feed topology and bandwidth notes.
- [02_AMD_Docs](../02_AMD_Docs/) points to upstream sources that need review before conclusions are accepted.
- [11_OCP_v1x_Public_Sources.md](11_OCP_v1x_Public_Sources.md) records the 2026-08-21 public OAM v1.x file retrieval (Verified / Unknown).

## Known Information
- The folder is organized by topic: architecture, clocking, cooling, management, PCIe, power, ideas, questions, and unknowns.
- Current note files contain RTF wrapper content rather than visible plain Markdown engineering notes.
- The repository root says undocumented behavior should be tracked as open questions instead of assumed.
- No hardware components or standards are named in the readable note contents.

## Open Questions
- The actual topic notes for power, PCIe, cooling, clocking, management, and architecture are still absent.
- There is no standard format for evidence, assumptions, decisions, or unresolved questions.

## TODO
- Convert placeholder files to plain Markdown.
- Add a shared note template for evidence, assumptions, decisions, and open questions.
