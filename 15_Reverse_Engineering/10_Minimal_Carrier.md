# Minimal Carrier

## Purpose

Define the smallest carrier-board concept that could operate one AMD Instinct MI250X OAM module using only repository-supported evidence. This document is a requirements and design-gate reference, not a schematic, layout, BOM, connector footprint, firmware architecture, or mechanical drawing.

The smallest valid carrier is a one-module carrier that removes every optional block until a source proves it is required. It still must provide the verified or inferred functions needed to mate to, power, cool, communicate with, and mechanically support one MI250X OAM module. All implementation details that are not documented in readable repository sources remain `Unknown`.

## Design Position

| Item | Minimal-carrier decision | Evidence status | Sources |
|---|---|---|---|
| Target module | Support one AMD Instinct MI250X OAM module. | Verified target context. | `13_Reference_Docs/ROCm/Overview.md`; `15_Reverse_Engineering/07_Component_ID.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| Scale | First carrier is single-module only; 2-, 4-, 8-, and possible 16-module planning must not add hardware to the smallest one-module carrier unless it is required for one module. | Inferred from project expansion goals and minimal-carrier scope. | `17_System_Architecture/04_Future_Expansion.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| Schematic status | The current repository does not contain enough verified connector, power, clock, PCIe, management, cooling, or mechanical evidence to draw a safe schematic. | Verified blocker. | `09_AI_Notes/10_Design_Checklist.md`; `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `15_Reverse_Engineering/08_Bringup.md` |
| Optional-block rule | Switches, retimers, redrivers, management MCU/BMC, EEPROM/FRU, sensors, fan controller, firmware flashing hardware, debug headers, and extra debug devices stay out of the smallest carrier until sourced requirements prove they are needed. | Inferred minimal design rule. | `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `15_Reverse_Engineering/04_Management.md`; `15_Reverse_Engineering/05_PCIe.md`; `15_Reverse_Engineering/07_Component_ID.md` |

## Required Interfaces

| Interface | Smallest carrier requirement | What remains unknown | Sources |
|---|---|---|---|
| OAM mating interface | Include the physical and electrical mating interface for the MI250X OAM module after connector type, pin count, pinout, mating height, stack-up, footprint, and mechanical envelope are verified. | Connector manufacturer, family, part number, pin count, pinout, current rating, mating height, stack-up, footprint, and AMD-specific pins. | `13_Reference_Docs/ROCm/Overview.md`; `02_AMD_Docs/GitHub_Links.rtf`; `15_Reverse_Engineering/01_OAM_Pin_Mapping.md` |
| Power interface | Provide the required MI250X/OAM input power, ground, enables, Power Good, protection, telemetry, and sequencing only after requirements are verified. | Rail names, voltages, currents, power pins, ground pins, current sharing, input power, connector rating, protection, PMBus, monitoring, and startup/shutdown order. | `15_Reverse_Engineering/02_Power_Rails.md`; `18_Component_Research/02_Power_Converters.md`; `18_Component_Research/09_Power_Connectors.md` |
| Host communication interface | Provide the host-facing interface needed for enumeration and ROCm/software use after the MI250X OAM host interface is verified. | PCIe generation, lane width, lane map, sidebands, reset, REFCLK, routing topology, switch/retimer/redriver need, and signal-integrity constraints. | `15_Reverse_Engineering/05_PCIe.md`; `13_Reference_Docs/ROCm/Overview.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| Clock and reset interface | Provide only the reference clocks and reset behavior that verified OAM/MI250X/host-link sources require. | REFCLK frequency, source, topology, routing, jitter, skew, clock generator/buffer/oscillator need, reset signal names, polarity, timing, and Power Good relationship. | `15_Reverse_Engineering/03_Clock_Tree.md`; `15_Reverse_Engineering/05_PCIe.md`; `15_Reverse_Engineering/08_Bringup.md` |
| Cooling interface | Provide a thermal solution sufficient for MI250X operation after thermal and mechanical requirements are verified. | Thermal design power, heatsink/cold-plate geometry, airflow/coolant requirement, thermal keepouts, mounting force, fan-control ownership, and sensor placement. | `15_Reverse_Engineering/06_Mechanical.md`; `18_Component_Research/07_Fan_Control.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| Mechanical support | Support the OAM module, connector, carrier PCB, retention hardware, and cooling hardware using verified mechanical data. | Module dimensions, board outline, mounting holes, standoff height, connector coordinates, PCB thickness, keepouts, weight, and tolerances. | `15_Reverse_Engineering/06_Mechanical.md`; `09_AI_Notes/08_Mechanical.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| PCB implementation | Implement the verified connector, power distribution, host-link routing, clocks, resets, mechanical support, thermal keepouts, and test access. | Stack-up, impedance, length matching, loss budget, plane requirements, connector footprint, high-current copper, keepouts, and fabrication constraints. | `09_AI_Notes/10_Design_Checklist.md`; `15_Reverse_Engineering/09_Block_Diagram.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |

## Optional Interfaces

