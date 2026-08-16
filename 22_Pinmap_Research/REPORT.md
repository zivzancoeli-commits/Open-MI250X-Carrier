# Public research report: AMD Instinct MI250X / OAM v1.x 688-contact pin map

**Date:** 2026-08-16  
**Scope:** Find a real, citable signal-to-pad map for OAM **v1.x with 688 contacts**. Do not invent pins. Do not use OAM r2.0.

Evidence labels used below:

| Label | Meaning |
|---|---|
| **Verified** | Direct quote, download, or machine extraction from a retrieved file |
| **Inferred** | Reasonable reading of those sources, not a new pin assignment |
| **Unknown** | Not found in public sources this run |

No production KiCad was modified. No electrical recommendations are made from guessed pins.

---

## 1. Bottom line

**Yes — a complete OAM v1.x 688-contact signal-to-pad map was retrieved.**

| Question | Answer | Label |
|---|---|---|
| Complete pad→signal map for both 688-contact connectors? | **Yes.** `OAM Pin map rev 1.0.xlsx` sheet **OCP Generic Pin Map** names all **688 Conn0** pads and all **688 Conn1** pads (1376 named locations). | Verified |
| Is it labeled “MI250X”? | **No.** It is the OCP **generic** v1.0 map (authors Intel/Facebook; last saved 2019-08-01). | Verified |
| Is it the v1.5-named spreadsheet? | **Not retrieved under a v1.5 filename.** OAM Design Spec v1.5 §8.3 still says the pad map is a “separated spreadsheet” and Table 4 still lists **P3V3 = 2, Conn0**, which matches this v1.0 map. | Verified (counts) / Unknown (whether any pad moved after v1.0) |
| Usable as r2.0? | **No. r2.0 is UNUSABLE for MI250X.** | Verified |

This is an **OCP generic** map, not an AMD GPIO/function overlay. AMD-specific use of TEST/GPIO/RFU pads on MI250X remains **Unknown**.

---

## 2. Downloads actually retrieved this run

| File saved | Source URL retrieved | Date / revision in file | v1.x or r2.0 | What it contains |
|---|---|---|---|---|
| `downloads/OAM_Pin_map_list_Rev1.0.zip` | https://forum.level1techs.com/uploads/short-url/kNAw6L53BtjROq77PJd9fiBq3Jz.zip (post 95, user TsuKitsune, 2026-08-03; CDN `level1techs.us-east-1.linodeobjects.com/original/4X/9/1/c/91c6800bbce75629075bc57fdf0dd4970fef5b95.zip`) | Zip of the two v1.0 xlsx below | **v1.x (v1.0)** | Pin list + pin map |
| `downloads/OAM_Pin_map_rev_1.0.xlsx` | Extracted from that zip | `dcterms:modified` **2019-08-01T06:53:57Z**; lastModifiedBy Whitney Zhao; creator De La Mora Hernandez, Omar; Company Intel; sheet Rev History row **Rev 1** | **v1.x (v1.0)** | **Complete 688+688 pad map** |
| `downloads/OAM_Pin_list_Rev1.0.xlsx` | Extracted from that zip | `dcterms:modified` **2019-08-01T06:50:41Z**; Rev History **Rev 1** / Excel date 43671 (2019-07-25) | **v1.x (v1.0)** | Signal **counts/descriptions** (Table 4 family), not pad numbers |
| `downloads/Farnell_Molex_2189101115_datasheet.pdf` | https://www.farnell.com/datasheets/3919676.pdf | Generated 01/05/2023 | Geometry only | 688 circuits; **no OCP signal names** |
| `downloads/Molex_Mirror_Mezz_15x11_OCP_connectors.pdf` | https://www.content.molex.com/dxresources/b3b7/b3b7bc64-a2fc-4845-90bd-f1efb35a3ffb.pdf | Marketing | Geometry only | 15×11 OCP footprint; series 209311 / 218910 / 218916 |
| `downloads/OCP_OAI_Group_update_lightning_talk_2019-09-26.pdf` | https://146a55aca6f00848c565-a7635525d40ac1c70300198708936b4e.ssl.cf1.rackcdn.com/images/18a84b960d9b11bb2fbc9a4d59f09fc01086d9b7.pdf | 2019-09-26 | v1.0 package pointer | Spec share token `t=938c61e5b1d3c5c2b5c33f95525b1412`; **no pad table** |

