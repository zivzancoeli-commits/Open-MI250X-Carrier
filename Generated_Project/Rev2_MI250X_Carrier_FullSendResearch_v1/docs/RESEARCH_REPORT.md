# Research report — full-send 2-OAM carrier (2026-08-17)

**Tree:** `Generated_Project/Rev2_MI250X_Carrier_FullSendResearch_v1`  
**Pin map authority:** `22_Pinmap_Research/downloads/OAM_Pin_map_rev_1.0.xlsx` sheet **OCP Generic Pin Map** (PR #1). CSV dump is convenience only.

Labels:

| Label | Meaning |
|---|---|
| **Verified** | Quote or file retrieved this run (see `URL_FETCH_LOG.txt` and `docs/downloads/`) |
| **Inferred** | Reading of those sources; not a new pin assignment |
| **Unknown** | Not found in public sources this run |

**Public UBB schematic / gerber / AOM-MCM-Q pad overlay: not found.** GitHub `opencomputeproject/OCP-SVR-OAI-Open_Accelerator_Infrastructure` retrieved as a project page (HTTP 200); no xlsx/gerber in that public tree.

r2.0 pinlists remain **UNUSABLE** (P3V3=6 vs v1.0/v1.5 P3V3=2).

---

## 1. Molex 218910-1115 voltage vs OCP 48 V

**Still OPEN as a fab/energize gate.** Do not invent a 12 V-to-OAM hack.

| Claim | Label | Source (retrieved) |
|---|---|---|
| Part: Mirror Mezz Pro hermaphroditic, 688 circuits, 15 pair × 11 row, BGA, mated height **5.00 mm**, **Mates With 2189101115** | Verified | `downloads/Farnell_Molex_2189101115.pdf` from https://www.farnell.com/datasheets/3919676.pdf (HTTP 200) |
| **Voltage - Maximum 30V AC (RMS)/DC** | Verified | Same Farnell sheet, Electrical table |
| Current max per contact **0.75 A (1 oz Cu) / 1.0 A (1.5 oz) / 1.2 A (2 oz)** | Verified | Same sheet |
| Product spec document name **2189100001-PS-000**; sales drawing **2189101115-SD-000** | Verified as filenames on the Farnell sheet | Full PS PDF **not downloaded** this run (Molex part-detail URL failed: curl 000) |
| Marketing: “Supports either **12V or 48V** input. Up to 200W (12V) or **500W (48V)**” | Verified marketing | `downloads/Molex_Supports_OCP_Open_Standards.pdf` https://www.content.molex.com/dxresources/7f7b/7f7b6bdf-bb6d-4339-b836-185ec7a3b999.pdf (HTTP 200) |
| Family brochure voltage **29.9V AC RMS**; current 0.75 A @ 1 oz / 1.2 A @ 2 oz | Verified | `downloads/Molex_Mirror_Mezz_overview.pdf` and `Molex_Mirror_Mezz_15x11_OCP.pdf` (HTTP 200) |
| OCP OAM v1.5: P48V **44–59.5 V**, 16 SE pads Conn0, up to 700 W class when Vin ≥ 44 V; connector MPN **218910-1115** | Verified | OAM v1.5 text via research pipeline; saved `retrieved_text/OCP_OAM_v1.5_extracted.txt` (opencompute.org PDF often Cloudflare) |
| Shipping SuperMicro MI250 system uses **54 V** on UBB power cable **CBL-PWEX-1280** (“Microfit (2X5 to 2X5), PH3.0, 53CM, **54V**, 9A/pin, 16AWG”) | Verified as a **UBB cable**, not the mezz | SuperMicro MNL-2507 / AS-4124GQ-TNMI kit lists (direct supermicro.com PDF **HTTP 403** from this cloud; text recovered via research pipeline → `retrieved_text/SuperMicro_MNL-2507_extracted.txt`; smicro.eu kit table also indexed) |
| HPE / AOM-MCM-Q 48 V on the **5 mm mezz contacts** measured | **Unknown** | No public continuity or voltage-on-pad table |

**Inferred:** OCP and at least one shipping UBB (SuperMicro AOM-MCM-Q-P in AS-4124GQ-TNMI) run **48/54 V into the OAM ecosystem** while Molex’s **generic** 2189101115 sheet still says **30 V**. That contradiction is not resolved by a hobbyist 12 V boost. Current on 16× P48V pads at 1.0 A would be 16 A (~768 W at 48 V) **if** the 1.0 A rating applied at 48 V — the rating is on a 30 V sheet, so do not treat that as a closed 48 V ampacity.

Farnell product HTML https://uk.farnell.com/molex/2189101115/connector-mezz-15pos-11row/dp/4145887 → **HTTP 403** this run (datasheet PDF was 200).

---

## 2. 48 V source + harness

| Item | Label | Notes |
|---|---|---|
| MEAN WELL **RCP-2000-48**: 48 V, 0–42 A, 2016 W, trim **42–56 V** | Verified | `downloads/MEANWELL_RCP-2000-SPEC.PDF` https://www.meanwell.com/Upload/PDF/RCP-2000/RCP-2000-SPEC.PDF (HTTP 200) |
| Output connector **Positronic PCIM34W13M400A1** (CN501) | Verified | Same PDF pin table |
| Remote sense: pin **14 +S**, pin **15 −S**. If unused, **+S must go to +V(signal) pin 10** and **−S to −V(signal) pin 9** or the unit will not regulate correctly | Verified | Same PDF §1.1 Remote Sense |
| +V pins 1–4, −V pins 5–8; Remote ON-OFF pin 17 vs +5V-AUX | Verified | Same PDF |
| OCP ORV3 48 V shelf / busbar | Verified as **architecture** | Not a 2-OAM harness. Do not buy a rack shelf for two GPUs. |
| SuperMicro **CBL-PWEX-1280** 54 V MicroFit 2×5 | Verified UBB cable | Does **not** mate to 218910-1115. Gender of 218910-1115 is **hermaphroditic** (Farnell: mates with itself). Carrier buy is **4×**, not male/female. |
| HOST_PWRGD (Conn0 H1) | Verified OCP name | OAM v1.5: *“Host power is good. Active high when P48V, P12V1/P12V2, P3V3 voltages are stable and within specifications. It is considered the Power Enable signal for the module. **10k PD on the baseboard.**”* |
| PWRBRK# (Conn0 C3) | Verified OCP name | CEM power break; 47k PU on the module |
| Finished OAM P48V pigtail PN | **Unknown** | Do not invent an 8-pin GPU 12 V cable onto P48V |
| P12V2 on 48 V modules | OCP generic vs AMD | OAM v1.5: *“Only **five P12V** power pins are mandatory when the supply power is **48V** (16 pins), and the rest of the P12V pins can be **NC**.”* That is **P12V1’s five pads**. Whether **this** MI250X still needs P12V2 live is **AMD Unknown**. Do not short P12V1 to P12V2. |

Two MI250X at 560 W peak ≈ 23 A at 48 V (**Inferred** from AMD TDP + Ohm’s law). RCP-2000-48 42 A has headroom **if** voltage-rating and harness gates close. That is not permission to apply power.

Dell **D3000E-S1** remains **+12.2 V / 245.9 A** (IT Creations https://www.itcreations.com/product/132053 HTTP 200). **Not** GPU P48V. Never mix with P48V.

---

## 3. AMD MI250X OAM overlay

Public Instinct docs retrieved:

| File / page | HTTP | What it gives |
|---|---|---|
| https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instinct-mi200-datasheet.pdf | 200 | OAM, **PCIe Gen 4**, 128 GB HBM2e, **500 W & 560 W TDP**, Infinity Fabric links **up to 8** on MI250X, coherency enabled. **No 688-pad table.** |
| https://www.amd.com/en/products/accelerators/instinct/mi200/mi250x.html | 200 | Form factor OAM; **Bus Type PCIe 4.0 x16** (singular); Cooling **Passive OAM** |
| https://instinct.docs.amd.com/projects/system-acceptance/en/latest/gpus/mi250.html | 200 | Dual GCD per OAM; PCI **1002:740c**; 4-OAM node **8** `lspci` entries (**2 per OAM**); pass: Gen4 x16. MI250X shares the same device ID. |
| https://rocm.docs.amd.com/en/latest/conceptual/gpu-arch/mi250.html | **404** this run | Indexed copy stated: *“Each GCD maintains its own PCIe x16 link to the host”* and some platforms offer **x8**. Treat as **Inferred pending a 200 fetch**; system-acceptance 200 page already shows **two endpoints per OAM**. |
| https://www.servethehome.com/amd-mi250x-and-toplogies-explained-at-hc34-hpe-gigabyte-supermicro/ | 200 | Dual GPU dies on one OAM; 400 GB/s on-package; PCIe switch topologies in OEM nodes |

**NDA / still missing (do not guess TEST\* straps):**

- TEST0–TEST14, TEST_MODE# function and required pull
- Which v1.0 `S1_*`…`S7_*` SerDes are xGMI vs unused
- SMBus slave addresses / PMBus map (do not invent 0x50)
- Exact mapping of two GCD x16 (or x8) links onto v1.0 `PCIE_TX/RX[15:0]`
- PE_BIF[1:0] default for MI250X
- Whether P12V2 must be live on this 48 V module
- Die / TIM / bolster ICD for a heatsink

No leaked public pin extras beyond OCP generic v1.0 were found.

---

## 4. PCIe to X11DPH-T Gen3

| Item | Label |
|---|---|
| X11DPH-T: **3× PCIe 3.0 x16 + 4× PCIe 3.0 x8** | Verified (manual PDF HTTP 200 from bargainhardware.co.uk, 226 pages, saved) |
| MI250X: PCIe **4.0**; will **downtrain** to Gen3 | Verified datasheet + PCIe spec behavior |
| Dual-GCD: **two** `1002:740c` endpoints per OAM | Verified system-acceptance HTML |
| SuperMicro shipping cable **CBL-MCIO-1278S5FYB1**: 4× MCIO-124p to 2× SlimSAS x8, “for MI-200” | Verified product page HTTP 200 https://www.wiredzone.com/shop/product/10026107-supermicro-cbl-mcio-1278s5fyb1-cable-kit-for-gpu-mi-200-11129 |
| That cable is UBB↔EPYC Gen4, **not** a CEM card for X11DPH-T | Inferred |
| Commercial CEM x16 ↔ dual SlimSAS 8i **products exist**: TI **CEM2SLIMSAS-EVM** (HTTP 200), ICY DOCK **MB308A** (HTTP 200), **SLM-1773-8I** (HTTP 200). Pinout **SFF-9402** storage. | Verified as products; **not** verified as OAM host PE |
| TI **DS160PT801** Gen4 8-lane retimer (HTTP 200 product page) | Verified as a chip that exists; **not** a closed BOM for this carrier |

If each GCD wants x16, **two OAMs imply four x16 endpoints** and X11DPH-T has **three** x16 slots. ROCm text (404 this run) mentioned some platforms use **x8 per GCD**. Topology **not closed**. Do not buy a random PCIe switch as “the” solution.

v1.0 names `PCIE_TXn` / `PCIE_RXn` + `PE_REFCLKP/N` + `PERST#`. Mapping those onto CEM pins is still **not invented** here.

---

## 5. Cooling

| Item | Label |
|---|---|
| MI250X **500 W / 560 W** TDP; Passive OAM | Verified AMD datasheet / product page |
| OCP v1.5 air note ~**450 W** on a shadowed 8× tray | Verified OAM spec (already in-repo mechanical notes) |
| SuperMicro kit PNs: **MCP-310-45802-0B** GPU air **shroud** for MI250; **MCP-240-45801-0N** stiffener; **MCP-240-45809-0N** sheet-metal tray | Verified as **chassis** parts in MNL-2507 extracted text — **not** a die-mating HS |
| **SNK-P0063P** in the same manual | CPU SP3 heatsink, **not** GPU |
| HPE spare air HS that mates the OAM bolster | **Unknown** — no public PN retrieved |
| OEM air HS height | **Unknown** |

**Do not** DIY a die clamp / custom cold plate. Chassis must leave **replaceable** cooling.

---

## 6. 8-GPU / UBB mechanical

| Item | Label |
|---|---|
| OCP **UBB Design Spec v1.5** board **417 mm × 585 mm × 3.2 mm**, 8 OAMs, 16 Mirror Mezz Pro | Verified (`retrieved_text/OCP_UBB_v1.5_extracted.txt`) |
| OAM module **102 × 165 mm**; connector-to-connector pitch **102 mm** | Verified OAM v1.5 §6.1 |
| Module-to-module numeric pitch on the UBB | In **figures** (not OCR’d to millimetres this run) |
| 4×2 tiling of 103×166 mm KOZ = **412 × 332 mm** | **Inferred** — **not** a UBB drawing |
| OCP UBB **r2.0** **417 × 655 mm** | Verified r2.0 — **wrong generation**; r2.0 pinlists UNUSABLE |
| Public UBB schematic/gerber/pin overlay | **Not found** |

First PCB in this tree is **2-OAM** (246 × 206 mm planning outline). The 417×585 mm rectangle is on **Dwgs.User** as later chassis volume only.

---

## 7. Host DRAM QVL (Memory Mode)

**Locked PMem:** 8× Dell **SNPHVY68C/128G** (eBay product page HTTP 200).

**DRAM SKU pick (this run):** SuperMicro **MEM-DR432L-SL01-ER29** = Samsung **M393A4K40CB2-CVF**, 32 GB DDR4-2933 **2Rx4 ECC RDIMM**, listed on the SuperMicro store page as validated for **MBD-X11DPH-T**.

- Direct curl of https://store.supermicro.com/us_en/32gb-ddr4-2933-mem-dr432l-sl01-er29.html → **HTTP 403** from this cloud.
- The same URL’s public HTML was retrieved via the research search pipeline (Validated Motherboards includes `MBD-X11DPH-T`). Label: **Verified via search-pipeline page**, not a 200 curl of store.supermicro.com.

**Memory Mode population (do not ignore):**

X11 user manual + `X11_memory_config_guide.pdf` (supermicro.com **403**; text via pipeline; 226-page user manual PDF **200** from bargainhardware):

- Only 2nd Gen Xeon (82xx/62xx/…) supports DCPMM. Gold **6230** is that generation.
- MM ratio DRAM:PMem generally **1:4 to 1:16**.
- **DRAM2** for MM 2-1-1 on 16-slot boards is **RDIMM only** (not LRDIMM). 32 GB 2Rx4 is in the DCPMM validation matrix.
- SuperMicro **16-slot** MM tables illustrate **2 DCPMM per socket** (4 PMem in the node), not 8. 8× 128 GB is the user’s locked capacity; it is **not** the illustrated 16-slot MM row. Rearrangements are allowed if they stay Intel/X11-legal — that **8-PMem map is not extracted as a locked table here**.

Practical buy: **8× MEM-DR432L-SL01-ER29** as cache DIMMs (256 GB DRAM vs 1024 GB PMem = **1:4**, at the MM ratio limit) **plus** follow SuperMicro slot silk when the board is in hand. If Memory Mode refuses 8 PMem, fall back to the illustrated **4 PMem + 8 or 12 RDIMM** map — extra PMem sit unused (bucket B/C, not a reason to skip DRAM).

Do not buy 8× PMem and **zero** DRAM.

---

## Fetch failures called out

| URL | Code |
|---|---|
| supermicro.com MNL-2507 PDF, X11 memory guide PDF, store DRAM page, product X11DPH-T | 403 |
| uk.farnell.com product HTML | 403 |
| opencompute.org wiki / several spec PDFs | 403 (text still recovered via pipeline) |
| noctua.at NH-U14S DX-3647 | 429 |
| molex.com part-detail 2189101115 | curl fail (000) |
| rocm.docs.amd.com `/en/latest/conceptual/gpu-arch/mi250.html` | 404 |
| RS UK 733-2032 RCP-2000-48 (previous PR) | 404 previously |

Saved binaries and HTML: `docs/downloads/`. Pipeline text: `docs/retrieved_text/`.
