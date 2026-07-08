# Open Questions / TODO

## OAM connector (P0)

- [ ] Import OAM_Pinlist_Pinmap spreadsheet — assign physical Mirror Mezz pin numbers
- [ ] Confirm Molex MPN 218910-1115 vs 218916-1115 for MI250X module revision
- [ ] Classify AMD-specific GPIO/sidebands not in OCP Table 4

## Power (P0)

- [ ] MI250X 12V current, sequencing, enable/PG signals
- [ ] 54V/48V pin requirement for MI250X — energize or NC?
- [ ] PMBus addresses for module VRM telemetry

## PCIe (P0)

- [ ] MI250X lane map: 1x16 vs 2x8 per GCD
- [ ] CLKREQ# / WAKE# pin assignments
- [ ] Host slot on X11DPH-T

## Management (P1)

- [ ] SMBus voltage level and pull-ups on OAM
- [ ] FRU EEPROM contents and IPMI compatibility
- [ ] Whether AMD firmware tools require carrier-side storage

## Mechanical / thermal (P1)

- [ ] Connector footprint and stack-up from Molex drawing
- [ ] Heatsink retention and TDP limits
