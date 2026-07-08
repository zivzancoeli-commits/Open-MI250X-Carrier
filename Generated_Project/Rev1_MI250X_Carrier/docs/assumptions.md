# Prototype Assumptions

These are **user-requested prototype features** or **engineering placeholders**, not verified AMD requirements.

1. **12V-only input** — OCP Conn0 also defines 54V/48V; prototype defers 54V until AMD rail table confirms need.
2. **Carrier-hosted FRU EEPROM** — User requirement; OCP does not mandate carrier FRU for minimal boot.
3. **STM32G071 management MCU** — Placeholder for I2C/PMBus/UART; part not verified against AMD firmware expectations.
4. **Direct PCIe x16** — No switch/retimer on Rev1; expansion sheet reserves DNP switch.
5. **3.3V management rail** — OCP Conn1 includes 3.3V pins; LDO from 12V input assumed.
