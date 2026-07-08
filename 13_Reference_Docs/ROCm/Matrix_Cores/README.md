# Matrix_Cores

## Purpose
This folder exists to capture software-compute knowledge about AMD CDNA matrix cores. It is useful for validation and performance context, not for carrier-board electrical, mechanical, thermal, or connector design.

## Engineering Questions
- What matrix-core capabilities are documented for MI250X?
- Which MFMA intrinsic examples exist for validation or software experiments?
- Which data formats and performance table entries are available in the copied article?
- Should engineers use direct intrinsics, rocBLAS, rocWMMA, or the AMD Matrix Instruction Calculator for exploration?

## Look Elsewhere
- [ROCm](../) provides broader MI200/MI250X memory-space, transfer, and software-behavior context.
- [02_AMD_Docs](../../../02_AMD_Docs/) tracks upstream matrix-core benchmark material.
- [09_AI_Notes](../../../09_AI_Notes/) should receive distilled compute-architecture observations and validation questions.
- Planned but not present: matrix-core validation may later connect to software benchmark or system-validation folders.

## Known Information
- The copied article covers GEMM acceleration, MFMA instructions, compiler intrinsic syntax, wavefront register layout, lane mapping, matrix dimensions, blocks, cycles, and flops/clock/CU.
- It references rocBLAS, rocWMMA, LLVM MFMA intrinsics, AMD Instinct MI200 ISA, AMD CDNA/CDNA2 whitepapers, and AMD Matrix Instruction Calculator.
- AMD CDNA matrix core processing units, SIMD/vector FMA units, MI100, MI250X, wavefront lanes, and compute units.
- The existing article is named `README (1).md`, not `README.md`, so it is preserved as source material.
- A similar `README (1).md` also exists one level up in `13_Reference_Docs/ROCm`.
- MI250X matrix-core table entries in the article list FP64 256, FP32 256, FP16 1024, BF16 1024, and INT8 1024 flops/clock/CU.
- MI250X vector FMA table entries list FP64 128 and FP32 128 flops/clock/CU.

## Open Questions
- Original source URL, commit, and publication date are not recorded.
- The reason for the apparent duplicate copy is not documented.

## TODO
- Confirm the original source and version of the matrix-core article.
- Decide whether to keep both matrix-core copies or consolidate them with clear references.
