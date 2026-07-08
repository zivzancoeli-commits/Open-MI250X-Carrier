# Purpose

Research temperature sensors, thermal monitoring, junction temperature, board temperature, telemetry, and I2C sensor requirements for an open-source AMD Instinct MI250X OAM carrier board using only repository-supported information.

This document is not a sensor selection, sensor placement plan, thermal design, telemetry map, schematic source, or BOM. The repository does not currently contain verified temperature sensor part numbers, I2C sensor part numbers, sensor technologies, sensor locations, junction-temperature access, board-temperature requirements, PMBus telemetry registers, thermal limits, airflow/coolant requirements, or carrier-vs-module monitoring ownership. Sources: `15_Reverse_Engineering/04_Management.md`; `15_Reverse_Engineering/02_Power_Rails.md`; `09_AI_Notes/07_Cooling.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`.

# Verified

Only facts directly supported by repository documents are included here.

| Topic | Verified repository fact | Sources |
|---|---|---|
| Project evidence workflow | The repository tracks unknown behavior instead of assuming it. | `README.md`; `AI_TASKS.md` |
| Temperature-sensor research scope | `06_Temperature_Sensors.md` is defined as temperature sensor research in the component-research index. | `18_Component_Research/README.md` |
| Management research scope | The management note includes temperature sensors, voltage monitoring, fan control, PMBus, health monitoring, and firmware management in its research scope. | `15_Reverse_Engineering/04_Management.md` |
| Management interface status | Temperature sensors, voltage monitoring, health-monitoring hardware, fan control, SMBus, I2C, and PMBus are undocumented in readable local files. | `15_Reverse_Engineering/04_Management.md` |
| Power telemetry scope | The power note tracks telemetry, monitoring, voltage/current/fault monitoring, PMBus, VRM behavior, and sensor requirements as unresolved topics. | `15_Reverse_Engineering/02_Power_Rails.md` |
| Thermal evidence gap | OAM Thermal Guidelines are marked missing. | `Wanted_Documents.md`; `09_AI_Notes/07_Cooling.md`; `18_Component_Research/07_Fan_Control.md` |
| Cooling references | Cold Plate Requirements, Cold Plate Development, Rack Manifold, Reservoir & Pumping Unit, Water Cooling, Glycol Cooling, and Immersion Cooling are indexed. | `13_Reference_Docs/Reference_Index.rtf`; `09_AI_Notes/07_Cooling.md`; `15_Reverse_Engineering/06_Mechanical.md` |
| Photo tracking | Front, back, and connector photos are marked found; heatsink and baseboard photos are not marked found. | `Wanted_Documents.md`; `15_Reverse_Engineering/06_Mechanical.md`; `18_Component_Research/07_Fan_Control.md` |
| Local photo gap | Front, back, and connector photos are marked found, but repository notes state that no image files are present in the readable repository. | `15_Reverse_Engineering/06_Mechanical.md`; `09_AI_Notes/09_Unknowns.md`; `18_Component_Research/01_OAM_Connector.md` |
| Health and validation references | MI250 Acceptance, Health Checks, System Validation, AMD Lab Notes, and GPU Accelerator Management Interfaces are indexed. | `13_Reference_Docs/Reference_Index.rtf`; `15_Reverse_Engineering/04_Management.md`; `15_Reverse_Engineering/08_Bringup.md` |
| System diagram sensor status | The system block diagram shows Temperature / Voltage Sensors as a support block with carrier role undocumented. | `17_System_Architecture/02_System_Block_Diagram.md` |
| Minimal carrier status | Temperature, voltage, current, and fault sensors are optional until requirements prove they are required on the carrier. | `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `15_Reverse_Engineering/10_Minimal_Carrier.md` |
| Component-identification status | Temperature sensors and PMBus devices are listed as undocumented component categories. | `15_Reverse_Engineering/07_Component_ID.md`; `18_Component_Research/README.md` |
| BOM status | The BOM lists temperature sensors and voltage/current/fault sensors as unknown component categories. | `18_Component_Research/10_BOM.md` |
| Fan-control relationship | Fan control is named as a management topic, but fan-control responsibility, thermal feedback, PWM, tachometer, and cooling implementation are undocumented. | `18_Component_Research/07_Fan_Control.md`; `15_Reverse_Engineering/04_Management.md` |

# Candidate Components

No temperature sensor, I2C sensor, thermal monitor, board-temperature sensor, or junction-temperature access path is verified as selected, required, or present.

| Sensor or category | Manufacturer | Part number | Status | Repository-supported information | Design position | Sources |
|---|---|---|---|---|---|---|
| Temperature sensor | Unknown | Unknown | Unknown category | Temperature sensors are named as a management research topic and undocumented component category. | Do not select or place a temperature sensor until requirement, location, interface, power, accuracy, and part number are verified. | `15_Reverse_Engineering/04_Management.md`; `15_Reverse_Engineering/07_Component_ID.md`; `18_Component_Research/10_BOM.md` |
| I2C temperature sensor | Unknown | Unknown | Unknown category | I2C is named as an undocumented management interface, but no readable source proves an I2C sensor requirement. | Treat as a research category only; do not assign an I2C address, voltage level, pullup, bus owner, or device. | `15_Reverse_Engineering/04_Management.md`; `09_AI_Notes/06_Management_Controller.md`; `18_Component_Research/05_Management_MCU.md` |
| Board-temperature sensor | Unknown | Unknown | Unknown category | No readable source defines board-temperature sensing, sensor placement, or board-temperature limits. | Do not add board-temperature sensors until thermal requirement and placement evidence exist. | `09_AI_Notes/07_Cooling.md`; `15_Reverse_Engineering/06_Mechanical.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| Junction-temperature telemetry path | Unknown | Unknown | Unknown category | No readable source defines junction-temperature access, telemetry source, register, or validation use. | Do not assume MI250X junction-temperature access path from the current repository. | `15_Reverse_Engineering/04_Management.md`; `15_Reverse_Engineering/02_Power_Rails.md`; `15_Reverse_Engineering/08_Bringup.md` |
| Voltage / current / fault sensor | Unknown | Unknown | Unknown category | Required voltage, current, temperature, and fault monitoring hardware is not documented at signal or controller level. | Treat as unresolved until telemetry and monitoring ownership are defined. | `15_Reverse_Engineering/02_Power_Rails.md`; `17_System_Architecture/02_System_Block_Diagram.md`; `18_Component_Research/10_BOM.md` |
| PMBus telemetry device | Unknown | Unknown | Unknown category | PMBus Controller Datasheet is missing; PMBus topology, addresses, commands, telemetry registers, and fault registers are undocumented. | Do not treat PMBus telemetry as a temperature-sensor interface until PMBus requirements are verified. | `Wanted_Documents.md`; `15_Reverse_Engineering/02_Power_Rails.md`; `18_Component_Research/02_Power_Converters.md` |
| Fan-control feedback sensor | Unknown | Unknown | Unknown category | Thermal feedback is listed as unknown; temperature sensor part numbers, locations, ownership, thermal coupling, and telemetry path are undocumented. | Do not tie fan control to any sensor until cooling method and ownership are verified. | `18_Component_Research/07_Fan_Control.md`; `09_AI_Notes/07_Cooling.md`; `15_Reverse_Engineering/04_Management.md` |

