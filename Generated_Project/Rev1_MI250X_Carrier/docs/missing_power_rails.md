# Missing Power Rails — Verification Required

Rev1 prototype carrier. OCP reference: OCP Accelerator Module Design Specification v1.5 §8.2 Conn0/Conn1 power.
AMD MI250X rail table not in repository — do not size or sequence from guesses.

## Placeholders replaced on Power System sheet

- REMOVED: OAM_MirrorMezz_Conn0_TODO (wrong sheet)
- REMOVED: MCU_STM32G071_TODO (belongs on Management)
- REMOVED: FRU_EEPROM_AT24C256 (belongs on Management)
- REMOVED: TEMP_TMP117 (belongs on Management)
- REMOVED: Generic text-only J_PWR / U_LDO blocks
- ADDED: J1 12V input connector block
- ADDED: D1 input protection (TVS) — rating TODO
- ADDED: F1 input fuse — rating TODO
- ADDED: CB1 bulk capacitors — values TODO
- ADDED: U1 hot-swap/eFuse TPS25942 class — SOA TODO
- ADDED: U2 OAM sequencer AMD_TODO — sequencing not implemented
- ADDED: U3 P48V block — explicitly NC Rev1
- ADDED: U4 LDO 3.3V management
- ADDED: U5 LDO 3.3V logic/OAM
- ADDED: F2 fan fuse — rating TODO
- ADDED: J2 fan 12V distribution header
- ADDED: N1 OAM 12V bus P12V1/P12V2 logical split

## OCP connector rails — status

| Rail | OCP name | Voltage | Status | Source |
|------|----------|---------|--------|--------|
| P48V | P48V | 48V / 54V (OCP) | NOT ROUTED Rev1 — 12V-only input; may be required for MI250X | OCP Accelerator Module Design Specification v1.5 Table 4 Conn0 |
| P12V1 | P12V1 | 12V | Logical net OAM_P12V1 — current/pin fanout TODO | OCP Accelerator Module Design Specification v1.5 Table 4 Conn0 |
| P12V2 | P12V2 | 12V | Logical net OAM_P12V2 — split vs P12V1 TODO | OCP Accelerator Module Design Specification v1.5 Table 4 Conn0 |
| P3V3 | P3V3 | 3.3V | Carrier LOGIC_3V3 planned — load current TODO | OCP Accelerator Module Design Specification v1.5 Table 4 Conn0 |
| P3V3_CONN1 | P3V3_CONN1 | 3.3V | May share LOGIC_3V3 — Conn1 pin assignment TODO | OCP Accelerator Module Design Specification v1.5 Table 4 Conn1 |
| PVREF | PVREF / PVREF_CONN1 | Reference output from module | Module output — not a carrier supply rail | OCP Accelerator Module Design Specification v1.5 Table 4 |

## AMD / module rails — unknown

- **Standby / auxiliary**: TODO — no AMD rail table in repo
- **Module internal VRM inputs**: TODO — on-module; MP2975 candidate unverified
- **Sequencing enables (all)**: TODO — OAM_EN, P12V1_EN, P12V2_EN timing unknown
- **Power Good thresholds**: TODO — OAM_PG behavior unknown
- **12V current per rail**: TODO — fuse/hot-swap SOA cannot be sized
- **54V vs 48V nominal**: TODO — confirm MI250X OAM input requirement

## Carrier rails — architecture present, ratings TODO

- **VIN_12V**: Input connector MPN and max current TODO
- **MGMT_3V3**: LDO selected — load budget TODO
- **LOGIC_3V3**: LDO selected — OAM 3.3V load TODO
- **FAN_12V**: Fan count, current, PWM control TODO

## Power domains on sheet

| Domain | Components | Hierarchical output |
|--------|------------|---------------------|
| 12V input | J1, D1, F1, CB1 | VIN_12V (in) |
| OAM 12V | U1 hot-swap, U2 seq TODO, N1 bus | OAM_12V, OAM_P12V1, OAM_P12V2 |
| 48V OAM | U3 P48V TODO | Not routed (NC Rev1) |
| 3.3V management | U4 LDO | MGMT_3V3 |
| 3.3V logic/OAM | U5 LDO | LOGIC_3V3 |
| Fan 12V | F2, J2 | FAN_12V |
| Sequencing | U2 OAM_Seq_AMD_TODO | OAM_EN_TODO, OAM_PG_TODO |
