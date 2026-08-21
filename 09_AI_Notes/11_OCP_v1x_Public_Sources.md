# OCP v1.x public sources (2026-08-21)

Short retrieval note for the System Architecture phase. No electrical design, no KiCad, no r2.0 pin maps.

Evidence labels: **Verified** = file or quote from a retrieved public source this pass (or a cited prior retrieval). **Unknown** = not obtained.

## Files placed this pass

| File | Location | Source URL that returned the real binary | Label |
|---|---|---|---|
| `OAM_0p90_ME.zip` (~16.9 MB; 3D/DXF/HARDWARE dated 2019-03/04, filenames `*_0p90.*`) | `01_OAM_Spec/` | Wayback `id_` `https://web.archive.org/web/20220421131019id_/http://files.opencompute.org/oc/public.php?service=files&t=938c61e5b1d3c5c2b5c33f95525b1412&download&path=//OAM_0p90_ME.zip` (HTTP 200, `application/zip`) | Verified |
| `OAM Pin map rev 1.0.xlsx` (`dcterms:modified` 2019-08-01T06:53:57Z) | `22_Pinmap_Research/` | Wayback `if_` (same capture as the requested `id_` URL) `https://web.archive.org/web/20220421131015if_/http://files.opencompute.org/oc/public.php?service=files&t=938c61e5b1d3c5c2b5c33f95525b1412&download&path=//OAM%20Pin%20map%20rev%201.0.xlsx` (HTTP 200, xlsx). First `id_` try was HTTP 429 HTML, not the spreadsheet. | Verified |
| `Farnell_Molex_2189101115_product_spec.pdf` (2 pages, generated 01/05/2023) | `13_Reference_Docs/Molex/` | `https://www.farnell.com/datasheets/3919676.pdf` (HTTP 200, `application/pdf`) | Verified |

Do not use OAM r2.0 pin maps or CAD. MI250X is v1.x (688 contacts). The retrieved pin map has **P3V3 on Conn0 C1 and C2 only** (two pads), matching OAM Design Spec v1.5 Table 4 **P3V3 = 2**. r2.0 Table 4 **P3V3 = 6** is a different generation.

## Pin map vs v1.5 text

- **Verified:** OAM Design Spec v1.5 §8.3 still only says the detailed pin mapping is in a “separated spreadsheet”; Table 4 is counts/descriptions, not pad IDs. Source: retrieved v1.5 text already in-repo (`Generated_Project/Rev2_MI250X_Carrier_FullSendResearch_v1/docs/retrieved_text/OCP_OAM_v1.5_extracted.txt`) quoting §8.3: “The detailed pin mapping to connectors is in the separated spreadsheet.”
- **Verified:** the last named pinmap in that changelog is `OAM_Pin_map_rev1.0` / `OAM Pin map rev 1.0` (2019). The spreadsheet retrieved this pass is last-saved **2019-08-01**. No later public spreadsheet revision after 2019-08-01 was retrieved.
- **Do not mark** the OAM connector pinout as fully verified for an MI250X overlay. TEST / RFU / DO_NOT_USE, PE_BIF, and xGMI on S1–S7 remain **NDA / Unknown**. The OCP generic v1.0 map is not an AMD GPIO/function overlay.

## Wiki / 3D / Molex still missing

- **Verified:** live OCP wiki v1.5 rows are PDF-only from this environment (live `opencompute.org` document URLs returned Cloudflare HTTP 403 HTML, not PDFs). STP/xlsx linked on that page for later rows are **r2.0** — do not use them for MI250X.
- **Unknown:** a formal **v1.5 3D zip** was not found as a public contribution this pass. The file that landed is `OAM_0p90_ME.zip` (v1.x mechanical package, 2019). groups.io “V1.5 Zipfile” is membership-gated.
- **Unknown:** Molex **2189101115-SD** sheet 2 land pattern and **2189100001-PS-000** reflow/thickness were **not** retrieved from molex.com this pass.

## Downloads that did not land (Unknown)

Live `files.opencompute.org` is Cloudflare 403; Wayback `id_` was preferred. These URLs were tried and did **not** yield the named PDF binary (HTTP 403/429/503 HTML):

- OAM Design Spec v1.5 (2022-02-23) PDF:
  - `https://www.opencompute.org/documents/ocp-accelerator-module-design-specification-v1p5-final-20220223-docx-1-pdf` (live 403)
  - `https://web.archive.org/web/20220527050804id_/https://www.opencompute.org/documents/ocp-accelerator-module-design-specification-v1p5-final-20220223-docx-1-pdf` (429)
  - `https://web.archive.org/web/20230920160600id_/https://www.opencompute.org/documents/ocp-accelerator-module-design-specification-v1p5-final-20220223-docx-1-pdf` (429)
  - `https://web.archive.org/web/20231221220028id_/https://www.opencompute.org/documents/ocp-accelerator-module-design-specification-v1p5-final-20220223-docx-1-pdf` (429)
  - matching `if_` URLs for 20220527050804, 20230920160600, 20260629091946 (429 or 503)
- UBB Design Spec v1.5 (2022-02-23) PDF:
  - `https://www.opencompute.org/documents/universal-baseboard-design-specification-v1p5-final-20220223-docx-pdf` (live 403)
  - `https://web.archive.org/web/20220603180932id_/https://www.opencompute.org/documents/universal-baseboard-design-specification-v1p5-final-20220223-docx-pdf` (503)
  - `https://web.archive.org/web/20220603180932if_/https://www.opencompute.org/documents/universal-baseboard-design-specification-v1p5-final-20220223-docx-pdf` (HTTP 200 PDF, **6.9 MB, 8 pages**, Producer `Skia/PDF m101 Google Docs Renderer`, Title `Universal Baseboard Design Specification__v1p5_Final_20220223.docx`). This is **not** a complete specification; it was **not** copied into `01_OAM_Spec/`.
  - `https://web.archive.org/web/20240203221943id_/https://www.opencompute.org/documents/universal-baseboard-design-specification-v1p5-final-20220223-docx-pdf` (429)
  - `https://web.archive.org/web/20220606072508id_/https://www.opencompute.org/documents/universal-baseboard-design-specification-v1p5-final-20220223-docx-pdf` (429)
  - `https://web.archive.org/web/20240716185725id_/https://www.opencompute.org/documents/universal-baseboard-design-specification-v1p5-final-20220223-docx-pdf` (429)
  - matching `if_` URLs for 20221004154423 and 20240716185725 (503 HTML “Temporarily Offline”)

CDX (Verified as archived, complete PDF binary not saved here): OAM v1.5 snapshots exist (`application/pdf`, ~3.9 MB, e.g. 20220527050804); UBB v1.5 snapshots exist (`application/pdf`, ~6.5 MB and ~0.97 MB, e.g. 20220603180932 / 20240203221943 / 20221004154423). The ~6.5 MB class matches the 8-page Google Docs renderer.

`13_Reference_Docs/OCP_OAM/ocp accelerator module design specification_v1p5_Final_20220223.docx (1) (1).pdf` is the same class of **Google Docs renderer, 8 pages**. It was **not** copied into `01_OAM_Spec/` as the OAM v1.5 spec.

Wanted_Documents: Mechanical Specification and Connector Specification are checked from `OAM_0p90_ME.zip` and the Farnell 2189101115 sheet. Baseboard Specification stays unchecked because a complete UBB v1.5 PDF did not land. Heatsink photo stays unchecked.

## Out of scope

- No PCBWay submission.
- No live power / no energizing hardware.
- No r2.0 pinlist, STP, or CAD import.
