# Purpose

Index component-level research needed to turn the AMD Instinct MI250X OAM carrier-board concept into a schematic and BOM using repository-supported engineering evidence only.

This folder is a hardware engineering component-selection notebook, not an approved schematic source or purchasable BOM. The repository identifies MI250X as the target OAM module and repeatedly marks connector, power, PCIe, clock, management, cooling, mechanical, and component-selection details as unresolved design inputs. Sources: `README.md`; `13_Reference_Docs/ROCm/Overview.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `15_Reverse_Engineering/07_Component_ID.md`.

# Verified

Only facts directly supported by repository documents are included here.

| Topic | Verified repository fact | Sources |
|---|---|---|
| Evidence workflow | Repository guidance requires sourced facts to be separated from unknowns and undocumented behavior to be tracked rather than assumed. | `README.md`; `AI_TASKS.md`; `15_Reverse_Engineering/README.md` |
| Target module | AMD Instinct MI250X is the carrier target and is documented as an OCP Accelerator Module with two GCDs and 128 GB total memory. | `13_Reference_Docs/ROCm/Overview.md`; `15_Reverse_Engineering/07_Component_ID.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| Component research role | This folder is the project location for OAM connector, power converter, clock, EEPROM/FRU, management, sensor, fan, PCIe signal-conditioning, power connector, and BOM research. | `18_Component_Research/01_OAM_Connector.md`; `18_Component_Research/02_Power_Converters.md`; `18_Component_Research/10_BOM.md` |
| Design gate | Component choices should not enter schematic or BOM until role, part number, interface, and constraints are supported by readable source documents or verified measurement. | `18_Component_Research/10_BOM.md`; `09_AI_Notes/10_Design_Checklist.md`; `15_Reverse_Engineering/07_Component_ID.md` |

# Candidate Components

This table is an index of the related research documents and their current component-confidence status.

| Document | Research focus | Status | Repository-supported current position | Related documents | Sources |
|---|---|---|---|---|---|
| `01_OAM_Connector.md` | OAM connector, pinout, footprint, mating height, and mechanical/electrical interface. | Unknown / Candidate reference | Molex Mirror Mezz is indexed as a candidate reference, but the actual MI250X OAM connector is not verified. | `02_Power_Converters.md`; `03_Clock_Generators.md`; `08_PCIe_Retimers.md`; `09_Power_Connectors.md` | `13_Reference_Docs/Reference_Index.rtf`; `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `15_Reverse_Engineering/07_Component_ID.md` |
| `02_Power_Converters.md` | Power rails, VRMs, `MP2975`, PMBus, regulators, sequencing, telemetry, and current requirements. | Candidate / Unknown | `MP2975` is a low-confidence candidate; rail names, voltages, currents, regulators, power stages, sequencing, and telemetry remain unknown. | `01_OAM_Connector.md`; `05_Management_MCU.md`; `06_Temperature_Sensors.md`; `09_Power_Connectors.md` | `13_Reference_Docs/Component_Index.rtf`; `15_Reverse_Engineering/02_Power_Rails.md`; `18_Component_Research/02_Power_Converters.md` |
| `03_Clock_Generators.md` | REFCLK, clock generators, oscillators, PLLs, buffers, jitter, skew, and clock distribution. | Unknown | No clock component part number, REFCLK frequency, source, topology, jitter budget, or skew budget is documented. | `01_OAM_Connector.md`; `02_Power_Converters.md`; `08_PCIe_Retimers.md` | `Wanted_Documents.md`; `15_Reverse_Engineering/03_Clock_Tree.md`; `18_Component_Research/03_Clock_Generators.md` |
| `04_EEPROM_FRU.md` | EEPROM, FRU EEPROM, I2C EEPROM, board identification, SMBus, configuration EEPROM, and metadata. | Unknown | EEPROM, FRU EEPROM, contents, ownership, bus, address, and firmware-storage relationship are undocumented. | `01_OAM_Connector.md`; `05_Management_MCU.md`; `10_BOM.md` | `15_Reverse_Engineering/04_Management.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `18_Component_Research/04_EEPROM_FRU.md` |
| `05_Management_MCU.md` | BMC, management MCU, PMBus, I2C/SMBus, GPIO, telemetry, firmware, fan control, and sequencing. | Unknown | Carrier-side MCU/BMC requirement, part number, bus topology, GPIO list, firmware role, and control ownership are undocumented. | `02_Power_Converters.md`; `04_EEPROM_FRU.md`; `06_Temperature_Sensors.md`; `07_Fan_Control.md` | `15_Reverse_Engineering/04_Management.md`; `09_AI_Notes/06_Management_Controller.md`; `18_Component_Research/05_Management_MCU.md` |
| `06_Temperature_Sensors.md` | Temperature sensors, board temperature, junction temperature, telemetry, and I2C sensors. | Unknown | Carrier-visible sensor requirements, locations, telemetry path, PMBus relationship, and part numbers are undocumented. | `02_Power_Converters.md`; `05_Management_MCU.md`; `07_Fan_Control.md` | `15_Reverse_Engineering/04_Management.md`; `09_AI_Notes/07_Cooling.md`; `18_Component_Research/06_Temperature_Sensors.md` |
| `07_Fan_Control.md` | Fan controller, PWM, tachometer, fan headers, airflow, thermal feedback, and cooling-control ownership. | Unknown | Fan requirement, controller requirement, PWM, tachometer, airflow/coolant targets, and cooling-control ownership are undocumented. | `05_Management_MCU.md`; `06_Temperature_Sensors.md`; `09_Power_Connectors.md` | `15_Reverse_Engineering/04_Management.md`; `09_AI_Notes/07_Cooling.md`; `18_Component_Research/07_Fan_Control.md` |
| `08_PCIe_Retimers.md` | PCIe switches, retimers, redrivers, equalization, lane mapping, Gen4/Gen5, and signal integrity. | Unknown | Switch, retimer, redriver, lane mapping, routing rules, equalization, and Gen5 requirements are not verified. | `01_OAM_Connector.md`; `03_Clock_Generators.md`; `10_BOM.md` | `15_Reverse_Engineering/05_PCIe.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `18_Component_Research/08_PCIe_Retimers.md` |
| `09_Power_Connectors.md` | Carrier input-power connector, PSU topology, high-current handling, cable assemblies, and connector ratings. | Unknown | Carrier input connector, PSU topology, connector ratings, cable assemblies, fusing, hot-swap, and current limiting are undocumented. | `01_OAM_Connector.md`; `02_Power_Converters.md`; `07_Fan_Control.md` | `15_Reverse_Engineering/02_Power_Rails.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `18_Component_Research/09_Power_Connectors.md` |
| `10_BOM.md` | Living BOM planning and component-confidence tracking. | Verified / Candidate / Unknown | MI250X is the verified target; `MP2975` and Molex Mirror Mezz are candidates; most carrier component categories remain unknown. | All component research documents in this folder. | `15_Reverse_Engineering/07_Component_ID.md`; `18_Component_Research/10_BOM.md` |