| Interface or block | Smallest-carrier position | Why optional now | Sources |
|---|---|---|---|
| PCIe switch | Exclude unless verified topology requires it. | No readable source proves a switch is required for one MI250X module. | `15_Reverse_Engineering/05_PCIe.md`; `18_Component_Research/08_PCIe_Retimers.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| PCIe retimer or redriver | Exclude unless verified signal-integrity analysis or a routing guide requires it. | PCIe Routing Guide is missing, and no retimer/redriver requirement or part number is documented. | `15_Reverse_Engineering/05_PCIe.md`; `18_Component_Research/08_PCIe_Retimers.md`; `15_Reverse_Engineering/07_Component_ID.md` |
| Carrier-side management MCU or BMC | Exclude unless a source proves carrier-side management is required. | Management ownership could be carrier-side, baseboard-side, host-side, module-side, external, or absent; no controller requirement is verified. | `15_Reverse_Engineering/04_Management.md`; `18_Component_Research/05_Management_MCU.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| EEPROM or FRU EEPROM | Exclude unless a source proves the carrier must provide identity, FRU, configuration, or firmware storage. | Requirement, bus, address, contents, ownership, and write protection are undocumented. | `15_Reverse_Engineering/04_Management.md`; `18_Component_Research/04_EEPROM_FRU.md`; `15_Reverse_Engineering/07_Component_ID.md` |
| Temperature, voltage, current, and fault sensors | Exclude or reserve footprints only after requirements are verified. | Carrier-visible sensor requirements, locations, limits, bus ownership, and part numbers are undocumented. | `15_Reverse_Engineering/04_Management.md`; `18_Component_Research/06_Temperature_Sensors.md`; `15_Reverse_Engineering/07_Component_ID.md` |
| Fan controller | Exclude unless the cooling method requires carrier-side fan control. | Fan-control ownership, PWM/tachometer signals, fan headers, and cooling-control policy are undocumented. | `18_Component_Research/07_Fan_Control.md`; `15_Reverse_Engineering/04_Management.md`; `15_Reverse_Engineering/06_Mechanical.md` |
| Firmware flashing hardware | Exclude unless the firmware-update path requires carrier hardware. | Firmware tools and update guides are indexed, but hardware dependencies, storage, controller role, and procedure are not extracted. | `13_Reference_Docs/Reference_Index.rtf`; `15_Reverse_Engineering/04_Management.md`; `18_Component_Research/04_EEPROM_FRU.md` |
| Debug LEDs / USB debug / generic debug headers | Exclude from the required set; add only if later bring-up requirements justify them. | Current engineering notes do not cite a requirement for these features. | `15_Reverse_Engineering/07_Component_ID.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |

## Power

| Power design item | Smallest carrier requirement | Unknowns blocking implementation | Sources |
|---|---|---|---|
| Input power | Provide whatever input power the verified MI250X/OAM carrier requirement demands. | Input voltage, connector type, current, cable assembly, baseboard power ownership, fusing, hot-swap, inrush, current limiting, and protection. | `15_Reverse_Engineering/02_Power_Rails.md`; `18_Component_Research/09_Power_Connectors.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| Rail generation | Generate only verified required rails. | Rail names, voltages, current limits, tolerances, sequencing, regulators, power stages, controller topology, and rail ownership. | `15_Reverse_Engineering/02_Power_Rails.md`; `18_Component_Research/02_Power_Converters.md` |
| Power pins and ground pins | Connect only verified OAM power and ground pins. | Pin assignments, current sharing, return-current strategy, current rating, and connector grouping. | `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `18_Component_Research/01_OAM_Connector.md`; `18_Component_Research/09_Power_Connectors.md` |
| Sequencing | Implement verified power-up, power-down, enable, Power Good, and reset-gating behavior. | Startup order, shutdown order, enable names, polarity, timing, Power Good thresholds, and fault behavior. | `15_Reverse_Engineering/02_Power_Rails.md`; `15_Reverse_Engineering/08_Bringup.md`; `18_Component_Research/02_Power_Converters.md` |
| PMBus / telemetry | Include only if verified rail control or health requirements need it. | PMBus controller identity, topology, addresses, commands, telemetry registers, fault registers, pullups, isolation, and firmware owner. | `15_Reverse_Engineering/04_Management.md`; `18_Component_Research/05_Management_MCU.md`; `15_Reverse_Engineering/02_Power_Rails.md` |
| MP2975 | Treat as a research lead, not a design part. | Presence, role, pins, package, rails controlled, PMBus behavior, power-stage pairing, and datasheet are not verified. | `13_Reference_Docs/Component_Index.rtf`; `15_Reverse_Engineering/07_Component_ID.md`; `18_Component_Research/02_Power_Converters.md` |

## Clock

| Clock design item | Smallest carrier requirement | Unknowns blocking implementation | Sources |
|---|---|---|---|
| REFCLK | Provide or route only the verified REFCLK required by the host link and OAM interface. | Source, frequency, topology, electrical standard, connector pins, jitter, skew, termination, spread spectrum, and validation method. | `15_Reverse_Engineering/03_Clock_Tree.md`; `15_Reverse_Engineering/05_PCIe.md`; `18_Component_Research/03_Clock_Generators.md` |
| Clock source ownership | Keep carrier-generated, host-supplied, baseboard-supplied, buffered, or module-supplied clocking open until sourced. | No readable source identifies clock ownership. | `15_Reverse_Engineering/03_Clock_Tree.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| Clock components | Do not select oscillator, clock generator, PLL, or buffer until required. | Manufacturer, part number, package, rail, output standard, fanout, programming, jitter, skew, and placement. | `15_Reverse_Engineering/07_Component_ID.md`; `18_Component_Research/03_Clock_Generators.md`; `18_Component_Research/10_BOM.md` |
| Reset-clock relationship | Release reset only after verified power, Power Good, and clock-valid relationships are known. | Reset signal names, polarity, timing, Power Good dependency, REFCLK dependency, and enumeration dependency. | `15_Reverse_Engineering/03_Clock_Tree.md`; `15_Reverse_Engineering/05_PCIe.md`; `15_Reverse_Engineering/08_Bringup.md` |

