# AGENTS.md — standing rules for the Open MI250X Carrier

Read this file at the start of every session. Do not reload old chats for pin facts, shopping decisions, or “what we decided last time.” Repo files and newly retrieved public sources win. If a chat and this repo disagree, the repo (and citations in it) win.

## Locked system (do not pivot)

- Compute: AMD Instinct **MI250X OAM** (not MI210). First system **2×**, later **8×**.
- Host: SuperMicro **X11DPH-T**, 2× Xeon Gold **6230 (SRF8W)**, 8× Dell **SNPHVY68C/128G** Optane PMem 100 in Memory Mode, DRAM cache **MEM-DR432L-SL01-ER29** (or another SuperMicro-validated RDIMM on that board). Cooler **NH-U14S DX-3647** only (not DX-4189).
- Desk: **B550M + Ryzen 5 5500**; optional used **RX 470** (5500 has no iGPU).
- Chassis: welded dual-chamber (desk + compute). Dell **D3000E-S1** is **12 V CRPS**, never GPU P48V.

## Buy / do-not-buy / do-not-power

| Allowed this week | Forbidden until gates close |
|---|---|
| Host computer parts (will POST) | **PCBWay / any fab** of in-repo KiCad |
| Desk computer parts (will POST) | **Energize** an MI250X / mate an OAM to a random PCB |
| **SendCutSend** chassis **sheet** (trays, skins, divider) | Treating SendCutSend metal as a bolster ICD or heatsink |
| Local square tube + weld consumables | OAM **r2.0** connectors / r2.0 pinlists (P3V3=6) |
| | Guessed VRM / 12-to-48 boost as the GPU path |
| | Invented TEST*/GPIO/RFU straps |

**Wait (do not close from public catalog sheets):** Brian Park’s answer on Molex **2189101115** **60 V / skip-pin** (OCP v1.5 Table 3 parenthetical: *“OAM supports 60V after Molex’s pin assignment review”*). Catalog sheets still say **30 V**. Do not tape out or apply P48V until that answer (or `2189100001-PS-000`) is in the repo with a citation.

## Pin and electrical rules

- **Do not invent pins.** OCP generic **v1.0** 688+688 map in `22_Pinmap_Research/` is the pad grid. It is **not** an AMD overlay.
- r2.0 pinlists are **UNUSABLE** for MI250X.
- Unmapped `TEST*` / `RFU` / `DO_NOT_USE` / AMD GPIO: leave **no net**. Do not strap.
- Never drive **PVREF** (module output).
- Never mix **P48V** with host/desk **12 V**.
- Do not map dual-GCD PCIe onto `PCIE_*` by guesswork.
- Label every engineering claim **Verified / Inferred / Unknown** (or Closed / Exhausted for hunt buckets).

## Mechanical rules

- OAM module **102 × 165 mm**, KOZ **103 × 166 mm**, stack **5 mm ± 0.15 mm**, M3.5 NPTH **φ 3.9 mm** — OCP v1.5 Figure 2.
- **Do not drill** the 8-GPU M3.5 pattern into chassis metal. 4×2 KOZ tiling **412 × 332 mm** is **Inferred**, not a UBB drawing. UBB v1.5 board is **417 × 585 mm**.
- SendCutSend PEM catalog has **M3 / M4 / …**, **not M3.5**. OAM M3.5 stays as loose hardware. Chassis fasteners may be M4 / 6-32 PEM.
- Do not freeze bay **height** until an OEM air HS is measured. Do not DIY a die clamp.

## Evidence

- Cite the file or URL actually retrieved. Log HTTP codes. 403/429 is not a dead product.
- Trust order: OCP official PDF > AMD official > Molex SD/PS > OEM manuals > slides > forums (supporting only).
- Do not treat OCP Table 3’s 60 V parenthetical as a retrieved Molex product spec.

## KiCad

- Copied `Generated_Project/Rev2_*` trees are **not** production. Do not overwrite `16_KiCad_Design/` or other Rev2 folders in place.
- KiCad ERC/DRC on a named-net stub is **not** a fab sign-off.
- If CSV and `OAM_Pin_map_rev_1.0.xlsx` disagree, **the xlsx wins**.

## Inbox / Molex

If Gmail/Drive MCP is authenticated, check for Brian Park’s **2189101115 60V/skip-pin** reply and file it under the current research tree **before** any P48V layout change. If MCP is not authenticated, **wait** — do not invent the answer.
