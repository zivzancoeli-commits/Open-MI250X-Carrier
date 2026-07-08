# Expansion Planning — Rev1 MI250X OAM Carrier

Interface planning only. **All expansion logic is DNP on Rev1.**
No switch MPN, lane bifurcation, or multi-module power sequencing is implemented.

## Revision scale-out path

| Revision | Modules | PCIe | Power | Management |
|----------|---------|------|-------|------------|
| Rev1 | 1 | Direct Host_PCIe x16 → OAM_Interface (no switch populated) | Single OAM_12V domain from Power_System | Management J2 I2C → Expansion sheet interface only |
| Rev2 | 2 | PCIe switch DNP placeholder — upstream from host, downstream to slot 1 + slot 2 | OAM_12V bus bar pads DNP — per-module hot-swap AMD TODO | I2C mux DNP — per-module SMBus/FRU addressing AMD TODO |
| Rev3 | 4 | Switch topology and lane bifurcation TODO — host upstream width unknown | Distributed 12V — current budget and sequencing TODO | Multi-drop SMBus arbitration TODO |
| Rev4 | 8 | Multi-switch or retimer fabric TODO — no verified topology in repo | Chassis-level distribution TODO | BMC/IPMI scale-out TODO |

## Rev1 active interface (not DNP)

- **I2C_SCL / I2C_SDA** — Management sheet J2 → Expansion sheet J1 (carrier/expansion I2C hook)
- All other Expansion sheet symbols are **DNP** — footprint and planning only

## PCIe switch integration (future — U1 DNP)

Rev1 bypasses the switch: Host_PCIe connects directly to OAM_Interface.

### Rev1 direct paths (active today)
- **Host_PCIe J3 (PCIE_Ln_TX/RX) ↔ OAM_Interface PET/PER** — Rev1 direct path — U1 switch DNP, footprint only
- **Clocking_Reset Y1/U1 → PE_REFCLKp/n → OAM_Interface** — Rev1 single refclk fanout — Expansion U3 REFCLK fanout DNP for multi-module
- **Clocking_Reset U2 → PERST_N → OAM_Interface** — Rev1 single reset — Expansion U4 PERST fanout DNP for additional slots

### Future switch port map (logical — not routed Rev1)

- **UPSTREAM**: nets `PCIE_L0..15_TX_P/N, PCIE_L0..15_RX_P/N (from Host_PCIe)` — Host root complex — lane count and bifurcation AMD TODO
- **DOWNSTREAM_0**: nets `PETp0..15, PETn0..15, PERp0..15, PERn0..15 (to OAM slot 1 / existing OAM_Interface)` — Rev1 active module — bypass switch in direct mode or wire to port 0 when populated
- **DOWNSTREAM_1**: nets `Same PET/PER naming — OAM slot 2 DNP connector J2` — Second Mirror Mezz — footprint DNP; full pin map on OAM_Interface sheet pattern
- **DOWNSTREAM_2..3**: nets `PET/PER logical groups — slots 3–4 DNP` — Rev3 planning — mechanical and thermal TODO
- **REFCLK_IN**: nets `PE_REFCLKp, PE_REFCLKn` — 100 MHz HCSL from Clocking_Reset — switch refclk fanout requirements TODO
- **PERST_IN**: nets `PERST_N` — PCIe reset — per-port PERST_OUTn from switch or separate fanout DNP
- **PRESNT_IN / PRESNT_OUTn**: nets `PRESNT_N per slot` — Module presence — Host_PCIe bridge today; per-slot presence TODO
- **CLKREQ_N / WAKE_N**: nets `CLKREQ_N_TODO, WAKE_N_TODO` — Not in OCP Table 4 — not routed Rev1; switch sideband support unknown

### PCIe switch open questions

- Switch vs retimer vs redriver — no verified requirement for 1× MI250X (see 15_Reverse_Engineering/05_PCIe.md)
- AMD MI250X dual-GCD lane map affects downstream port width — TODO
- Host upstream: x16 vs bifurcated x8/x8 for dual module — TODO
- AC coupling on PET path per OCP — per-port cap placement when switch inserted — TODO
- Switch reference clock jitter budget vs OCP PE_REFCLK — REFCLK guide missing
- Switch power rail (3.3V / 1.8V / 12V) — not on Power_System Rev1
- Firmware/OS enumeration with switch — software topology TODO

## Expansion sheet placeholders (all DNP except J1)

| Ref | Symbol | Value | DNP | Notes |
|-----|--------|-------|-----|-------|
| U1 | Exp_PCIe_Switch_DNP | PCIe_Switch_DNP | yes | PCIe Gen4 switch fabric for 2/4/8 OAM — DNP Rev1; footprint reserved |
| J2 | Exp_OAM_Slot2_DNP | OAM_Slot2_DNP | yes | Second OAM module connector placeholder — 688-pin map not expanded on this sheet |
| J3 | Exp_Power_Bus_DNP | OAM_12V_BusBar_DNP | yes | 12V distribution taps for additional OAM modules — DNP Rev1 |
| U2 | Exp_I2C_Mux_DNP | I2C_Mux_Exp_DNP | yes | Expansion-side I2C fanout for per-module management — DNP Rev1 |
| U3 | Exp_REFCLK_Fanout_DNP | PE_REFCLK_Fanout_DNP | yes | Multi-module PE_REFCLK fanout when switch populated — DNP Rev1 |
| U4 | Exp_PERST_Fanout_DNP | PERST_Fanout_DNP | yes | Per-module PERST# distribution — AMD sequencing TODO |
| J1 | Exp_Mgmt_I2C_Interface | I2C_Exp_Interface | no | Rev1 active interface hook — not expansion logic; connects Management to Expansion sheet |

## Hierarchical nets on Expansion sheet

- `I2C_SCL` (bidirectional)
- `I2C_SDA` (bidirectional)
- `OAM_12V` (input)
- `MGMT_3V3` (input)
- `GND` (passive)
- `PE_REFCLKp` (input)
- `PE_REFCLKn` (input)
- `PERST_N` (input)

## Placeholders replaced

- REMOVED: OAM_MirrorMezz_Conn0_TODO (belongs on OAM_Interface sheet)
- REMOVED: MCU_STM32G071_TODO / FRU_EEPROM / TEMP_TMP117 (belong on Management sheet)
- REMOVED: build_child() generic stubs
- ADDED: U1 PCIe switch DNP — footprint + integration planning
- ADDED: J2 OAM slot 2 connector DNP — key OCP nets only
- ADDED: J3 OAM_12V bus bar DNP — multi-module power taps
- ADDED: U2 I2C mux DNP — per-module management fanout
- ADDED: U3 REFCLK fanout DNP, U4 PERST fanout DNP
- ADDED: J1 I2C interface from Management (Rev1 hook)
- DOCUMENTED: PCIe switch upstream/downstream/refclk/reset — docs/expansion_planning.md