## Management

| Management item | Smallest carrier requirement | Unknowns blocking implementation | Sources |
|---|---|---|---|
| Management ownership | Do not add a carrier MCU/BMC unless a source proves the carrier owns management. | Whether management is carrier-side, host-side, baseboard-side, module-side, external, or not required. | `15_Reverse_Engineering/04_Management.md`; `18_Component_Research/05_Management_MCU.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| SMBus / I2C | Do not assign management buses until required pins, owner, topology, voltage, pullups, and addresses are known. | Bus requirement, device list, connector pins, bus speed, voltage levels, pullups, addresses, isolation, and hot-plug behavior. | `15_Reverse_Engineering/04_Management.md`; `18_Component_Research/04_EEPROM_FRU.md`; `18_Component_Research/05_Management_MCU.md` |
| PMBus | Keep PMBus as an investigation path tied to power telemetry and VRM research. | Controller identity, addresses, commands, telemetry registers, fault registers, and firmware behavior. | `Wanted_Documents.md`; `15_Reverse_Engineering/04_Management.md`; `15_Reverse_Engineering/02_Power_Rails.md` |
| GPIO / reset / enables / interrupts | Do not create carrier GPIO nets until verified. | Required signal names, directions, voltage levels, pullups, polarity, timing, and ownership. | `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `15_Reverse_Engineering/04_Management.md`; `18_Component_Research/05_Management_MCU.md` |
| Firmware and health hooks | Add only if firmware-update or health-check sources require carrier hardware. | Firmware update flow, storage, recovery, health-check telemetry, pass/fail criteria, and management interface. | `13_Reference_Docs/Reference_Index.rtf`; `15_Reverse_Engineering/04_Management.md`; `15_Reverse_Engineering/08_Bringup.md` |

## PCIe

| PCIe design item | Smallest carrier requirement | Unknowns blocking implementation | Sources |
|---|---|---|---|
| Host link | Provide the verified host-facing link needed for one MI250X OAM module. | Whether the carrier uses direct PCIe, switch, retimer, redriver, cable/riser, baseboard-specific topology, or another topology. | `15_Reverse_Engineering/05_PCIe.md`; `15_Reverse_Engineering/09_Block_Diagram.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| Lane map | Do not route lanes until verified. | PCIe generation, lane width, lane order, TX/RX direction, connector pins, polarity, lane reversal, bifurcation, and per-GCD mapping. | `15_Reverse_Engineering/05_PCIe.md`; `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `18_Component_Research/08_PCIe_Retimers.md` |
| Sidebands | Implement only verified sidebands. | PERST#, CLKREQ#, WAKE#, reset signals, polarity, voltage levels, pin assignments, timing, pullups, and owner. | `15_Reverse_Engineering/05_PCIe.md`; `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `15_Reverse_Engineering/08_Bringup.md` |
| Signal integrity | Do not choose layer stack, impedance, AC-coupling, length matching, loss budget, or equalization without a source. | PCIe Routing Guide is missing; equalization and routing constraints are undocumented. | `Wanted_Documents.md`; `15_Reverse_Engineering/05_PCIe.md`; `18_Component_Research/08_PCIe_Retimers.md` |
| Switch / retimer / redriver | Keep out of the smallest carrier unless required by verified topology or signal-integrity analysis. | Requirement, part number, lane count, placement, clocking, reset, power rails, management, and settings. | `15_Reverse_Engineering/05_PCIe.md`; `18_Component_Research/08_PCIe_Retimers.md`; `18_Component_Research/10_BOM.md` |

## Cooling

