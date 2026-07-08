# Purpose

Research power rails, VRMs, `MP2975`, PMBus, voltage regulators, sequencing, Power Good, telemetry, and current requirements for an open-source AMD Instinct MI250X OAM carrier board using only repository-supported information.

This document is not a regulator selection, schematic, layout guide, PMBus programming guide, or purchasable BOM. The repository does not currently contain verified MI250X rail names, rail voltage values, input voltage range, rail current requirements, total power budget, sequencing rules, Power Good timing, enable timing, power-stage part numbers, PMBus addresses, PMBus commands, telemetry registers, regulator part numbers, or fault behavior. Sources: `15_Reverse_Engineering/02_Power_Rails.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `18_Component_Research/10_BOM.md`.

# Verified

Only facts directly supported by repository documents are included here.

| Topic | Verified repository fact | Sources |
|---|---|---|
| Project goal | The project goal is to design an open hardware carrier board capable of operating AMD Instinct MI250X OAM accelerator modules. | `AI_PROJECT_CONTEXT.md`; `README.md` |
| Evidence rules | Project rules say to never invent hardware requirements and to separate information into `Verified`, `Inferred`, and `Unknown`. | `AI_PROJECT_CONTEXT.md`; `AI_TASKS.md` |
| Target module | MI250 and MI250X are OCP Accelerator Modules with two GCDs and 128 GB total memory, exposed to software as two devices with separate 64 GB VRAM blocks. | `13_Reference_Docs/ROCm/Overview.md`; `15_Reverse_Engineering/07_Component_ID.md` |
| OAM power source | The repository tracks `https://github.com/oam-dev/spec` as the official Open Accelerator Module specification. | `02_AMD_Docs/GitHub_Links.rtf`; `15_Reverse_Engineering/02_Power_Rails.md` |
| OAM power relevance | The OAM specification is described as useful for power specification. | `02_AMD_Docs/GitHub_Links.rtf`; `09_AI_Notes/04_Power_Architecture.md`; `15_Reverse_Engineering/02_Power_Rails.md` |
| OAM document status | `Wanted_Documents.md` marks OAM Specification as found. | `Wanted_Documents.md`; `15_Reverse_Engineering/02_Power_Rails.md` |
| Missing PMBus source | PMBus Controller Datasheet is marked missing. | `Wanted_Documents.md`; `09_AI_Notes/04_Power_Architecture.md`; `15_Reverse_Engineering/04_Management.md` |
| Missing VRM source | VRM Datasheet is marked missing. | `Wanted_Documents.md`; `09_AI_Notes/04_Power_Architecture.md`; `15_Reverse_Engineering/02_Power_Rails.md` |
| MP2975 identity | `MP2975` is listed in the component index. | `13_Reference_Docs/Component_Index.rtf`; `09_AI_Notes/04_Power_Architecture.md`; `15_Reverse_Engineering/07_Component_ID.md` |
| MP2975 manufacturer | `MP2975` manufacturer is listed as Monolithic Power Systems (MPS). | `13_Reference_Docs/Component_Index.rtf`; `09_AI_Notes/04_Power_Architecture.md` |
| MP2975 function | `MP2975` function is listed as a digital multiphase VRM controller. | `13_Reference_Docs/Component_Index.rtf`; `15_Reverse_Engineering/07_Component_ID.md` |
| MP2975 confidence | `MP2975` is listed as believed present on MI250X and not visually confirmed. | `13_Reference_Docs/Component_Index.rtf`; `09_AI_Notes/04_Power_Architecture.md`; `15_Reverse_Engineering/07_Component_ID.md` |
| MP2975 datasheet status | No public MP2975 datasheet is available in the repository. | `13_Reference_Docs/Component_Index.rtf`; `09_AI_Notes/04_Power_Architecture.md` |
| Power validation tasks | Project tasks include reverse engineering power rails, sequencing, telemetry, validating power rails, and voltage validation. | `AI_TASKS.md`; `15_Reverse_Engineering/02_Power_Rails.md` |
| System hardware goal | System goals include reliable power sequencing. | `17_System_Architecture/01_System_Goals.md`; `15_Reverse_Engineering/02_Power_Rails.md` |
| Block diagram status | The system block diagram marks power subsystem rails, sequencing, Power Good, and telemetry as undocumented. | `17_System_Architecture/02_System_Block_Diagram.md`; `15_Reverse_Engineering/09_Block_Diagram.md` |
| Minimal carrier status | Minimal carrier requirements mark power rail implementation, current requirements, sequencing, enables, Power Good, and monitoring as unresolved. | `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `15_Reverse_Engineering/10_Minimal_Carrier.md` |
| Component-identification status | Power stages and PMBus devices are listed as undocumented component categories. | `15_Reverse_Engineering/07_Component_ID.md`; `18_Component_Research/10_BOM.md` |

# Candidate Components

| Component or category | Manufacturer | Part number | Status | Repository-supported information | Design position | Sources |
|---|---|---|---|---|---|---|
| Digital multiphase VRM controller | Monolithic Power Systems (MPS) | MP2975 | Candidate | Listed as a digital multiphase VRM controller, believed present on MI250X, not visually confirmed, with no public datasheet in the repository. | Investigate only; do not place in schematic or BOM until visually or documentarily confirmed. | `13_Reference_Docs/Component_Index.rtf`; `15_Reverse_Engineering/07_Component_ID.md`; `18_Component_Research/10_BOM.md` |
| PMBus controller / PMBus device | Unknown | Unknown | Unknown | PMBus Controller Datasheet is missing; PMBus controller identity, topology, addresses, commands, telemetry registers, and fault behavior are not documented. | Do not select or assign PMBus devices yet. | `Wanted_Documents.md`; `15_Reverse_Engineering/04_Management.md`; `18_Component_Research/05_Management_MCU.md` |
| VRM controller | Unknown | Unknown | Unknown | Actual MI250X or carrier VRM implementation is not verified beyond the low-confidence `MP2975` candidate reference. | Do not define VRM topology yet. | `Wanted_Documents.md`; `15_Reverse_Engineering/02_Power_Rails.md`; `15_Reverse_Engineering/07_Component_ID.md` |
| Voltage regulator / converter | Unknown | Unknown | Unknown | No specific regulator or converter part number is verified for the carrier or MI250X module. | Do not select regulators until rails, currents, sequencing, and thermal constraints are sourced. | `18_Component_Research/10_BOM.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `15_Reverse_Engineering/02_Power_Rails.md` |
| Power stage | Unknown | Unknown | Unknown | Power stages are undocumented in readable local files. | Do not select phases, packages, or current ratings until rail requirements are known. | `15_Reverse_Engineering/07_Component_ID.md`; `18_Component_Research/10_BOM.md` |
| Carrier input-power connector | Unknown | Unknown | Unknown | Carrier input-power connector and baseboard power architecture are not documented. | Do not select an input connector until input voltage, current, protection, and baseboard requirements are verified. | `15_Reverse_Engineering/02_Power_Rails.md`; `18_Component_Research/10_BOM.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| Voltage / current / fault sensors | Unknown | Unknown | Unknown | Required voltage, current, temperature, and fault monitoring hardware is not documented at signal or controller level. | Treat monitoring components as unresolved until telemetry and monitoring ownership are defined. | `15_Reverse_Engineering/04_Management.md`; `18_Component_Research/06_Temperature_Sensors.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |

# Unknown

- **Unknown:** Required MI250X/OAM rail names, voltage values, voltage tolerances, input voltage range, standby rails, auxiliary rails, main rails, and total power budget. Sources: `15_Reverse_Engineering/02_Power_Rails.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`.
- **Unknown:** Current requirement for every rail, connector current rating, return-current needs, copper sizing requirements, fusing requirements, and regulator power-stage sizing. Sources: `15_Reverse_Engineering/02_Power_Rails.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `09_AI_Notes/10_Design_Checklist.md`.
- **Unknown:** OAM connector power-pin and ground-pin assignments. Sources: `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `18_Component_Research/01_OAM_Connector.md`.
- **Unknown:** Power-up sequence, power-down sequence, standby-to-main transition, enable order, Power Good behavior, reset release timing, clock dependencies, shutdown behavior, and fault recovery behavior. Sources: `15_Reverse_Engineering/02_Power_Rails.md`; `15_Reverse_Engineering/08_Bringup.md`; `18_Component_Research/03_Clock_Generators.md`.
- **Unknown:** Enable signal names, locations, polarities, voltage levels, ownership, and timing. Sources: `15_Reverse_Engineering/02_Power_Rails.md`; `18_Component_Research/05_Management_MCU.md`.
- **Unknown:** Power Good signal names, locations, thresholds, timing, and reset-gating relationship. Sources: `15_Reverse_Engineering/02_Power_Rails.md`; `17_System_Architecture/02_System_Block_Diagram.md`.
- **Unknown:** Actual VRM controller, regulator topology, power-stage devices, phase count, compensation, switching behavior, power rails controlled, and electrical constraints. Sources: `13_Reference_Docs/Component_Index.rtf`; `15_Reverse_Engineering/07_Component_ID.md`; `Wanted_Documents.md`.
- **Unknown:** Whether `MP2975` is actually present on MI250X hardware; it is listed as believed present and not visually confirmed. Sources: `13_Reference_Docs/Component_Index.rtf`; `15_Reverse_Engineering/07_Component_ID.md`.
- **Unknown:** `MP2975` pinout, register map, PMBus behavior, telemetry registers, fault registers, sequencing features, and power-stage pairings because no public MP2975 datasheet is available in the repository. Sources: `13_Reference_Docs/Component_Index.rtf`; `09_AI_Notes/04_Power_Architecture.md`.
- **Unknown:** PMBus controller identity, PMBus bus topology, addresses, commands, telemetry registers, fault registers, pullups, isolation, bus ownership, and firmware ownership. Sources: `Wanted_Documents.md`; `15_Reverse_Engineering/04_Management.md`; `18_Component_Research/05_Management_MCU.md`.
- **Unknown:** Required telemetry signals, voltage monitoring, current monitoring, temperature monitoring, fault monitoring, telemetry ownership, and whether telemetry is carrier-side, module-side, host-side, BMC-side, or MCU-side. Sources: `15_Reverse_Engineering/04_Management.md`; `18_Component_Research/06_Temperature_Sensors.md`; `17_System_Architecture/02_System_Block_Diagram.md`.
- **Unknown:** Whether required power requirements are OAM-defined, AMD-specific to MI250X, baseboard-specific, host-system-specific, or implementation-specific. Sources: `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `15_Reverse_Engineering/10_Minimal_Carrier.md`.
- **Unknown:** Carrier input-power connector, protection, hot-swap behavior, fusing, current limiting, and baseboard power architecture. Sources: `15_Reverse_Engineering/02_Power_Rails.md`; `18_Component_Research/10_BOM.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`.

# Design Implications

- Do not invent or assume rail voltages, input voltages, current requirements, total power, sequencing order, Power Good timing, or enable polarity.
- Do not select regulators, voltage converters, VRM controllers, power stages, fuses, hot-swap controllers, current sensors, PMBus devices, input-power connectors, rail names, or connector current ratings from the current repository alone.
- Treat `MP2975` and MPS as candidate research items only until verified by hardware evidence or a readable MI250X-specific source.
- Do not place `MP2975` into a schematic or purchasable BOM until its presence, role, pins, rails controlled, telemetry behavior, and electrical requirements are verified.
- Do not name PMBus nets, assign PMBus addresses, define PMBus telemetry registers, or write PMBus firmware behavior until topology and datasheets are available.
- Do not begin schematic capture until connector power pins, ground pins, voltage rails, current requirements, sequencing, enables, Power Good, reset dependencies, telemetry, monitoring, and fault behavior are verified.
- Keep power, management, sensor, cooling, connector, clock, and bring-up notes linked because PMBus, telemetry, fault behavior, voltage/current monitoring, thermal limits, and reset release cross subsystem boundaries.
- For multi-module goals, do not extrapolate one-module power distribution to 2, 4, 8, or possible 16 modules until one-module power requirements are verified.

# Future Research

| Priority | Research task | Required output | Sources |
|---|---|---|---|
| High | Obtain and extract the OAM power specification. | Verified OAM-defined rails, input power, power pins, ground pins, current requirements, sequencing, enables, and Power Good behavior. | `02_AMD_Docs/GitHub_Links.rtf`; `Wanted_Documents.md`; `15_Reverse_Engineering/02_Power_Rails.md` |
| High | Obtain the missing Connector Specification or another verified MI250X OAM pinout. | Verified power, ground, enable, Power Good, telemetry, management, and fault-related connector pins. | `Wanted_Documents.md`; `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `18_Component_Research/01_OAM_Connector.md` |
| High | Determine MI250X rail requirements. | Verified rail names, voltage values, tolerances, input voltage range, standby rails, auxiliary rails, main rails, and total power budget. | `15_Reverse_Engineering/02_Power_Rails.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| High | Determine current requirements. | Verified current requirement for every rail, connector current rating, return-current strategy, copper sizing inputs, fusing inputs, and regulator/power-stage sizing inputs. | `15_Reverse_Engineering/02_Power_Rails.md`; `09_AI_Notes/10_Design_Checklist.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| High | Determine sequencing and reset-power-clock timing. | Verified power-up order, power-down order, enable order, Power Good timing, reset release timing, clock dependency, shutdown behavior, and fault response. | `15_Reverse_Engineering/08_Bringup.md`; `15_Reverse_Engineering/03_Clock_Tree.md`; `15_Reverse_Engineering/02_Power_Rails.md` |
| High | Confirm or reject `MP2975` on actual MI250X hardware. | Visual or document-backed confirmation of presence, location, role, associated rails, and related power stages. | `13_Reference_Docs/Component_Index.rtf`; `15_Reverse_Engineering/07_Component_ID.md`; `18_Component_Research/10_BOM.md` |
| High | Obtain MP2975 documentation or an alternate verified VRM source. | Verified pinout, rail-control role, PMBus behavior, telemetry registers, fault registers, sequencing features, power-stage pairing, and electrical requirements. | `13_Reference_Docs/Component_Index.rtf`; `09_AI_Notes/04_Power_Architecture.md` |
| High | Obtain the PMBus Controller Datasheet. | Verified PMBus controller identity, topology, addresses, commands, telemetry registers, fault registers, pullups, isolation, and ownership. | `Wanted_Documents.md`; `15_Reverse_Engineering/04_Management.md`; `18_Component_Research/05_Management_MCU.md` |
| Medium | Determine monitoring and telemetry ownership. | Verified voltage, current, temperature, and fault monitoring hardware, telemetry bus, polling owner, alert behavior, and health-check dependency. | `15_Reverse_Engineering/04_Management.md`; `18_Component_Research/06_Temperature_Sensors.md`; `17_System_Architecture/02_System_Block_Diagram.md` |
| Medium | Build a bring-up validation checklist after requirements are sourced. | Pre-power inspection, standby validation, main rail validation, sequencing validation, Power Good validation, reset validation, telemetry validation, and fault-response validation. | `AI_TASKS.md`; `15_Reverse_Engineering/08_Bringup.md`; `09_AI_Notes/10_Design_Checklist.md` |
| Medium | Define scale-out power distribution only after single-module power is verified. | Verified power-distribution approach for 2, 4, 8, and possible 16 MI250X configurations. | `AI_PROJECT_CONTEXT.md`; `17_System_Architecture/01_System_Goals.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |

# Sources

- `AI_PROJECT_CONTEXT.md` - Defines the open MI250X carrier goal and the rule to avoid invented hardware requirements.
- `AI_TASKS.md` - Lists power rails, power sequencing, telemetry, power validation, and voltage validation as project tasks or unknowns.
- `README.md` - States the public-evidence workflow and that undocumented behavior should be tracked rather than assumed.
- `Wanted_Documents.md` - Marks PMBus Controller Datasheet and VRM Datasheet as missing and tracks OAM, connector, PCIe, REFCLK, power, cooling, and photo evidence.
- `02_AMD_Docs/GitHub_Links.rtf` - Links the official OAM specification and states it is useful for power specification.
- `13_Reference_Docs/Component_Index.rtf` - Identifies `MP2975`, Monolithic Power Systems, digital multiphase VRM controller function, believed-present status, visual-confirmation gap, public reference, and missing public datasheet.
- `13_Reference_Docs/ROCm/Overview.md` - Identifies MI250 and MI250X as OCP Accelerator Modules; provides software context, not power-rail values.
- `09_AI_Notes/04_Power_Architecture.md` - Summarizes OAM power specification relevance, PMBus/VRM gaps, and MP2975 uncertainty.
- `09_AI_Notes/06_Management_Controller.md` - Links PMBus, VRM control, telemetry, reset, enable, and management-side questions.
- `09_AI_Notes/10_Design_Checklist.md` - States that schematic capture and PCB layout must wait for connector, PCIe/REFCLK, power, management, and baseboard requirements.
- `15_Reverse_Engineering/01_OAM_Pin_Mapping.md` - Records power-pin, ground-pin, telemetry-pin, management-pin, and connector assignments as unknown until a verified pinout is available.
- `15_Reverse_Engineering/02_Power_Rails.md` - Main source for rails, sequencing, current, PMBus, VRM, telemetry, monitoring, unknowns, and power research tasks.
- `15_Reverse_Engineering/03_Clock_Tree.md` - Records reset-clock and REFCLK gaps that affect power sequencing and reset release.
- `15_Reverse_Engineering/04_Management.md` - Records PMBus, voltage monitoring, management interface, telemetry, firmware, and health-monitoring gaps.
- `15_Reverse_Engineering/07_Component_ID.md` - Lists `MP2975` as a low-confidence candidate and power stages / PMBus devices as undocumented.
- `15_Reverse_Engineering/08_Bringup.md` - Records power prerequisites, standby/main power, sequencing, enables, Power Good, clock startup, reset release, and validation gaps.
- `15_Reverse_Engineering/09_Block_Diagram.md` - Shows the power system and power/reset/sideband blocks as undocumented architecture dependencies.
- `15_Reverse_Engineering/10_Minimal_Carrier.md` - Describes minimum carrier power delivery, sequencing, and unresolved implementation details.
- `17_System_Architecture/01_System_Goals.md` - Lists reliable power sequencing as a hardware goal.
- `17_System_Architecture/02_System_Block_Diagram.md` - Marks power subsystem rails, sequencing, Power Good, and telemetry as undocumented.
- `17_System_Architecture/03_Minimal_Carrier_Requirements.md` - Lists power rail implementation, current, sequencing, enables, Power Good, monitoring, PMBus/VRM investigation, and power risks.
- `18_Component_Research/01_OAM_Connector.md` - Records connector power-pin, ground-pin, current-rating, telemetry, and sideband gaps.
- `18_Component_Research/03_Clock_Generators.md` - Records reset-clock-power timing and REFCLK gaps.
- `18_Component_Research/05_Management_MCU.md` - Records PMBus, telemetry ownership, reset, enables, Power Good, GPIO, and fault handling as unresolved.
- `18_Component_Research/06_Temperature_Sensors.md` - Records voltage/current/fault monitoring and PMBus telemetry as unresolved.
- `18_Component_Research/10_BOM.md` - Tracks `MP2975` as a candidate and power converters, regulators, power stages, PMBus devices, and input-power connector as unknown.