# Unknown

- **Unknown:** Exact MI250X OAM connector manufacturer, family, part number, pin count, pinout, mating height, current rating, and AMD-specific pins. Sources: `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `18_Component_Research/01_OAM_Connector.md`.
- **Unknown:** Power rails, current requirements, power sequencing, enable signals, Power Good behavior, regulators, power stages, monitoring, and input-power connector requirements. Sources: `15_Reverse_Engineering/02_Power_Rails.md`; `18_Component_Research/02_Power_Converters.md`; `18_Component_Research/09_Power_Connectors.md`.
- **Unknown:** Clock generators, oscillators, buffers, PLLs, REFCLK topology, frequency, jitter, skew, and routing requirements. Sources: `15_Reverse_Engineering/03_Clock_Tree.md`; `18_Component_Research/03_Clock_Generators.md`.
- **Unknown:** EEPROM, FRU EEPROM, management MCU, BMC interaction, sensors, fan control, firmware-management hardware, PCIe switches, retimers, and redrivers are not proven required at the carrier level. Sources: `15_Reverse_Engineering/04_Management.md`; `15_Reverse_Engineering/05_PCIe.md`; `18_Component_Research/04_EEPROM_FRU.md`; `18_Component_Research/08_PCIe_Retimers.md`.
- **Unknown:** Cooling method, thermal design power, thermal interface, airflow/coolant requirements, fan-control ownership, sensor placement, and mechanical mounting constraints. Sources: `09_AI_Notes/07_Cooling.md`; `15_Reverse_Engineering/06_Mechanical.md`; `18_Component_Research/07_Fan_Control.md`.
- **Unknown:** Approved procurement BOM quantities, approved manufacturers, part numbers, packages, footprints, alternates, lifecycle status, and sourcing links. Sources: `15_Reverse_Engineering/07_Component_ID.md`; `18_Component_Research/10_BOM.md`.

# Design Implications

- Treat this folder as a component-selection notebook, not a list of approved parts.
- Keep all component documents in the same structure: `Purpose`, `Verified`, `Candidate Components`, `Unknown`, `Design Implications`, `Future Research`, and `Sources`.
- Do not place components into schematic capture, PCB layout, or procurement until the related document has verified role, part number, interface, constraints, footprint, and sourcing evidence.
- Keep related documents linked because connector, power, clock, management, sensor, fan, PCIe, cooling, mechanical, and BOM decisions depend on each other.
- Treat `MP2975` and Molex Mirror Mezz as candidate research items only until readable MI250X-specific evidence or verified physical inspection confirms them.

# Future Research

| Priority | Research task | Required output | Sources |
|---|---|---|---|
| High | Obtain or extract missing integration specifications. | Connector Specification, Baseboard Specification, PCIe Routing Guide, REFCLK Guide, PMBus Controller Datasheet, VRM Datasheet, OAM Thermal Guidelines, and related photo/mechanical evidence. | `Wanted_Documents.md`; `09_AI_Notes/10_Design_Checklist.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| High | Verify named candidate parts. | Evidence-backed confirmation or rejection of `MP2975` and Molex Mirror Mezz for MI250X hardware. | `13_Reference_Docs/Component_Index.rtf`; `13_Reference_Docs/Reference_Index.rtf`; `15_Reverse_Engineering/07_Component_ID.md` |
| High | Keep every component report source-backed. | Each document should retain only sourced facts, candidate categories, explicit unknowns, design implications, future research tasks, and source lists. | `README.md`; `AI_TASKS.md`; `18_Component_Research/10_BOM.md` |
| Medium | Convert the notebook into a procurement BOM after requirements mature. | Verified quantity, manufacturer, part number, package, footprint, rating, lifecycle, alternates, and source citation for every required carrier component. | `18_Component_Research/10_BOM.md`; `17_System_Architecture/05_Component_Selection.md`; `09_AI_Notes/10_Design_Checklist.md` |

