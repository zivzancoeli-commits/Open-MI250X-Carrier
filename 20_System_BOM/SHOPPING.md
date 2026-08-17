# SHOPPING.md — first system buy pack (2026-08-17)

**Honest bottom line:** you can buy a host and a desk PC **this week** and they will run. You **cannot** buy this list and have 2× MI250X (256 GB HBM) working tomorrow. The carrier in `Generated_Project/Rev2_MI250X_Carrier_BuyableFirstSystem_v1/` maps the OCP **generic v1.0** 688-contact names. It is **not fab-ready** and **must not be energized**.

URL check this run (HEAD/GET from the cloud agent). A 403/429/405 often means bot-block, not a dead product. **404 is called out.** Prices are **listing snapshots / cost bands**, not quotes. Surplus listings vanish; re-check before paying.

Locked first system (do not pivot):

- Welded dual-chamber chassis (desk + compute)
- Compute: 2× AMD Instinct **MI250X OAM** (later 8×). Not MI210.
- Host: SuperMicro **X11DPH-T**, 2× **Gold 6230 (SRF8W)**, ~1 TB via **Dell SNPHVY68C/128G** Optane PMem 100 **Memory Mode**
- Cooler: **NH-U14S DX-3647** (not DX-4189)
- Desk: **B550M + Ryzen 5 5500**; optional **RX 470**
- Dell **D3000E-S1** 3 kW is **12 V CRPS**, not 48 V GPU power

---

## A. Buy now — host + desk (will POST)

These do not depend on the carrier being finished.

| Qty | Item | PN / notes | Why | Buy link (this run) | Cost band | Evidence |
|---|---|---|---|---|---|---|
| 1 | Host motherboard | SuperMicro **MBD-X11DPH-T** (X11DPH-T). E-ATX 330.2×304.8 mm. 3× Gen3 x16 + 4× Gen3 x8. Optane PMem Memory Mode up to 2 TB (Cascade Lake). BIOS ≥ 3.0a for 2nd-gen Xeon. | Locked host | SuperMicro product: https://www.supermicro.com/en/products/motherboard/X11DPH-T *(HTTP 403 here)* · Newegg: https://www.newegg.com/supermicro-mbd-x11dph-t-o-2nd-generation-intel-xeon-scalable-processors-intel-xeon-scalable-proces/p/1B4-005W-001B0 *(HTTP 200)* | Used/new **~$300–1200** (used-market chatter; RefurbTech listed £818 — not re-fetched as 200) | SuperMicro + Newegg |
| 2 | CPU | Intel Xeon **Gold 6230**, sSpec **SRF8W**, 20C/40T, **125 W**, LGA3647. **Not** 6258R (older BOM). | Locked SKU; inside typical X11DPH-T TDP class | https://www.servermonkey.com/intel-xeon-gold-6230-processor-2-1-ghz-20c-27-5mb-cache.html *(HTTP 403 here; search snippet showed ~$150)* · search `SRF8W` on eBay | **~$120–250 each** used | ServerMonkey / Intel sSpec |
| 8 | PMem | **Dell SNPHVY68C/128G** (AA664973) 128 GB Optane PMem 100, DDR4-2666. 8× = 1 TB. | Locked Memory Mode capacity | eBay UK product: https://www.ebay.co.uk/p/24064262136 *(HTTP 200; listings ~£100–240)* · Techbuyer URL **HTTP 404 this run** · Provantage / ServerOrbit pages 403 here | **~$100–250 each** surplus | Dell PN + eBay |
| 8 | DRAM cache | **SKU not locked.** Memory Mode **requires DRAM as cache**. Typical 1 DRAM + 1 PMem per channel on 16-DIMM 8-channel boards. | Required companion | SuperMicro X11DPH-T memory QVL — pick a cheap **DDR4-2666 ECC RDIMM** 16 GB or 32 GB that is on the QVL. Do not mix random LRDIMM. | **Unknown** until QVL pick | Intel Memory Mode + 16 DIMM slots |
| 2 | CPU cooler | Noctua **NH-U14S DX-3647** only. Dual-socket **fit Unknown** (CPU pitch not measured). | Locked cooler | Official: https://noctua.at/en/nh-u14s-dx-3647 *(HTTP 429 here)* · Amazon UK ASIN B07DPR7TTD *(HTTP 503 here)* · Newegg `3C6-00VU-00239` *(challenge page)* | Often **OOS**; historically premium-cooler band. **Do not substitute DX-4189.** | Noctua |
| 1 | Host PSU | **Standard 24-pin ATX + 8-pin EPS** 80+ Gold, **750–1200 W**. X11DPH-T is an ATX-style server board. | Will POST. 2×125 W CPU + PMem + board | Any reputable ATX/EPS (Seasonic/Corsair/etc.). **Do not** wait on Dell CRPS breakout. | **~$100–250** | Board power connectors |
| 1 | Boot SSD | Not re-locked this pass. Older BOM: Samsung PM983 960 GB ×2 RAID1. Any NVMe/SATA that the board’s M.2/SATA will boot. | OS | Newegg / Amazon current SKU | **~$40–150** | Planning |
| 1 | Desk combo | **Ryzen 5 5500** (100-100000457BOX, no iGPU) + **B550M** (Newegg combo used ASUS PRIME B550M-A AC as example, not the only legal board) | Locked desk chamber | https://www.newegg.com/Product/ComboDealDetails?ItemList=Combo.4881708 *(HEAD 405; product path 200 on related Farnell-style URLs — re-open in a browser)* | CPU+board often **~$180–250** in combo ads | Newegg combo pages |
| 1 | Desk RAM | 16 GB DDR4-3200 kit if not in the combo | 5500 has no iGPU; board needs RAM | Included in some combos (Team/GeIL 2×8 GB) | **~$30–50** | |
| 1 | Desk PSU | 450–650 W ATX | Desk only | Commodity | **~$50–90** | |
| 0–1 | Optional GPU | **RX 470** used. 5500 has **no iGPU** — you need **either** RX 470 **or** another display GPU **or** a 5500GT/G-series (that would be a pivot; don’t). | Display for desk | eBay `RX 470` | Used **~$50–80** (search chatter; not a live itemized 200) | |
| 1 | Desk cooler | 5500 box Wraith is enough | 65 W | Included with boxed CPU | $0 | AMD boxed |
| lot | Chassis steel | Mild-steel **square tube** + **16–18 ga CRS** skins. Cut-list: `Generated_Project/Rev2_MI250X_Carrier_BuyableFirstSystem_v1/docs/CHASSIS_CUT_LIST.md` | Locked mechanical | Local steel supplier. **Do not** freeze height until GPU HS is measured. | **Unknown** (scrap/steel by the foot) | User process |
| lot | Weld/consumables | Wire, gas, grinding discs, primer | You weld | Local | **Unknown** | |

