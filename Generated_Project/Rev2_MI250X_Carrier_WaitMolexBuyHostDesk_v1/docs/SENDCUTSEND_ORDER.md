# SendCutSend order — chassis sheet only

**Vendor:** https://sendcutsend.com/  
**Upload:** DXF, 1:1, millimetres. Files: `cad/dxf/*.dxf` (regenerate with `python3 cad/generate_sendcutsend_dxf.py`).  
**Material (all seven parts):** **A1008 mild steel 0.059"** (1.50 mm) — SendCutSend stock nearest **16 ga**. Page: https://sendcutsend.com/materials/mild-steel/ (retrieved this run). 18 ga nearest stock is **0.048"**.

**Services:** laser cut. Optional: deburr. Optional: **M4 PEM nuts** on the 4.5 mm flange holes (app auto-resizes). Hardware page: https://sendcutsend.com/services/hardware/ (retrieved this run). Metric nuts in the public catalog write-up: **M3, M4, M5, M6 — not M3.5**.

**Limits (Verified, same hardware page):** min part 1" × 1.5"; max **36" × 46"**; laser hole ≥ 50% of thickness. These DXFs fit.

**Tolerance:** ±0.005" (vendor mild-steel page).

**Orientation:** every part has a **6 × 6 mm** square notch at **(0,0)** (lower-left). That is a chassis fiducial, not an OAM feature.

---

## Cart

| File | Qty | Outer (mm) | What it is | Do not |
|---|---|---|---|---|
| `01_host_tray_x11dph_t.dxf` | 1 | 360.2 × 334.8 | Tray for X11DPH-T **330.2 × 304.8 mm** (Verified SuperMicro) + 15 mm margin | Motherboard standoffs (Unknown extra E-ATX holes; ATX Figure 3 mm not extracted) |
| `02_desk_tray_matx_class.dxf` | 1 | 280 × 280 | Desk mATX-class tray. 244 × 244 mm is **Inferred** typical microATX | Assume ASUS PRIME B550M-A AC hole map |
| `03_compute_tray_2oam.dxf` | 1 | 286 × 246 | Plate under 2-OAM planning carrier (246 × 206) / 2× KOZ **206 × 166** (Verified tiling) | OAM M3.5 NPTH, Molex pads, 8-GPU grid |
| `04_divider_12v_48v.dxf` | 1 | 500 × 450 | Divider; **trim** after bay height known | Share 12 V and P48V |
| `05_skin_compute_front.dxf` | 1 | 520 × 500 | Compute front skin | Fan holes (HS height Unknown) |
| `06_skin_compute_top.dxf` | 1 | 520 × 470 | Compute top (or bottom) skin | Weld as a cold plate |
| `07_skin_host_rear.dxf` | 1 | 420 × 500 | Host rear skin | ATX 6.25" × 1.75" I/O (X11DPH-T is server I/O; cut after tracing the shield) |

Flange holes: **4.5 mm**, 15 mm from edges, plus mid-side holes on parts ≥ 300 mm. Hole XY: `cad/MANIFEST.json`.

Powder coat is optional (mild steel rusts). If coating, do it **after** you confirm I/O/fan recuts, or leave skins raw and paint locally after trim.

---

## Not in this cart (buy elsewhere)

| Item | Why |
|---|---|
| Mild-steel **square tube** | SendCutSend is sheet. Cut-list still in `Generated_Project/Rev2_MI250X_Carrier_FullSendResearch_v1/docs/CHASSIS_CUT_LIST.md` (Inferred lengths; height TBD). |
| M3.5 OAM screws | OCP §6.7.2. Mixed 8–16 mm assortment. **Not** SCS PEM. |
| φ3 mm alignment pins | OCP PEM **TPS-3mm-8** or equivalent — different PEM family than SCS M3 nuts. |
| PCB | **Do not send KiCad to PCBWay.** |

---

## After the parts arrive

1. Weld the tube frame. Do **not** freeze height under 300 mm until GPU HS is measured (U14S is **165 mm** Verified; GPU cooling height **Unknown**).
2. Bolt trays to tube with M4 / 6-32. Drill motherboard standoffs **on the bench** with the X11DPH-T and B550M in hand.
3. Keep the compute tray **empty of OAM holes**. The M3.5 pattern lives on the **carrier PCB** (blocked).
4. Divider stays between desk/host **12 V** and future **48 V**. No P48V until Brian Park / PS-000.

**Do not energize OAMs. These parts are not a carrier.**