| Cooling item | Smallest carrier requirement | Unknowns blocking implementation | Sources |
|---|---|---|---|
| Cooling method | Provide the verified thermal solution required for one MI250X OAM module. | Air vs liquid vs cold plate, thermal design power, allowable temperatures, airflow/coolant requirements, and validation criteria. | `15_Reverse_Engineering/06_Mechanical.md`; `18_Component_Research/07_Fan_Control.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| Heatsink / cold plate | Do not design mechanical interface until sourced. | Geometry, mounting, force, thermal interface, weight, keepout, retention, and part number. | `Wanted_Documents.md`; `15_Reverse_Engineering/06_Mechanical.md`; `18_Component_Research/10_BOM.md` |
| Fan control | Exclude carrier fan controller unless cooling requirements prove carrier-side control is needed. | Fan quantity, voltage, current, PWM, tachometer, fault, presence, headers, firmware owner, and fail-safe behavior. | `18_Component_Research/07_Fan_Control.md`; `15_Reverse_Engineering/04_Management.md`; `18_Component_Research/10_BOM.md` |
| Thermal monitoring | Include only verified sensor paths. | Junction-temperature path, board-temperature sensors, locations, limits, bus ownership, alert behavior, and health-check use. | `15_Reverse_Engineering/04_Management.md`; `18_Component_Research/06_Temperature_Sensors.md`; `15_Reverse_Engineering/08_Bringup.md` |

## Mechanical

| Mechanical item | Smallest carrier requirement | Unknowns blocking implementation | Sources |
|---|---|---|---|
| Board outline | Define only from verified OAM/baseboard/mechanical data. | Module dimensions, carrier outline, baseboard envelope, service envelope, and chassis constraints. | `15_Reverse_Engineering/06_Mechanical.md`; `09_AI_Notes/08_Mechanical.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| Connector placement | Place connector only after verified coordinates, footprint, and stack-up. | Connector center coordinates, pin-1 datum, orientation, mating height, body height, placement tolerance, and keepout. | `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `15_Reverse_Engineering/06_Mechanical.md`; `18_Component_Research/01_OAM_Connector.md` |
| Mounting and retention | Support module and cooling assembly from verified drawings. | Hole count, hole coordinates, fasteners, standoff height, retention hardware, mounting force, weight, and shock/handling constraints. | `15_Reverse_Engineering/06_Mechanical.md`; `18_Component_Research/10_BOM.md`; `09_AI_Notes/10_Design_Checklist.md` |
| PCB stack-up | Choose stack-up only after high-speed, power, connector, and mechanical constraints are known. | Layer count, thickness, impedance, power-plane copper, loss budget, connector footprint constraints, and fabrication rules. | `09_AI_Notes/10_Design_Checklist.md`; `15_Reverse_Engineering/05_PCIe.md`; `15_Reverse_Engineering/06_Mechanical.md` |
| Keepouts | Keepouts must include OAM module, connector, cooling, component height, service, and chassis constraints once verified. | All keepout dimensions are undocumented. | `15_Reverse_Engineering/06_Mechanical.md`; `18_Component_Research/07_Fan_Control.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |

## EEPROM

| EEPROM item | Smallest carrier position | Unknowns blocking implementation | Sources |
|---|---|---|---|
| EEPROM requirement | Optional until a readable source proves the carrier must provide one. | Whether EEPROM is carrier-side, module-side, baseboard-side, host-side, BMC-side, MCU-side, or absent. | `15_Reverse_Engineering/04_Management.md`; `18_Component_Research/04_EEPROM_FRU.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| FRU EEPROM | Optional until a source proves FRU identity storage is required. | FRU format, contents, owner, bus, address, write-protect, provisioning, and validation role. | `15_Reverse_Engineering/04_Management.md`; `18_Component_Research/04_EEPROM_FRU.md`; `18_Component_Research/10_BOM.md` |
| Firmware storage / SPI flash | Optional until firmware-update path requires it. | Storage type, bus, address, contents, update process, security, recovery, and owner. | `15_Reverse_Engineering/04_Management.md`; `18_Component_Research/04_EEPROM_FRU.md`; `13_Reference_Docs/Reference_Index.rtf` |

## Debug Headers

| Debug item | Smallest carrier position | Unknowns blocking implementation | Sources |
|---|---|---|---|
| Management access header | Recommended investigation provision only after nets are identified. | Which buses or signals require access, connector type, voltage levels, pullups, isolation, and ownership. | `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `15_Reverse_Engineering/04_Management.md`; `18_Component_Research/05_Management_MCU.md` |
| JTAG / UART / SPI debug | Optional until firmware, management, or programming requirements prove them necessary. | Required protocols, owners, voltage levels, pin assignments, connector type, and access policy. | `15_Reverse_Engineering/04_Management.md`; `18_Component_Research/05_Management_MCU.md`; `13_Reference_Docs/Reference_Index.rtf` |
| USB debug | Not required by current evidence. | No readable source identifies a USB debug requirement. | `15_Reverse_Engineering/07_Component_ID.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| Debug LEDs | Not required by current evidence. | No readable source identifies required LED signals, colors, polarity, or firmware behavior. | `15_Reverse_Engineering/07_Component_ID.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| Generic debug headers | Optional only if later bring-up evidence requires them. | Header signals, voltage levels, protection, connector type, placement, and use cases. | `15_Reverse_Engineering/07_Component_ID.md`; `15_Reverse_Engineering/08_Bringup.md`; `09_AI_Notes/10_Design_Checklist.md` |

