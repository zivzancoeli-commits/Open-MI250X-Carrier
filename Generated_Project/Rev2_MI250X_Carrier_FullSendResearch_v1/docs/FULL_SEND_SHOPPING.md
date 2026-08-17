# FULL_SEND_SHOPPING.md — one cart, three buckets (2026-08-17)

**Honest bottom line:** you can put **host + desk + 2× MI250X + Molex + a 48 V brick** in **one order**. That is a **shopping** decision. It does **not** make 256 GB HBM work, and it does **not** make this KiCad PCBWay-ready.

**Do not send this board to PCBWay. Do not energize OAMs.**

URL check this run: see `URL_FETCH_LOG.txt`. **404/403/429/000** are called out. Prices are **bands**, not quotes.

Locked system (do not pivot): dual-chamber welded chassis; 2× **MI250X OAM** now (later 8×, not MI210); SuperMicro **X11DPH-T**; 2× Gold **6230 SRF8W**; Optane PMem 100 **SNPHVY68C/128G** ×8 Memory Mode; cooler **NH-U14S DX-3647** (not 4189); desk **B550M + Ryzen 5 5500**; optional RX 470; Dell **D3000E-S1 is 12 V CRPS**, not GPU power.

---

## A. Must buy for host + desk (will work)

These POST as two computers without any OAM, carrier, or 48 V.

| Qty | Item | PN / notes | Buy link (this run) | Cost band | HTTP |
|---|---|---|---|---|---|
| 1 | Host board | SuperMicro **MBD-X11DPH-T** | https://www.newegg.com/supermicro-mbd-x11dph-t-o-2nd-generation-intel-xeon-scalable-processors-intel-xeon-scalable-proces/p/1B4-005W-001B0 | used/new ~$300–1200 | **200** (supermicro.com product **403**) |
| 2 | CPU | Xeon Gold **6230** sSpec **SRF8W**, 125 W, LGA3647 | search `SRF8W` / ServerMonkey (often 403 here) | ~$120–250 each used | re-check in browser |
| 8 | PMem | Dell **SNPHVY68C/128G** 128 GB Optane PMem 100 | https://www.ebay.co.uk/p/24064262136 | ~$100–250 each surplus | **200** |
| **8** | DRAM cache | **MEM-DR432L-SL01-ER29** / Samsung **M393A4K40CB2-CVF** 32 GB DDR4-2933 2Rx4 ECC RDIMM. SuperMicro store lists **MBD-X11DPH-T** as a validated motherboard. | https://store.supermicro.com/us_en/32gb-ddr4-2933-mem-dr432l-sl01-er29.html | 32 GB RDIMM used ~$30–80 each | store **403** here; SKU from search-pipeline page. **Required for Memory Mode.** |
| 2 | CPU cooler | Noctua **NH-U14S DX-3647** only | https://noctua.at/en/nh-u14s-dx-3647 | often OOS | **429** here |
| 1 | Host PSU | ATX 24-pin + EPS 8-pin, 750–1200 W 80+ Gold | any reputable ATX/EPS | ~$100–250 | — |
| 1 | Boot SSD | NVMe/SATA the board will boot | Newegg/Amazon current | ~$40–150 | — |
| 1 | Desk combo | Ryzen **5 5500** + **B550M** | Newegg combo pages (previous pack) | ~$180–250 | re-open in browser |
| 1 | Desk RAM | 16 GB DDR4-3200 if not in combo | — | ~$30–50 | — |
| 1 | Desk PSU | 450–650 W ATX | commodity | ~$50–90 | — |
| 0–1 | Optional GPU | **RX 470** used (5500 has no iGPU) | eBay `RX 470` | ~$50–80 | — |
| lot | Steel | square tube + 16–18 ga CRS; cut-list in PR #2 chassis doc | local | Unknown | — |
| lot | M3.5 hardware | mixed 8–16 mm + nuts (OAM later) | McMaster/local | ~$20–40 | — |

**BIOS:** 3.0a+ for 2nd-gen Xeon. Enable Memory Mode; populate DRAM per SuperMicro silk. See research report: illustrated 16-slot MM tables show **4** DCPMM, not 8 — 8× PMem is locked capacity, not a verified slot map.

**Dell D3000E-S1:** https://www.itcreations.com/product/132053 **HTTP 200**, **+12.2 V**. May buy as a 12 V brick collection. **Does not replace ATX/EPS this week** and is **never GPU P48V**.

---

## B. Buy-together for 2× OAM — **will sit unused** until carrier / cooling / 48 V close

Buy only if you accept shelf time. **Do not apply 48 V. Do not mate an OAM to a random PCB.**

