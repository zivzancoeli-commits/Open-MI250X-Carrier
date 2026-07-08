# PCIe Interface

## Purpose
- Track verified PCIe and data-movement facts while identifying missing high-speed interface information required for schematic capture and PCB routing.

## Verified
- PCIe Routing Guide and REFCLK Guide are listed as missing. Source: `Wanted_Documents.rtf`.
- MI210 is described as a standard PCIe 4.0 x16 card with one GCD and 64 GB HBM2e. Source: `13_Reference_Docs/ROCm/Overview.md`.
- MI200 SDMA engines are described as mainly tuned for PCIe 4.0 x16 and up to 32 GB/s. Source: `13_Reference_Docs/ROCm/Overview.md`.
- MI250X systems using Infinity Fabric may not max out the faster interconnect through SDMA. Source: `13_Reference_Docs/ROCm/Overview.md`.
- Infinity Fabric, MI250X, node topology, bandwidth matrix, and MPI bandwidth are named as useful research topics. Source: `08_Research_Papers/01_Architecture/notes.rtf`.

## Inferred
- PCIe and REFCLK are schematic-critical because missing guides are explicitly tracked in `Wanted_Documents.rtf`.
- ROCm data-movement facts may inform bring-up validation, but not lane assignment, because `Overview.md` describes software-visible transfer behavior rather than connector pinout.

## Unknown
- Needs Verification: MI250X OAM connector lane mapping is not present in readable local documents.
- Needs Verification: PCIe lane count, polarity rules, routing constraints, REFCLK topology, reset signals, and sideband requirements are not documented locally.
- Needs Verification: local readable docs do not confirm whether a minimal carrier uses PCIe directly, another host link, or baseboard-specific topology.

## Source Documents
- `Wanted_Documents.rtf`
- `13_Reference_Docs/ROCm/Overview.md`
- `08_Research_Papers/01_Architecture/notes.rtf`

## Design Implications
- Do not route PCIe until OAM connector and baseboard specifications are verified.
- Use `Overview.md` transfer details for validation planning, not as electrical routing constraints.
- Keep REFCLK requirements linked to `05_Clock_Architecture.md`.

## Open Questions
- What are the lane mappings and sideband signals at the OAM connector?
- What routing rules apply to PCIe and REFCLK on this carrier?
- What topology should be used for host connectivity?
