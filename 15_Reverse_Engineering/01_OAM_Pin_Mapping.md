# OAM Pin Mapping

# Purpose

| Label | Statement | Sources |
|---|---|---|
| Verified | This document is an engineering reference for repository-supported OAM connector, OCP/OAM source, MI250X module, connector-candidate, signal-category, and pin-mapping evidence. | `AI_PROJECT_CONTEXT.md`; `README.md`; `15_Reverse_Engineering/README.md` |
| Verified | The project rules require hardware requirements to be separated into `Verified`, `Inferred`, and `Unknown`, and undocumented behavior must be tracked instead of assumed. | `AI_PROJECT_CONTEXT.md`; `AI_TASKS.md`; `README.md` |
| Verified | Pinouts should only be marked verified when supported by documentation. | `AI_PROJECT_CONTEXT.md`; `18_Component_Research/01_OAM_Connector.md` |
| Inferred | This file should be treated as a requirements-discovery reference, not as a schematic pinout, connector footprint, routing guide, or purchasable BOM. | `15_Reverse_Engineering/10_Minimal_Carrier.md`; `18_Component_Research/01_OAM_Connector.md`; `18_Component_Research/10_BOM.md` |

# Verified OAM Connector Information

Only facts directly supported by readable repository documents are listed as `Verified`. The repository does not yet contain a verified MI250X OAM connector pin map, pin numbers, signal names, or electrical assignment table. Sources: `09_AI_Notes/02_OAM_Interface.md`; `15_Reverse_Engineering/10_Minimal_Carrier.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`.

