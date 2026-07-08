# Engineering Review Report

**Project:** Open MI250X Carrier — Generated Prototype Rev1  
**Date:** 2026-07-07 (updated full-project review)  
**Artifact:** `Generated_Project/Rev1_MI250X_Carrier/`  
**Generator:** `Generated_Project/tools/generate_kicad_project.py`  
**Reviewer:** AI-assisted audit (requires human sign-off before fab)  
**Scope:** All 7 hierarchical child sheets + root; consistency audit across nets, buses, clocks, power, management, test points, designators, footprints. **No schematic modifications were made.**

---

## 1. Executive Summary

The project is a **KiCad 9 hierarchical schematic scaffold** for a single-MI250X OAM prototype carrier. All eight sheets (root + seven children) have been regenerated from Python subsystem modules with OCP OAM v1.5 logical naming, structured placeholders, and per-domain audit documentation.

| Metric | Value |
|--------|-------|
| Child schematic sheets | 7 |
| Hierarchical net labels (child) | 280 |
| Root sheet instance pins | 216 |
| Symbols placed (child sheets) | 65 |
| Wires / net ties (project-wide) | **0** |
| Footprints assigned (real library) | **0** (3 TODO strings, 62 empty) |
| OAM connector logical pins | 688 × 2 (Conn0 + Conn1) |
| OAM physical pin map resolved | **0** (~844 `PHYS_PIN_TODO_*` placeholders) |
| KiCad ERC run | **No** (`kicad-cli` unavailable) |

**Verdict:** Suitable as an **architecture baseline, interface contract, and documentation artifact**. **Not suitable** for PCB layout, BOM procurement, or energized bring-up. The design correctly avoids inventing AMD-specific signals; blocking TODOs are explicit.

**Estimated completeness:** ~30% architecture scaffold (up from initial ~11% generic placeholders). Remaining work is pin-map import, inter-sheet wiring, component wiring, footprints, SI/layout, and AMD power/sequencing verification.

---

## 2. Hierarchical Consistency

### 2.1 Sheet inventory

```
Root (MI250X_Carrier_Rev1.kicad_sch)
├── 04_power_system     — 12 symbols, 10 hierarchical labels
├── 02_oam_interface    —  2 symbols, 78 hierarchical labels
├── 03_host_pcie        —  2 symbols, 137 hierarchical labels
├── 05_clocking_reset   —  9 symbols, 13 hierarchical labels
├── 06_management       — 13 symbols, 13 hierarchical labels
├── 07_test_points      — 20 symbols, 21 hierarchical labels
└── 08_expansion        —  7 symbols,  8 hierarchical labels (6 DNP)
```

### 2.2 Root ↔ child pin contract

| Sheet | Root pins | Child labels | Match |
|-------|-----------|--------------|-------|
| Power_System | 10 | 10 | **PASS** |
| OAM_Interface | 78 | 78 | **PASS** |
| Host_PCIe | 73 | 137 | **FAIL** — 64 `PCIE_Ln_TX/RX_P/N` labels on child not exposed on root |
| Clocking_Reset | 13 | 13 | **PASS** |
| Management | 13 | 13 | **PASS** |
| Test_Points | 21 | 21 | **PASS** |
| Expansion | 8 | 8 | **PASS** |

**Finding (P1):** `03_host_pcie` declares 64 host-side `PCIE_L0..15_TX/RX_P/N` hierarchical labels, but the root `Host_PCIe` sheet instance only exposes OAM-facing `PET/PER` lanes and support signals (73 pins). KiCad ERC will flag **sheet pin count / name mismatch** until root pins are added or child labels are changed to local labels tied to `J1` internally.

### 2.3 Inter-sheet connectivity

**88 net names** appear on two or more child sheets (correct architectural sharing). Examples:

| Net | Sheets sharing name |
|-----|---------------------|
| `OAM_12V` | Power, OAM, Test_Points, Expansion |
| `PE_REFCLKp/n` | Clocking, OAM, Host, Test_Points, Expansion |
| `PERST_N` | Clocking, OAM, Host, Test_Points, Expansion |
| `PETp0` / `PERp0` | OAM, Host |
| `SMBUS_CLK/DATA` | OAM, Host, Management, Test_Points |
| `I2C_SCL/SDA` | Management, Test_Points, Expansion |

**Finding (P0):** Root schematic has **zero wires**. No inter-sheet net is electrically connected. Hierarchical labels define the contract only.

