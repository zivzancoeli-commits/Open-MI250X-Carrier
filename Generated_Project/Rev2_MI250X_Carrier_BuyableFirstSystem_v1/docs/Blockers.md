# Blockers.md — remaining Unknowns that prevent “just buy and plug in”

**Date:** 2026-08-17  
**Tree:** `Generated_Project/Rev2_MI250X_Carrier_BuyableFirstSystem_v1`  
Labels: **Verified** / **Inferred** / **Unknown**

You can buy a host + desk PC this week and they will POST. You cannot buy this list and have two MI250X modules running ROCm tomorrow.

---

## 1. AMD MI250X overlay (NDA) — blocking energize

| Item | Status | Why it blocks |
|---|---|---|
| TEST0–TEST14, TEST_MODE# | Named in v1.0 map; **AMD function Unknown** | Pads left **unmapped** (no net). Forum talk of pullups on AOM-MCM-Q is **not** a pad assignment. |
| RFU / DO_NOT_USE | Named reserved | Unmapped. Do not strap. |
| Dual-GCD host PCIe (1×16 vs 2×8) | **Unknown** | MI250X is two GCDs / two software devices. `PE_BIF[1:0]` exists on Conn1 (OCP). Default for MI250X not in the public map. |
| Which S1–S7 SerDes are xGMI / Infinity Fabric | **Unknown** | Named, assigned on PCB, **not routed** between the two OAMs. |
| SMBus slave addresses / FRU / PMBus map | **Unknown** | `SMBus_SLV_*` stubbed only. Do not invent 0x50 as a requirement (Level1Techs discussion is not an AMD register map). |
| P12V2 required on 48 V MI250X? | Pin list: P12V2 is **required for P12V-based OAM**. MI250X is 48 V class. **Unknown** whether P12V2 must be live. | Do **not** short P12V1 to P12V2. |
| HOST_PWRGD timing vs rail windows | OCP: active when P48V/P12V1/P12V2/P3V3 in spec | Exact delays **Unknown** without AMD/OCP bring-up overlay. |
| LINK_CONFIG[4:0] coding for PCIe vs alternate | OCP table exists in the spec family; MI250X row **Unknown** | Leave open this stub (module weak PU → 1). |

Public Instinct docs (product page + MI200 datasheet, HTTP 200 this run): OAM form factor, PCIe 4.0 x16, 500 W / 560 W peak, 128 GB HBM2e, dual GCD implied by MI250 family docs. **No 688-pad overlay.**

---

## 2. 48 V path — blocking energize

| Item | Status |
|---|---|
| Dell D3000E-S1 3 kW | **Verified 12.2 V** CRPS (IT Creations: +12.2 V 245.9 A / +12 VSB 2.0 A). **Not** GPU P48V. Never mix with P48V. |
| OCP P48V | **Verified** v1.0 pin list: 44–59.5 V, 16 SE pads, Conn0 only, up to 700 W class when Vin ≥ 44 V. |
| Mean Well RCP-2000-48 | **Verified** vendor spec: 48 V, 0–42 A, 2016 W, trim 42–56 V. Electrically in the OCP window **if** trim/output is confirmed in-spec under load. **Not** a finished OAM harness. Needs AC inlet, output connector, fusing, sense, and carrier entry — all **Unknown** as a designed assembly. |
| OCP Open Rack v3 48 V shelf | **Verified** as an architecture (narrow-range 48 V busbar). Whole-rack ORV3 is **Do not buy yet** for a 2-GPU welded chassis. |
| 12 V → OAM hack | **Forbidden.** Do not invent a boost converter onto P48V pads. |
| Molex voltage rating | Farnell 2189101115 sheet: **30 V AC/DC max**. OCP uses this MPN on 48 V OAMs. **Unresolved.** Do not energize P48V through these pads until Molex PS `2189100001-PS-000` / OEM practice is cited. |

Two MI250X at 560 W peak ≈ 1120 W at 48 V ≈ 23 A (**Inferred** from AMD TDP + Ohm’s law, not a measured input current). RCP-2000-48 42 A has headroom **if** the voltage-rating and harness gates close. That is not permission to apply power.