SHA-256 of saved binaries: `extracted/SHA256SUMS.txt`.

### URLs fetched as HTML/text (not saved as the original binary)

OCP document pages and wiki are behind Cloudflare from this environment. Content was still recovered via the research fetch pipeline / search snippets:

| URL | Result | v1.x / r2.0 |
|---|---|---|
| https://www.opencompute.org/documents/ocp-accelerator-module-design-specification-v1p5-final-20220223-docx-1-pdf | Text of OAM Design Spec **v1.5** (2022-02-23). §8.3: *“The detailed pin mapping to connectors is in the separated spreadsheet.”* Table 4 is **counts**. Changelog still names `OAM_Pin_map_rev1.0` / `OAM_Pin_list_Rev1.0`. | v1.x |
| https://www.opencompute.org/documents/ocp-accelerator-module-design-specification-v1p1-1-pdf | v1.1 PDF; same “separated spreadsheet” language | v1.x |
| https://www.opencompute.org/documents/ocp-accelerator-module-design-specification-v1p0-3-pdf | v1.0 PDF | v1.x |
| https://www.opencompute.org/documents/oai-oam-base-specification-r2-0-v1-0-20230919-pdf | r2.0 v1.0 PDF names `OAI OAM_Pinlist_Pinmap_r2.0_v1.0.xlsx`; Table 4 **P3V3 = 6 Conn0** | **r2.0 UNUSABLE** |
| https://www.opencompute.org/documents/oai-oam-base-specification-r2-0-v0-75-2-pdf | r2.0 v0.75 names `OAM_Pinlist_Pinmap_r2.0_v0.75.xlsx`; **P3V3 = 6 Conn0** | **r2.0 UNUSABLE** |
| https://www.opencompute.org/wiki/Server/OAI | Package index (v0.85–v1.5, r2.0 “Pinlist Mechanical Drawing”) | index |
| https://github.com/opencomputeproject/OCP-SVR-OAI-Open_Accelerator_Infrastructure | Project page only; **no xlsx** | n/a |
| https://ocp-all.groups.io/g/OCP-OAI/attachment/5/0/ocp%20accelerator%20module%20design%20specification_v1p0_Candidate0725.pdf | v1.0 candidate PDF; pin mapping “will be provided in separated spreadsheet” | v1.x counts |
| https://ocp-all.groups.io/g/OCP-OAI/topic/ocp_oai_june_updates/83416097 | Public thread: OAM2.0 pin list “done”; members asking Whitney Zhao to **share** it (Nov 2021–Jul 2022) with **no public attachment** | r2.0 work, members-only |

### Internet Archive CDX hits (xlsx existed; live file fetch 503 this run)

These are **Verified as having been archived** (CDX: HTTP 200, `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`). Direct `web.archive.org` file download returned **503** during this run, so the IA copies were **not** saved here. The Level1Techs zip is the copy that was actually retrieved.

| Archived original | Snapshot examples | Size (CDX) |
|---|---|---|
| `http://files.opencompute.org/oc/public.php?service=files&t=938c61e5b1d3c5c2b5c33f95525b1412&download&path=//OAM Pin map rev 1.0.xlsx` | 20211205194306, 20220421131015 | ~221–227 KB |
| `http://files.opencompute.org/oc/public.php?service=files&t=938c61e5b1d3c5c2b5c33f95525b1412&download&path=//OAM_Pin list_Rev1.0.xlsx` | 20200924024102, 20211205195533, 20220421131010 | ~159 KB |
| `http://files.opencompute.org/oc/public.php?service=files&t=fb91baceba6c1dfaa9dc5531365b4f45&download&path=//oam_pin list_rev1.1.xlsx` | 20211205210451, 20221225104050 | ~160 KB |
| `http://files.opencompute.org/oc/public.php?service=files&t=a2fc3d6565098cbd15f9dd7abe52ef02&download&path=//OAM Pin list_Rev0.88.xlsx` | 20230201083822 | ~248 KB |
| `http://files.opencompute.org/oc/public.php?service=files&t=a2fc3d6565098cbd15f9dd7abe52ef02&download&path=//OAM Pin map rev 0.80.xlsx` | 20230201094028 | ~215 KB |
| `HIB_UBB_HD_Conn_Pin_Assignment_v1p0_20200217.xlsx` (same files.opencompute.org share) | 20211205205103 | ~93 KB — **HIB/UBB host connector, not OAM mezz** |