| Topic | Status | Repository-supported information | Sources |
|---|---|---|---|
| Project target | Verified | The project goal is to design an open hardware carrier board capable of operating AMD Instinct MI250X OAM accelerator modules. | `AI_PROJECT_CONTEXT.md`; `README.md`; `18_Component_Research/01_OAM_Connector.md` |
| MI250X module class | Verified | MI250 and MI250X are described as OCP Accelerator Modules. | `13_Reference_Docs/ROCm/Overview.md`; `09_AI_Notes/02_OAM_Interface.md`; `15_Reverse_Engineering/07_Component_ID.md` |
| MI250X software-visible context | Verified | MI250 and MI250X are described as two-GCD modules with 128 GB total memory, exposed to software as two devices with separate 64 GB VRAM blocks. | `13_Reference_Docs/ROCm/Overview.md`; `15_Reverse_Engineering/07_Component_ID.md`; `18_Component_Research/10_BOM.md` |
| Official OAM source link | Verified | The repository tracks `https://github.com/oam-dev/spec` as the official Open Accelerator Module specification source. | `02_AMD_Docs/GitHub_Links.rtf`; `09_AI_Notes/02_OAM_Interface.md`; `18_Component_Research/01_OAM_Connector.md` |
| OAM specification relevance | Verified | The OAM specification link is described as useful for mechanical drawings, connector specification, and power specification. | `02_AMD_Docs/GitHub_Links.rtf`; `02_AMD_Docs/README.md`; `15_Reverse_Engineering/06_Mechanical.md` |
| OAM document availability | Verified | `Wanted_Documents.md` marks OAM Specification as found. | `Wanted_Documents.md`; `09_AI_Notes/02_OAM_Interface.md`; `09_AI_Notes/10_Design_Checklist.md` |
| Missing connector source | Verified | `Wanted_Documents.md` marks Connector Specification as not found. | `Wanted_Documents.md`; `09_AI_Notes/02_OAM_Interface.md`; `18_Component_Research/01_OAM_Connector.md` |
| Missing mechanical/baseboard sources | Verified | `Wanted_Documents.md` marks Mechanical Specification and Baseboard Specification as not found. | `Wanted_Documents.md`; `15_Reverse_Engineering/06_Mechanical.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| Indexed OAM/OCP references | Verified | OAM Base Spec, OCP Accelerator Spec, Universal Baseboard, and OAI EXP are indexed under OCP/OAM references. | `13_Reference_Docs/Reference_Index.rtf`; `09_AI_Notes/02_OAM_Interface.md`; `18_Component_Research/01_OAM_Connector.md` |
| Indexed Molex references | Verified | Mirror Mezz Datasheet, Mirror Mezz Brochure, and Mirror Mezz Product Guide are indexed under Molex. | `13_Reference_Docs/Reference_Index.rtf`; `09_AI_Notes/08_Mechanical.md`; `15_Reverse_Engineering/07_Component_ID.md` |
| Mirror Mezz limitation | Verified | Molex Mirror Mezz is a candidate connector reference only; no readable local source confirms Mirror Mezz as the MI250X OAM connector. | `15_Reverse_Engineering/07_Component_ID.md`; `18_Component_Research/01_OAM_Connector.md`; `18_Component_Research/10_BOM.md` |
| Photo tracking | Verified | Front, back, and connector photos are marked found, while heatsink and baseboard photos are not marked found. | `Wanted_Documents.md`; `15_Reverse_Engineering/06_Mechanical.md`; `09_AI_Notes/08_Mechanical.md` |
| Photo availability gap | Unknown | Repository notes state the front, back, and connector photos marked found are not present as readable image files in the repository. | `09_AI_Notes/09_Unknowns.md`; `15_Reverse_Engineering/06_Mechanical.md`; `18_Component_Research/01_OAM_Connector.md` |

# Source Availability Matrix

| Source or reference category | Repository status | What it supports | What remains undocumented | Sources |
|---|---|---|---|---|
| OAM Specification | Found as a tracked source/link | OAM is a relevant source for mechanical, connector, and power work. | Extracted pin-level connector data is not present in readable local files. | `02_AMD_Docs/GitHub_Links.rtf`; `Wanted_Documents.md`; `09_AI_Notes/02_OAM_Interface.md` |
| Connector Specification | Missing | No verified connector-specific pinout can be extracted from the current repository. | Connector manufacturer, family, part number, pin count, pin numbering, signal map, footprint, stack-up, and current rating. | `Wanted_Documents.md`; `18_Component_Research/01_OAM_Connector.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| Baseboard Specification | Missing | Baseboard-level integration must remain unresolved. | Host/baseboard topology, connector placement assumptions, power-entry expectations, and sideband ownership. | `Wanted_Documents.md`; `09_AI_Notes/02_OAM_Interface.md`; `15_Reverse_Engineering/10_Minimal_Carrier.md` |
| Mechanical Specification | Missing | Mechanical constraints must remain unresolved. | Module dimensions, connector coordinates, mounting pattern, keepouts, PCB thickness, standoff height, and mating height. | `Wanted_Documents.md`; `15_Reverse_Engineering/06_Mechanical.md`; `09_AI_Notes/08_Mechanical.md` |
| PCIe Routing Guide | Missing | PCIe routing and signal-integrity details must remain unresolved. | PCIe generation, lane width, lane mapping, polarity, loss budget, equalization, AC-coupling, impedance, and routing limits. | `Wanted_Documents.md`; `15_Reverse_Engineering/05_PCIe.md`; `18_Component_Research/08_PCIe_Retimers.md` |
| REFCLK Guide | Missing | REFCLK details must remain unresolved. | REFCLK frequency, source, topology, electrical standard, jitter, skew, termination, and connector pins. | `Wanted_Documents.md`; `15_Reverse_Engineering/03_Clock_Tree.md`; `18_Component_Research/03_Clock_Generators.md` |
| PMBus Controller Datasheet | Missing | PMBus details must remain unresolved. | PMBus controller identity, topology, addresses, commands, telemetry registers, pullups, isolation, fault behavior, and ownership. | `Wanted_Documents.md`; `15_Reverse_Engineering/04_Management.md`; `18_Component_Research/05_Management_MCU.md` |
| VRM Datasheet | Missing | VRM implementation details must remain unresolved. | VRM controller, power stages, rail mapping, telemetry, sequencing behavior, and electrical constraints. | `Wanted_Documents.md`; `15_Reverse_Engineering/02_Power_Rails.md`; `18_Component_Research/02_Power_Converters.md` |
| OAM Thermal Guidelines | Missing | Thermal connector-adjacent decisions must remain unresolved. | Cooling envelope, thermal keepouts, airflow/coolant requirements, mounting force, and fan-control ownership. | `Wanted_Documents.md`; `09_AI_Notes/07_Cooling.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |

# Candidate Connector References

| Candidate or reference | Status | Repository-supported information | Limitations | Sources |
|---|---|---|---|---|
| Molex Mirror Mezz | Candidate reference | Mirror Mezz Datasheet, Mirror Mezz Brochure, and Mirror Mezz Product Guide are indexed under Molex. | Not confirmed as the MI250X OAM connector; no readable local file provides exact part number, pitch, pin count, mating height, stack-up, footprint, current rating, or signal-integrity data. | `13_Reference_Docs/Reference_Index.rtf`; `09_AI_Notes/08_Mechanical.md`; `15_Reverse_Engineering/07_Component_ID.md`; `18_Component_Research/10_BOM.md` |
| MI250X OAM mating connector | Unknown actual connector | A minimal carrier must provide the physical and electrical mating interface for the MI250X OAM module after connector type, pin count, pinout, and mechanical stack-up are verified. | Manufacturer, family, part number, pinout, and implementation are not documented in readable local files. | `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `15_Reverse_Engineering/10_Minimal_Carrier.md`; `18_Component_Research/01_OAM_Connector.md` |
| OAM/OCP indexed reference set | Source set, not connector selection | OAM Base Spec, OCP Accelerator Spec, Universal Baseboard, and OAI EXP are indexed. | The index does not itself provide the MI250X connector manufacturer, connector part number, pinout, or dimensions. | `13_Reference_Docs/Reference_Index.rtf`; `09_AI_Notes/02_OAM_Interface.md`; `13_Reference_Docs/README.md` |

# Signal Classification Summary

