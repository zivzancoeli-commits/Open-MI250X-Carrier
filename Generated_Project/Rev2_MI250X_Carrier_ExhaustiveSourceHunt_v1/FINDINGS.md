# FINDINGS — exhaustive public-source hunt for remaining MI250X carrier blockers

**Date:** 2026-08-17  
**Tree:** `Generated_Project/Rev2_MI250X_Carrier_ExhaustiveSourceHunt_v1/`  
**Pin map already in repo (not rediscovered):** `22_Pinmap_Research/` OCP generic **v1.0** 688+688 pad map (P3V3=2 Conn0). r2.0 pinlists remain **UNUSABLE**.

Labels:

| Label | Meaning |
|---|---|
| **Closed** | Cited public source answers the question for this bucket |
| **Exhausted** | Unknown after this hunt; every URL tried is in `URL_LOG.md` |
| **Verified** | Quote or file retrieved this run |
| **Inferred** | Reading of those sources; not a new pin assignment |

Trust ranking used when sources conflict: **OCP official PDF > AMD official > Molex official SD/PS > SuperMicro/HPE/Lenovo manuals > IEEE/OCP slides > Level1Techs/forums (supporting only).** Count independent sources; one forum post does not outvote OCP.

**Do not send this (or any in-repo) board to PCBWay. Do not energize OAMs.**

---

## Bottom line (one line)

**Can they PCBWay? No** — 48 V mezz rating vs Molex catalog 30 V is not closed by a retrieved `2189100001-PS-000`, AMD overlay is NDA, and UBB Figure 44 millimetre coordinates were not OCR’d from a public binary PDF.

---

## Scoreboard

| # | Bucket | Status | What won |
|---|---|---|---|
| 1 | Molex 218910-1115 voltage/current at 48–54 V | **Exhausted as an energize gate** (catalog 30 V is Closed; 48 V mezz use is documented by OCP *after pin-assignment review*, not by Molex PS) | Catalog **30 V**: Molex/Farnell + OCP Table 3 first clause. System **48/54/60 V**: OCP Table 3 parenthetical + Table 5 + shipping UBB. **PS-000 not retrieved.** |
| 2 | OCP v1.5 named pinmap spreadsheet | **Exhausted** (filename). Count-level match to v1.0 **Closed** | No v1.5-named xlsx found. Changelog last names `OAM_Pin_map_rev1.0`. Table 4 still P3V3=2. |
| 3 | AMD MI250X OAM hardware integration | **Exhausted** (overlay). Dual-GCD PCIe existence **Closed** | Public Instinct docs only. NDA wall listed. Do not guess TEST*. |
| 4 | UBB v1.5 gerber / Figure 44 XY / module pitch | **Exhausted** (gerber + Figure 44 mm). Board **417 × 585 mm Closed** | Coordinates live in figures; binary PDF Cloudflare/IA 498; no public gerber. |
| 5 | Donor designs (AOM-MCM-Q, HPE, Penguin, GitHub) | **Exhausted** | Manuals/listings only; no schematic/gerber/overlay. |
| 6 | PCIe OAM → CEM/MCIO for X11DPH-T Gen3 | **Closed as “no honest product”** | Many CEM↔SlimSAS/MCIO **test/storage** cards exist. None is an OAM host PE. SuperMicro CBL-MCIO is UBB cable. |
| 7 | OAM air heatsink PNs that mate bolster | **Exhausted** | Fivetech PN is the **handle**. Shroud/tray PNs are chassis. No bolster-mating HS MPN. |
| 8 | HOST_PWRGD / P48V sequence (OCP v1.5 tables) | **Closed** (OCP generic notes) | §8.5 notes 1–8 + 100 ms MODULE_PWRGD→PERST#. AMD-specific delays still Unknown. |
| 9 | SendCutSend / sheet | **Closed as chassis-only** | Can cut aluminum + PEM. Not electrical, not bolster ICD, not a substitute for voltage/overlay. |

---

## 1. Molex 218910-1115 / 2189100001-PS-000 / Mirror Mezz Pro — voltage and current at 48–54 V

### Status: Exhausted as a fab/energize gate

Do not invent a 12 V-to-OAM hack. Dell D3000E-S1 remains 12 V CRPS. Never drive PVREF.

### What was retrieved (Verified)