# Sources

- `README.md` - States the public-evidence workflow and that undocumented behavior should be tracked rather than assumed.
- `AI_TASKS.md` - Lists evidence-label rules and current connector, power, clock, management, EEPROM, sensor, fan, thermal, and validation unknowns.
- `Wanted_Documents.md` - Tracks missing connector, baseboard, PCIe, REFCLK, PMBus, VRM, thermal, and photo evidence.
- `13_Reference_Docs/Component_Index.rtf` - Identifies `MP2975` as a low-confidence candidate.
- `13_Reference_Docs/Reference_Index.rtf` - Indexes OAM/OCP, Molex Mirror Mezz, cooling, firmware, memory, and GPU management references.
- `13_Reference_Docs/ROCm/Overview.md` - Identifies MI250X OAM module context.
- `15_Reverse_Engineering/01_OAM_Pin_Mapping.md` - Main source for OAM connector and pinout unknowns.
- `15_Reverse_Engineering/02_Power_Rails.md` - Main source for power rail, sequencing, PMBus, telemetry, and power unknowns.
- `15_Reverse_Engineering/03_Clock_Tree.md` - Main source for REFCLK and clocking unknowns.
- `15_Reverse_Engineering/04_Management.md` - Main source for management, EEPROM, PMBus, firmware, sensors, and fan-control unknowns.
- `15_Reverse_Engineering/05_PCIe.md` - Main source for PCIe, lane mapping, switch, retimer, and signal-integrity unknowns.
- `15_Reverse_Engineering/06_Mechanical.md` - Main source for mechanical and cooling-adjacent unknowns.
- `15_Reverse_Engineering/07_Component_ID.md` - Component-confidence table and unknown component category list.
- `15_Reverse_Engineering/10_Minimal_Carrier.md` - Minimum carrier requirement and optional hardware source.
- `17_System_Architecture/03_Minimal_Carrier_Requirements.md` - Main source for required, recommended, optional, unknown, and risk categories.
- `17_System_Architecture/05_Component_Selection.md` - Empty candidate-parts sections for future verified component choices.
- `18_Component_Research/01_OAM_Connector.md` - OAM connector research.
- `18_Component_Research/02_Power_Converters.md` - Power converter and regulator research.
- `18_Component_Research/03_Clock_Generators.md` - Clock generator, oscillator, PLL, buffer, and REFCLK research.
- `18_Component_Research/04_EEPROM_FRU.md` - EEPROM and FRU EEPROM research.
- `18_Component_Research/05_Management_MCU.md` - Management MCU and BMC-side hardware research.
- `18_Component_Research/06_Temperature_Sensors.md` - Temperature sensor and telemetry research.
- `18_Component_Research/07_Fan_Control.md` - Fan controller and cooling-control research.
- `18_Component_Research/08_PCIe_Retimers.md` - PCIe retimer, redriver, switch, and signal-conditioning research.
- `18_Component_Research/09_Power_Connectors.md` - Carrier input-power connector research.
- `18_Component_Research/10_BOM.md` - Living BOM planning and component-confidence research.