## Test Points

| Test-point category | Smallest carrier requirement | Unknowns blocking placement | Sources |
|---|---|---|---|
| Power test points | Provide measurement access only for verified rails, enables, Power Good, protection, and telemetry signals. | Rail names, safe measurement points, expected values, current limits, thresholds, and sequencing. | `15_Reverse_Engineering/02_Power_Rails.md`; `15_Reverse_Engineering/08_Bringup.md`; `09_AI_Notes/10_Design_Checklist.md` |
| Clock test points | Provide only if clock requirements and measurement method allow it. | REFCLK source, electrical standard, measurement point, loading limits, frequency, jitter/skew limits, and reset-clock dependency. | `15_Reverse_Engineering/03_Clock_Tree.md`; `18_Component_Research/03_Clock_Generators.md`; `15_Reverse_Engineering/08_Bringup.md` |
| Reset and sideband test points | Provide only for verified reset/sideband nets. | PERST#, CLKREQ#, WAKE#, reset ownership, polarity, voltage, timing, and connector pins. | `15_Reverse_Engineering/05_PCIe.md`; `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `15_Reverse_Engineering/08_Bringup.md` |
| Management-bus test points | Provide only for verified SMBus/I2C/PMBus or other management nets. | Bus owner, voltage, pullups, addresses, topology, isolation, and commands. | `15_Reverse_Engineering/04_Management.md`; `18_Component_Research/05_Management_MCU.md`; `18_Component_Research/04_EEPROM_FRU.md` |
| Sensor and thermal test points | Provide only for verified sensors or telemetry paths. | Sensor locations, limits, bus path, ownership, and health-check criteria. | `15_Reverse_Engineering/04_Management.md`; `18_Component_Research/06_Temperature_Sensors.md`; `18_Component_Research/07_Fan_Control.md` |
| PCIe test fixtures | Do not add intrusive test access unless routing and compliance sources permit it. | Allowed probing method, insertion loss, impedance, fixture type, equalization, and compliance criteria. | `15_Reverse_Engineering/05_PCIe.md`; `18_Component_Research/08_PCIe_Retimers.md`; `Wanted_Documents.md` |

## Unknown Requirements

| Unknown area | Missing requirement | Why it blocks the smallest carrier | Sources |
|---|---|---|---|
| OAM connector | Connector identity, pinout, power/ground pins, sidebands, clocks, management pins, reserved pins, footprint, and stack-up. | The carrier cannot mate electrically or mechanically without it. | `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `18_Component_Research/01_OAM_Connector.md`; `Wanted_Documents.md` |
| Power | Rail names, voltages, currents, input power, sequencing, enables, Power Good, PMBus, telemetry, protection, and current sharing. | Wrong power design could prevent operation or damage hardware. | `15_Reverse_Engineering/02_Power_Rails.md`; `18_Component_Research/02_Power_Converters.md`; `18_Component_Research/09_Power_Connectors.md` |
| Clock and reset | REFCLK source/frequency/topology, jitter/skew, reset signal names, timing, and power-clock-reset relationships. | PCIe enumeration depends on unresolved clock and reset requirements. | `15_Reverse_Engineering/03_Clock_Tree.md`; `15_Reverse_Engineering/05_PCIe.md`; `15_Reverse_Engineering/08_Bringup.md` |
| PCIe | Generation, lane width, lane map, topology, sidebands, routing constraints, switch/retimer/redriver need, equalization, and compliance. | Host communication and software use cannot be designed or validated without it. | `15_Reverse_Engineering/05_PCIe.md`; `18_Component_Research/08_PCIe_Retimers.md`; `13_Reference_Docs/ROCm/Overview.md` |
| Management | Ownership, buses, addresses, GPIO, interrupts, firmware hooks, health monitoring, PMBus, EEPROM, sensors, and fan control. | Bring-up and health validation may require interfaces not yet identified. | `15_Reverse_Engineering/04_Management.md`; `18_Component_Research/05_Management_MCU.md`; `13_Reference_Docs/Reference_Index.rtf` |
| EEPROM / FRU | Requirement, owner, bus, address, contents, write protection, provisioning, and validation role. | Board identity or configuration storage cannot be added or omitted safely until sourced. | `15_Reverse_Engineering/04_Management.md`; `18_Component_Research/04_EEPROM_FRU.md` |
| Cooling | Cooling method, TDP, thermal interface, airflow/coolant, heatsink/cold plate, fan control, sensors, and thermal limits. | The module cannot be operated safely without verified thermal constraints. | `15_Reverse_Engineering/06_Mechanical.md`; `18_Component_Research/07_Fan_Control.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| Mechanical | Dimensions, board outline, connector coordinates, mounting pattern, PCB thickness, standoffs, keepouts, weight, and tolerances. | PCB layout, connector footprint, mounting, and cooling cannot be completed without dimensions. | `15_Reverse_Engineering/06_Mechanical.md`; `09_AI_Notes/08_Mechanical.md`; `09_AI_Notes/10_Design_Checklist.md` |
| Debug and test | Required debug headers, test points, pass/fail values, safe probing methods, and validation fixtures. | Bring-up access must not load or expose unknown nets incorrectly. | `15_Reverse_Engineering/08_Bringup.md`; `15_Reverse_Engineering/07_Component_ID.md`; `09_AI_Notes/10_Design_Checklist.md` |