| Claim | Source | HTTP |
|---|---|---|
| **Voltage - Maximum 30V AC (RMS)/DC**. Current 0.75 A (1 oz) / 1.0 A (1.5 oz) / 1.2 A (2 oz). 688 circuits, 5.00 mm mated height, mates with itself. Product spec filename **2189100001-PS-000**; sales drawing **2189101115-SD-000**. | Farnell sheet `docs/downloads/Farnell_Molex_2189101115.pdf` https://www.farnell.com/datasheets/3919676.pdf | **200** PDF |
| **Voltage (max.): 29.9V AC RMS**. Mirror Mezz / Pro current 1.0 A; Enhanced 0.75 A. Dielectric withstand **500 V DC**. | Molex 15×11 OCP flyer `Molex_Mirror_Mezz_15x11_OCP.pdf` and overview `Molex_Mirror_Mezz_overview.pdf` (content.molex.com) | **200** PDF |
| Marketing: “Supports either **12V or 48V** input. Up to 200W (12V) or **500W (48V)**.” Current “1.0A per pin @ 1.5oz. Copper after derating”. | `Molex_Supports_OCP_Open_Standards.pdf` | **200** PDF |
| **OCP Table 3 (v1.5):** “Max Voltage Application **30V AC (OAM supports 60V after Molex’s pin assignment review)**.” Current “**1A/pin after 20% derating** 1.5oz copper” @ 80 °C. Withstand 500 V min. | OAM Design Spec v1.5 §8.1 Table 3 (extracted `docs/retrieved_text/OCP_OAM_v1.5_extracted.txt`; same quote on Scribd copy of the same PDF) | OCP site Cloudflare; text recovered |
| **OCP Table 5:** P48V **44 V min to 60 V max**, 16 pins, **16 A when at 44 V**. | Same v1.5 §8.4.1 | same |
| SuperMicro **CBL-PWEX-1280** is a **54 V UBB cable** (MicroFit 2×5), **not** a mezz rating. | MNL-2507 (supermicro.com **403** this run; prior extracted text) | 403 |
| UBB v1.5 BOM: Amphenol **10028917-001LF** listed as “**54V Connector**” ×4 — that is the **UBB input** power connector, not 218910-1115. | UBB v1.5 Table 49 | extracted text |

### What was **not** retrieved

`2189100001-PS-000` PDF and `2189101115-SD-000` PDF: **molex.com timed out** (HTTP 0) on every `pdm_docs/ps`, `pdm_docs/sd`, and `content/dam/.../salesdrawingpdf` URL tried, HTTP/1.1 and default. Digi-Key **403**, Newark **403**, Octopart **403**, Arrow **000**, Studocu SD page **403**. Mouser **200** but JS shell (no PS PDF). LCSC **200** HTML is a **wrong part** (DSE453226 inductor image on that SKU page) — discarded.

Internet Archive snapshots of the v1.0 xlsx (unrelated to PS) returned **498** this run.

### Conflict resolution (count + trust)

| Position | Independent sources | Trust |
|---|---|---|
| Catalog / generic max **30 V** (or 29.9 V RMS) | Farnell/Molex catalog sheet; Molex 15×11 flyer; Molex overview; **OCP Table 3 first clause** | Molex official catalog + OCP official. **Wins the published connector rating.** |
| OAM **may use 60 V after Molex pin-assignment review** | **OCP Table 3 parenthetical** (one official sentence) | OCP official, but it is a **review caveat**, not a retrieved Molex PS table. |
| System **48/54 V** into the OAM *ecosystem* | OCP Table 5 P48V 44–60 V; OCP high-level 44–59.5 V / 700 W; Facebook OAM 2019 blog 12 V and 48 V; SuperMicro 54 V **cable**; UBB 54 V **input connector**; Molex **marketing** 48 V / 500 W | OCP + OEM system. **Does not re-rate the generic 30 V catalog line.** |

**Winner for “what does the connector sheet say?”:** **30 V** (more catalog sources **and** OCP Table 3’s primary cell).  
**Winner for “do shipping UBBs run 48/54 V somewhere?”:** **Yes, on the UBB power path** (OCP + SuperMicro cable + UBB BOM). That is **not** a retrieved Molex statement that every 218910-1115 contact is 48 V capable.

OCP’s own reconciliation is the parenthetical: 30 V application, **60 V only after Molex pin-assignment review** (i.e. the 16 named P48V pads, not a blanket 48 V on all 688 contacts). **Until `2189100001-PS-000` is in hand, that review is not citable from Molex.** Do not tape out P48V into this footprint as “closed.”

Current at 48–54 V **if** the review applies: OCP Table 5 16 A / 16 pins = 1 A/pin at 44 V, which matches Table 3 and Farnell 1.0 A @ 1.5 oz. That arithmetic is **not** permission to apply 48 V.

---

## 2. OCP v1.5 named pinmap spreadsheet (§8.3)

### Status: Exhausted (no v1.5-named map). Count-level identity with v1.0 **Closed**.

