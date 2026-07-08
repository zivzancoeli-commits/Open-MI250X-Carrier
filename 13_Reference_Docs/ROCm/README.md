# ROCm

## Purpose
This folder exists to explain software-visible MI200/MI250X behavior that can affect system assumptions, bring-up, and validation. It is not an electrical or mechanical authority for the carrier board.

## Engineering Questions
- How does software see MI250X memory and devices?
- What HIP memory modes, SDMA behavior, and XNACK behavior matter for validation?
- Which data movement assumptions involve PCIe 4.0 x16, Infinity Fabric, or managed memory?
- Which matrix-core programming references are available for compute validation?

## Look Elsewhere
- [Matrix_Cores](Matrix_Cores/) expands the MFMA, rocBLAS, rocWMMA, and MI250X compute notes.
- [Memory_HBM](../Memory_HBM/) is the hardware-memory reference area for HBM/HBM2E context.
- [08_Research_Papers/01_Architecture](../../08_Research_Papers/01_Architecture/) contains topology and bandwidth research notes that should be compared with ROCm behavior.
- [09_AI_Notes](../../09_AI_Notes/) should capture architecture, PCIe, management, and validation implications.
- [02_AMD_Docs](../../02_AMD_Docs/) tracks upstream ROCm compatibility and matrix-core links.

## Known Information
- MI210: described in `Overview.md` as a PCIe 4.0 x16 card with one GCD and 64 GB HBM2e.
- MI250 and MI250X: described as OAMs with two GCDs, 128 GB total memory, and software presentation as two devices with separate 64 GB VRAM blocks.
- `Overview.md` states that pinned host memory can improve transfer bandwidth versus pageable memory, and that MI200 SDMA engines are tuned for PCIe 4.0 x16 up to 32 GB/s.
- `Overview.md` states XNACK page migration can be enabled with `HSA_XNACK=1` on MI200 platforms where available.
- The folder also references HIP APIs, `rocminfo`, `HSA_ENABLE_SDMA=0`, SDMA, Infinity Fabric, rocBLAS, rocWMMA, LLVM MFMA intrinsics, HMM, and the AMD Instinct MI200 ISA reference.

## Open Questions
- Source URLs and retrieval dates are not recorded for local copies.
- The repository does not explain whether the two matrix-core article copies are intentional.
- `MI200_Memory_Space.pdf` reports invalid PDF structure and needs verification.

## TODO
- Confirm provenance for each copied ROCm article.
- Annotate or consolidate duplicate matrix-core material after review.
- Add a short index mapping ROCm concepts to carrier-design questions.
