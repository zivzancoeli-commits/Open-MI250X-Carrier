# Project Overview

## Purpose
- Establish the project goal, evidence workflow, and current documentation coverage for schematic capture, PCB layout, prototype bring-up, and validation.

## Verified
- Project goal is to design a minimal open-source carrier board for surplus AMD Instinct MI250X OAM modules using only publicly available documentation. Source: `README.md`.
- Undocumented behavior should be tracked as an open question rather than assumed. Source: `README.md`.
- Manual project status items are documentation gathering, OAM understanding, undocumented-interface identification, architecture, schematic, PCB layout, and prototype. Source: `README.md`.
- The repository is described as reference material used to reverse engineer and document the AMD Instinct MI250X OAM accelerator. Source: `13_Reference_Docs/README.rtf`.
- Tracked reference categories include AMD, ROCm, OCP/OAM, Molex, cooling, firmware, memory, application notes, and GPU management interfaces. Source: `13_Reference_Docs/Reference_Index.rtf`.

## Inferred
- The engineering workflow is documentation collection -> fact extraction -> unknown tracking -> design use, because the root README emphasizes public evidence and the reference index organizes source categories. Sources: `README.md`, `13_Reference_Docs/Reference_Index.rtf`.
- `09_AI_Notes` should act as the engineering notebook between raw references and design artifacts because it contains topic notes for architecture, PCIe, power, cooling, clocking, management, questions, and unknowns. Source: `09_AI_Notes/README.md`.

## Unknown
- Needs Verification: no schematic, PCB layout, BOM, or mechanical design files were found in the current file tree.
- Needs Verification: `Understanding_Data_Movement.pdf`, `MI200_Memory_Space.pdf`, and `SamsungFlashbolt.pdf` report invalid PDF structure and cannot currently be used as evidence.
- Needs Verification: front, back, and connector photos are marked found in `Wanted_Documents.rtf`, but no image files were found in the repository.

## Source Documents
- `README.md`
- `Wanted_Documents.rtf`
- `13_Reference_Docs/README.rtf`
- `13_Reference_Docs/Reference_Index.rtf`
- `09_AI_Notes/README.md`

## Design Implications
- Treat this notebook as evidence tracking, not design authority.
- Require a readable source for any schematic or layout decision.
- Keep missing or proprietary behavior in `09_Unknowns.md` until verified.

## Open Questions
- Which found photos exist outside this repository?
- Which indexed references have already been reviewed?
- Which references are mandatory before schematic capture can begin?