| Signal or pin category | Status | Repository-supported finding | Sources |
|---|---|---|---|
| Standard OAM signals | Unknown | OAM/OCP references are indexed and the OAM specification is tracked, but standard OAM signal names and pin assignments are not extracted into readable local files. | `13_Reference_Docs/Reference_Index.rtf`; `09_AI_Notes/02_OAM_Interface.md`; `15_Reverse_Engineering/10_Minimal_Carrier.md` |
| AMD-specific signals | Unknown | The reverse-engineering goal is to separate OAM-standard features from AMD-specific features, but no readable local source distinguishes AMD-specific MI250X connector signals. | `15_Reverse_Engineering/README.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `18_Component_Research/01_OAM_Connector.md` |
| PCIe lanes | Unknown | MI210 PCIe 4.0 x16 and MI200 SDMA context are documented, but MI250X OAM PCIe generation, lane width, lane mapping, polarity, and pin assignments are not documented. | `13_Reference_Docs/ROCm/Overview.md`; `15_Reverse_Engineering/05_PCIe.md`; `18_Component_Research/08_PCIe_Retimers.md` |
| PCIe sideband signals | Unknown | PERST#, WAKE#, CLKREQ#, reset signals, enumeration requirements, and OAM pin assignments are documented as unknown. | `15_Reverse_Engineering/05_PCIe.md`; `15_Reverse_Engineering/08_Bringup.md`; `18_Component_Research/08_PCIe_Retimers.md` |
| Clock signals | Unknown | REFCLK Guide is missing, and REFCLK frequency, source, topology, fanout, jitter, skew, termination, and OAM pin assignments are not documented. | `Wanted_Documents.md`; `15_Reverse_Engineering/03_Clock_Tree.md`; `18_Component_Research/03_Clock_Generators.md` |
| Management signals | Unknown | SMBus, I2C, PMBus, EEPROM, FRU EEPROM, BMC interaction, management MCU, firmware-management hardware, and health-monitoring hardware are undocumented at connector level. | `15_Reverse_Engineering/04_Management.md`; `18_Component_Research/04_EEPROM_FRU.md`; `18_Component_Research/05_Management_MCU.md` |
| Power pins | Unknown | OAM power relevance is verified, but OAM connector power-pin assignments, rail names, voltage values, current requirements, and pin grouping are not documented. | `02_AMD_Docs/GitHub_Links.rtf`; `15_Reverse_Engineering/02_Power_Rails.md`; `18_Component_Research/09_Power_Connectors.md` |
| Ground pins | Unknown | Required ground-pin assignments, return-current strategy, current sharing, and connector current rating are not documented. | `15_Reverse_Engineering/02_Power_Rails.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `18_Component_Research/01_OAM_Connector.md` |
| Reserved pins | Unknown | Reserved, no-connect, optional, vendor-specific, and AMD-specific pin lists are not documented in readable local files. | `15_Reverse_Engineering/README.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `18_Component_Research/01_OAM_Connector.md` |
| Unknown pins | Unknown | No readable local document provides MI250X OAM connector pin numbers, pin names, or pin functions, so every connector pin remains unmapped. | `09_AI_Notes/02_OAM_Interface.md`; `15_Reverse_Engineering/10_Minimal_Carrier.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |

# Connector Pin Map Status

No verified MI250X OAM connector pin row can be created from the current readable repository because connector pin numbers, pin names, pin functions, and OAM-vs-AMD-specific classifications are undocumented. Sources: `09_AI_Notes/02_OAM_Interface.md`; `15_Reverse_Engineering/10_Minimal_Carrier.md`; `18_Component_Research/01_OAM_Connector.md`.

| Pin group | Verified pin numbers | Verified signal names | Verified electrical role | Status | Sources |
|---|---|---|---|---|---|
| Standard OAM pins | None documented | None documented | None documented | Unknown | `09_AI_Notes/02_OAM_Interface.md`; `13_Reference_Docs/Reference_Index.rtf`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| AMD-specific pins | None documented | None documented | None documented | Unknown | `15_Reverse_Engineering/README.md`; `15_Reverse_Engineering/10_Minimal_Carrier.md`; `18_Component_Research/01_OAM_Connector.md` |
| PCIe lane pins | None documented | None documented | None documented | Unknown | `15_Reverse_Engineering/05_PCIe.md`; `18_Component_Research/08_PCIe_Retimers.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| PCIe sideband pins | None documented | PERST#, WAKE#, and CLKREQ# are named only as undocumented PCIe sideband topics. | None documented | Unknown | `15_Reverse_Engineering/05_PCIe.md`; `15_Reverse_Engineering/08_Bringup.md`; `18_Component_Research/08_PCIe_Retimers.md` |
| Clock pins | None documented | REFCLK is named only as an undocumented clock topic. | None documented | Unknown | `Wanted_Documents.md`; `15_Reverse_Engineering/03_Clock_Tree.md`; `18_Component_Research/03_Clock_Generators.md` |
| Management pins | None documented | SMBus, I2C, PMBus, EEPROM, FRU EEPROM, BMC, MCU, GPIO, telemetry, firmware, health, and fan-control topics are undocumented. | None documented | Unknown | `15_Reverse_Engineering/04_Management.md`; `18_Component_Research/04_EEPROM_FRU.md`; `18_Component_Research/05_Management_MCU.md` |
| Power pins | None documented | Rail names, enable signals, Power Good signals, telemetry signals, and fault signals are not documented at pin level. | None documented | Unknown | `15_Reverse_Engineering/02_Power_Rails.md`; `18_Component_Research/02_Power_Converters.md`; `18_Component_Research/09_Power_Connectors.md` |
| Ground pins | None documented | None documented | Return-current and current-sharing roles are not documented. | Unknown | `15_Reverse_Engineering/02_Power_Rails.md`; `18_Component_Research/01_OAM_Connector.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| Reserved pins | None documented | None documented | None documented | Unknown | `15_Reverse_Engineering/README.md`; `18_Component_Research/01_OAM_Connector.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| No-connect or optional pins | None documented | None documented | None documented | Unknown | `18_Component_Research/01_OAM_Connector.md`; `15_Reverse_Engineering/10_Minimal_Carrier.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |

# PCIe Lanes

| Item | Status | Repository-supported information | Design implication | Sources |
|---|---|---|---|---|
| MI210 PCIe context | Verified reference | MI210 is described as a standard PCIe 4.0 x16 card with one GCD and 64 GB HBM2e. | MI210 context must not be used as an MI250X OAM pinout. | `13_Reference_Docs/ROCm/Overview.md`; `15_Reverse_Engineering/05_PCIe.md`; `18_Component_Research/08_PCIe_Retimers.md` |
| MI200 SDMA context | Verified reference | MI200 SDMA engines are described as tuned for PCIe 4.0 x16 and up to 32 GB/s. | SDMA context is validation/software context, not connector-lane evidence. | `13_Reference_Docs/ROCm/Overview.md`; `15_Reverse_Engineering/05_PCIe.md`; `15_Reverse_Engineering/08_Bringup.md` |
| MI250X OAM PCIe generation | Unknown | The repository lists PCIe Gen4 as a hardware goal, but no readable local file verifies MI250X OAM PCIe generation at the connector. | Do not lock schematic or compliance target from the current repository alone. | `17_System_Architecture/01_System_Goals.md`; `15_Reverse_Engineering/05_PCIe.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| MI250X OAM lane width | Unknown | Lane width is not documented in readable local files. | Do not assign x16, x8, bifurcation, or multi-link topology without source evidence. | `15_Reverse_Engineering/05_PCIe.md`; `09_AI_Notes/03_PCIe_Interface.md`; `18_Component_Research/08_PCIe_Retimers.md` |
| MI250X OAM lane mapping | Unknown | Lane mapping, polarity rules, and lane assignments are not documented in readable local files. | Do not route lanes or assign connector pins until verified. | `AI_TASKS.md`; `15_Reverse_Engineering/05_PCIe.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| Switch / retimer / redriver need | Unknown | PCIe switch, retimer, and redriver needs are not proven for one MI250X module. | Treat signal-conditioning components as optional until topology and signal-integrity evidence require them. | `15_Reverse_Engineering/05_PCIe.md`; `15_Reverse_Engineering/10_Minimal_Carrier.md`; `18_Component_Research/08_PCIe_Retimers.md` |

# Sideband Signals

| Signal or group | Status | Repository-supported information | Sources |
|---|---|---|---|
| PERST# | Unknown | PERST# is named as an undocumented PCIe sideband/reset topic; no OAM pin assignment, polarity, or timing is documented. | `15_Reverse_Engineering/05_PCIe.md`; `18_Component_Research/08_PCIe_Retimers.md`; `15_Reverse_Engineering/08_Bringup.md` |
| WAKE# | Unknown | WAKE# is named as an undocumented PCIe sideband topic; no OAM pin assignment, requirement, or behavior is documented. | `15_Reverse_Engineering/05_PCIe.md`; `18_Component_Research/08_PCIe_Retimers.md` |
| CLKREQ# | Unknown | CLKREQ# is named as an undocumented PCIe sideband topic; no OAM pin assignment, requirement, or behavior is documented. | `15_Reverse_Engineering/05_PCIe.md`; `18_Component_Research/08_PCIe_Retimers.md` |
| Reset signals | Unknown | Required reset signal names and release timing are undocumented. | `15_Reverse_Engineering/05_PCIe.md`; `15_Reverse_Engineering/08_Bringup.md`; `15_Reverse_Engineering/10_Minimal_Carrier.md` |
| Enable signals | Unknown | Enable signal names, locations, polarities, voltage levels, ownership, and timing are undocumented. | `15_Reverse_Engineering/02_Power_Rails.md`; `18_Component_Research/02_Power_Converters.md`; `18_Component_Research/05_Management_MCU.md` |
| Power Good signals | Unknown | Power Good signal names, locations, thresholds, timing, and reset-gating relationships are undocumented. | `15_Reverse_Engineering/02_Power_Rails.md`; `17_System_Architecture/02_System_Block_Diagram.md`; `18_Component_Research/02_Power_Converters.md` |
| Fault or alert signals | Unknown | Fault reporting, fault latching, shutdown behavior, retry behavior, telemetry ownership, and alert behavior are undocumented. | `15_Reverse_Engineering/02_Power_Rails.md`; `18_Component_Research/05_Management_MCU.md`; `18_Component_Research/06_Temperature_Sensors.md` |