v1.5 §8.3: *“The detailed pin mapping to connectors is in the separated spreadsheet. This section only shows the pin list and description.”* **No filename** (unlike r2.0, which names `OAI OAM_Pinlist_Pinmap_r2.0_v1.0.xlsx`).

Changelog in the same PDF:

- Spec **v1.0** (2019-07-25): *“Update OAM_Pin_map to rev1.0 … refer to OAM_Pin_map_rev1.0 spreadsheet”* and `OAM_Pin_list_Rev1.0`.
- Spec **v1.1 / v1.5**: IO table notes, `DEBUG_PORT_PRSNT#`, power-off sequence, Mirror Mezz → Mirror Mezz Pro, 112G PAM4. **No new pin-map filename.**

Count check vs in-repo v1.0 map (`22_Pinmap_Research/extracted/OAM_v1.0_signal_counts.csv`):

| Signal | v1.0 map (Conn0) | v1.5 Table 4 | r2.0 Table 4 |
|---|---|---|---|
| P3V3 | **2** | **2** Conn0 | **6** (UNUSABLE) |
| P48V | **16** | **16** Conn0 | split Conn0+Conn1 |

**Pad-by-pad identity of a later v1.5 xlsx vs this v1.0 grid: Unknown.** Counts matching is **not** a pad move audit. Do not invent deltas.

### URLs tried (all failed to yield a v1.5-named xlsx)

| URL | Status |
|---|---|
| GitHub code search `OAM_Pin_map_rev1.0` (logged-out HTML) | **200**, `result_count: 0` |
| `opencomputeproject/OCP-SVR-OAI-Open_Accelerator_Infrastructure` | **200** project page; no xlsx |
| `files.opencompute.org` tokens `938c61e5…` (v1.0 pkg) and `fb91bace…` (v1.1 list) | **403** Cloudflare |
| Wayback snapshots of those xlsx (2020–2022) | **498** (not the file) |
| OCP wiki / v1.5 document pages | Cloudflare challenge from curl; WebSearch pipeline still returns PDF **text** |
| Groups.io `OCP-OAI` June updates | **200** — members asking Whitney Zhao to **share OAM2.0** map; no v1.5 attachment |
| `oam_pin list_rev1.1.xlsx` via IA | **498** this run (CDX previously showed ~160 KB **list**, counts-only class) |

A v1.5-named **map** was not in prior IA CDX either (only v1.0 map + v1.1 **list**). **Stop for this item: Unknown + log.** Use the in-repo v1.0 map as the generic OCP grid; do not mix r2.0.

---

## 3. AMD MI250X OAM hardware integration — public crumbs + NDA wall

### Status: Overlay **Exhausted**. Dual-GCD host endpoints **Closed**.

### Newly Closed this run (was 404 on `rocm.docs` previously)

https://instinct.docs.amd.com/latest/gpu-arch/mi250.html **HTTP 200**:

> “The MI250 OAMs attach to the host system via **PCIe Gen 4 x16** links … **Each GCD maintains its own PCIe x16** link to the host … some platforms may offer an **x8** interface to the GCDs.”

Same page: on-package Infinity Fabric between the two GCDs; additional xGMI between OAMs. **No 688-pad table. No mapping of those two x16 (or x8) links onto v1.0 `PCIE_TX/RX[15:0]`.**

| Source | HTTP | What it gives |
|---|---|---|
| https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instinct-mi200-datasheet.pdf | **200** | OAM, PCIe Gen 4, 500 W & 560 W TDP, Passive & Liquid, up to 8 Infinity Fabric links. **No pin table.** |
| https://www.amd.com/en/products/accelerators/instinct/mi200/mi250x.html | **200** | Form factor OAM; Bus Type PCIe 4.0 x16 (singular on the product page). |
| https://instinct.docs.amd.com/projects/system-acceptance/en/latest/gpus/mi250.html | **200** | Dual GCD; PCI **1002:740c**; MI250X same ID; 4-OAM node 8 `lspci` entries. |
| https://rocm.docs.amd.com/en/latest/conceptual/gpu-arch/mi250.html | **404** | Content now lives on instinct.docs (above). |
| AMD CDNA2 white paper URL tried | **404** | |
| ServeTheHome HC34 | **200** | Dual die, OEM topologies; no pad map. |

### NDA wall (do not guess)