---

## 3. Cooling — blocking energize

| Item | Status |
|---|---|
| OEM air heatsink height | **Unknown.** Photos under `07_Photos/04_Cooling/` are not dimensioned. Planning keep-out is 100 mm, not a measured brick. |
| OCP air note | v1.5 §7.5.3 ~450 W air on a shadowed 8× tray. MI250X is **500 / 560 W**. Air-first is BOM **intent**, not a qualification. |
| Custom cold plate on bare die | **Do not.** TIM / die ICD is NDA. Chassis must leave **replaceable** cooling. |
| Fan curve / duct | **Unknown.** Buy fans only as chassis airflow, not as “MI250X qualified.” |

---

## 4. Dual NH-U14S DX-3647 collision — blocking frozen sheet metal

| Item | Status |
|---|---|
| Cooler | **Verified** NH-U14S DX-3647, LGA3647, 150 × 78 × 165 mm with fan (Noctua). **Not** DX-4189. |
| X11DPH-T CPU1/CPU2 pitch | **Unknown.** Envelope CAD places towers as placeholders. Dual-tower vs DIMM/VRM clash is **Unknown**. |
| Narrow vs square ILM | Cooler supports both; which ILM is on a given X11DPH-T board must be checked on the hardware. |

---

## 5. PCIe / host link — blocking enumeration

| Item | Status |
|---|---|
| X11DPH-T | **Verified** 3× Gen3 x16 + 4× Gen3 x8 (SuperMicro). |
| MI250X | **Verified** PCIe 4.0 x16 (AMD). **Will downtrain** to Gen3. |
| CEM adapter / cable / retimer | **Not closed.** v1.0 names `PCIE_TXn` / `PCIE_RXn` + `PE_REFCLKp/n` + `PERST#`. Mapping those onto a CEM x16 edge is a **carrier topology** that this stub **does not invent**. No retimer or switch BOM. |
| Bifurcation / slot population | Dual x16 slots exist physically. BIOS bifurcation, REFCLK from each slot, and AC coupling are **Unknown** as a finished path. |
| Cable length SI at Gen3 | **Unknown.** Do not buy random SlimSAS/MCIO “GPU cables” and assume they mate to OAM. |

---

## 6. Connector / mechanical — blocking tape-out (not blocking host buy)

| Item | Status |
|---|---|
| Gender | **Verified** hermaphroditic: Farnell 2189101115 “Mates With 2189101115”. Buy **4× for the carrier** (modules already have two each). Not a male/female pair. |
| Stack | **Verified** 5.00 mm mated height; OCP 5 mm ± 0.15 mm. 218916 is a different height — **do not buy** unless a non-5 mm stack is documented. |
| PIN A3 | Geometry on Molex SD / Figure 2. Candidate footprint rotation 180° is **Inferred**. Overlay-check before fab. |
| M3.5 / 5 mm stack / 102×165 / 103×166 | **Verified** OCP v1.5 (see chassis cut-list). Screw **length** depends on bolster — **Unknown**. |

---

## 7. BMC / management — blocking a “complete” carrier

OCP wants SMBus to a BMC, I2C with level shift off PVREF, UART to a bridge. No BMC part is selected. Host AST2500 on X11DPH-T is a **server BMC**, not proven as the OAM SMBus owner. **Unknown.**

---

## 8. Memory Mode companion DRAM

Intel Memory Mode uses DRAM as cache; PMem is the OS-visible memory. Exact X11DPH-T population (which slots, minimum DRAM per channel) is in the SuperMicro memory QVL / user manual — **not extracted into a locked SKU here**. Do not buy 8× PMem and zero DRAM and expect Memory Mode to work.

---

## What is *not* a blocker for this week’s host/desk buy

X11DPH-T + 2× Gold 6230 + PMem + DRAM cache + DX-3647 + a **standard ATX/EPS** PSU + B550M/5500 desk combo can be purchased and assembled as two computers. That does not power OAMs.
