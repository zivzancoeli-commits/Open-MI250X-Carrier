# OAM v1.x pin-map research (2026-08-16)

This folder is **research only**. It does not modify production KiCad.

- `REPORT.md` — structured findings (Verified / Inferred / Unknown).
- `OAM Pin map rev 1.0.xlsx` — OCP v1.0 pad map retrieved 2026-08-21 from Wayback (`if_` of the 20220421131015 files.opencompute.org snapshot). Same SHA-256 as `downloads/OAM_Pin_map_rev_1.0.xlsx`.
- `downloads/` — files actually retrieved this run.
- `extracted/` — CSV extracted from the v1.0 OCP spreadsheets. Do not treat CSV as a new invention; it is a machine dump of the xlsx.

**Do not import r2.0 pinlists.** MI250X is OAM v1.x (688 contacts). The retrieved v1.0 map has **2× P3V3** on Conn0, matching OAM Design Spec v1.5 Table 4.

A 2-OAM named-net stub (not fab-ready) that consumes this map lives in `Generated_Project/Rev2_MI250X_Carrier_BuyableFirstSystem_v1/`. Shopping list: `20_System_BOM/SHOPPING.md`.
