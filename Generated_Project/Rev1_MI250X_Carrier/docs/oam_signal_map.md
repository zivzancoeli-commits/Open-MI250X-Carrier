# OAM Signal Map (Logical — OCP Verified Names)

Physical pin numbers: **TODO** — see OAM_Pinlist_Pinmap spreadsheet.

## Connector hardware (OCP verified)

| Item | Value | Source |
|------|-------|--------|
| Connector family | Molex Mirror Mezz Pro | OCP OAM v1.5 §6.2 |
| Quantity | 2 × 688-pin | OCP OAM v1.5 §8.1 |
| MPN (examples) | 218910-1115, 218916-1115 | OCP OAM v1.5 |
| Impedance | 90 Ω ± 5% nominal | OCP OAM v1.5 |

## Conn0 — host link (OCP verified categories)

| Signal | Direction (module) | Notes |
|--------|-------------------|-------|
| PETp/n[15:0] | Output (module TX) | AC coupling on baseboard/carrier |
| PERp/n[15:0] | Input (module RX) | Host TX → module RX |
| PE_REFCLKp/n | Input | 100 MHz, PCIe Gen5 compliant per OCP Table 4 |
| PERST# | — | PCIe reset sideband |
| SMBus | — | Management |
| OAM_PRESENT# / PRESNT# | — | Presence detect |
| 12V / 54V/48V power | Input | Prototype: 12V only — 54V TODO |
| GND | — | Multiple return pins |

## Conn1 (partial — OCP verified categories)

| Signal | Notes |
|--------|-------|
| 3.3V power | Management/aux |
| JTAG | — |
| GPIO | AMD-specific usage **TODO** |
| Additional SerDes | Inter-accelerator — N/A single module Rev1 |

## AMD-specific (TODO — do not assign)

- All GPIO functions on Conn1
- Dual-GCD PCIe topology
- Module-internal PMBus device map