### 2.4 OAM ↔ Host PCIe alignment

Root `OAM_Interface` and `Host_PCIe` instances share **73 identical nets** (`PET/PER` lanes + PCIe support). OAM root adds five power nets (`OAM_12V`, `OAM_P12V1`, `OAM_P12V2`, `LOGIC_3V3`, `GND`) not on Host — **correct** (power sourced from Power_System).

---

## 3. Net Names

### 3.1 Naming convention summary

| Domain | Convention | OCP alignment | Notes |
|--------|------------|---------------|-------|
| OAM SerDes TX | `PETp0..15`, `PETn0..15` | OCP Table 4 | Consistent across OAM + Host |
| OAM SerDes RX | `PERp0..15`, `PERn0..15` | OCP Table 4 | Consistent |
| Host CEM lanes | `PCIE_Ln_TX_P/N`, `PCIE_Ln_RX_P/N` | PCIe CEM Gen4 | Host sheet only; mapping documented |
| Ref clock | `PE_REFCLKp`, `PE_REFCLKn` | OCP Table 4 | Used project-wide |
| Host ref (Mode B) | `HOST_REFCLKp`, `HOST_REFCLKn` | PCIe CEM | Clocking sheet only — do not short to `PE_REFCLK*` |
| Reset (OAM) | `PERST_N` | OCP `PERST#` | Active-low; underscore style |
| Reset (host) | `PERST_HOST_N` | PCIe CEM `PERST#` | Separate net on Clocking sheet |
| Presence | `PRESNT_N` | OCP `PRESNT#` | Consistent |
| SMBus | `SMBUS_CLK`, `SMBUS_DATA`, `SMBUS_ALERT_N` | OCP `SMBus_CLK`, `SMBus_D`, `SMB_ALERT#` | Underscore carrier style; OCP hash→`_N` |
| PMBus | `PMBUS_SCL`, `PMBUS_SDA` | User prototype | Module addresses TODO |
| I2C | `I2C_SCL`, `I2C_SDA` | Standard | Management + expansion |
| UART | `DBG_UART_TX`, `DBG_UART_RX` | User prototype | Split nets (not aggregate `DBG_UART`) |
| Power | `VIN_12V`, `OAM_12V`, `OAM_P12V1/2`, `MGMT_3V3`, `LOGIC_3V3`, `FAN_12V` | OCP + carrier | Consistent |
| TODO sidebands | `CLKREQ_N_TODO`, `WAKE_N_TODO` | Not in OCP Table 4 | Correctly not routed |

### 3.2 Naming issues

| ID | Severity | Issue |
|----|----------|-------|
| N-1 | Info | `PERST_N` vs `PERST_HOST_N` — intentional split for OAM vs host reset paths; must be explicitly bridged or buffered in wiring phase |
| N-2 | Info | `HOST_REFCLKp/n` vs `PE_REFCLKp/n` — Mode A/B clock topology; must not be tied together without buffer analysis |
| N-3 | Low | Test point references use concatenated names (`TPVIN_12V`) rather than `TP1` + value field — valid but non-standard |
| N-4 | Pass | No legacy `OAM_PRESENT_N` or `SMBus_D` mixed with `SMBUS_DATA` on active sheets |

---

## 4. Differential Pairs

### 4.1 Inventory (naming consistency)

| Pair group | Count | Naming | Sheets |
|------------|-------|--------|--------|
| Host TX | 16 | `PCIE_Ln_TX_P` / `PCIE_Ln_TX_N` | Host_PCIe |
| Host RX | 16 | `PCIE_Ln_RX_P` / `PCIE_Ln_RX_N` | Host_PCIe |
| OAM module TX | 16 | `PETpn` / `PETnn` | OAM, Host |
| OAM module RX | 16 | `PERpn` / `PERnn` | OAM, Host |
| OAM ref clock | 1 | `PE_REFCLKp` / `PE_REFCLKn` | Clocking, OAM, Host, TP, Expansion |
| Host ref clock | 1 | `HOST_REFCLKp` / `HOST_REFCLKn` | Clocking |

**Assessment:** Pair suffix convention (`p`/`n` or `_P`/`_N`) is **internally consistent** per domain. Host CEM uses `_P/_N`; OCP PET/PER uses `p/n` index suffix — documented mapping in `host_pcie.py`.

### 4.2 SI / implementation gaps