# Clock Signals

| Clock item | Status | Repository-supported information | Sources |
|---|---|---|---|
| REFCLK | Unknown | REFCLK Guide is missing, and REFCLK frequency, topology, source, fanout, jitter budget, skew, termination, and OAM pin assignments are undocumented. | `Wanted_Documents.md`; `15_Reverse_Engineering/03_Clock_Tree.md`; `18_Component_Research/03_Clock_Generators.md` |
| Clock source ownership | Unknown | No readable local source documents whether REFCLK is supplied by host, baseboard, carrier, module, clock generator, oscillator, buffer, PLL, or another source. | `15_Reverse_Engineering/03_Clock_Tree.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `18_Component_Research/03_Clock_Generators.md` |
| Clock generator / oscillator / PLL / buffer | Unknown | No clock generator, oscillator, PLL, or clock buffer part number is verified. | `15_Reverse_Engineering/07_Component_ID.md`; `18_Component_Research/03_Clock_Generators.md`; `18_Component_Research/10_BOM.md` |
| Reset-clock-power relationship | Unknown | Reset release timing relative to power rails, Power Good, and clocks is undocumented. | `15_Reverse_Engineering/02_Power_Rails.md`; `15_Reverse_Engineering/03_Clock_Tree.md`; `15_Reverse_Engineering/08_Bringup.md` |

# Management Signals

| Management item | Status | Repository-supported information | Sources |
|---|---|---|---|
| SMBus | Unknown | SMBus is included in management research scope, but no bus topology, pins, voltage levels, pullups, ownership, or addresses are documented. | `15_Reverse_Engineering/04_Management.md`; `18_Component_Research/05_Management_MCU.md`; `18_Component_Research/04_EEPROM_FRU.md` |
| I2C | Unknown | I2C is included in management research scope, but no bus topology, pins, voltage levels, pullups, ownership, or addresses are documented. | `15_Reverse_Engineering/04_Management.md`; `09_AI_Notes/06_Management_Controller.md`; `18_Component_Research/04_EEPROM_FRU.md` |
| PMBus | Unknown | PMBus Controller Datasheet is missing, and PMBus identity, topology, addresses, commands, telemetry registers, fault registers, pullups, isolation, and ownership are undocumented. | `Wanted_Documents.md`; `15_Reverse_Engineering/04_Management.md`; `18_Component_Research/02_Power_Converters.md` |
| EEPROM / FRU EEPROM | Unknown | EEPROM or FRU EEPROM requirement, address, contents, ownership, and OAM pin mapping are undocumented. | `15_Reverse_Engineering/04_Management.md`; `18_Component_Research/04_EEPROM_FRU.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| BMC / Management MCU | Unknown | Carrier-side MCU or BMC requirement, part number, bus topology, firmware role, and interaction with host/baseboard/module are undocumented. | `15_Reverse_Engineering/04_Management.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `18_Component_Research/05_Management_MCU.md` |
| GPIO / interrupts / firmware hardware | Unknown | Required GPIO list, reset lines, interrupts, firmware-update wiring, firmware storage, firmware flow, and hardware dependencies are undocumented. | `15_Reverse_Engineering/04_Management.md`; `15_Reverse_Engineering/08_Bringup.md`; `18_Component_Research/05_Management_MCU.md` |
| Sensors and fan control | Unknown | Temperature, voltage, current, fault, fan PWM, tachometer, fan fault, and cooling-control ownership are undocumented at connector level. | `15_Reverse_Engineering/04_Management.md`; `18_Component_Research/06_Temperature_Sensors.md`; `18_Component_Research/07_Fan_Control.md` |

# Power and Ground Pins

| Power or ground item | Status | Repository-supported information | Sources |
|---|---|---|---|
| Power-pin assignments | Unknown | OAM connector power-pin assignments are not documented in readable local files. | `15_Reverse_Engineering/02_Power_Rails.md`; `18_Component_Research/01_OAM_Connector.md`; `18_Component_Research/09_Power_Connectors.md` |
| Ground-pin assignments | Unknown | OAM connector ground-pin assignments and current return requirements are not documented. | `15_Reverse_Engineering/02_Power_Rails.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `18_Component_Research/09_Power_Connectors.md` |
| Rail names and voltages | Unknown | Required MI250X/OAM rail names, voltage values, voltage tolerances, input voltage range, standby rails, auxiliary rails, main rails, and total power budget are undocumented. | `15_Reverse_Engineering/02_Power_Rails.md`; `18_Component_Research/02_Power_Converters.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| Current requirements | Unknown | Current requirement for every rail, connector current rating, current-sharing requirements, return-current strategy, copper sizing inputs, and fusing inputs are undocumented. | `15_Reverse_Engineering/02_Power_Rails.md`; `18_Component_Research/09_Power_Connectors.md`; `09_AI_Notes/10_Design_Checklist.md` |
| Sequencing | Unknown | Power-up order, power-down order, enable order, Power Good timing, reset release timing, clock dependency, shutdown behavior, and fault response are undocumented. | `15_Reverse_Engineering/02_Power_Rails.md`; `15_Reverse_Engineering/08_Bringup.md`; `18_Component_Research/02_Power_Converters.md` |
| PMBus / VRM relationship | Unknown | MP2975 is a low-confidence candidate digital multiphase VRM controller, but actual presence, role, pins, rails controlled, telemetry behavior, and electrical requirements are not verified. | `13_Reference_Docs/Component_Index.rtf`; `15_Reverse_Engineering/07_Component_ID.md`; `18_Component_Research/02_Power_Converters.md` |

# Reserved, Optional, and Unknown Pins

| Pin class | Status | Repository-supported information | Sources |
|---|---|---|---|
| Reserved pins | Unknown | Reserved pins are not documented in readable local files. | `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `18_Component_Research/01_OAM_Connector.md`; `15_Reverse_Engineering/README.md` |
| No-connect pins | Unknown | No-connect pins are not documented in readable local files. | `18_Component_Research/01_OAM_Connector.md`; `15_Reverse_Engineering/10_Minimal_Carrier.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| Optional pins | Unknown | Optional pins are not documented in readable local files. | `18_Component_Research/01_OAM_Connector.md`; `15_Reverse_Engineering/10_Minimal_Carrier.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| Vendor-specific pins | Unknown | Vendor-specific pins are not documented in readable local files. | `15_Reverse_Engineering/README.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `18_Component_Research/01_OAM_Connector.md` |
| AMD-specific pins | Unknown | AMD-specific MI250X pins are not documented in readable local files. | `15_Reverse_Engineering/README.md`; `15_Reverse_Engineering/10_Minimal_Carrier.md`; `18_Component_Research/01_OAM_Connector.md` |
| Unknown pins | Unknown | Every MI250X OAM connector pin remains unknown until a verified connector pinout source is recovered and extracted. | `09_AI_Notes/02_OAM_Interface.md`; `15_Reverse_Engineering/10_Minimal_Carrier.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |

# Design Implications

| Rule | Status | Engineering implication | Sources |
|---|---|---|---|
| Do not assign pins | Inferred | Do not assign OAM connector pin numbers, signal names, rail names, PCIe lanes, REFCLK pins, reset pins, sideband pins, management pins, EEPROM pins, sensor pins, fan-control pins, reserved pins, or no-connect pins until a verified pinout source exists. | `AI_PROJECT_CONTEXT.md`; `09_AI_Notes/10_Design_Checklist.md`; `18_Component_Research/01_OAM_Connector.md` |
| Do not create final footprint | Inferred | Do not create a final connector footprint, symbol, 3D model, board outline, connector placement, or routing constraint until connector manufacturer, part number, pin count, mating height, stack-up, and mechanical constraints are verified. | `15_Reverse_Engineering/06_Mechanical.md`; `09_AI_Notes/08_Mechanical.md`; `18_Component_Research/01_OAM_Connector.md` |
| Do not assume Mirror Mezz | Inferred | Do not treat Molex Mirror Mezz as the actual MI250X connector without direct evidence from readable documentation or verified physical inspection. | `13_Reference_Docs/Reference_Index.rtf`; `15_Reverse_Engineering/07_Component_ID.md`; `18_Component_Research/10_BOM.md` |
| Do not infer MI250X PCIe from MI210 | Inferred | Treat MI210 PCIe 4.0 x16 and MI200 SDMA information as software/data-movement context, not as MI250X OAM connector pinout, lane mapping, or routing evidence. | `13_Reference_Docs/ROCm/Overview.md`; `15_Reverse_Engineering/05_PCIe.md`; `18_Component_Research/08_PCIe_Retimers.md` |
| Keep OAM and AMD-specific categories separate | Inferred | Create separate OAM-standard and AMD-specific signal tables only after a verified source provides enough information to classify signals. | `15_Reverse_Engineering/README.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `18_Component_Research/01_OAM_Connector.md` |
| Gate schematic capture | Inferred | A safe schematic is blocked until connector, power, PCIe/REFCLK, reset, management, mechanical, baseboard, cooling, and high-speed constraints are verified. | `09_AI_Notes/10_Design_Checklist.md`; `15_Reverse_Engineering/10_Minimal_Carrier.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |

# Future Research

