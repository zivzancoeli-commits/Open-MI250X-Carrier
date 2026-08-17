# Exhaustive public-source hunt — remaining MI250X OAM carrier blockers

**Tree:** `Generated_Project/Rev2_MI250X_Carrier_ExhaustiveSourceHunt_v1/`  
**Date:** 2026-08-17  
**Does not overwrite** production Rev2 or `16_KiCad_Design/`.

This copied tree is **research only**. It is **not** a PCBWay package and **not** permission to energize OAMs.

| File | What it is |
|---|---|
| `FINDINGS.md` | Each hunt bucket Closed vs Exhausted, citations, which source won (count + trust) |
| `URL_LOG.md` | Every fetch HTTP status this run |
| `docs/downloads/` | Public PDFs/HTML actually retrieved (see license note in FINDINGS) |
| `docs/retrieved_text/` | Text extracts of OCP v1.5 OAM/UBB (already in-repo) plus new AMD/Molex extracts |
| `tools/fetch_urls.py` | Logger used for this hunt |

**Can they PCBWay?** **No.** Voltage+overlay+UBB-pitch gates are not closed. See FINDINGS bottom line.