| ID | Severity | Gap |
|----|----------|-----|
| D-1 | P0 | No AC coupling capacitors on PET path (OCP baseboard requirement) |
| D-2 | P0 | No differential routing constraints in `.kicad_pro` (empty `diff_pair_dimensions`) |
| D-3 | P1 | Lane reversal / polarity inversion rules not defined (AMD dual-GCD TODO) |
| D-4 | P1 | No stub test points on HS lanes — **correct** per `07_test_points` policy |

---

## 5. Power Rails

### 5.1 Carrier rails (Power_System sheet)

| Net | Source block | Status |
|-----|--------------|--------|
| `VIN_12V` | J1 input | Scaffold — MPN/fuse/TVS ratings TODO |
| `OAM_12V` | N1 bus after U1 hot-swap | Scaffold — sequencing via U2 AMD TODO |
| `OAM_P12V1` | N1 logical split | Named per OCP; fanout TODO |
| `OAM_P12V2` | N1 logical split | Named per OCP; split vs P12V1 TODO |
| `MGMT_3V3` | U4 LDO | Scaffold — load budget TODO |
| `LOGIC_3V3` | U5 LDO → OAM P3V3 | Scaffold — OAM load TODO |
| `FAN_12V` | J2 fused rail | Optional Rev1 |
| `GND` | Return | Multiple hierarchical taps |
| `OAM_EN_TODO` | U2 sequencer | Not implemented |
| `OAM_PG_TODO` | AMD PG input | Gates PERST release — timing TODO |

### 5.2 OAM connector rails not implemented

| Rail | Status | Risk |
|------|--------|------|
| `P48V` / 54V | U3 block explicitly NC Rev1 | **Critical** — MI250X may require 48V/54V |
| Conn1 `P3V3` | May share `LOGIC_3V3` | Pin assignment TODO |
| `PVREF` | Module output | Not a carrier supply |

**Assessment:** Power **architecture is separated correctly** (mgmt vs logic 3V3, OAM 12V domain, fan rail). **No current ratings, sequencing, or PG thresholds** — blocking for power-on.

---

## 6. Clock Distribution

**Sheet:** `05_clocking_reset` — documented in `docs/clocking_reset_audit.md`

| Component | Ref | Role | Status |
|-----------|-----|------|--------|
| 100 MHz oscillator | Y1 | PE_REFCLK source (Mode A) | Placeholder — footprint empty |
| PCIe clock buffer | U1 | Fanout Y1 → OAM (+ optional host) | Placeholder |
| Termination | R1 | PE_REFCLK termination | Values TODO |
| Host REFCLK input | J1 | Mode B passthrough | Placeholder |
| PERST distribution | U2 | `PERST_N` fanout | Placeholder |
| AUX 100M | U3 | OCP optional — NC | TODO |
| WARMRST | U4 | OCP optional — NC | TODO |
| PERST Conn1 | U5 | Conn1 PERST — NC | TODO |
| AMD seq gate | U6 | Reset sequencing — NC | TODO |

**Topology:** Mode A (carrier Y1) vs Mode B (host `HOST_REFCLK*`) documented. **No wires** between Y1, U1, OAM, or host.

**Gaps:** REFCLK jitter/skew limits TODO; SSC requirement unknown; Expansion U3 `PE_REFCLK_Fanout_DNP` reserved for multi-module (DNP).

---

## 7. Reset Signals

| Signal | Sheet(s) | Role | Routed |
|--------|----------|------|--------|
| `PERST_N` | Clocking, OAM, Host, TP, Expansion | OCP PCIe reset to module | Labels only |
| `PERST_HOST_N` | Clocking | Host-side PERST# | Labels only |
| `PERST_CONN1_N_TODO` | Clocking | Conn1 PERST — NC | No |
| `WARMRST_N_TODO` | Clocking | OCP warm reset — NC | No |
| `OAM_PG_TODO` | Power, Clocking | PG gates PERST release | Labels only |
| `OAM_EN_TODO` | Power | Module enable (not reset) | Labels only |
| `PRESNT_N` | OAM, Host, TP | Presence detect | Labels only |
| `CLKREQ_N_TODO` | OAM, Host | Clock request — not OCP Table 4 | No |
| `WAKE_N_TODO` | OAM, Host | Wake — not OCP Table 4 | No |

**Assessment:** Reset inventory is **complete for Rev1 scope**. AMD PERST release timing vs `OAM_PG_TODO` is documented as TODO. Expansion U4 `PERST_Fanout_DNP` reserved (DNP).

