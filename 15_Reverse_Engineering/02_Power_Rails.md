# Power Rails

# Purpose

Extract every repository-supported power-rail, power-sequencing, enable, Power Good, PMBus, monitoring, protection, and startup-order fact for the AMD Instinct MI250X OAM carrier project. This document does not invent rail names, voltages, currents, or timing values.

| Label | Statement | Sources |
|---|---|---|
| Verified | Hardware requirements must not be invented, and incomplete documentation must be marked as `Unknown`. | `AI_PROJECT_CONTEXT.md`; `AI_TASKS.md`; `README.md` |
| Verified | Pinouts should only be marked verified when supported by documentation. | `AI_PROJECT_CONTEXT.md`; `18_Component_Research/01_OAM_Connector.md` |
| Verified | The current readable repository does not contain verified MI250X/OAM rail names, rail voltages, rail currents, enable signal names, Power Good signal names, PMBus addresses, PMBus commands, telemetry registers, protection requirements, or startup order. | `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `18_Component_Research/02_Power_Converters.md`; `18_Component_Research/09_Power_Connectors.md` |

# Verified

## Verified Power Rail Extraction

No verified MI250X/OAM module power rail can be extracted from the current readable repository. The table below is intentionally empty of rail values rather than populated with guesses.

| Rail name | Voltage | Current | Purpose | Sequencing | Enable signals | Power Good | PMBus | Monitoring | Protection | Startup order | Sources |
|---|---|---|---|---|---|---|---|---|---|---|---|
| None verified | None verified | None verified | None verified | None verified | None verified | None verified | None verified | None verified | None verified | None verified | `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `18_Component_Research/02_Power_Converters.md`; `18_Component_Research/09_Power_Connectors.md` |

## Verified Power-Related Evidence

