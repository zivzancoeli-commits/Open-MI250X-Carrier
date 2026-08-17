# BLOCKERS_REMAINING.md — what still prevents PCBWay + plug-in

**Date:** 2026-08-17  
**KiCad:** 9.0.9 CLI ERC/DRC ran on this copied tree. **That is not a fab sign-off.**

**Do not send this board to PCBWay. Do not energize OAMs.** Full-send shopping is a cart decision, not a power-on decision.

---

## Closed enough to buy host+desk (A)

X11DPH-T + 2× 6230 + 8× SNPHVY68C/128G + **8× MEM-DR432L-SL01-ER29** + DX-3647 + ATX/EPS + B550M/5500 will POST. DRAM SKU is the SuperMicro-validated 32 GB 2Rx4 RDIMM (store page 403 here; search pipeline listed MBD-X11DPH-T). Memory Mode **8× PMem slot map** is still not the illustrated 16-slot MM table (see research report).

---

## Still blocking fabrication

1. **Molex 218910-1115 30 V datasheet vs OCP/OEM 48–54 V.** Farnell sheet (HTTP 200) says 30 V max. OCP v1.5 and SuperMicro CBL-PWEX-1280 (54 V UBB cable) show 48/54 V in the OAM *system*. Product spec `2189100001-PS-000` PDF was **not** retrieved. **Do not tape out P48V into this footprint until that is resolved with Molex/OEM practice — not a 12 V hack.**
2. **PIN A3 orientation** still needs a plot overlay (Inferred 180° rotation).
3. **No signal integrity:** no tracks, 499 DRC unconnected items, P48V netclass vs 0.4 mm pad pitch (8 clearance violations — inherent Molex pitch vs 0.64 mm >40 V internal rule).
4. **BGA attach** of 218910-1115 is a factory process, not a JLCPCB default.
5. **ERC:** 378 violations (dangling labels, hierarchical mismatch, multiple net names) because this is a **named-net stub**, not a wired schematic.

## Still blocking energize / plug-in

| Gate | Status |
|---|---|
| 48 V **harness** from RCP-2000-48 (Positronic) to P48V pads, fuse, sense, never mixing 12 V CRPS | **Open** |
| HOST_PWRGD 10k PD + sequence vs P48V/P12V1/P3V3 in-spec | Named; **not implemented** |
| P12V2 on this 48 V MI250X | OCP allows NC extra P12V on 48 V boards; **AMD Unknown** |
| PVREF | Must **not** be driven |
| TEST*/RFU/DO_NOT_USE | **Unmapped** — do not strap |
| Dual-GCD PCIe onto v1.0 `PCIE_*` pads and X11DPH-T **Gen3** (3× x16) | **Open** (2 endpoints per OAM is public; lane map is not) |
| xGMI which S-link | Named, **not routed** |
| SMBus addresses | **Unknown** |
| Air HS that mates the **OAM bolster** (not shroud/tray PNs) | **Unknown height / no HPE HS PN** |
| Dual U14S vs X11DPH-T CPU pitch | **Unknown** |

## What is *not* a UBB

This PCB is **2 electrical seats**. UBB v1.5 **417 × 585 mm** is a **chassis volume** on Dwgs.User. 4×2 KOZ tiling **412 × 332 mm** is **Inferred**, not a UBB. **No public UBB gerber/schematic/overlay** was found.

KiCad reports: `docs/kicad_reports/` (ERC 378, DRC 12 + 499 unconnected).