---

## 8. I2C Buses

| Bus | Nets | Devices / endpoints | Pull-ups | Status |
|-----|------|---------------------|----------|--------|
| I2C1 (MCU) | `I2C1_SCL/SDA` on U1 symbol | U2 FRU EEPROM, U5 TMP117 | R1 (`Mgmt_I2C_Pullups`) | Symbols placed; **not wired** |
| I2C2 (MCU) | `I2C2_SCL/SDA` on U1 | U3 PMBus path, U4 SMBus bridge MCU side | R1 | Symbols placed; **not wired** |
| Carrier expansion | `I2C_SCL`, `I2C_SDA` | Management J2 → Expansion J1 → Test J1 dbg | Documented 2.2k on R1 | Hierarchical only |
| I2C mux (optional) | — | U6 `Mgmt_I2C_Mux_DNP` | — | **Not marked `(dnp yes)` in KiCad** — see §12 |
| Expansion mux | — | U2 `Exp_I2C_Mux_DNP` | — | Correctly DNP |

**Assessment:** Two-MCU-bus architecture is **sound**. FRU and temp sensor on I2C1 matches prototype requirements. Expansion I2C hook is the only active Rev1 cross-sheet management interface.

---

## 9. PMBus

| Item | Status |
|------|--------|
| `PMBUS_SCL/SDA` hierarchical nets | Present on Management outputs, Test_Points |
| U3 `Mgmt_PMBus_PassThrough` | Placed — module telemetry path |
| U9 `Mgmt_AMD_PMBus_TODO` | NC block — addresses not invented |
| Module device map (MP2975?) | **TODO** — candidate only |
| Wiring to OAM | **Not implemented** |

**Assessment:** PMBus is a **logical placeholder** only. Correctly avoids inventing module addresses.

---

## 10. EEPROM (FRU)

| Item | Detail |
|------|--------|
| Reference | U2 on Management sheet |
| Symbol | `Mgmt_FRU_EEPROM` / AT24C256 class |
| Bus | I2C1 (MCU pins `I2C1_SCL/SDA`) |
| Address straps | A0/A1/A2 on symbol — **TODO** |
| Write protect | WP pin — strap **TODO** |
| FRU data format | IPMI compatibility **TODO** |
| Footprint | **Empty** |

**Assessment:** FRU EEPROM is **architecturally placed** per user requirement. No content model, wiring, or footprint.

---

## 11. Test Points

**Sheet:** `07_test_points` — documented in `docs/bringup_checklist.md`

| Category | Count | Nets |
|----------|-------|------|
| Power TPs | 8 | `VIN_12V`, `OAM_12V`, `OAM_P12V1/2`, `MGMT_3V3`, `LOGIC_3V3`, `FAN_12V`, `GND` |
| PCIe sideband TPs | 4 | `PE_REFCLKp/n`, `PERST_N`, `PRESNT_N` |
| Management TPs | 7 | SMBus ×3, PMBus ×2, UART ×2 |
| Debug header | 1 | J1 I2C (SCL, SDA, 3V3, GND) |

**Policy compliance:** HS lanes (`PET/PER`, `PCIE_L*`) correctly have **no** stub TPs.

**Gaps:** Pass/fail voltage limits all TODO; TPs not wired to hierarchical labels; footprint empty on `Tp_Signal` and `Dbg_Header_I2C`.

---

## 12. Reference Designators

### 12.1 Per-sheet allocation

| Sheet | Key refs |
|-------|----------|
| OAM_Interface | J1 Conn0, J2 Conn1 |
| Host_PCIe | J1 host slot, J2 OAM bridge |
| Power_System | J1/J2, U1–U5, D1, F1/F2, CB1, N1 |
| Clocking_Reset | Y1, U1–U6, R1, J1 |
| Management | U1–U10, R1, J1–J2 |
| Test_Points | TP×19, J1 |
| Expansion | J1–J3, U1–U4 (U1–U4/J2–J3 DNP) |

### 12.2 Cross-sheet collisions

Nine reference strings (`J1`, `J2`, `R1`, `U1`–`U6`) appear on multiple sheets. This is **normal for hierarchical KiCad** (each sheet has independent annotation scope) but will require **BOM merge by full symbol path** or re-annotation before production BOM export.

### 12.3 DNP flag consistency