| Topic | Verified repository fact | Engineering meaning | Sources |
|---|---|---|---|
| OAM power source | The repository tracks `https://github.com/oam-dev/spec` as the official Open Accelerator Module specification. | The OAM specification is a power-research source, but extracted rail details are not present in readable local files. | `02_AMD_Docs/GitHub_Links.rtf`; `09_AI_Notes/02_OAM_Interface.md`; `18_Component_Research/02_Power_Converters.md` |
| OAM power relevance | The OAM specification link is described as useful for power specification. | OAM power requirements should be extracted from the specification before schematic capture. | `02_AMD_Docs/GitHub_Links.rtf`; `09_AI_Notes/04_Power_Architecture.md`; `18_Component_Research/02_Power_Converters.md` |
| OAM document status | `Wanted_Documents.md` marks OAM Specification as found. | The project knows the OAM specification source exists, but local extracted rail tables are still absent. | `Wanted_Documents.md`; `09_AI_Notes/10_Design_Checklist.md`; `18_Component_Research/02_Power_Converters.md` |
| Missing connector/baseboard sources | Connector Specification and Baseboard Specification are marked missing. | Power-pin assignment, ground-pin assignment, and baseboard power-entry expectations remain unresolved. | `Wanted_Documents.md`; `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `18_Component_Research/09_Power_Connectors.md` |
| Missing PMBus source | PMBus Controller Datasheet is marked missing. | PMBus topology, address, command, telemetry, and fault details cannot be verified. | `Wanted_Documents.md`; `15_Reverse_Engineering/04_Management.md`; `18_Component_Research/05_Management_MCU.md` |
| Missing VRM source | VRM Datasheet is marked missing. | VRM controller behavior, power-stage pairing, rail mapping, and sequencing behavior cannot be verified. | `Wanted_Documents.md`; `15_Reverse_Engineering/04_Management.md`; `18_Component_Research/02_Power_Converters.md` |
| MI250X module context | MI250 and MI250X are OCP Accelerator Modules with two GCDs and 128 GB total memory, exposed to software as two devices with separate 64 GB VRAM blocks. | This identifies the target module class; it does not define carrier rail names or rail values. | `13_Reference_Docs/ROCm/Overview.md`; `15_Reverse_Engineering/07_Component_ID.md`; `18_Component_Research/10_BOM.md` |
| Power validation tasks | Project tasks include reverse engineering power rails, sequencing, telemetry, validating power rails, and voltage validation. | Power requirements remain active reverse-engineering tasks. | `AI_TASKS.md`; `18_Component_Research/02_Power_Converters.md` |
| System hardware goal | System goals include reliable power sequencing. | Reliable sequencing is a project goal, not a verified MI250X startup-order table. | `17_System_Architecture/01_System_Goals.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| Block diagram status | The system block diagram marks power subsystem rails, sequencing, Power Good, and telemetry as undocumented. | The architecture identifies the power subsystem as required but unresolved. | `17_System_Architecture/02_System_Block_Diagram.md`; `15_Reverse_Engineering/09_Block_Diagram.md`; `18_Component_Research/02_Power_Converters.md` |
| Minimal carrier power status | Minimal carrier requirements mark rail names, input voltages, current requirements, power pins, ground pins, standby rails, protection, and monitoring as not defined. | Regulator selection, copper sizing, fusing, connector assignment, and safe operation are blocked. | `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `18_Component_Research/02_Power_Converters.md`; `18_Component_Research/09_Power_Connectors.md` |

## Verified Candidate Component Evidence

| Component or category | Manufacturer | Part number | Status | Repository-supported information | Design position | Sources |
|---|---|---|---|---|---|---|
| Digital multiphase VRM controller | Monolithic Power Systems | MP2975 | Candidate | `MP2975` is listed as a digital multiphase VRM controller, believed present on MI250X, not visually confirmed, with no public datasheet in the repository. | Investigate only; do not use it to infer rails, voltages, currents, PMBus behavior, or sequencing. | `13_Reference_Docs/Component_Index.rtf`; `15_Reverse_Engineering/07_Component_ID.md`; `18_Component_Research/02_Power_Converters.md` |
| PMBus controller / PMBus device | Unknown | Unknown | Unknown | PMBus Controller Datasheet is missing; PMBus controller identity, topology, addresses, commands, telemetry registers, and fault behavior are undocumented. | Do not assign PMBus devices, addresses, commands, or firmware behavior. | `Wanted_Documents.md`; `15_Reverse_Engineering/04_Management.md`; `18_Component_Research/05_Management_MCU.md` |
| VRM controller / power stages | Unknown | Unknown | Unknown | Actual MI250X or carrier VRM implementation is not verified beyond the low-confidence MP2975 candidate reference. | Do not define VRM topology, phase count, rail mapping, or power-stage sizing. | `13_Reference_Docs/Component_Index.rtf`; `15_Reverse_Engineering/07_Component_ID.md`; `18_Component_Research/02_Power_Converters.md` |

## Verified System-Level Power Planning That Is Not a Module Rail

| Planning item | Status | Repository-supported information | Why it is not a verified MI250X/OAM rail | Sources |
|---|---|---|---|---|
| Three redundant 3000W CRPS server power supplies | Verified as system-BOM planning target | `20_System_BOM/Power.md` lists this under `Target`, while the same file says power is `Under design` and the final PSU model will be selected after chassis design. | It is a chassis/system planning target, not a verified module input voltage, rail current, carrier connector, or OAM rail requirement. | `20_System_BOM/Power.md`; `18_Component_Research/09_Power_Connectors.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| 12V distribution | Verified as system-BOM design goal | `20_System_BOM/Power.md` lists `12V distribution` under design goals. | It is not verified as an MI250X OAM module input rail or carrier rail; carrier input voltage remains undocumented in the component and architecture notes. | `20_System_BOM/Power.md`; `18_Component_Research/09_Power_Connectors.md`; `18_Component_Research/02_Power_Converters.md` |
| N+1 redundancy and hot swap | Verified as system-BOM design goals | `20_System_BOM/Power.md` lists `N+1 redundancy` and `Hot swap`. | These are system power goals; carrier protection, hot-swap, fusing, current limiting, and baseboard power architecture remain unknown. | `20_System_BOM/Power.md`; `18_Component_Research/09_Power_Connectors.md` |

# Inferred

## Inferred Power Requirements

