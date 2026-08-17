# Buy now — host, desk, SendCutSend (2026-08-17)

**OK this week.** These POSTs as two computers and cut chassis **sheet**. They do **not** make 256 GB HBM work.

**Still waiting:** Brian Park / Molex **2189101115 60 V skip-pin** ([MOLEX_2189101115_QUESTIONS.md](MOLEX_2189101115_QUESTIONS.md)).

**Do not:** PCBWay; energize OAMs; invent pins.

Locked SKUs unchanged from PR #2/#3. URL check this run: [URL_LOG.md](URL_LOG.md). Prices are **bands**, not quotes. 403/429 often means bot-block.

---

## A. Host (will POST)

| Qty | Item | PN | Buy link | Cost band | HTTP this run |
|---|---|---|---|---|---|
| 1 | Host board | SuperMicro **MBD-X11DPH-T** | https://www.newegg.com/supermicro-mbd-x11dph-t-o-2nd-generation-intel-xeon-scalable-processors-intel-xeon-scalable-proces/p/1B4-005W-001B0 | used/new ~$300–1200 | **200** |
| 2 | CPU | Xeon Gold **6230** sSpec **SRF8W**, 125 W, LGA3647 | search `SRF8W` | ~$120–250 each used | re-check in browser |
| 8 | PMem | Dell **SNPHVY68C/128G** | https://www.ebay.co.uk/p/24064262136 | ~$100–250 each surplus | **200** |
| 8 | DRAM cache | **MEM-DR432L-SL01-ER29** / Samsung **M393A4K40CB2-CVF** 32 GB DDR4-2933 2Rx4 ECC RDIMM | https://store.supermicro.com/us_en/32gb-ddr4-2933-mem-dr432l-sl01-er29.html | used ~$30–80 each | **403** here (bot-block; SKU still SuperMicro-validated from prior hunt) |
| 2 | Cooler | Noctua **NH-U14S DX-3647** only | https://noctua.at/en/nh-u14s-dx-3647 | often OOS | **429** here |
| 1 | Host PSU | ATX 24-pin + EPS 8-pin, 750–1200 W 80+ Gold | any reputable ATX/EPS | ~$100–250 | — |
| 1 | Boot SSD | NVMe/SATA the board will boot | current Newegg/Amazon | ~$40–150 | — |

**BIOS:** 3.0a+ for 2nd-gen Xeon. Memory Mode needs DRAM cache (do not buy 8× PMem and zero RDIMM). Dual U14S vs CPU pitch is still **Unknown** — buy the coolers; do not assume both towers clear DIMMs until the board is measured.

**Dell D3000E-S1:** may buy as a **12 V** brick collection (https://www.itcreations.com/product/132053). **Does not replace ATX/EPS this week. Never GPU P48V.**

---

## A. Desk (will POST)

| Qty | Item | Notes | Cost band |
|---|---|---|---|
| 1 | **Ryzen 5 5500** + **B550M** | Combo example previously used ASUS PRIME B550M-A AC — not the only legal board | ~$180–250 |
| 1 | 16 GB DDR4-3200 | if not in the combo | ~$30–50 |
| 1 | 450–650 W ATX PSU | desk only | ~$50–90 |
| 0–1 | **RX 470** used | 5500 has **no iGPU** | ~$50–80 |

---

## A. Chassis metal

| Qty | Item | Where | Notes |
|---|---|---|---|
| 7 DXFs | SendCutSend A1008 **0.059"** | [SENDCUTSEND_ORDER.md](SENDCUTSEND_ORDER.md) | Trays + skins + divider. **OK to buy.** Vendor pages **HTTP 200** this run. |
| lot | Mild-steel **square tube** | local | Not SCS. Cut-list Inferred; **do not freeze height**. |
| lot | Weld wire, gas, discs, primer | local | — |
| lot | M4 / 6-32 for trays | SCS PEM optional, or local | **Not** OAM M3.5 |
| lot | M3.5 mixed 8–16 mm | McMaster/local | For **later** OAM; not for these DXFs |

---

## B. Still shelf-only (do not energize)

Unchanged from FullSend: 2× MI250X surplus, 4× **218910-1115**, MEAN WELL RCP-2000-48 **as a brick on the bench**, fans, φ3 mm pins. **Do not apply 48 V. Do not mate an OAM to a random PCB.** Connector voltage gate = this wait.

---

## C. Do not buy in the same breath

PCBWay of in-repo KiCad; r2.0 OAM parts; 218916-1115 unless a non-5 mm stack is documented; guessed 12-to-48 boost; PCIe switch as “the” OAM adapter; DX-4189; Gold 6258R; 50 A busway; D3000E-S1 as GPU power; DIY die clamp.

---

## Cost-band rollup (not a quote)

| Bucket | Band |
|---|---|
| Host + desk electronics | **~$2.5k–6k** (PMem + DRAM dominate) |
| SendCutSend 0.059" skins/trays | **Unknown until upload** (vendor instant quote) |
| Square tube + weld | **Unknown** (local) |
| Working HBM | **Not for sale** — waiting Molex + overlay + cooling |