**Host BIOS:** 2nd-gen Xeon needs BIOS **3.0a+**. Cascade Lake-R would need 3.2+; 6230 is Cascade Lake (not -R). Enable **Memory Mode** in the Intel PMem menu; populate DRAM per SuperMicro QVL.

**Dell D3000E-S1:** you may buy it as a **12 V** brick collection, but **this week it does not replace the ATX/EPS PSU**. It needs a CRPS backplane/breakout that is **not designed here**. Listing that is live: https://www.itcreations.com/product/132053 *(HTTP 200; +12.2 V 245.9 A)*. Put extra units in **C** if you were stocking 8-GPU 12 V shelves.

---

## B. Buy for 2× MI250X — justified, with blockers

Buy these only if you accept they will **sit on a shelf** until Blockers.md gates close. **Do not apply 48 V. Do not mate an OAM to a random PCB.**

| Qty | Item | PN / notes | Why | Buy link | Cost band | Blocker |
|---|---|---|---|---|---|---|
| 2 | MI250X OAM | HPE **P41933-001** and/or AMD **100-D65201** / board **102-D65201-0B** (eBay listing). 128 GB HBM2e, 500 W / 560 W peak, OAM, PCIe 4.0 x16. | Locked compute | AMD: https://www.amd.com/en/products/accelerators/instinct/mi200/mi250x.html *(200)* · datasheet https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instinct-mi200-datasheet.pdf *(200)* · eBay CA item 306199683179 *(200; US $2,994.99 OBO, 1 sold — surplus, not a store)* · harddiskdirect P41933-001 *(403 here)* | **~$2k–4k each** surplus; **highly volatile** | Cooling, 48 V, carrier, overlay |
| 4 | OAM connector | Molex **218910-1115** / **2189101115**. 688 ckt, 15×11, **hermaphroditic**, mated **5.00 mm**, **mates with itself**. Carrier needs 4 (2 OAMs × 2). Modules already have connectors. | OCP v1.5 §5/§6.2 + Farnell | Datasheet https://www.farnell.com/datasheets/3919676.pdf *(200)* · product-style https://uk.farnell.com/molex/2189101115/connector-mezz-15pos-11row/dp/4145887 *(200)* · factory pack **150 / reel** — ask for **cut tape / each** | Broker pages showed **~$50/ea** (not an authorized quote). Reel is expensive. | 30 V datasheet vs 48 V OCP; BGA attach; PIN A3 overlay |
| 1 | 48 V source (candidate, not a finished path) | **MEAN WELL RCP-2000-48**: 48 V, 42 A, 2016 W, trim **42–56 V** (vendor spec PDF). In OCP 44–59.5 V window **if** set ≥ 44 V. | Real 48 V, not Dell 12 V | Spec PDF https://www.meanwell.com/Upload/PDF/RCP-2000/RCP-2000-SPEC.PDF *(200)* · series page https://www.meanwellaustralia.com.au/products/RCP-2000 *(200)* · RS UK 733-2032 **HTTP 404 this run** — search Mouser/Digi-Key `RCP-2000-48` in a browser | **~$400–700** class from distributor snippets (RS £525 was **404** here — treat as unverified) | Harness, sense, fusing, Molex 30 V issue, HOST_PWRGD sequencing |
| 0–1 | 48 V shelf (architecture, not 2-GPU BOM) | OCP **Open Rack v3** 48 V power shelf | Evidence that 48 V busbars exist | https://www.opencompute.org/documents/ocp-open-rack-v3-power-shelf-rev-1-0-1-pdf *(403 here)* | Whole rack: **do not buy for 2-GPU** | Overkill; 240 V/50 A class |
| lot | M3.5 hardware | OCP four **M3.5** screws / φ3.9 mm holes / 5 mm stack | Mechanical | McMaster/local: M3.5 × mixed lengths 8–16 mm + nuts | **~$20–40** | Screw length vs bolster Unknown |
| 4 | φ3 mm alignment pins | PEM **TPS-3mm-8** or equivalent (OCP §6.4.2) | KOZ alignment | PEM distributor | **Unknown $** | |
| 2–4 | 12 V PWM fans | Chassis airflow only | Front-to-rear intent | Noctua / Delta 120 or 140 mm after bay height known | **~$20–80** | Not a GPU HS |
| — | P12V1 / P3V3 | Up to 50 W @ 12 V and 5 W @ 3.3 V (OCP pin list) | Can come from **host ATX** once a harness exists | Do not buy extra VRMs | $0 extra if ATX exists | Sequencing Unknown |
| — | P12V2 | Required **for 12 V OAMs**. MI250X is 48 V class. | **Do not buy a guessed high-current 12 V GPU path** | — | — | AMD-unknown whether P12V2 must be live |
| — | PCIe CEM / retimer / switch | X11DPH-T Gen3 x16 slots ×2 could eventually take two adapters | **Path not closed** | **Do not buy** a PCIe switch or random MCIO cable as “the” solution | — | See Blockers |