| Inferred item | Rail name | Voltage | Current | Purpose | Sequencing | Enable signals | Power Good | PMBus | Monitoring | Protection | Startup order | Sources |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Carrier power delivery | Unknown | Unknown | Unknown | A minimal carrier must provide whatever input power and ground paths are required by the MI250X OAM module. | Unknown | Unknown | Unknown | Unknown | Unknown | Unknown | Unknown | `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `15_Reverse_Engineering/10_Minimal_Carrier.md`; `18_Component_Research/09_Power_Connectors.md` |
| OAM power-specification dependency | Unknown | Unknown | Unknown | OAM-defined power requirements are a schematic blocker because the OAM specification is identified as useful for power specification. | Unknown | Unknown | Unknown | Unknown | Unknown | Unknown | Unknown | `02_AMD_Docs/GitHub_Links.rtf`; `09_AI_Notes/04_Power_Architecture.md`; `18_Component_Research/02_Power_Converters.md` |
| Connector dependency | Unknown | Unknown | Unknown | Power and ground pins cannot be assigned until the OAM connector pinout is verified. | Unknown | Unknown | Unknown | Unknown | Unknown | Unknown | Unknown | `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `18_Component_Research/01_OAM_Connector.md`; `09_AI_Notes/10_Design_Checklist.md` |
| PMBus investigation | Unknown | Unknown | Unknown | PMBus is a power-management research area because PMBus Controller Datasheet is missing and MP2975 is a candidate digital multiphase VRM controller. | Unknown | Unknown | Unknown | Unknown | Unknown | Unknown | Unknown | `Wanted_Documents.md`; `13_Reference_Docs/Component_Index.rtf`; `15_Reverse_Engineering/04_Management.md` |
| Telemetry and monitoring investigation | Unknown | Unknown | Unknown | Telemetry and voltage monitoring may overlap with PMBus/VRM work, but signal-level requirements are undocumented. | Unknown | Unknown | Unknown | Unknown | Unknown | Unknown | Unknown | `15_Reverse_Engineering/04_Management.md`; `18_Component_Research/05_Management_MCU.md`; `18_Component_Research/06_Temperature_Sensors.md` |
| Multi-module power distribution | Unknown | Unknown | Unknown | Future 2-, 4-, 8-, and possible 16-module goals will require later power-distribution research after one-module requirements are verified. | Unknown | Unknown | Unknown | Unknown | Unknown | Unknown | Unknown | `AI_PROJECT_CONTEXT.md`; `17_System_Architecture/04_Future_Expansion.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |

## Inferred Startup Dependency Chain

This is an inferred bring-up dependency map, not a verified MI250X startup order. Rail names, voltage values, timing, enables, and Power Good behavior remain unknown.

| Step | Inferred dependency | Verified rail name | Verified voltage | Verified current | What is known | What remains unknown | Sources |
|---|---|---|---|---|---|---|---|
| 1 | Standby power | None | None | None | Standby power is listed as an inferred first bring-up dependency. | Standby rail name, voltage, current, source, enable, Power Good, and timing. | `15_Reverse_Engineering/08_Bringup.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| 2 | Management initialization | None | None | None | Management initialization is listed as a likely bring-up step because firmware, health, validation, and GPU management references are indexed. | Whether management is carrier-side, module-side, host/baseboard-side, or required at all. | `15_Reverse_Engineering/08_Bringup.md`; `13_Reference_Docs/Reference_Index.rtf`; `15_Reverse_Engineering/04_Management.md` |
| 3 | Main power | None | None | None | Main power is listed as required to operate the module. | Main rail names, voltages, current, sequencing, enables, Power Good, and protection. | `15_Reverse_Engineering/08_Bringup.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `18_Component_Research/02_Power_Converters.md` |
| 4 | Clock startup | None | None | None | Clock startup is listed as a bring-up dependency if PCIe or other reference clocks are exposed on the carrier. | REFCLK source, frequency, topology, timing, and reset-clock relationship. | `15_Reverse_Engineering/08_Bringup.md`; `15_Reverse_Engineering/03_Clock_Tree.md`; `18_Component_Research/03_Clock_Generators.md` |
| 5 | Reset release | None | None | None | Reset release is listed as required for PCIe enumeration in typical hardware bring-up. | Reset signal names, release timing, power-good dependencies, and clock dependencies. | `15_Reverse_Engineering/08_Bringup.md`; `15_Reverse_Engineering/05_PCIe.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| 6 | PCIe enumeration | None | None | None | PCIe enumeration is a bring-up objective. | PCIe generation, lane width, lane mapping, sidebands, enumeration hardware requirements, and reset timing. | `15_Reverse_Engineering/08_Bringup.md`; `15_Reverse_Engineering/05_PCIe.md`; `18_Component_Research/08_PCIe_Retimers.md` |