## Complete Engineering Checklist

### Evidence Gate

- [ ] Confirm the exact MI250X module/revision to be supported. Sources: `13_Reference_Docs/ROCm/Overview.md`; `15_Reverse_Engineering/07_Component_ID.md`.
- [ ] Obtain and extract OAM connector, baseboard, mechanical, PCIe routing, REFCLK, power, PMBus/VRM, and thermal source documents. Sources: `Wanted_Documents.md`; `09_AI_Notes/10_Design_Checklist.md`.
- [ ] Locate usable front, back, connector, heatsink, and baseboard photos or document that they remain unavailable. Sources: `Wanted_Documents.md`; `15_Reverse_Engineering/06_Mechanical.md`.
- [ ] Confirm all candidate components visually or from readable source documents before BOM entry. Sources: `13_Reference_Docs/Component_Index.rtf`; `15_Reverse_Engineering/07_Component_ID.md`.

### Interface Checklist

- [ ] Verify OAM connector manufacturer, family, part number, pin count, pinout, footprint, mating height, stack-up, current rating, and keepouts. Sources: `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `18_Component_Research/01_OAM_Connector.md`.
- [ ] Separate OAM-standard and AMD-specific signals from sourced pinout evidence. Sources: `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`.
- [ ] Identify every required, optional, reserved, no-connect, and vendor-specific connector pin before schematic capture. Sources: `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `18_Component_Research/01_OAM_Connector.md`.

### Power Checklist