| Symbol | Sheet | Value implies DNP | KiCad `(dnp yes)` |
|--------|-------|---------------------|-------------------|
| `Exp_PCIe_Switch_DNP` | Expansion | Yes | **Yes** |
| `Exp_OAM_Slot2_DNP` | Expansion | Yes | **Yes** |
| `Exp_Power_Bus_DNP` | Expansion | Yes | **Yes** |
| `Exp_I2C_Mux_DNP` | Expansion | Yes | **Yes** |
| `Exp_REFCLK_Fanout_DNP` | Expansion | Yes | **Yes** |
| `Exp_PERST_Fanout_DNP` | Expansion | Yes | **Yes** |
| `Mgmt_I2C_Mux_DNP` | Management | Yes | **No** — inconsistency |
| `Mgmt_Fan_PWM_TODO` | Management | Optional DNP | **No** |
| `Mgmt_AMD_*_TODO` | Management | NC | **No** (acceptable — NC blocks) |

**Finding (P2):** Management optional blocks U6/U7 should have `(dnp yes)` when DNP policy is applied project-wide.

---

## 13. Missing Footprints

| Status | Count | Notes |
|--------|-------|-------|
| Empty `Footprint` property | 62 | All discrete/passive/IC placeholders |
| `TODO — …` string only | 3 | Mirror Mezz J1/J2, Host PCIe J1 |
| Footprint library directory | **Missing** | `fp-lib-table` points to empty `footprints/` |
| `.kicad_pcb` | **Not present** | No layout started |

### Critical footprint gaps (P0 for layout)

| Ref | Sheet | Component | Footprint status |
|-----|-------|-----------|------------------|
| J1 | OAM_Interface | Molex Mirror Mezz Pro 218910-1115 | `TODO — Molex Mirror Mezz Pro 688` |
| J2 | OAM_Interface | Molex Mirror Mezz Pro 218916-1115 | `TODO — Molex Mirror Mezz Pro 688` |
| J1 | Host_PCIe | PCIe x16 Gen4 edge | `TODO — PCIe x16 edge or cable connector` |
| J1 | Power_System | 12V input | Empty |
| Y1 | Clocking_Reset | 100 MHz HCSL oscillator | Empty |
| U1 | Management | STM32G071 | Empty |
| U2 | Management | AT24C256 FRU | Empty |

---

## 14. Requirements Traceability (updated)

| Requirement | Implementation | Status |
|-------------|----------------|--------|
| Single OAM module | `02_oam_interface` — Molex Conn0/1, 688 logical pins each | Scaffold — physical map TODO |
| PCIe Gen4 x16 | `03_host_pcie` — direct x16, PET/PER + PCIE_L naming | Scaffold — root pin mismatch; GCD map TODO |
| 12V input | `04_power_system` — full power tree blocks | Scaffold — ratings/sequencing TODO |
| FRU EEPROM | `06_management` U2 AT24C256 | Scaffold — FRU format TODO |
| I2C | `06_management` — dual bus MCU architecture | Scaffold — unwired |
| PMBus | `06_management` U3 + hierarchical nets | Scaffold — addresses TODO |
| Temperature | `06_management` U5 TMP117 | Scaffold |
| Debug UART | `06_management` J1 + TP UART probes | Scaffold |
| Test points | `07_test_points` — 19 TPs + I2C header | Scaffold — limits TODO |
| Multi-OAM future | `08_expansion` — DNP switch/slot/power/mux | Planning only — **correct** |
| OCP compliance | OCP naming, Mirror Mezz MPN, PE_REFCLK 100 MHz | Partial — pin spreadsheet missing |
| No invented AMD signals | TODO labels and NC blocks | **Pass** |
| Hierarchical sheets | 7 children + root | **Pass** |

---

## 15. ERC / DRC / Tooling

| Check | Result |
|-------|--------|
| KiCad CLI / ERC | **Not run** — `kicad-cli` not in environment |
| Schematic syntax | KiCad 9 `20250114` — open in KiCad 9 recommended |
| Root ↔ child pin match | **1 failure** (Host_PCIe 64 pins) |
| Inter-sheet wiring | **0 wires** — all nets floating |
| Power flags | Power symbols in `lib_symbols` only |
| Footprints | **0% assigned** |
| PCB | Not started |

**Predicted ERC classes on first open:**
1. Hierarchical sheet pin mismatch (Host_PCIe)
2. Unconnected hierarchical labels (all sheets)
3. Unconnected symbol pins (all components)
4. Power input not driven (all ICs)
5. Duplicate sheet-local references (informational for BOM)