# Unknown

## Unknown Rail Requirements

| Unknown category | Rail name | Voltage | Current | Purpose | Sequencing | Enable signals | Power Good | PMBus | Monitoring | Protection | Startup order | Sources |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| MI250X/OAM rail list | Unknown | Unknown | Unknown | Unknown | Unknown | Unknown | Unknown | Unknown | Unknown | Unknown | Unknown | `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `18_Component_Research/02_Power_Converters.md` |
| Input power | Unknown | Unknown | Unknown | Unknown | Unknown | Unknown | Unknown | Unknown | Unknown | Unknown | Unknown | `18_Component_Research/09_Power_Connectors.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| Standby / always-on / auxiliary rails | Unknown | Unknown | Unknown | Unknown | Unknown | Unknown | Unknown | Unknown | Unknown | Unknown | Unknown | `15_Reverse_Engineering/08_Bringup.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| Main rails | Unknown | Unknown | Unknown | Unknown | Unknown | Unknown | Unknown | Unknown | Unknown | Unknown | Unknown | `15_Reverse_Engineering/08_Bringup.md`; `15_Reverse_Engineering/10_Minimal_Carrier.md`; `18_Component_Research/02_Power_Converters.md` |
| OAM connector power pins | Unknown | Unknown | Unknown | Unknown | Unknown | Unknown | Unknown | Unknown | Unknown | Unknown | Unknown | `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `18_Component_Research/01_OAM_Connector.md`; `18_Component_Research/09_Power_Connectors.md` |
| OAM connector ground pins | Unknown | Unknown | Unknown | Unknown | Unknown | Unknown | Unknown | Unknown | Unknown | Unknown | Unknown | `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `18_Component_Research/01_OAM_Connector.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| Connector current sharing | Unknown | Unknown | Unknown | Unknown | Unknown | Unknown | Unknown | Unknown | Unknown | Unknown | Unknown | `18_Component_Research/01_OAM_Connector.md`; `18_Component_Research/09_Power_Connectors.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |

## Unknown Control, Telemetry, and Protection

| Topic | Unknown information | Why it blocks design | Sources |
|---|---|---|---|
| Sequencing | Power-up order, power-down order, standby-to-main transition, enable order, Power Good behavior, reset release timing, clock dependencies, shutdown behavior, and fault recovery behavior are undocumented. | Incorrect sequencing may prevent bring-up or damage hardware. | `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `15_Reverse_Engineering/08_Bringup.md`; `18_Component_Research/02_Power_Converters.md` |
| Enable signals | Enable signal names, locations, polarities, voltage levels, ownership, and timing are undocumented. | Enables cannot be assigned to connector pins, controller GPIO, or sequencing logic. | `15_Reverse_Engineering/08_Bringup.md`; `18_Component_Research/02_Power_Converters.md`; `18_Component_Research/05_Management_MCU.md` |
| Power Good | Power Good signal names, locations, thresholds, timing, and reset-gating relationship are undocumented. | Reset release, fault handling, and bring-up validation cannot be defined. | `17_System_Architecture/02_System_Block_Diagram.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `18_Component_Research/02_Power_Converters.md` |
| PMBus | Controller identity, bus topology, addresses, commands, telemetry registers, fault registers, pullups, isolation, bus ownership, and firmware ownership are undocumented. | PMBus nets, addresses, register maps, and firmware cannot be defined. | `Wanted_Documents.md`; `15_Reverse_Engineering/04_Management.md`; `18_Component_Research/05_Management_MCU.md` |
| Monitoring | Required voltage, current, temperature, and fault monitoring hardware, locations, telemetry path, bus ownership, addresses, accuracy, limits, and validation role are undocumented. | Health monitoring and validation cannot be specified. | `15_Reverse_Engineering/04_Management.md`; `18_Component_Research/06_Temperature_Sensors.md`; `17_System_Architecture/02_System_Block_Diagram.md` |
| Protection | Fusing, current limiting, hot-swap, inrush control, precharge, fault isolation, and shutdown behavior are undocumented. | Input protection, safe startup, and fault containment cannot be designed. | `18_Component_Research/09_Power_Connectors.md`; `18_Component_Research/02_Power_Converters.md`; `09_AI_Notes/04_Power_Architecture.md` |
| VRM implementation | Actual VRM controller, regulator topology, power-stage devices, phase count, compensation, switching behavior, rails controlled, and electrical constraints are undocumented. | Regulators and power stages cannot be selected or connected. | `13_Reference_Docs/Component_Index.rtf`; `15_Reverse_Engineering/07_Component_ID.md`; `18_Component_Research/02_Power_Converters.md` |
| MP2975 behavior | MP2975 pinout, register map, PMBus behavior, telemetry registers, fault registers, sequencing features, and power-stage pairings are undocumented. | The candidate MP2975 cannot drive schematic, firmware, or BOM decisions. | `13_Reference_Docs/Component_Index.rtf`; `09_AI_Notes/04_Power_Architecture.md`; `18_Component_Research/02_Power_Converters.md` |

## Unknown Requirement Ownership

| Requirement area | Unknown ownership question | Sources |
|---|---|---|
| OAM-defined vs AMD-specific power | No readable local source separates OAM-defined power requirements from AMD-specific MI250X power requirements. | `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `15_Reverse_Engineering/10_Minimal_Carrier.md`; `18_Component_Research/01_OAM_Connector.md` |
| Carrier vs baseboard power entry | Baseboard power architecture and carrier input connector requirements are not documented. | `Wanted_Documents.md`; `18_Component_Research/09_Power_Connectors.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| Carrier vs module vs host monitoring | Required telemetry ownership is not documented as carrier-side, module-side, host-side, BMC-side, or MCU-side. | `15_Reverse_Engineering/04_Management.md`; `18_Component_Research/05_Management_MCU.md`; `18_Component_Research/06_Temperature_Sensors.md` |
| System PSU vs module rail | `12V distribution` and `3000W CRPS` are system-BOM planning targets, but no readable local source maps them to MI250X OAM rails or carrier input requirements. | `20_System_BOM/Power.md`; `18_Component_Research/09_Power_Connectors.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |

# Design Implications

| Rule | Status | Engineering implication | Sources |
|---|---|---|---|
| Do not invent rail values | Inferred | Do not assign rail names, voltages, currents, tolerances, input voltage, total power, or startup order from the current repository alone. | `AI_PROJECT_CONTEXT.md`; `18_Component_Research/02_Power_Converters.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| Do not assign connector power pins | Inferred | Do not assign power pins, ground pins, connector current sharing, connector current rating, or return-current strategy until connector and power sources are verified. | `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `18_Component_Research/01_OAM_Connector.md`; `18_Component_Research/09_Power_Connectors.md` |
| Do not select power components | Inferred | Do not select regulators, converters, VRM controllers, power stages, fuses, hot-swap controllers, current sensors, PMBus devices, or input-power connectors until electrical requirements are sourced. | `18_Component_Research/02_Power_Converters.md`; `18_Component_Research/09_Power_Connectors.md`; `18_Component_Research/10_BOM.md` |
| Do not promote MP2975 | Inferred | Treat MP2975 as a candidate research item only until visually or documentarily confirmed, with role, rails controlled, PMBus behavior, and electrical requirements verified. | `13_Reference_Docs/Component_Index.rtf`; `15_Reverse_Engineering/07_Component_ID.md`; `18_Component_Research/02_Power_Converters.md` |
| Keep system power separate | Inferred | Treat `12V distribution`, `3000W CRPS`, `N+1`, and `hot swap` as system planning targets, not verified MI250X rail requirements. | `20_System_BOM/Power.md`; `18_Component_Research/09_Power_Connectors.md` |
| Gate schematic capture | Inferred | Schematic capture must wait for verified connector power pins, ground pins, rail names, voltages, currents, sequencing, enables, Power Good, PMBus, monitoring, protection, and fault behavior. | `09_AI_Notes/10_Design_Checklist.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `15_Reverse_Engineering/10_Minimal_Carrier.md` |

# Future Research

| Priority | Research task | Required output | Sources |
|---|---|---|---|
| High | Extract OAM power requirements. | Verified OAM-defined rail names, voltages, tolerances, current limits, power pins, ground pins, sequencing rules, enables, and Power Good behavior. | `02_AMD_Docs/GitHub_Links.rtf`; `Wanted_Documents.md`; `09_AI_Notes/04_Power_Architecture.md` |
| High | Obtain the missing Connector Specification and Baseboard Specification. | Verified power-pin assignments, ground-pin assignments, connector current rating, current-sharing strategy, input-power topology, and baseboard power expectations. | `Wanted_Documents.md`; `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `18_Component_Research/09_Power_Connectors.md` |
| High | Determine MI250X rail requirements. | Verified rail names, voltage values, input voltage range, standby rails, auxiliary rails, main rails, total power budget, and per-rail current requirements. | `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `18_Component_Research/02_Power_Converters.md`; `18_Component_Research/10_BOM.md` |
| High | Determine startup and sequencing. | Verified startup order, shutdown order, enable order, Power Good dependencies, reset-release timing, clock dependencies, fault handling, and validation points. | `15_Reverse_Engineering/08_Bringup.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `18_Component_Research/03_Clock_Generators.md` |
| High | Obtain PMBus and VRM documentation. | Verified PMBus topology, addresses, commands, telemetry registers, fault registers, pullups, isolation, VRM role, rail mapping, and sequencing features. | `Wanted_Documents.md`; `15_Reverse_Engineering/04_Management.md`; `13_Reference_Docs/Component_Index.rtf` |
| High | Confirm or reject MP2975 on actual MI250X hardware. | Visual or document-backed confirmation of presence, location, role, associated rails, related power stages, and PMBus behavior. | `13_Reference_Docs/Component_Index.rtf`; `15_Reverse_Engineering/07_Component_ID.md`; `18_Component_Research/02_Power_Converters.md` |
| Medium | Determine monitoring and protection requirements. | Verified voltage, current, temperature, and fault monitoring; fusing, hot-swap, inrush, precharge, current limiting, fault isolation, and shutdown behavior. | `18_Component_Research/06_Temperature_Sensors.md`; `18_Component_Research/09_Power_Connectors.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| Medium | Reconcile system-BOM power planning with carrier requirements. | Verified mapping, or explicit non-mapping, between system PSU/chassis goals and carrier/module electrical requirements. | `20_System_BOM/Power.md`; `18_Component_Research/09_Power_Connectors.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |

# Sources

| Source | Use in this reference |
|---|---|
| `AI_PROJECT_CONTEXT.md` | Defines the open MI250X carrier goal and the rule to avoid invented hardware requirements. |
| `AI_TASKS.md` | Lists reverse-engineering power rails, sequencing, telemetry, power-up testing, cable routing, validating power rails, and voltage validation as tasks or unknowns. |
| `README.md` | States the public-evidence workflow and that undocumented behavior should be tracked rather than assumed. |
| `Wanted_Documents.md` | Marks OAM Specification found and Connector Specification, Baseboard Specification, PMBus Controller Datasheet, VRM Datasheet, and OAM Thermal Guidelines as missing. |
| `02_AMD_Docs/GitHub_Links.rtf` | Links the official Open Accelerator Module specification and states it is useful for power specification. |
| `13_Reference_Docs/Component_Index.rtf` | Identifies MP2975, Monolithic Power Systems, digital multiphase VRM controller function, believed-present status, visual-confirmation gap, public reference, and missing public datasheet. |
| `13_Reference_Docs/Reference_Index.rtf` | Indexes firmware tools, health checks, system validation, MI250 acceptance, GPU management references, and OAM/OCP references. |
| `13_Reference_Docs/ROCm/Overview.md` | Identifies MI250 and MI250X as OCP Accelerator Modules; provides module and software context, not power-rail values. |
| `09_AI_Notes/02_OAM_Interface.md` | Summarizes OAM interface evidence and connector, mechanical, baseboard, and power-source gaps. |
| `09_AI_Notes/04_Power_Architecture.md` | Summarizes OAM power specification relevance, PMBus/VRM gaps, MP2975 uncertainty, and missing power requirements. |
| `09_AI_Notes/06_Management_Controller.md` | Links PMBus, VRM control, voltage monitoring, telemetry, reset, enable, and management-side questions. |
| `09_AI_Notes/07_Cooling.md` | Records that MI250X thermal design power and thermal requirements are not documented locally. |
| `09_AI_Notes/10_Design_Checklist.md` | States that schematic capture and PCB layout must wait for connector, PCIe/REFCLK, power, management, mechanical, baseboard, and footprint-critical requirements. |
| `15_Reverse_Engineering/01_OAM_Pin_Mapping.md` | Records power pins, ground pins, telemetry pins, management pins, and connector assignments as unknown until a verified pinout is available. |
| `15_Reverse_Engineering/03_Clock_Tree.md` | Records reset-clock and REFCLK gaps that affect sequencing and reset release. |
| `15_Reverse_Engineering/04_Management.md` | Records PMBus, voltage monitoring, management interface, telemetry, firmware, and health-monitoring gaps. |
| `15_Reverse_Engineering/05_PCIe.md` | Records PCIe and reset dependencies that affect startup and enumeration. |
| `15_Reverse_Engineering/07_Component_ID.md` | Lists MP2975 as a low-confidence candidate and power stages / PMBus devices as undocumented. |
| `15_Reverse_Engineering/08_Bringup.md` | Records inferred standby power, management initialization, main power, clock startup, reset release, PCIe enumeration, and validation gaps. |
| `15_Reverse_Engineering/09_Block_Diagram.md` | Shows power system and power/reset/sideband blocks as undocumented architecture dependencies. |
| `15_Reverse_Engineering/10_Minimal_Carrier.md` | Describes minimum carrier power delivery, sequencing, and unresolved implementation details. |
| `17_System_Architecture/01_System_Goals.md` | Lists reliable power sequencing as a hardware goal. |
| `17_System_Architecture/02_System_Block_Diagram.md` | Marks power subsystem rails, sequencing, Power Good, and telemetry as undocumented. |
| `17_System_Architecture/03_Minimal_Carrier_Requirements.md` | Lists power rail implementation, current, sequencing, enables, Power Good, monitoring, PMBus/VRM investigation, and power risks. |
| `17_System_Architecture/04_Future_Expansion.md` | Records future single-, dual-, four-, and eight-MI250X system revisions that may affect later power distribution. |
| `18_Component_Research/01_OAM_Connector.md` | Records connector power-pin, ground-pin, current-rating, current-sharing, telemetry, and sideband gaps. |
| `18_Component_Research/02_Power_Converters.md` | Main related component research for power rails, VRMs, MP2975, PMBus, voltage regulators, sequencing, Power Good, telemetry, and current requirements. |
| `18_Component_Research/03_Clock_Generators.md` | Records reset-clock-power timing and REFCLK gaps that affect startup sequencing. |
| `18_Component_Research/05_Management_MCU.md` | Records PMBus, telemetry ownership, reset, enables, Power Good, GPIO, fault handling, and sequencing ownership as unresolved. |
| `18_Component_Research/06_Temperature_Sensors.md` | Records voltage/current/fault monitoring and PMBus telemetry as unresolved. |
| `18_Component_Research/09_Power_Connectors.md` | Records carrier input-power connector, PSU topology, cable assembly, connector rating, fusing, hot-swap, current limiting, power pins, and ground pins as unknown. |
| `18_Component_Research/10_BOM.md` | Tracks MP2975 as a candidate and power converters, regulators, power stages, PMBus devices, and input-power connector as unknown. |
| `20_System_BOM/Power.md` | Provides system-level planning targets for CRPS supplies, 12V distribution, N+1, hot swap, eight MI250X modules, and dual host systems; these are not verified module rails. |