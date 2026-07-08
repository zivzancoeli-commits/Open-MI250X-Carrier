# Rev1 Prototype BOM (Placeholder)

**Status:** Planning — footprints and ratings incomplete. Do not procure for production.

| Ref | Category | Value / MPN | Qty | Evidence | Notes |
|-----|----------|-------------|-----|----------|-------|
| J1, J2 | OAM connector | Molex Mirror Mezz Pro 218910-1115 or 218916-1115 | 2 | OCP OAM v1.5 §8.1 | Footprint **TODO** — import pin map |
| J3 | Host PCIe | PCIe x16 edge fingers | 1 | User req Gen4 x16 | CEM edge **TODO** mechanical |
| J4 | Power input | 12V input — MPN **TODO** | 1 | User req + OCP 12V | Match system CRPS harness |
| J5 | Debug UART | 1×3 header 2.54 mm | 1 | User req | 3.3V UART |
| Y1 | Oscillator | 100 MHz differential **TODO** | 1 | OCP PE_REFCLK Table 4 | Select after REFCLK guide |
| U1 | LDO | 3.3V management **TODO** | 1 | OCP Conn1 3.3V + mgmt | e.g. AMS1117 class — TBD |
| U2 | MCU | STM32G071 **TODO** | 1 | User req I2C/PMBus/UART | Placeholder — verify AMD fw needs |
| U3 | FRU EEPROM | AT24C256 **TODO** | 1 | User req FRU | IPMI FRU format **TODO** |
| U4 | Temp sensor | TMP117 **TODO** | 1 | User req | Board temp — placement **TODO** |
| F1 | Fuse | Rating **TODO** | 1 | Inferred protection | Size after 12V current **TODO** |
| — | Caps / resistors | Per IC datasheets | — | Design rules | Local decoupling required |
| U5 | PCIe switch | DNP | 0 | Expansion sheet | Future multi-OAM |