The 2019 lightning-talk token `938c61e5b1d3c5c2b5c33f95525b1412` is the v1.0 **spec package** that contained both v1.0 xlsx files.

---

## 3. If a pinlist exists: completeness and quoted rows

### 3.1 Pin map (pad assignments) — complete

**Verified.** File: `OAM Pin map rev 1.0.xlsx`, sheet `OCP Generic Pin Map`.

Grid: Molex-style columns **A, B, C, D, E, F, G, H, J, K, L** (no letter I) × rows **1–64** = **704** possible sites; **688** are named (the remainder are unused/blank in the sheet). Extraction in `extracted/OAM_v1.0_OCP_Generic_Pin_Map.csv`.

Title cell B1 (quote):

> OCP Compute Accelerator Mezzanine Connector Pin map  
> Top-down view of mezzanine module with ASIC/GPU mounted on top side & both connectors mounted on bottom side

Conn0 note in the sheet: `P48V, P12V, P3V3, PLVIO, PCIE, SERDES 1/2/3, MISC`.  
Conn1 note: `SERDES 4/5/6/7, MISC`.

**P3V3 count = 2 on Conn0 only** — matches OAM v1.5 Table 4 and **does not** match r2.0 (6× P3V3).

Example rows **from the xlsx grid** (not invented):

| Connector | Pad | Signal | Voltage (from pin list, same package) | Source |
|---|---|---|---|---|
| Conn0 | C1 | P3V3 | 3.3V | Pin map Rev 1.0 + Pin list Rev 1.0 row P3V3 |
| Conn0 | C2 | P3V3 | 3.3V | same |
| Conn0 | H59, K59, H60, K60, H61, J61, K61, L61, H62, J62, K62, L62, H63, J63, H64, J64 | P48V (16 pads) | 44V–59.5V | Pin map; pin list: 16 SE pins, Conn0 |
| Conn0 | G1, G2 | PVREF | Vref (pin list: 1.5V–3.3V range in Rev 1 notes) | Pin map + pin list |
| Conn0 | F45 | PE_REFCLKP | (diff pair with F46) | Pin map |
| Conn0 | F46 | PE_REFCLKN | | Pin map |
| Conn0 | D1 | PERST# | 3.3V | Pin map + pin list |
| Conn0 | H1 | HOST_PWRGD | 3.3V | Pin map |
| Conn0 | G3 | I2C_D | Vref | Pin map |
| Conn0 | G4 | I2C _CLK | Vref | Pin map (space in name as in file) |
| Conn0 | J3 | SMBus_SLV_CLK | 3.3V | Pin map |
| Conn0 | L3 | SMBus_SLV_D | 3.3V | Pin map |
| Conn0 | A3 | MANF_MODE# | 3.3V | Pin map (Molex SD “PIN A3” is geometry; this is the OCP name on pad A3) |
| Conn1 | F58 | DWN_PERST# | 3.3V | Pin map |

Conn0 power/ground counts from the map (Verified): GND 334, P12V2 27, P48V 16, P12V1 5, P3V3 2, PVREF 2.

### 3.2 Pin list spreadsheet — counts only

**Verified.** `OAM_Pin_list_Rev1.0.xlsx` sheet `Pin List` is the same class of table as OAM spec Table 4: **signal name, direction, description, voltage, required/optional, diff-pair count, SE pin count, Conn0 or Conn1**. It does **not** assign Molex pad IDs.

Quoted pin-list rows:

| Signal | Direction | Voltage | SE or diff count | Connector | Source |
|---|---|---|---|---|---|
| P48V | Power Input | 44V-59.5V | 16 SE | Conn0 | Pin list B4 |
| P3V3 | Power Input | 3.3V | 2 SE | Conn0 | Pin list B7 |
| PVREF | Power Output | Vref | 2 SE | Conn0 | Pin list B8 |
| PE_REFCLKp/n | Input | (blank in SE/voltage cols) | 1 diff pair | Conn0 | Pin list B25 |
| PERST# | Input | 3.3V | 1 SE | Conn0 | Pin list B29 |

Pin list also names Molex **209311-1115** / family **Mirror Mezz** (original 112G part), **not** 218910-1115. That is a **connector MPN in the v1.0 package**, not a second pin map.

### 3.3 OAM Design Spec v1.5 PDF — counts and figures, not pads

**Verified** from the v1.5 PDF text:

- §8.1: two **688-pin** Molex Mirror Mezz Pro connectors.
- §8.3: detailed mapping is in the **separated spreadsheet**; Table 4 is pin **counts**.
- Table 4: **P3V3 Required 2 Conn0**; **P48V Required 16 Conn0**.
- Figures 33/34 exist (mezzanine pin map / pin-out view). This run did **not** OCR those figures into pad names; the xlsx is the citable pad list.
- Changelog v1.0: *“Update OAM_Pin_map to rev1.0 … refer to OAM_Pin_map_rev1.0 spreadsheet”* and *“OAM_Pin_list_Rev1.0 spreadsheet”*.

**Unknown:** whether a later v1.1/v1.5 xlsx moved any pads. A file `oam_pin list_rev1.1.xlsx` is in IA CDX (~160 KB, similar size to the v1.0 **list**, i.e. likely still counts-only). No v1.5-named pin **map** xlsx appeared in CDX this run.

### 3.4 Gaps explicitly not filled

- AMD MI250X-specific meaning of TEST0–TEST14, RFU, DO_NOT_USE, GPIO, dual-GCD lane mapping to PET/PER vs xGMI: **Unknown**.
- v1.5-only pad deltas vs this v1.0 map: **Unknown** (counts for P3V3/P48V still match).
- Physical Molex BGA ball vs OCP column letter: the spreadsheet uses OCP column letters A–L skipping I, which is the same lettering family as Mirror Mezz “PIN A3”. A Molex SD was **not** successfully downloaded this run (HTTP/2 error from molex.com).

---

## 4. r2.0 files found — UNUSABLE for MI250X

| Artifact | Why UNUSABLE |
|---|---|
| OAI-OAM Base Spec r2.0 v1.0 PDF (2023-09-19) + named `OAI OAM_Pinlist_Pinmap_r2.0_v1.0.xlsx` | Different power split (P48V on Conn0 **and** Conn1); **P3V3 = 6** vs v1.5/v1.0 **P3V3 = 2** |
| OAI-OAM Base Spec r2.0 v0.75 PDF + `OAM_Pinlist_Pinmap_r2.0_v0.75.xlsx` | Same class of r2.0 changes; **P3V3 = 6 Conn0** |
| Wiki rows “OAI-OAM r2.0 … Pinlist Mechanical Drawing” (2023-09-14) | r2.0 package |
| Groups.io 2021-06 Whitney Zhao: “OAM2.0 pin list and pin map : done” | That work is **OAM 2.0 / r2.0**, not MI250X v1.x |
| AMD MI300 Series Cluster Reference Architecture (public) | Describes **UBB 2.0 / MI300** — different generation |

The r2.0 xlsx files were **not** downloaded (and must not be imported into the MI250X carrier).

---

## 5. How to obtain files still missing

