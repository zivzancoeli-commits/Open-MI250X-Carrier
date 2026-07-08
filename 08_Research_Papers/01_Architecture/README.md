# 01_Architecture

## Purpose
This folder exists to capture architecture research about MI250X data movement and accelerator topology. It is useful for understanding system context before interpreting carrier-board requirements.

## Engineering Questions
- What topology information is relevant to carrier documentation?
- Which bandwidth figures should be reviewed before making system-level assumptions?
- How do Infinity Fabric, RCCL, and MPI appear in the available research notes?

## Look Elsewhere
- [08_Research_Papers](../) provides the parent research context.
- [13_Reference_Docs/ROCm](../../13_Reference_Docs/ROCm/) contains readable ROCm notes about memory spaces, SDMA, PCIe, Infinity Fabric, and XNACK that should be compared with this research.
- [09_AI_Notes](../../09_AI_Notes/) should receive verified architecture findings and any unresolved topology questions.
- Planned but not present: extracted topology and bandwidth findings should later connect to schematics, architecture drawings, and validation plans.

## Known Information
- `notes.rtf` names Infinity Fabric, MI250X, RCCL, MPI, node topology, bandwidth matrix, and MPI bandwidth.
- The notes identify Fig 1 as node topology, Fig 6 as bandwidth matrix, and Fig 10 as MPI bandwidth.
- The note "Use topology for carrier documentation" is preserved as the current engineering takeaway.

## Open Questions
- Authors, source URL, publication date, and exact paper title are not recorded.
- The topology and bandwidth figures have not been extracted into plain notes.
- Details beyond the filename and `notes.rtf` require verification because the PDF could not be read.

## TODO
- Add citation metadata and a source link.
- Summarize the named figures in a carrier-design context.
