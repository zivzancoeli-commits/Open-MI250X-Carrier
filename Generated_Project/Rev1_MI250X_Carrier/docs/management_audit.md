# Management Sheet — Requirements Audit

OCP reference: OCP Accelerator Module Design Specification v1.5 Table 4 OAM Pinouts (SMBus on Conn0).

## Verified prototype requirements

| Item | Source | Notes |
|------|--------|-------|
| SMBus on OAM Conn0 | OCP Accelerator Module Design Specification v1.5 Table 4 OAM Pinouts | SMBus_D, SMBus_CLK, SMB_ALERT# — OCP verified category |
| FRU EEPROM on carrier | User prototype requirement | Board identification; IPMI format TODO |
| Management MCU | User prototype requirement | I2C×2, UART; STM32G071 placeholder |
| I2C local bus | User prototype requirement | FRU + temp sensor + expansion |
| PMBus interface | User prototype requirement | Telemetry path; module devices AMD TODO |
| Temperature sensor | User prototype requirement | Carrier board temp — TMP117 class |
| Debug UART | User prototype requirement | 3.3V 3-pin header |

## Optional features (not required for Rev1 MVP)

- **I2C mux PCA9548**: DNP Rev1 — multi-OAM expansion Rev2+
- **Fan PWM/tach**: Optional until thermal/fan plan defined
- **BMC / IPMI host interface**: Not in prototype scope — no verified requirement
- **Voltage/current monitors**: INA226 etc. — not in user MVP list
- **Module firmware update path**: Indexed in repo but wiring unknown

## AMD-specific management — TODO (do not route)

- **OAM SMBus device addresses**: TODO — scan procedure and map unknown
- **OAM SMBus I/O voltage**: TODO — level shifter VCCB may be 1.8V
- **PMBus module addresses (MP2975?)**: TODO — candidate only, not verified
- **PMBus commands / telemetry registers**: TODO — no datasheet in repo
- **Conn1 GPIO management functions**: TODO — AMD-specific
- **Module vs carrier management ownership**: TODO — BMC/MCU on module unknown
- **FRU fields for MI250X compatibility**: TODO — custom carrier format
- **Firmware update / JTAG wiring**: TODO — not on Management sheet Rev1

## Architecture blocks on sheet

| Ref | Block | Category |
|-----|-------|----------|
| U1 | Mgmt_MCU_STM32G071 | verified |
| U2 | Mgmt_FRU_EEPROM | verified |
| R1 | Mgmt_I2C_Pullups | verified |
| U3 | Mgmt_PMBus_PassThrough | verified |
| U4 | Mgmt_SMBus_LevelShift | verified |
| U5 | Mgmt_Temp_TMP117 | verified |
| J1 | Mgmt_UART_Debug | verified |
| J2 | Mgmt_I2C_Exp_Connector | verified |
| U6 | Mgmt_I2C_Mux_DNP | optional |
| U7 | Mgmt_Fan_PWM_TODO | optional |
| U8 | Mgmt_AMD_SMBus_TODO | amd_todo |
| U9 | Mgmt_AMD_PMBus_TODO | amd_todo |
| U10 | Mgmt_AMD_GPIO_TODO | amd_todo |

## Placeholders replaced

- REMOVED: OAM_MirrorMezz_Conn0_TODO (wrong sheet)
- REMOVED: Embedded lib-only MCU/FRU/TEMP stubs without architecture
- REMOVED: Aggregate DBG_UART / I2C_FRU hierarchical labels
- ADDED: U1 STM32G071 management MCU with I2C1/I2C2/UART/SWD
- ADDED: U2 AT24C256 FRU EEPROM with address straps
- ADDED: R1 I2C pull-up network
- ADDED: U3 PMBus pass-through interface
- ADDED: U4 SMBus level shifter (OCP → MCU)
- ADDED: U5 TMP117 temperature sensor
- ADDED: J1 debug UART 3-pin header
- ADDED: J2 I2C expansion connector
- ADDED: U6 I2C mux DNP (optional)
- ADDED: U7 fan PWM optional block
- ADDED: U8–U10 AMD SMBus/PMBus/GPIO TODO blocks (NC)