- TEST0–TEST14, TEST_MODE# function and required pull
- Which v1.0 `S1_*`…`S7_*` are xGMI vs unused on **this** MI250X
- SMBus slave addresses / PMBus map (do **not** invent 0x50 from forum EEPROM talk)
- Exact mapping of two GCD x16 (or x8) onto v1.0 `PCIE_*`
- PE_BIF[1:0] default for MI250X
- Whether P12V2 must be live on this 48 V module (OCP allows extra P12V NC on 48 V boards)
- Die / TIM / bolster ICD for a heatsink
- Any AMD “OAM hardware integration guide” / baseboard pin overlay

No leaked-but-public pin extras beyond the OCP generic v1.0 map were found.

---

## 4. UBB v1.5 gerber / placement / Figure 44 coordinates / 8× OAM XY

### Status: Board size **Closed**. Figure 44 millimetres **Exhausted**. Gerber **Exhausted**.

| Item | Status | Citation |
|---|---|---|
| UBB PCB **417 mm × 585 mm × 3.2 mm** | **Closed** | UBB v1.5 §8.4 / high-level table |
| OAM module **102 × 165 mm**; connector-to-connector **102 mm**; KOZ **103 × 166 mm** | **Closed** | OAM v1.5 §6.1 / §6.5.2 (already in chassis envelope CSV) |
| Figure 44 “UBB high speed and power connectors **coordinate**” (page ~84) | Figure **exists**; **XY not extracted** | Text pipeline does not OCR the drawing. Binary PDF: opencompute.org Cloudflare; Wayback **498**. |
| Figure 46 “OAM through holes” (32 holes to bolster) | Same — figure exists, **mm Unknown** | |
| Public UBB gerber / Altium / KiCad | **Not found** | GitHub OCP-SVR-OAI page only; GitHub code search 0 for pinmap; GrabCAD search page 200 with no citable UBB gerber in this fetch |
| Module-to-module pitch in mm | **Unknown** | Do **not** invent from 4×2 × 103 mm tiling (that was previously labeled Inferred and is **not** Figure 44) |

OCP UBB v1.5 §8.5.3: “3D files are on the OCP-OAI wiki.” Wiki is Cloudflare + login. **Stop: Unknown + log.**

---

## 5. Donor designs

### Status: Exhausted

| Donor | What is public | Pad map / gerber? |
|---|---|---|
| SuperMicro **AOM-MCM-Q-P** in AS-4124GQ-TNMI | Datasheet/manual **403** from supermicro.com this run; prior MNL-2507 extract: 4× MI250 OAM, shroud **MCP-310-45802-0B**, stiffener **MCP-240-45801-0N**, tray **MCP-240-45809-0N**, MCIO cables, **CBL-PWEX-1280** 54 V. eBay photos of the UBB. | **No** |
| HPE **P41933-001** | Spare **MI250X OAM module** (“SPS-PCA MI250X OAM MCM”), not a tray gerber. alinc.com **403** this run. | **No** |
| HPE Cray EX235a | Architecture in STH/AMD; psnow URL **000** | **No** |
| Penguin Computing | Homepage **200**; no public UBB design files | **No** |
| Gigabyte G492-HA0 | Datasheet **200** — **10× PCIe Gen4 CEM GPUs**, not OAM | n/a |
| OCP contribution GitHub | Spec charter README; **no** schematic/gerber | **No** |
| Inspur / Hyve / ZT / Inventec UBB v1.0 “reference boards” | Named in UBB v1.5 §7.8; files on wiki | **Not public here** |
| KiCad/Altium public 218910-1115 carrier | GitHub search empty; KiCad Molex.pretty archived, no this MPN | **No** |

Level1Techs thread **200** (supporting only): community path is still a donor UBB + v1.0 OCP map; no public continuity table.

---

## 6. PCIe OAM → CEM/MCIO products vs locked host X11DPH-T Gen3

### Status: Closed as “honest: these do not attach OAM host PE to X11DPH-T”

Locked host: X11DPH-T, 3× PCIe **3.0** x16 + 4× x8. MI250X is PCIe **4.0** and will downtrain. Dual-GCD ⇒ **two** endpoints per OAM (Verified). Two OAMs ⇒ **four** endpoints vs **three** x16 slots if each GCD wants x16. Some platforms use **x8 per GCD** (instinct.docs). Topology still not a finished BOM.

| Product | HTTP | Honest use |
|---|---|---|
| SuperMicro **CBL-MCIO-1278S5FYB1** | 200 Wiredzone | **MI-200 UBB cable**, not X11DPH-T CEM |
| TI **CEM2SLIMSAS-EVM** + UG `snlu278.pdf` | 200 | CEM x16 ↔ dual SlimSAS **SFF-9402 storage** AIC |
| Micro SATA **SLM-1773-8I** | 200 | Same class, ReDriver, storage pinout |
| C-Payne SlimSAS x16 AIC | 200 | CEM x16 → 2× SlimSAS 8i; Gen3/4; **not OAM** |
| Teledyne/i-wave **PE-G5-MCIO124Pin-X16SLOT-X** | 200 PDF | Analyzer **host adapter**: MCIO SFF-TA-1016 cable **into a CEM slot** for test. **Not** an OAM mezz breakout. |
| X11DPH-T | (prior 200 bargainhardware manual) | **No onboard MCIO** |