- [ ] Build a sourced rail table with rail name, voltage, current, tolerance, purpose, source, load, and measurement point. Sources: `15_Reverse_Engineering/02_Power_Rails.md`; `18_Component_Research/02_Power_Converters.md`.
- [ ] Verify input power source, connector, cable assembly, current rating, fusing, hot-swap/inrush, and protection. Sources: `18_Component_Research/09_Power_Connectors.md`; `15_Reverse_Engineering/02_Power_Rails.md`.
- [ ] Verify OAM power pins, ground pins, current sharing, return-current strategy, and connector current rating. Sources: `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `18_Component_Research/09_Power_Connectors.md`.
- [ ] Verify startup order, shutdown order, enables, Power Good, reset gating, clock dependency, fault handling, and recovery behavior. Sources: `15_Reverse_Engineering/02_Power_Rails.md`; `15_Reverse_Engineering/08_Bringup.md`.
- [ ] Confirm or reject MP2975 and any power stages from visual/source evidence before using them. Sources: `13_Reference_Docs/Component_Index.rtf`; `15_Reverse_Engineering/07_Component_ID.md`.

### Clock And Reset Checklist

- [ ] Verify REFCLK source, frequency, topology, electrical standard, connector pins, routing, jitter, skew, and validation method. Sources: `15_Reverse_Engineering/03_Clock_Tree.md`; `18_Component_Research/03_Clock_Generators.md`.
- [ ] Determine whether the carrier generates, receives, buffers, or only routes clocks. Sources: `15_Reverse_Engineering/03_Clock_Tree.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`.
- [ ] Verify oscillator, clock generator, PLL, or clock buffer requirements before selecting parts. Sources: `15_Reverse_Engineering/07_Component_ID.md`; `18_Component_Research/03_Clock_Generators.md`.
- [ ] Verify reset signal names, polarity, timing, owner, Power Good dependency, and REFCLK dependency. Sources: `15_Reverse_Engineering/05_PCIe.md`; `15_Reverse_Engineering/08_Bringup.md`.

### PCIe Checklist

- [ ] Verify host topology for one module: direct link, switch, retimer, redriver, cable/riser, baseboard-specific path, or another sourced topology. Sources: `15_Reverse_Engineering/05_PCIe.md`; `15_Reverse_Engineering/09_Block_Diagram.md`.
- [ ] Verify PCIe generation, lane width, lane order, TX/RX direction, polarity, bifurcation, and connector pins. Sources: `15_Reverse_Engineering/05_PCIe.md`; `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`.
- [ ] Verify PERST#, CLKREQ#, WAKE#, reset, and any other sideband pin assignments and behavior. Sources: `15_Reverse_Engineering/05_PCIe.md`; `18_Component_Research/08_PCIe_Retimers.md`.
- [ ] Obtain routing constraints for impedance, loss, length matching, AC-coupling, equalization, vias, return path, and compliance. Sources: `Wanted_Documents.md`; `18_Component_Research/08_PCIe_Retimers.md`.
- [ ] Add switch, retimer, or redriver only if verified topology or signal-integrity evidence requires it. Sources: `15_Reverse_Engineering/05_PCIe.md`; `18_Component_Research/08_PCIe_Retimers.md`.

### Management And EEPROM Checklist

- [ ] Determine whether carrier-side management MCU/BMC is required or whether management belongs elsewhere. Sources: `15_Reverse_Engineering/04_Management.md`; `18_Component_Research/05_Management_MCU.md`.
- [ ] Verify SMBus, I2C, PMBus, SPI, JTAG, UART, GPIO, reset, interrupt, enable, Power Good, telemetry, and fan-control pins before assigning nets. Sources: `15_Reverse_Engineering/04_Management.md`; `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`.
- [ ] Verify PMBus devices, addresses, commands, telemetry registers, fault registers, pullups, isolation, and firmware ownership. Sources: `Wanted_Documents.md`; `15_Reverse_Engineering/04_Management.md`.
- [ ] Determine whether EEPROM, FRU EEPROM, I2C EEPROM, SPI flash, firmware storage, or no storage is required. Sources: `18_Component_Research/04_EEPROM_FRU.md`; `15_Reverse_Engineering/04_Management.md`.
- [ ] If EEPROM/FRU is required, verify part type, bus, address, contents, write protection, provisioning, and validation role. Sources: `18_Component_Research/04_EEPROM_FRU.md`; `13_Reference_Docs/Reference_Index.rtf`.

### Cooling And Mechanical Checklist

- [ ] Verify thermal design power, thermal limits, cooling method, heatsink/cold-plate interface, airflow/coolant, and validation criteria. Sources: `15_Reverse_Engineering/06_Mechanical.md`; `18_Component_Research/07_Fan_Control.md`.
- [ ] Verify fan-control ownership and whether a carrier fan controller or fan header is required. Sources: `18_Component_Research/07_Fan_Control.md`; `15_Reverse_Engineering/04_Management.md`.
- [ ] Verify module dimensions, board outline, connector coordinates, mounting holes, standoff height, PCB thickness, keepouts, weight, and tolerances. Sources: `15_Reverse_Engineering/06_Mechanical.md`; `09_AI_Notes/08_Mechanical.md`.
- [ ] Create connector footprint, board outline, mounting, and 3D/mechanical models only after verified dimensions exist. Sources: `09_AI_Notes/10_Design_Checklist.md`; `18_Component_Research/01_OAM_Connector.md`.
- [ ] Validate cooling and mechanical support before sustained operation. Sources: `15_Reverse_Engineering/08_Bringup.md`; `15_Reverse_Engineering/06_Mechanical.md`.

### Debug And Test Checklist

- [ ] Define power, clock, reset, sideband, management, sensor, and thermal test points only after net names and safe measurement methods are verified. Sources: `15_Reverse_Engineering/08_Bringup.md`; `09_AI_Notes/10_Design_Checklist.md`.
- [ ] Add management/debug headers only after required protocols, voltage levels, ownership, and connector pins are known. Sources: `15_Reverse_Engineering/04_Management.md`; `18_Component_Research/05_Management_MCU.md`.
- [ ] Do not add USB debug, debug LEDs, or generic debug headers unless later requirements justify them. Sources: `15_Reverse_Engineering/07_Component_ID.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`.
- [ ] Define bring-up pass/fail criteria for all test points before applying power. Sources: `15_Reverse_Engineering/08_Bringup.md`; `15_Reverse_Engineering/02_Power_Rails.md`.

### Release Gate

- [ ] Confirm every required interface has a source-backed schematic symbol, footprint, constraint, and validation method. Sources: `09_AI_Notes/10_Design_Checklist.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`.
- [ ] Confirm every optional interface is either omitted with justification or included with a sourced requirement. Sources: `15_Reverse_Engineering/04_Management.md`; `15_Reverse_Engineering/05_PCIe.md`.
- [ ] Confirm no rail value, current value, timing value, bus address, part number, connector pin, mechanical dimension, or cooling limit was invented. Sources: `README.md`; `AI_TASKS.md`.
- [ ] Confirm the first prototype is documented as a one-MI250X carrier and does not include scale-out-only hardware. Sources: `17_System_Architecture/04_Future_Expansion.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`.

## Sources

- `README.md` - States the public-evidence workflow and that undocumented behavior should be tracked rather than assumed.
- `AI_TASKS.md` - Lists power-up testing, voltage validation, clock validation, PCIe enumeration, GPU initialization, ROCm detection, stress testing, thermal testing, signal integrity, long-duration testing, and validation tasks.
- `Wanted_Documents.md` - Tracks missing Connector Specification, Baseboard Specification, PCIe Routing Guide, REFCLK Guide, PMBus Controller Datasheet, VRM Datasheet, OAM Thermal Guidelines, heatsink photo, and baseboard photo.
- `02_AMD_Docs/GitHub_Links.rtf` - Links the official OAM specification and identifies connector, mechanical, and power relevance.
- `13_Reference_Docs/Component_Index.rtf` - Identifies MP2975 as a low-confidence candidate and records the missing public datasheet.
- `13_Reference_Docs/Reference_Index.rtf` - Indexes OAM/OCP, firmware tools, firmware update guides, MI250 acceptance, health checks, system validation, AMD lab notes, GPU management, Molex, and cooling references.
- `13_Reference_Docs/ROCm/Overview.md` - Identifies MI250/MI250X as OCP Accelerator Modules with two GCDs, 128 GB total memory, and two software-visible devices; provides ROCm validation context.
- `09_AI_Notes/08_Mechanical.md` - Summarizes mechanical connector, board outline, mounting, keepout, and Mirror Mezz reference gaps.
- `09_AI_Notes/10_Design_Checklist.md` - States that schematic capture and PCB layout must wait for connector, PCIe/REFCLK, power, management, mechanical, baseboard, and high-speed constraints.
- `15_Reverse_Engineering/01_OAM_Pin_Mapping.md` - Main source for OAM connector, pinout, signal-category, power, ground, PCIe, sideband, clock, management, reserved, and unknown-pin gaps.
- `15_Reverse_Engineering/02_Power_Rails.md` - Main source for power rails, voltages, currents, sequencing, enables, Power Good, PMBus, telemetry, monitoring, protection, and startup-order gaps.
- `15_Reverse_Engineering/03_Clock_Tree.md` - Main source for REFCLK, oscillator, clock generator, PLL, clock buffer, fanout, routing, frequency, jitter, skew, synchronization, and reset-interaction gaps.
- `15_Reverse_Engineering/04_Management.md` - Main source for SMBus, I2C, PMBus, BMC, MCU, EEPROM, FRU EEPROM, temperature sensors, voltage monitoring, firmware update, and health-monitoring gaps.
- `15_Reverse_Engineering/05_PCIe.md` - Main source for PCIe generation, lane count, lane routing, REFCLK, PERST#, CLKREQ#, WAKE#, lane polarity, retimers, switches, equalization, and routing constraints.
- `15_Reverse_Engineering/06_Mechanical.md` - Main source for module dimensions, connector locations, mounting holes, PCB thickness, cooling envelope, weight, heatsink, keepouts, connector height, and mechanical tolerance gaps.
- `15_Reverse_Engineering/07_Component_ID.md` - Lists verified module/reference components, low-confidence candidates, and unknown carrier component categories including debug LEDs, USB debug, and generic debug headers.
- `15_Reverse_Engineering/08_Bringup.md` - Provides the gated bring-up checklist and test-access dependencies for power, clocks, management, PCIe, firmware, ROCm, health, validation, debug, and recovery.
- `15_Reverse_Engineering/09_Block_Diagram.md` - Shows CPU, PCIe, switch/retimer/redriver, OAM connector, MI250X, clock, power, management, EEPROM, sensors, and cooling blocks with `TBD` labels.
- `17_System_Architecture/02_System_Block_Diagram.md` - Architecture-level Mermaid diagram showing the same carrier subsystems with undocumented implementation details.
- `17_System_Architecture/03_Minimal_Carrier_Requirements.md` - Main source for required, recommended, optional, unknown, and risk categories for the minimal carrier.
- `17_System_Architecture/04_Future_Expansion.md` - Records future one-, two-, four-, eight-, and possible sixteen-module planning that must not drive the smallest one-module carrier unless required.
- `18_Component_Research/01_OAM_Connector.md` - Related connector research documenting unknown connector identity, pinout, power pins, ground pins, clock pins, management pins, mating height, stack-up, current rating, and placement.
- `18_Component_Research/02_Power_Converters.md` - Related power research documenting MP2975 candidate status and unknown regulator, power stage, PMBus, sequencing, telemetry, monitoring, and protection requirements.
- `18_Component_Research/03_Clock_Generators.md` - Related clock research documenting unknown REFCLK source, oscillator, clock generator, PLL, clock buffer, jitter, skew, routing, and fanout requirements.
- `18_Component_Research/04_EEPROM_FRU.md` - Related EEPROM research documenting unknown EEPROM, FRU EEPROM, I2C EEPROM, configuration EEPROM, firmware storage, board identification, bus, address, and contents.
- `18_Component_Research/05_Management_MCU.md` - Related management research documenting unknown BMC, MCU, PMBus, I2C, SMBus, GPIO, telemetry, firmware, fan control, sequencing, reset, and Power Good ownership.
- `18_Component_Research/06_Temperature_Sensors.md` - Related sensor research documenting unknown temperature, voltage, current, fault, telemetry, junction-temperature, board-temperature, and sensor ownership.
- `18_Component_Research/07_Fan_Control.md` - Related fan and cooling-control research documenting unknown fan, fan controller, PWM, tachometer, fan header, airflow, coolant, pump, reservoir, manifold, and cooling ownership.
- `18_Component_Research/08_PCIe_Retimers.md` - Related PCIe component research documenting unknown retimer, redriver, switch, equalization, Gen4/Gen5 applicability, lane mapping, and signal-integrity requirements.
- `18_Component_Research/09_Power_Connectors.md` - Related power-entry research documenting unknown input-power connector, PSU topology, cable assemblies, connector ratings, fusing, hot-swap, current limiting, power pins, and ground pins.
- `18_Component_Research/10_BOM.md` - BOM planning document tracking candidate and unknown components and warning against promoting unknowns to schematic or procurement lines.