| Priority | Research task | Required output | Sources |
|---|---|---|---|
| High | Obtain and extract the missing Connector Specification or another verified MI250X OAM connector source. | Verified connector manufacturer, family, part number, pin count, pin numbering, footprint, mating height, stack-up, and full pinout. | `Wanted_Documents.md`; `18_Component_Research/01_OAM_Connector.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| High | Extract the OAM Specification sections relevant to connector, power, mechanical, clocks, sideband, and management interfaces. | Verified OAM-standard signal categories and constraints separated from MI250X-specific unknowns. | `02_AMD_Docs/GitHub_Links.rtf`; `13_Reference_Docs/Reference_Index.rtf`; `09_AI_Notes/02_OAM_Interface.md` |
| High | Determine AMD-specific MI250X connector signals. | Verified AMD-specific signal list, pin assignments, required handling, and relationship to standard OAM pins. | `15_Reverse_Engineering/README.md`; `15_Reverse_Engineering/10_Minimal_Carrier.md`; `18_Component_Research/01_OAM_Connector.md` |
| High | Map PCIe lanes and sidebands. | Verified PCIe generation, lane width, lane order, polarity rules, sideband pins, REFCLK pins, reset pins, and routing constraints. | `Wanted_Documents.md`; `15_Reverse_Engineering/05_PCIe.md`; `18_Component_Research/08_PCIe_Retimers.md` |
| High | Map power and ground pins. | Verified rail names, voltages, current requirements, power pins, ground pins, current sharing, connector current rating, sequencing, enables, and Power Good behavior. | `15_Reverse_Engineering/02_Power_Rails.md`; `18_Component_Research/02_Power_Converters.md`; `18_Component_Research/09_Power_Connectors.md` |
| High | Map management and firmware-related pins. | Verified SMBus, I2C, PMBus, EEPROM/FRU, BMC/MCU, GPIO, telemetry, interrupt, firmware-update, sensor, fan, and health-monitoring pins or verified absence of each category. | `15_Reverse_Engineering/04_Management.md`; `18_Component_Research/04_EEPROM_FRU.md`; `18_Component_Research/05_Management_MCU.md` |
| High | Locate the front, back, and connector photos marked found. | Photo files, provenance, scale/reference method, and any verified connector markings, orientation, placement, or visible vendor clues. | `Wanted_Documents.md`; `09_AI_Notes/09_Unknowns.md`; `15_Reverse_Engineering/06_Mechanical.md` |
| Medium | Confirm or reject Molex Mirror Mezz. | Evidence-backed connector vendor/family decision and, if applicable, exact part number and footprint data. | `13_Reference_Docs/Reference_Index.rtf`; `15_Reverse_Engineering/07_Component_ID.md`; `18_Component_Research/10_BOM.md` |
| Medium | Build final pin tables after verified source recovery. | Separate tables for standard OAM pins, AMD-specific pins, PCIe lanes, sidebands, clocks, management, power, ground, reserved pins, no-connect pins, optional pins, and unknown pins. | `15_Reverse_Engineering/README.md`; `09_AI_Notes/10_Design_Checklist.md`; `18_Component_Research/01_OAM_Connector.md` |

# Sources

| Source | Use in this reference |
|---|---|
| `AI_PROJECT_CONTEXT.md` | Defines project goal, evidence labels, rule against invented requirements, and pinout verification rule. |
| `AI_TASKS.md` | Lists reverse-engineering tasks and high-priority unknowns including OAM connector pinout, PCIe lane assignment, EEPROM requirements, management interface, power sequencing, and clock topology. |
| `README.md` | States the public-evidence workflow and that undocumented behavior should be tracked rather than assumed. |
| `Wanted_Documents.md` | Tracks found and missing OAM, mechanical, baseboard, connector, PCIe, REFCLK, power, cooling, and photo evidence. |
| `02_AMD_Docs/README.md` | Identifies the OAM link as useful for mechanical drawings, connector specification, and power specification. |
| `02_AMD_Docs/GitHub_Links.rtf` | Links the official Open Accelerator Module specification and describes its connector, mechanical, and power relevance. |
| `13_Reference_Docs/README.md` | Describes the local reference library and states that many index entries lack matching local files. |
| `13_Reference_Docs/README.rtf` | Describes the MI250X research library and lists planned photos, mechanical measurements, teardown photos, PCB analysis, vendor documentation, and Mirror Mezz connector documentation. |
| `13_Reference_Docs/Reference_Index.rtf` | Indexes OAM/OCP references, Molex Mirror Mezz references, firmware tools, health checks, system validation, and GPU management references. |
| `13_Reference_Docs/Component_Index.rtf` | Identifies MP2975 as a low-confidence candidate digital multiphase VRM controller and records its datasheet gap. |
| `13_Reference_Docs/ROCm/Overview.md` | Identifies MI250 and MI250X as OCP Accelerator Modules and provides MI210/MI200 PCIe context that is not a connector pinout. |
| `09_AI_Notes/02_OAM_Interface.md` | Summarizes OAM interface evidence and connector, mechanical, and baseboard gaps. |
| `09_AI_Notes/03_PCIe_Interface.md` | Summarizes PCIe lane mapping, sideband, routing, and REFCLK gaps. |
| `09_AI_Notes/04_Power_Architecture.md` | Summarizes OAM power specification relevance, PMBus/VRM gaps, and power-rail unknowns. |
| `09_AI_Notes/05_Clock_Architecture.md` | Summarizes missing REFCLK frequency, topology, source, fanout, jitter, skew, termination, and reset-clock relationships. |
| `09_AI_Notes/06_Management_Controller.md` | Summarizes management-controller, firmware, health, bus, reset, interrupt, and enable gaps. |
| `09_AI_Notes/08_Mechanical.md` | Summarizes mechanical connector, board outline, mounting, keepout, and Mirror Mezz reference gaps. |
| `09_AI_Notes/09_Unknowns.md` | Consolidates missing specifications, photo location gaps, and invalid/unreadable PDF limitations. |
| `09_AI_Notes/10_Design_Checklist.md` | States that schematic capture and PCB layout must wait for connector, PCIe/REFCLK, power, management, mechanical, baseboard, and high-speed constraints. |
| `15_Reverse_Engineering/README.md` | Defines the reverse-engineering goal to identify required interfaces, separate OAM-standard and AMD-specific features, determine mandatory signals, and identify undocumented hardware. |
| `15_Reverse_Engineering/02_Power_Rails.md` | Main source for power rail, power-pin, ground-pin, sequencing, enable, Power Good, PMBus, telemetry, and current-requirement gaps. |
| `15_Reverse_Engineering/03_Clock_Tree.md` | Main source for REFCLK, clock source, clock buffer, oscillator, PLL, routing, jitter, skew, synchronization, and clock unknowns. |
| `15_Reverse_Engineering/04_Management.md` | Main source for management MCU/BMC, SMBus, I2C, PMBus, EEPROM, FRU EEPROM, firmware, health monitoring, sensors, and fan-control unknowns. |
| `15_Reverse_Engineering/05_PCIe.md` | Main source for PCIe generation, lane width, lane mapping, REFCLK, reset, switch, retimer, and signal-integrity gaps. |
| `15_Reverse_Engineering/06_Mechanical.md` | Main source for mechanical connector placement, dimensions, mounting, keepouts, photo tracking, and baseboard gaps. |
| `15_Reverse_Engineering/07_Component_ID.md` | Lists MI250X, MP2975, Molex Mirror Mezz, and unknown component categories with confidence levels. |
| `15_Reverse_Engineering/08_Bringup.md` | Records power, clocks, reset, management, EEPROM, firmware, PCIe, ROCm detection, and health-check bring-up gaps. |
| `15_Reverse_Engineering/09_Block_Diagram.md` | Shows the OAM connector as an undocumented architecture block with power, reset, sideband, clock, management, and PCIe dependencies. |
| `15_Reverse_Engineering/10_Minimal_Carrier.md` | Describes the OAM connector as required only after connector type, pin count, pinout, and mechanical stack-up are verified. |
| `17_System_Architecture/02_System_Block_Diagram.md` | Shows OAM connector, PCIe, optional switch/retimer, power, clock, management, EEPROM, sensors, fan, and cooling blocks with details undocumented. |
| `17_System_Architecture/03_Minimal_Carrier_Requirements.md` | Lists OAM connector implementation and signal classification as schematic blockers. |
| `18_Component_Research/01_OAM_Connector.md` | Related research for OAM connector, Mirror Mezz limitations, connector pinout, and connector mechanical/electrical unknowns. |
| `18_Component_Research/02_Power_Converters.md` | Related research for power rails, power pins, ground pins, sequencing, telemetry, PMBus, and VRM unknowns. |
| `18_Component_Research/03_Clock_Generators.md` | Related research for REFCLK, clock generator, oscillator, PLL, clock buffer, jitter, skew, and connector clock-pin unknowns. |
| `18_Component_Research/04_EEPROM_FRU.md` | Related research for EEPROM, FRU EEPROM, configuration storage, board identification, bus, and firmware-storage unknowns. |
| `18_Component_Research/05_Management_MCU.md` | Related research for management MCU/BMC, PMBus/I2C/SMBus, GPIO, telemetry, firmware, fan control, and sequencing unknowns. |
| `18_Component_Research/06_Temperature_Sensors.md` | Related research for temperature, voltage, current, fault, telemetry, and sensor-ownership unknowns. |
| `18_Component_Research/07_Fan_Control.md` | Related research for fan, fan controller, PWM, tachometer, fan header, cooling-control ownership, and thermal-control unknowns. |
| `18_Component_Research/08_PCIe_Retimers.md` | Related research for PCIe switch, retimer, redriver, signal integrity, Gen4/Gen5, equalization, REFCLK, and lane-mapping unknowns. |
| `18_Component_Research/09_Power_Connectors.md` | Related research for OAM connector power pins, ground pins, current rating, current sharing, and power-entry unknowns. |
| `18_Component_Research/10_BOM.md` | Tracks MI250X as the verified target, Molex Mirror Mezz as a candidate reference, and the MI250X OAM mating connector plus most carrier component categories as unknown. |