# Unknown

- **Unknown:** Temperature sensor manufacturer, part number, package, sensor technology, temperature range, accuracy, resolution, power rail, interface, address behavior, and footprint. Sources: `15_Reverse_Engineering/04_Management.md`; `15_Reverse_Engineering/07_Component_ID.md`; `18_Component_Research/10_BOM.md`.
- **Unknown:** I2C sensor requirement, I2C topology, bus ownership, addresses, voltage levels, pullups, muxing, isolation, connector pins, and device list. Sources: `15_Reverse_Engineering/04_Management.md`; `09_AI_Notes/06_Management_Controller.md`; `18_Component_Research/05_Management_MCU.md`.
- **Unknown:** Junction-temperature source, limit, access method, telemetry register, polling owner, alert behavior, and validation use. Sources: `15_Reverse_Engineering/04_Management.md`; `15_Reverse_Engineering/02_Power_Rails.md`; `15_Reverse_Engineering/08_Bringup.md`.
- **Unknown:** Board-temperature requirement, board sensor count, sensor locations, board limits, mechanical attachment, thermal coupling, and test method. Sources: `15_Reverse_Engineering/06_Mechanical.md`; `09_AI_Notes/07_Cooling.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`.
- **Unknown:** Sensor locations, mechanical attachment, thermal coupling, keepouts, and whether sensors are module-side, carrier-side, baseboard-side, host-side, MCU/BMC-side, or external. Sources: `15_Reverse_Engineering/06_Mechanical.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `17_System_Architecture/02_System_Block_Diagram.md`.
- **Unknown:** Required thermal design power, thermal limits, cold plate or heatsink interface, airflow/coolant requirements, mounting force, fan-control responsibility, and thermal envelope. Sources: `09_AI_Notes/07_Cooling.md`; `15_Reverse_Engineering/06_Mechanical.md`; `Wanted_Documents.md`.
- **Unknown:** PMBus telemetry relationship to temperature, including controller identity, topology, addresses, command set, telemetry registers, fault registers, pullups, and isolation. Sources: `Wanted_Documents.md`; `15_Reverse_Engineering/04_Management.md`; `15_Reverse_Engineering/02_Power_Rails.md`.
- **Unknown:** Required telemetry signals, telemetry bus, register set, polling ownership, alert/fault behavior, and health-check dependency. Sources: `15_Reverse_Engineering/02_Power_Rails.md`; `15_Reverse_Engineering/04_Management.md`; `18_Component_Research/05_Management_MCU.md`.
- **Unknown:** Whether temperature, voltage, current, or fault sensors are required for minimal operation, recommended for bring-up, or useful only for validation. Sources: `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `15_Reverse_Engineering/08_Bringup.md`; `18_Component_Research/10_BOM.md`.

