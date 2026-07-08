# Bring-Up Checklist — Rev1 MI250X OAM Carrier

Gated procedure per `15_Reverse_Engineering/08_Bringup.md`.
**Pass/fail voltage, current, and timing limits are TODO** — do not energize OAM module until AMD rail table exists.

## Power rails — test points required

| Net | Test point | Source | Pass/fail limit |
|-----|------------|--------|-----------------|
| VIN_12V | TP_VIN_12V | Power_System J1 input | TODO — AMD/input spec |
| OAM_12V | TP_OAM_12V | Power_System N1 bus | TODO — MI250X 12V draw |
| OAM_P12V1 | TP_OAM_P12V1 | OCP Table 4 OAM Pinouts P12V1 logical | TODO |
| OAM_P12V2 | TP_OAM_P12V2 | OCP Table 4 OAM Pinouts P12V2 logical | TODO |
| MGMT_3V3 | TP_MGMT_3V3 | Power_System U4 LDO | 3.3V nominal — tolerance TODO |
| LOGIC_3V3 | TP_LOGIC_3V3 | Power_System U5 LDO → OAM P3V3 | TODO — OAM load unknown |
| FAN_12V | TP_FAN_12V | Power_System J2 fan rail | TODO |
| GND | TP_GND | Power return — multiple locations | 0V reference |

## PCIe — suitable for debug (test points on sheet)

- **PE_REFCLKp** (`TP_PE_REFCLKp`) — 100 MHz diff (p) — scope probe; keep stub short
- **PE_REFCLKn** (`TP_PE_REFCLKn`) — 100 MHz diff (n) — scope probe
- **PERST_N** (`TP_PERST_N`) — Active-low PCIe reset — logic analyzer
- **PRESNT_N** (`TP_PRESNT_N`) — Module presence — logic level TODO

## PCIe — NOT suitable for stub test points

- **PETp0..15 / PETn0..15** — High-speed differential — no stub TPs; probe at Mirror Mezz or host edge only
- **PERp0..15 / PERn0..15** — High-speed differential — SI probe at connector, not solder TP
- **PCIE_Ln_TX/RX_*** — Host slot lanes — same as above
- **CLKREQ_N_TODO** — TODO — not routed; no TP until verified
- **WAKE_N_TODO** — TODO — not routed

## Debug headers

- **J_I2C_DBG** (J1): 1=SCL, 2=SDA, 3=MGMT_3V3, 4=GND — nets: I2C_SCL, I2C_SDA. Carrier/expansion I2C — 2.2k pull-ups on Management R1
- **J_UART_DBG** (J2): 1=TX, 2=RX, 3=GND — nets: DBG_UART_TX, DBG_UART_RX. 3.3V UART — match Management J1 pinout

## Management debug access

- **SMBus (OAM)**: SMBUS_CLK, SMBUS_DATA, SMBUS_ALERT_N — TP_SMBUS_CLK, TP_SMBUS_DATA, TP_SMBUS_ALERT_N (OCP Table 4 OAM Pinouts — Management U4)
- **PMBus**: PMBUS_SCL, PMBUS_SDA — TP_PMBUS_SCL, TP_PMBUS_SDA (Management U3 — module addresses AMD TODO)
- **I2C expansion**: I2C_SCL, I2C_SDA — J_I2C_DBG (4-pin) (Management J2 → Expansion sheet)
- **Debug UART**: DBG_UART_TX, DBG_UART_RX — J_UART_DBG on Management J1 (primary) (Management U1 — 3.3V UART)

## Numbered bring-up checklist

| Phase | Step | Action | Stop condition |
|-------|------|--------|----------------|
| 0 | Evidence gate | Confirm OAM pin map, rail table, REFCLK guide before energizing | STOP if Wanted_Documents still missing |
| 1 | Unpowered check | Visual inspect; GND continuity at TP_GND; no short VIN→GND | STOP on short — limits TODO |
| 1 | Power — input | Apply current-limited VIN_12V; measure TP_VIN_12V | STOP — pass/fail voltage TODO |
| 1 | Power — management | Verify TP_MGMT_3V3, TP_LOGIC_3V3 with VIN present | STOP if not ~3.3V nominal (tolerance TODO) |
| 1 | Power — OAM rails | Measure TP_OAM_12V, TP_OAM_P12V1, TP_OAM_P12V2 after hot-swap enable | STOP — sequencing AMD TODO; do not enable OAM until documented |
| 1 | Power — fan | Measure TP_FAN_12V if fan rail enabled | Optional Rev1 |
| 2 | Clock | Scope TP_PE_REFCLKp/n — expect 100 MHz diff per OCP Table 4 | STOP — amplitude/jitter limits TODO (REFCLK Guide missing) |
| 2 | Reset idle | Verify TP_PERST_N asserted (low) before release | STOP — polarity/timing TODO |
| 3 | UART | Connect to Management J1 / probe TP_UART_TX/RX — MCU console if firmware present | STOP if no firmware — expected Rev1 |
| 3 | I2C scan | Use J_I2C_DBG — scan for FRU EEPROM (U2) and TMP117 (U5) addresses | STOP — addresses TODO; do not assume |
| 3 | SMBus | Probe TP_SMBUS_CLK/DATA — OAM module not installed or level shifter U4 only | STOP — OAM SMBus addresses AMD TODO |
| 3 | PMBus | Probe TP_PMBUS_SCL/SDA — module telemetry AMD TODO | STOP — no invented addresses |
| 3 | Temperature | Read TMP117 via I2C if address verified | STOP — limit thresholds TODO |
| 4 | Presence | Check TP_PRESNT_N with module seated | STOP — logic level TODO |
| 4 | PERST release | Release PERST# per AMD timing TODO after PE_REFCLK valid + OAM_PG | STOP — sequencing not documented |
| 4 | PCIe enumerate | Host BIOS/OS link training — no stub TPs on PET/PER lanes | STOP on training failure — lane map TODO |
| 5 | ROCm | After successful enumeration: rocminfo / driver load per 08_Bringup.md | Software validation only — not hardware proof |

## Placeholders replaced on Test_Points sheet

- REMOVED: OAM_MirrorMezz_Conn0_TODO (wrong sheet)
- REMOVED: MCU/FRU/TEMP embedded stubs
- REMOVED: Only 4 hierarchical labels (VIN, OAM_12V, PE_REFCLKp/n)
- ADDED: TP per primary rail (8 nets from Power_System)
- ADDED: PCIe sideband TPs (PE_REFCLKp/n, PERST_N, PRESNT_N)
- ADDED: SMBus + PMBus TPs
- ADDED: UART probe TPs + I2C debug header J1
- ADDED: Documented unsuitable HS lane TPs (PET/PER)