| Missing file | How to get it | Access |
|---|---|---|
| Same v1.0 xlsx from OCP (not forum) | Wayback CDX URLs above when archive.org is healthy; or OCP wiki package “OAM Design Spec Package v1.0” (token `938c61e5b1d3c5c2b5c33f95525b1412`) | Public if IA/OCP files CDN is up; OCP site itself often wants an account + Cloudflare |
| `oam_pin list_rev1.1.xlsx` | IA CDX token `fb91baceba6c1dfaa9dc5531365b4f45`; OCP “Design Spec Package v1.1” (2020-07-22) | Public archive / OCP account |
| Any v1.5-named pin **map** xlsx | OCP contribution “OAM Design Specification v1.5” (2022-02-23) package on https://www.opencompute.org/wiki/Server/OAI | Typically **OCP login**; may be in the zip next to the PDF |
| OAM r2.0 pinlist (do not use for MI250X) | Wiki “OAI-OAM Base Specification r2.0 v1.0 Pinlist Mechanical Drawing” | OCP account |
| AMD Instinct MI250X OAM hardware integration / baseboard pin overlay | AMD product / OEM NDA portal | **NDA** — not in public Instinct system-acceptance docs |
| Groups.io OCP-OAI attachments beyond the public candidate PDF | https://ocp-all.groups.io/g/OCP-OAI — join OCP-OAI | **OCP membership / group join**; 2021 thread shows even members had to **ask** for OAM2.0 maps |

Practical path already sufficient for an OCP-generic v1.x carrier netlist: the **v1.0 pin map xlsx in `downloads/`**. Confirm against v1.1 list / v1.5 package if OCP account access is available; do not assume r2.0.

---

## 6. Donor hardware path (public teardown / continuity)

| Source | What is public | Pad map? |
|---|---|---|
| Level1Techs thread https://forum.level1techs.com/t/someone-needs-to-figure-out-how-to-adapt-mi250-gpus-to-pcie/250596 | Working discussion of Supermicro **AOM-MCM-Q**, HPE/Cray MI250X, SEQ_FAULT, P12V2/P48V **board** connectors, EEPROM at 0x50. **Post 95 is the v1.0 zip.** Post 96: JTAG0/TEST pullups to VREF on AOM-MCM-Q — **signal names, not pad numbers**. | No public continuity table of UBB pads |
| Supermicro MNL-2507 / H12 Universal GPU datasheet | AOM-MCM-Q-P is the MI250 UBB; cable/power PNs; **no OAM mezz pinout** | No |
| eBay AOM-MCM-Q listings | Photos of a 4-OAM UBB | Photos ≠ pad map |
| HPE Cray EX235a / Frontier | Architecture in AMD Instinct docs (xGMI mesh, dual GCD) | No connector pad map |
| Molex 218910-1115 / 2189101115-SD | Farnell sheet: 688 circuits, 15 pair × 11 row, PIN A3 on SD (not retrieved as PDF this run) | Geometry only |
| NVIDIA SXM2 teardowns | Irrelevant form factor | n/a |

**Verified:** no public UBB continuity spreadsheet mapping Molex pads to nets was found. A donor AOM-MCM-Q (or other v1.x UBB) plus the v1.0 OCP map is the documented community path; unpowered clustering of shorted pads is **not** a substitute for lane/clock/reset assignment (as already noted in-repo).

---

## 7. Other sources searched (negative or limited)

| Source | Result |
|---|---|
| GitHub `opencomputeproject/OCP-SVR-OAI-Open_Accelerator_Infrastructure` | Project README only |
| GitHub code search `OAM_Pin_list_Rev1.0` / `OAI-OAM_Pinlist_Pinmap` | Rate-limited / no public repo dump of the xlsx |
| AMD instinct.docs / MI250X product page | OAM form factor, PCIe 4.0 x16, Infinity Fabric; **no connector pin table** |
| OEM (HPE, Lenovo, Dell, Penguin, Supermicro manuals) | System/UBB presence; **no 688-pad map** |
| IEEE / random PDFs embedding Table 33/34 pad grids | Not found |
| Scribd copies of OAM PDFs | Same PDFs as OCP; still counts + “separated spreadsheet” |

---

## 8. What this does *not* authorize

- Do not treat this map as AMD-signed MI250X GPIO documentation.
- Do not mix r2.0 pad assignments with this grid.
- Do not invent nets for `RFU` / `DO_NOT_USE` / `TEST*`.
- Do not modify production KiCad from this research commit beyond storing the files.

Extraction CSVs are a convenience dump of the official v1.0 xlsx. If they ever disagree with the xlsx, **the xlsx wins**.