---

## 16. Risks Summary

| Risk | Severity | Mitigation |
|------|----------|------------|
| Zero schematic wiring | Critical | Wire root bus matrix; then child sheets |
| Host_PCIe root pin mismatch | High | Add 64 `PCIE_L*` pins to root or localize labels |
| OAM pin spreadsheet missing | Critical | Import OCP `OAM_Pinlist_Pinmap` |
| 48V/54V rail requirement unknown | Critical | AMD power extraction before energizing |
| PCIe lane / GCD mapping unknown | High | AMD integration guide |
| No footprints / no PCB | High | Mirror Mezz + edge connector first |
| PERST/REFCLK topology unwired | High | Complete Clocking sheet wiring per Mode A/B decision |
| Management U6 DNP flag missing | Low | Set `(dnp yes)` when updating generator |
| Cross-sheet ref collisions | Low | Re-annotate at BOM export |

---

## 17. Recommended Next Steps

1. **Fix Host_PCIe hierarchical contract** — add `PCIE_L0..15_TX/RX_P/N` to root instance (or remove from child if host slot is fully local).
2. **Wire root schematic** — connect shared nets between sheet instances (power, PET/PER, REFCLK, PERST, SMBus, management).
3. **Import OAM_Pinlist_Pinmap** — replace `PHYS_PIN_TODO_*` with physical Molex pad numbers.
4. **Run KiCad 9 ERC** — iterate generator until clean hierarchical contract.
5. **Assign footprints** — Mirror Mezz Pro 688, PCIe x16 edge, 12V input, STM32, AT24C256, TMP117, passives.
6. **Wire Power_System** — input protection, hot-swap, LDO decoupling; resolve AMD sequencing before OAM enable.
7. **Wire Clocking_Reset** — choose Mode A or B; connect Y1/U1/R1/U2.
8. **Wire Management** — I2C1/I2C2, SMBus level shifter, PMBus pass-through, UART header.
9. **Extract AMD 12V/48V requirements** — confirm P48V necessity; size F1/U1.
10. **Define diff-pair constraints** in `.kicad_pro` when layout starts.

---

## 18. Audit Documentation Index

| Document | Content |
|----------|---------|
| `docs/sources.md` | Evidence sources |
| `docs/assumptions.md` | Design assumptions |
| `docs/open_questions.md` | Open questions |
| `docs/oam_signal_map.md` | OAM signal map |
| `docs/remaining_unknown_pins.md` | ~844 unknown OAM pins |
| `docs/host_pcie_support_signals.md` | PCIe sideband audit |
| `docs/missing_power_rails.md` | Power rail gaps |
| `docs/clocking_reset_audit.md` | Clock/reset inventory |
| `docs/management_audit.md` | Management requirements |
| `docs/bringup_checklist.md` | Test points + bring-up gates |
| `docs/expansion_planning.md` | Multi-OAM DNP + PCIe switch plan |

---

## 19. Files in Generated Project

```
Generated_Project/
├── ENGINEERING_REVIEW.md          (this file)
├── README.md
├── BOM_Rev1_Prototype.md
├── tools/
│   ├── generate_kicad_project.py
│   ├── oam_mirror_mezz.py
│   ├── host_pcie.py
│   ├── power_system.py
│   ├── clocking_reset.py
│   ├── management_system.py
│   ├── test_points_system.py
│   └── expansion_system.py
└── Rev1_MI250X_Carrier/
    ├── MI250X_Carrier_Rev1.kicad_pro
    ├── MI250X_Carrier_Rev1.kicad_sch
    ├── sym-lib-table / fp-lib-table
    ├── symbols/MI250X-Carrier.kicad_sym
    ├── docs/  (11 audit files)
    └── sheets/  (7 child schematics)
```

---

## 20. Sign-Off Checklist (Human)

- [ ] Host_PCIe hierarchical pin mismatch resolved  
- [ ] Root inter-sheet wiring complete  
- [ ] OCP pin map imported and reviewed  
- [ ] AMD power rails confirmed (12V-only vs 48V/54V)  
- [ ] PCIe lane / GCD map confirmed  
- [ ] Clock Mode A vs B selected and wired  
- [ ] KiCad ERC clean  
- [ ] Footprints assigned for all populated parts  
- [ ] Peer review of management architecture  
- [ ] Thermal solution defined (off-schematic)  
- [ ] Approval to proceed to layout  

**Approved by:** _______________  **Date:** _______________