# Design Implications

- Do not select temperature sensors, I2C sensors, PMBus devices, fan-feedback sensors, voltage sensors, current sensors, or fault sensors from the current repository alone.
- Do not assume junction-temperature access, board-temperature limits, thermal thresholds, sensor locations, thermal coupling, or sensor ownership without verified thermal, management, or mechanical sources.
- Do not assign I2C, SMBus, PMBus, telemetry, alert, interrupt, fan-control, or sensor nets until connector pinout, management topology, and sensor requirements are verified.
- Treat Temperature / Voltage Sensors in system diagrams as a dependency placeholder, not a verified schematic requirement.
- Treat indexed cooling, health-check, and validation references as research leads only; they do not define carrier-visible sensors or telemetry requirements.
- Keep sensor research linked to management, power, fan control, cooling, mechanical, connector, and bring-up notes because thermal monitoring, PMBus telemetry, fan feedback, and health checks cross subsystem boundaries.

# Future Research

| Priority | Research task | Required output | Sources |
|---|---|---|---|
| High | Obtain OAM Thermal Guidelines or another verified MI250X thermal source. | Verified thermal limits, sensor expectations, cooling envelope, heatsink/cold-plate interface, airflow/coolant requirements, and validation criteria. | `Wanted_Documents.md`; `09_AI_Notes/07_Cooling.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| High | Determine whether carrier-visible temperature sensors are required. | Verified carrier-side, module-side, baseboard-side, host-side, external, or no-carrier-temperature-sensor responsibility. | `15_Reverse_Engineering/04_Management.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `17_System_Architecture/02_System_Block_Diagram.md` |
| High | Determine junction-temperature access. | Verified source, limit, access method, telemetry path, polling owner, alert behavior, and validation use, or verified statement that no carrier-visible junction-temperature access is required. | `15_Reverse_Engineering/04_Management.md`; `15_Reverse_Engineering/08_Bringup.md`; `13_Reference_Docs/Reference_Index.rtf` |
| High | Determine board-temperature requirements. | Verified board sensor count, location, limit, attachment method, thermal coupling, interface, and test procedure, or verified statement that no board-temperature sensing is required. | `09_AI_Notes/07_Cooling.md`; `15_Reverse_Engineering/06_Mechanical.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| High | Obtain verified management and sensor-bus documentation. | Verified I2C/SMBus/PMBus pins, voltage levels, pullups, addresses, bus ownership, muxing, isolation, and sensor devices if required. | `15_Reverse_Engineering/04_Management.md`; `18_Component_Research/05_Management_MCU.md`; `18_Component_Research/01_OAM_Connector.md` |
| Medium | Determine PMBus telemetry relationship. | Verified whether PMBus carries temperature, voltage, current, fault, or VRM telemetry, including register and ownership details if applicable. | `Wanted_Documents.md`; `15_Reverse_Engineering/02_Power_Rails.md`; `18_Component_Research/02_Power_Converters.md` |
| Medium | Locate or recover thermal and photo evidence. | Usable front/back/connector/heatsink/baseboard photos or thermal drawings with provenance and measurement method. | `Wanted_Documents.md`; `15_Reverse_Engineering/06_Mechanical.md`; `09_AI_Notes/09_Unknowns.md` |
| Medium | Identify candidate sensors only after requirements are known. | Verified manufacturer, part number, package, interface, accuracy, range, power rail, address behavior, and BOM status for any required sensor. | `15_Reverse_Engineering/07_Component_ID.md`; `17_System_Architecture/05_Component_Selection.md`; `18_Component_Research/10_BOM.md` |
| Medium | Add bring-up and validation sensor checks after requirements are sourced. | Verified thermal monitoring checks, telemetry checks, health-check inputs, pass/fail criteria, and logging method if required. | `AI_TASKS.md`; `15_Reverse_Engineering/08_Bringup.md`; `13_Reference_Docs/Reference_Index.rtf` |

# Sources

- `README.md` - States the evidence workflow and that undocumented behavior should be tracked rather than assumed.
- `AI_TASKS.md` - Lists thermal monitoring, fan control, sensor placement, thermal testing, telemetry, and validation tasks as unresolved project areas.
- `Wanted_Documents.md` - Marks OAM Thermal Guidelines, heatsink photo, baseboard photo, PMBus Controller Datasheet, and VRM Datasheet as missing.
- `13_Reference_Docs/Reference_Index.rtf` - Indexes cooling references, firmware references, health checks, system validation, MI250 acceptance, and GPU accelerator management interfaces.
- `09_AI_Notes/07_Cooling.md` - Summarizes cooling evidence and gaps, including missing OAM Thermal Guidelines, missing thermal photos/drawings, and unknown sensor locations.
- `15_Reverse_Engineering/02_Power_Rails.md` - Main source for PMBus, telemetry, voltage/current/fault monitoring, and sensor unknowns.
- `15_Reverse_Engineering/04_Management.md` - Main source for management, temperature sensors, voltage monitoring, I2C/SMBus, PMBus, fan control, firmware, and health-monitoring gaps.
- `15_Reverse_Engineering/06_Mechanical.md` - Records cooling envelope, thermal keepout, heatsink geometry, mounting, dimensions, and photo evidence gaps.
- `15_Reverse_Engineering/07_Component_ID.md` - Lists temperature sensors and PMBus devices as undocumented component categories.
- `15_Reverse_Engineering/08_Bringup.md` - Records management initialization, voltage validation, health checks, and bring-up prerequisites as unresolved.
- `15_Reverse_Engineering/10_Minimal_Carrier.md` - Lists sensors and fan controller as optional until proven required.
- `17_System_Architecture/02_System_Block_Diagram.md` - Shows Temperature / Voltage Sensors as a block with carrier role undocumented.
- `17_System_Architecture/03_Minimal_Carrier_Requirements.md` - Lists temperature, voltage, current, and fault sensors as optional until requirements prove they are required on the carrier.
- `18_Component_Research/README.md` - Defines `06_Temperature_Sensors.md` as temperature sensor research and marks sensor requirements and locations as unknown.
- `18_Component_Research/02_Power_Converters.md` - Summarizes PMBus telemetry, voltage/current monitoring, and fault monitoring as unknown.
- `18_Component_Research/05_Management_MCU.md` - Summarizes I2C/SMBus/PMBus, telemetry ownership, sensor telemetry, and monitoring ownership as unknown.
- `18_Component_Research/07_Fan_Control.md` - Records thermal feedback, fan-control ownership, PWM, tachometer, and cooling-control requirements as unresolved.
- `18_Component_Research/10_BOM.md` - Tracks temperature sensors and voltage/current/fault sensors as unknown component categories.