**PVREF:** module **output**. Never buy a 1.8/2.5/3.3 V supply to “feed Vref.”

**Cables:** no verified OAM power cable PN. Do not invent a 12 V 8-pin GPU pigtail onto P48V.

---

## C. Do not buy yet

| Item | Why |
|---|---|
| 6 more MI250X (8-GPU) | Carrier, cooling, 48 V, and xGMI overlay are not done. Floor reserve is **Inferred 412×332 mm**, not a UBB. |
| OAM r2.0 connectors / r2.0 pinmap parts | **UNUSABLE** for MI250X (P3V3=6, different 48 V split). |
| Molex **218916-1115** | Different connector height; OCP 5 mm stack is **218910-1115**. |
| Guessed VRM / MP2975 / 12-to-48 boost | Invented. Forbidden as the GPU path. |
| PCIe switch / retimer BOM | Pinmap + X11DPH-T does not close SI or dual-GCD mapping. |
| 240 V / **50 A** service hardware | 2-GPU + dual 125 W Xeon is not an 8-OAM tray. Plan a normal **240 V 20 A** (or 120 V with honest load calc) later; don’t buy 50 A busway now. |
| Dell D3000E-S1 **as GPU power** | **12.2 V**. Host-only, and even then it needs a breakout you don’t have. |
| Three N+1 3 kW CRPS for 8-GPU 12 V | Old BOM; contradicts 48 V OAM. |
| Custom cold plate / DIY die clamp | NDA ICD missing. Replaceable cooling only. |
| DX-4189 coolers | Wrong socket generation. |
| Gold 6258R | Unlocked older BOM; you locked **6230**. |
| Donor AOM-MCM-Q as a *required* buy | Useful for reverse-mapping (PR #1 notes). Not required to **buy a host**. Optional research tool, not a 2-OAM run path. |

---

## Cost-band rollup (not a quote)

| Bucket | Band | Notes |
|---|---|---|
| A. Host + desk + steel (no GPUs) | **~$2k–5k** | Dominated by 8× PMem + board + 2× 6230 + steel. DRAM extra. |
| B. 2× MI250X surplus | **~$4k–8k** | One eBay ask was ~$3k **each**. |
| B. 4× Molex + 48 V PSU candidate | **~$0.6k–1.5k** | Connectors may only sell on reels. |
| Fab-ready carrier + cooling + harness | **Not for sale** — still blocked | |

---

## This week vs later

**This week (A):** X11DPH-T, 2× SRF8W, 8× SNPHVY68C/128G, DRAM cache per QVL, 2× DX-3647 if you can find them, ATX/EPS PSU, boot drive, B550M+5500 combo, desk PSU/RAM, optional RX 470, steel + M3.5 assortment, start welding **bays** (not OAM hole patterns).

**May buy, must not energize (B):** 2× MI250X, 4× 218910-1115, Mean Well 48 V **as a brick on the bench**, fans, alignment pins.

**Do not energize OAMs** until Blockers.md is empty enough that P48V, connector voltage, cooling, and overlay straps are actually closed.

**Do not send the KiCad in this PR to a fab.**