| Qty | Item | PN / notes | Buy link | Cost band | HTTP / blocker |
|---|---|---|---|---|---|
| 2 | MI250X OAM | HPE **P41933-001** / AMD **102-D65201-0B** class. 128 GB HBM2e, 500/560 W, OAM, PCIe 4.0 | https://www.amd.com/en/products/accelerators/instinct/mi200/mi250x.html · datasheet PDF **200** · surplus eBay (listings vanish) | **~$2k–4k each** volatile | Cooling, 48 V, overlay, carrier |
| 4 | Connector | Molex **218910-1115** / **2189101115**. Hermaphroditic, 5.00 mm, **mates with itself**. Modules already have two each. | Datasheet https://www.farnell.com/datasheets/3919676.pdf **200**. Product HTML **403**. Factory pack 150/reel — ask cut-tape | broker ~$50/ea unverified | **30 V sheet vs 48 V OCP** still OPEN |
| 1 | 48 V brick (candidate, not a harness) | MEAN WELL **RCP-2000-48** 48 V 42 A 2016 W, trim 42–56 V. Connector **PCIM34W13M400A1**. Sense pins 14/15. | Spec https://www.meanwell.com/Upload/PDF/RCP-2000/RCP-2000-SPEC.PDF **200** · series https://www.meanwellaustralia.com.au/products/RCP-2000 **200** | ~$400–700 class | Harness, fusing, Molex 30 V, HOST_PWRGD |
| 4 | φ3 mm pins | PEM **TPS-3mm-8** or equivalent (OCP §6.4.2) | PEM distributor | Unknown | — |
| 2–4 | Chassis fans | 12 V PWM, not a GPU HS | Noctua/Delta after bay height known | ~$20–80 | Not cooling the die |
| — | SuperMicro MI250 **shroud/tray** (optional research) | **MCP-310-45802-0B** shroud, **MCP-240-45801-0N** stiffener, **MCP-240-45809-0N** tray | spare market; not a die HS | Unknown | Chassis, not TIM |
| — | MCIO kit (optional, **will not** plug into X11DPH-T CEM) | **CBL-MCIO-1278S5FYB1** 4× MCIO-124p to 2× SlimSAS x8 “for MI-200” | https://www.wiredzone.com/shop/product/10026107-supermicro-cbl-mcio-1278s5fyb1-cable-kit-for-gpu-mi-200-11129 **200** | ~$250+ class | EPYC UBB cable, not this host |

**PVREF:** module output. Never buy a supply to “feed Vref.”

**P12V1 / P3V3:** can come from host ATX later. **P12V2:** OCP says extra P12V may be NC on 48 V boards; AMD need **Unknown** — do not buy a guessed high-current 12 V GPU path.

---

## C. Do not buy in the same cart

| Item | Why |
|---|---|
| 6 more MI250X (8-GPU) | Carrier, cooling, 48 V, xGMI overlay not done. Floor reserve is not a UBB. |
| OAM **r2.0** connectors / r2.0 pinmap parts | **UNUSABLE** (P3V3=6). |
| Molex **218916-1115** | Different stack height unless a non-5 mm stack is documented. |
| Guessed VRM / MP2975 / **12-to-48 boost** | Forbidden GPU path. |
| PCIe switch as “the” solution | Dual-GCD vs 3× Gen3 x16 not closed. CEM↔SlimSAS cards are SFF-9402 storage. |
| TI CEM2SLIMSAS-EVM / MB308A / SLM-1773-8I **as the OAM adapter** | Real products; **wrong pinout proof**. Optional lab toys, not this cart. |
| 240 V / **50 A** service hardware | 2-GPU is not an 8-OAM tray. |
| Dell D3000E-S1 **as GPU power** | **12.2 V**. |
| ORV3 48 V shelf / busway | Whole-rack. |
| Custom cold plate / DIY die clamp | NDA ICD missing. |
| DX-4189 coolers | Wrong socket. |
| Gold 6258R | You locked **6230**. |
| Donor AOM-MCM-Q as a *required* buy | Optional reverse-mapping tool, not a 2-OAM run path. |

---

## Cost-band rollup (not a quote)

| Bucket | Band |
|---|---|
| A. Host + desk + steel + **8× 32 GB RDIMM** | **~$2.5k–6k** (PMem + DRAM dominate) |
| B. 2× MI250X surplus | **~$4k–8k** |
| B. 4× Molex + RCP-2000-48 | **~$0.6k–1.5k** |
| Fab-ready carrier + HS + harness | **Not for sale** — blocked |

**Full-send cart ≠ working HBM.**
