# OAM Interface

## Purpose
- Capture what is known about the OAM interface and identify the missing connector, mechanical, baseboard, and power information needed for carrier-board design.

## Verified
- The repository tracks the official Open Accelerator Module specification at `https://github.com/oam-dev/spec`. Source: `02_AMD_Docs/GitHub_Links.rtf`.
- The OAM specification is noted as useful for mechanical drawings, connector specification, and power specification. Source: `02_AMD_Docs/GitHub_Links.rtf`.
- OAM Specification is marked found, while Mechanical Specification, Baseboard Specification, and Connector Specification are marked missing. Source: `Wanted_Documents.rtf`.
- OAM Base Spec, OCP Accelerator Spec, Universal Baseboard, and OAI EXP are indexed under OCP/OAM references. Source: `13_Reference_Docs/Reference_Index.rtf`.
- MI250 and MI250X are described as OCP Accelerator Modules with two GCDs and 128 GB total memory, exposed to software as two devices with separate 64 GB VRAM blocks. Source: `13_Reference_Docs/ROCm/Overview.md`.

## Inferred
- OAM mechanical, connector, and power details are schematic/layout blockers because the OAM spec link is explicitly called useful for those areas. Source: `02_AMD_Docs/GitHub_Links.rtf`.
- Universal Baseboard and OAI EXP may be relevant to host/baseboard integration because they are indexed under OCP/OAM. Source: `13_Reference_Docs/Reference_Index.rtf`.

## Unknown
- Needs Verification: OAM connector pinout is not available in readable local files.
- Needs Verification: mechanical keepouts, module outline, mounting requirements, and connector stack-up are not available in readable local files.
- Needs Verification: baseboard requirements are listed as missing in `Wanted_Documents.rtf`.

## Source Documents
- `02_AMD_Docs/GitHub_Links.rtf`
- `Wanted_Documents.rtf`
- `13_Reference_Docs/Reference_Index.rtf`
- `13_Reference_Docs/ROCm/Overview.md`

## Design Implications
- Do not assign connector pins until the OAM connector specification is verified.
- Extract mechanical drawings before board outline or connector placement.
- Link any OAM power findings to `04_Power_Architecture.md`.

## Open Questions
- What is the exact OAM connector pinout?
- What mechanical and baseboard requirements apply to a minimal carrier?
- Which OCP/OAM documents must be local before schematic capture?