There is **no** public “OAM to PCIe adapter” analogous to SXM risers. Do not buy random SlimSAS/MCIO GPU cables and assume they mate 218910-1115.

---

## 7. OAM air heatsink PNs that mate the bolster

### Status: Exhausted

| PN / claim | What it actually is |
|---|---|
| **Fivetech 62-57P-064-7-02-5** | OCP v1.5 §6.7.1 **folding handle**, not the HS |
| SuperMicro **MCP-310-45802-0B** | GPU **air shroud** |
| **MCP-240-45801-0N** / **MCP-240-45809-0N** | Stiffener / sheet-metal **tray** |
| **SNK-P0063P** | CPU SP3 HS |
| IT Creations MI250 OAM listing | “CONTENT INCLUDES: (1) ONE OAM HEATSINK” — **no MPN**; Passive bidirectional airflow |
| OCP air note | ~450 W on a shadowed 8× tray; MI250X is **500/560 W** |
| Boyd / Cooler Master / Wiwynn | Named as OCP thermal contributors; **no buyable MI250X bolster HS PN** |

Do not DIY a die clamp. Chassis must leave replaceable cooling. TIM/die ICD remains NDA.

---

## 8. HOST_PWRGD / P48V sequence from OCP v1.5

### Status: Closed (OCP generic). AMD-specific timing Unknown.

**HOST_PWRGD** (Conn0 H1 in v1.0 map): *“Host power is good. Active high when P48V, P12V1/P12V2, P3V3 voltages are stable and within specifications. It is considered the Power Enable signal for the module. **10k PD on the baseboard.**”* (v1.5 Table 4 family)

**§8.5 System power sequencing** (verbatim notes; Figures 35/36 are drawings not OCR’d):

1. In a disaggregated design, HOST_PWRGD is the baseboard power-good indication.
2. **All voltages** on the baseboard that the OAM plugs into must be in spec **before HOST_PWRGD is asserted**.
3. HOST_PWRGD is the **enable** to the voltage regulators **on the OAM**.
4. As module voltages ramp, baseboard reference clocks begin to run.
5. After module voltages are in spec, the module asserts **MODULE_PWRGD**.
6. Baseboard should tri-state OAM single-ended inputs before MODULE_PWRGD (except sequence-required signals).
7. **At least 100 ms after MODULE_PWRGD assertion**, the baseboard de-asserts **PERST#**.
8. Optional WARMRST# de-asserts simultaneously or later than PERST#.

UBB v1.5 §6.1.11 repeats the 100 ms PERST# rule and adds UBB-specific retimer/CPLD notes (MODULE_ENABLE, graceful shutdown if MODULE_PWRGD does not drop in 100 ms). Those are **UBB CPLD** details, not a 2-OAM hobbyist schematic.

P48V window: Table 5 **44–60 V** (pin list family also 44–59.5 V). Exact AMD UV/OV and HOST_PWRGD delay vs rail windows: **Unknown** without AMD overlay.

---

## 9. SendCutSend / sheet metal

### Status: Closed as chassis-only. Not electrical.

SendCutSend **200**: laser/CNC aluminum (5052/6061/7075) + PEM nuts/standoffs/studs. Useful **after** OCP M3.5 / 102×165 / 103×166 / 5 mm stack are locked — for trays, ducts, covers. **Not** a bolster ICD, **not** a heatsink, **not** a 48 V mezz close.

OCP UBB reference bolster: **4 mm aluminum alloy** (UBB v1.5 §8.7.2). Screw length still depends on the module stiffener (**Unknown**).

---

## What this does *not* authorize

- Do not treat OCP Table 3’s 60 V parenthetical as a retrieved Molex PS.
- Do not mix r2.0 pads (P3V3=6) with the v1.0 grid.
- Do not invent TEST*/RFU/DO_NOT_USE nets.
- Do not map dual-GCD lanes onto `PCIE_*` by guesswork.
- Do not PCBWay-fab or energize OAMs.

KiCad CLI: Ubuntu `kicad` package exists but this tree is research-only. Prior FullSend tree already ran KiCad 9.0.9 ERC/DRC on a **named-net stub** (not fab sign-off). No production KiCad was modified.
