# Purpose

Research BMC, management MCU, PMBus, I2C, SMBus, GPIO, telemetry, firmware, fan control, and power-sequencing requirements for an open-source AMD Instinct MI250X OAM carrier board using only repository information.

This document is not a management-controller selection, firmware architecture, bus topology, GPIO list, sequencing controller design, thermal-control design, schematic source, or BOM. The repository does not currently contain a verified management MCU or BMC part number, required carrier-side controller, required GPIO list, PMBus/I2C/SMBus topology, telemetry register map, reset-control scheme, fan-control wiring, firmware-update wiring, firmware flow, or power-sequencing implementation for the MI250X OAM carrier. Sources: `15_Reverse_Engineering/04_Management.md`; `09_AI_Notes/06_Management_Controller.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`.

# Verified

Only facts directly supported by repository documents are included here.

| Topic | Verified repository fact | Sources |
|---|---|---|
| Project evidence workflow | The repository tracks unknown behavior instead of assuming it. | `README.md`; `AI_TASKS.md` |
| Management research scope | The management note includes SMBus, I2C, PMBus, EEPROM, FRU EEPROM, BMC interaction, management MCU, fan control, temperature sensors, voltage monitoring, firmware management, and health monitoring. | `15_Reverse_Engineering/04_Management.md` |
| Management interface status | SMBus, I2C, PMBus, EEPROM, FRU EEPROM, BMC interaction, management MCU, fan control, temperature sensors, voltage monitoring, firmware-management hardware, and health-monitoring hardware are undocumented in readable local files. | `15_Reverse_Engineering/04_Management.md` |
| Firmware references | Firmware Tool v2.3, Firmware Tool v2.2, AMD FW Flash Guide, and Firmware Update Guide are indexed. | `13_Reference_Docs/Reference_Index.rtf`; `15_Reverse_Engineering/04_Management.md`; `09_AI_Notes/06_Management_Controller.md` |
| Health and validation references | MI250 Acceptance, Health Checks, System Validation, AMD Lab Notes, and GPU Accelerator Management Interfaces are indexed. | `13_Reference_Docs/Reference_Index.rtf`; `15_Reverse_Engineering/04_Management.md`; `15_Reverse_Engineering/08_Bringup.md` |
| PMBus document gap | PMBus Controller Datasheet is marked missing. | `Wanted_Documents.md`; `15_Reverse_Engineering/04_Management.md`; `18_Component_Research/02_Power_Converters.md` |
| VRM document gap | VRM Datasheet is marked missing. | `Wanted_Documents.md`; `15_Reverse_Engineering/04_Management.md`; `15_Reverse_Engineering/02_Power_Rails.md` |
| MP2975 context | `MP2975` is listed as a Monolithic Power Systems digital multiphase VRM controller, believed present on MI250X and not visually confirmed. | `13_Reference_Docs/Component_Index.rtf`; `15_Reverse_Engineering/07_Component_ID.md`; `18_Component_Research/02_Power_Converters.md` |
| MP2975 datasheet status | No public MP2975 datasheet is available in the repository. | `13_Reference_Docs/Component_Index.rtf`; `09_AI_Notes/04_Power_Architecture.md` |
| Component-identification status | Management controllers, PMBus devices, EEPROMs, sensors, fan controllers, and other component categories are undocumented. | `15_Reverse_Engineering/07_Component_ID.md`; `18_Component_Research/README.md` |
| Component-selection status | The component-selection note contains a Management MCU candidate-parts section, but no candidate parts are filled in. | `17_System_Architecture/05_Component_Selection.md` |
| BOM status | The BOM tracks Management MCU and BMC as unknown categories. | `18_Component_Research/10_BOM.md` |
| Minimal carrier status | Management MCU, EEPROM/FRU, firmware flashing hardware, fan controller, and sensors are optional or unknown until a readable source proves they are required. | `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `15_Reverse_Engineering/10_Minimal_Carrier.md` |
| System diagram status | The system block diagram shows Management MCU / BMC, EEPROM / FRU EEPROM, sensors, and fan controller as support blocks with requirements undocumented. | `17_System_Architecture/02_System_Block_Diagram.md`; `15_Reverse_Engineering/09_Block_Diagram.md` |
| Bring-up status | Management initialization, EEPROM access, firmware loading, health checks, reset sequence, power sequencing, enables, and Power Good signals are undocumented in readable local files. | `15_Reverse_Engineering/08_Bringup.md`; `15_Reverse_Engineering/02_Power_Rails.md`; `15_Reverse_Engineering/04_Management.md` |
| Fan-control status | Fan control is named as a management topic, but fan-control responsibility and cooling implementation are undocumented. | `15_Reverse_Engineering/04_Management.md`; `18_Component_Research/07_Fan_Control.md` |
| Telemetry status | Required telemetry signals, telemetry bus, telemetry register set, and telemetry ownership are not documented. | `15_Reverse_Engineering/02_Power_Rails.md`; `18_Component_Research/02_Power_Converters.md`; `18_Component_Research/06_Temperature_Sensors.md` |

# Candidate Components

No management MCU, BMC, or microcontroller family is verified as selected, required, or present.

| Candidate or category | Manufacturer | Part number | Status | Repository-supported information | Design position | Sources |
|---|---|---|---|---|---|---|
| Specific management MCU | Unknown | Unknown | Unknown category | No management-controller part number is identified in readable local files. | Do not select or place a management MCU until requirement, interfaces, power, pins, firmware role, and part number are verified. | `09_AI_Notes/06_Management_Controller.md`; `15_Reverse_Engineering/07_Component_ID.md`; `18_Component_Research/README.md` |
| Specific BMC | Unknown | Unknown | Unknown category | BMC interaction is listed as undocumented, and no BMC part number or carrier-side requirement is verified. | Do not assume a carrier-side or host-side BMC architecture. | `15_Reverse_Engineering/04_Management.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `18_Component_Research/10_BOM.md` |
| Generic MCU family | Unknown | Unknown | Unknown category | No readable local source identifies MCU family, architecture, package, voltage, memory, peripheral, boot, debug, or firmware requirements. | Do not select an MCU family from general capability assumptions. | `09_AI_Notes/06_Management_Controller.md`; `15_Reverse_Engineering/04_Management.md`; `17_System_Architecture/05_Component_Selection.md` |
| Management access provision | Unknown | Unknown | Investigation category | Minimal carrier requirements recommend preserving management access in the investigation plan, while buses and pins are not assigned. | Plan research and test access only after nets are known; do not create schematic nets from this placeholder. | `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `15_Reverse_Engineering/04_Management.md`; `09_AI_Notes/10_Design_Checklist.md` |
| PMBus controller / PMBus device | Unknown | Unknown | Unknown category | PMBus Controller Datasheet is missing; PMBus topology, addresses, commands, telemetry, and fault behavior are undocumented. | Do not treat a PMBus device as the management MCU or define firmware behavior from PMBus references alone. | `Wanted_Documents.md`; `15_Reverse_Engineering/04_Management.md`; `18_Component_Research/02_Power_Converters.md` |

# Unknown

- **Unknown:** Whether a carrier-side management MCU is required. Sources: `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `15_Reverse_Engineering/04_Management.md`.
- **Unknown:** Whether a carrier-side BMC is required or whether management belongs to a host, baseboard, module, external controller, or no carrier-visible controller. Sources: `15_Reverse_Engineering/04_Management.md`; `17_System_Architecture/02_System_Block_Diagram.md`; `18_Component_Research/04_EEPROM_FRU.md`.
- **Unknown:** Management MCU or BMC manufacturer, part number, package, power rail, peripherals, boot method, debug interface, programming interface, memory requirements, and firmware environment. Sources: `15_Reverse_Engineering/07_Component_ID.md`; `17_System_Architecture/05_Component_Selection.md`; `09_AI_Notes/06_Management_Controller.md`.
- **Unknown:** Firmware architecture, firmware update flow, firmware loading sequence, firmware storage, firmware-management hardware, and whether a management controller participates in firmware update or health checks. Sources: `13_Reference_Docs/Reference_Index.rtf`; `15_Reverse_Engineering/04_Management.md`; `15_Reverse_Engineering/08_Bringup.md`.
- **Unknown:** SMBus, I2C, PMBus, SPI, JTAG, UART, reset, interrupt, enable, GPIO, and sideband topology. Sources: `09_AI_Notes/06_Management_Controller.md`; `15_Reverse_Engineering/04_Management.md`; `18_Component_Research/04_EEPROM_FRU.md`.
- **Unknown:** Required GPIO list, directions, names, voltage levels, reset lines, enable lines, interrupts, fan-control pins, telemetry pins, connector pins, and ownership. Sources: `09_AI_Notes/06_Management_Controller.md`; `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `15_Reverse_Engineering/02_Power_Rails.md`.
- **Unknown:** PMBus controller identity, topology, addresses, commands, telemetry registers, fault registers, pullups, isolation, bus ownership, and firmware ownership. Sources: `Wanted_Documents.md`; `15_Reverse_Engineering/04_Management.md`; `18_Component_Research/02_Power_Converters.md`.
- **Unknown:** Required telemetry signals, telemetry bus, telemetry register set, polling ownership, alert behavior, fault behavior, voltage/current/temperature/fault monitoring hardware, and health-check dependency. Sources: `15_Reverse_Engineering/02_Power_Rails.md`; `18_Component_Research/06_Temperature_Sensors.md`; `17_System_Architecture/02_System_Block_Diagram.md`.
- **Unknown:** Reset release timing, reset signal names, enable signal names, Power Good signal names, fault behavior, shutdown behavior, retry behavior, and whether any management controller controls or observes them. Sources: `15_Reverse_Engineering/02_Power_Rails.md`; `15_Reverse_Engineering/08_Bringup.md`; `18_Component_Research/02_Power_Converters.md`.
- **Unknown:** Fan-control ownership, PWM requirement, tachometer requirement, fan fault signaling, fan-present detection, fail-safe behavior, fan-controller IC, and whether firmware controls cooling. Sources: `18_Component_Research/07_Fan_Control.md`; `15_Reverse_Engineering/04_Management.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`.
- **Unknown:** Which management behaviors are OAM-defined, AMD-specific to MI250X, baseboard-specific, host-system-specific, or implementation-specific. Sources: `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `15_Reverse_Engineering/10_Minimal_Carrier.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`.

# Design Implications

- Do not invent firmware architecture, firmware state machines, firmware update flow, polling loops, telemetry register maps, fan-control policy, power-sequencing policy, or reset sequencing from the current repository.
- Do not select a management MCU, BMC, PMBus controller, fan controller, sensor, EEPROM, SPI flash, or related support component until its requirement, role, part number, interface, power, and constraints are verified.
- Do not assign SMBus, I2C, PMBus, GPIO, reset, interrupt, enable, Power Good, fan PWM, tachometer, telemetry, EEPROM, FRU, firmware, or health-check nets from the current repository alone.
- Treat the Management MCU / BMC block in diagrams as a dependency placeholder, not a verified schematic requirement.
- Treat indexed firmware and health-check references as research leads only; they do not define carrier firmware wiring or MCU/BMC responsibility.
- Keep management research linked to power, EEPROM/FRU, sensors, fan control, connector, and bring-up notes because telemetry, sequencing, reset release, firmware loading, and validation cross subsystem boundaries.

# Future Research

| Priority | Research task | Required output | Sources |
|---|---|---|---|
| High | Determine whether a carrier-side management MCU or BMC is required. | Verified carrier-side, module-side, host/baseboard-side, external, or no-carrier-controller responsibility. | `15_Reverse_Engineering/04_Management.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `15_Reverse_Engineering/10_Minimal_Carrier.md` |
| High | Obtain verified management interface documentation. | Verified SMBus, I2C, PMBus, GPIO, reset, interrupt, enable, Power Good, telemetry, EEPROM/FRU, and fan-control pins, or verified absence of those interfaces. | `15_Reverse_Engineering/04_Management.md`; `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `18_Component_Research/01_OAM_Connector.md` |
| High | Obtain PMBus and VRM documentation. | Verified PMBus controller identity, topology, addresses, commands, telemetry registers, fault registers, pullups, isolation, bus ownership, and relation to power sequencing. | `Wanted_Documents.md`; `18_Component_Research/02_Power_Converters.md`; `15_Reverse_Engineering/02_Power_Rails.md` |
| High | Determine power-sequencing ownership. | Verified source for whether sequencing, enables, Power Good, reset release, shutdown, and fault response are controlled by hardware, module, baseboard, host, MCU/BMC, or another mechanism. | `15_Reverse_Engineering/02_Power_Rails.md`; `15_Reverse_Engineering/08_Bringup.md`; `18_Component_Research/02_Power_Converters.md` |
| High | Determine firmware-management requirements. | Verified firmware update path, required hardware, storage role, access interface, management-controller role, and health-check dependency, or verified statement that no carrier firmware architecture is required. | `13_Reference_Docs/Reference_Index.rtf`; `15_Reverse_Engineering/04_Management.md`; `18_Component_Research/04_EEPROM_FRU.md` |
| Medium | Determine telemetry and monitoring ownership. | Verified voltage, current, temperature, fan, fault, and health telemetry ownership and bus path. | `18_Component_Research/06_Temperature_Sensors.md`; `18_Component_Research/07_Fan_Control.md`; `17_System_Architecture/02_System_Block_Diagram.md` |
| Medium | Identify candidate controllers only after requirements are known. | Verified manufacturer, part number, package, power, peripherals, firmware constraints, and BOM status for any required MCU, BMC, PMBus device, or fan controller. | `15_Reverse_Engineering/07_Component_ID.md`; `17_System_Architecture/05_Component_Selection.md`; `18_Component_Research/10_BOM.md` |
| Medium | Add bring-up validation steps after management requirements are sourced. | Verified management bus checks, GPIO checks, telemetry checks, firmware checks, fan-control checks, and sequencing checks if required. | `AI_TASKS.md`; `15_Reverse_Engineering/08_Bringup.md`; `09_AI_Notes/10_Design_Checklist.md` |

# Sources

- `README.md` - States the evidence workflow and that undocumented behavior should be tracked rather than assumed.
- `AI_TASKS.md` - Lists management interface, power sequencing, telemetry, EEPROM requirements, fan control, and validation tasks as unresolved project areas.
- `Wanted_Documents.md` - Marks PMBus Controller Datasheet and VRM Datasheet as missing and tracks other missing integration evidence.
- `13_Reference_Docs/Reference_Index.rtf` - Indexes firmware tools, firmware update guides, health checks, system validation, MI250 acceptance, and GPU accelerator management interfaces.
- `13_Reference_Docs/Component_Index.rtf` - Identifies `MP2975` as a candidate digital multiphase VRM controller, relevant to PMBus/telemetry investigation but not a management MCU.
- `09_AI_Notes/04_Power_Architecture.md` - Summarizes PMBus/VRM evidence and MP2975 uncertainty.
- `09_AI_Notes/06_Management_Controller.md` - Summarizes management-controller, firmware, sideband, SMBus/I2C, PMBus, JTAG, SPI flash, UART, reset, interrupt, and enable gaps.
- `15_Reverse_Engineering/01_OAM_Pin_Mapping.md` - Records management buses, EEPROM/FRU, PMBus, telemetry, and OAM pin mapping as undocumented at connector level.
- `15_Reverse_Engineering/02_Power_Rails.md` - Records PMBus, telemetry, monitoring, enable, Power Good, fault, and reset-power relationship gaps.
- `15_Reverse_Engineering/04_Management.md` - Main management evidence document for MCU, BMC, SMBus, I2C, PMBus, EEPROM, FRU EEPROM, firmware, health monitoring, voltage monitoring, sensors, and fan control.
- `15_Reverse_Engineering/07_Component_ID.md` - Lists management controllers, PMBus devices, EEPROMs, sensors, fan controllers, and other component categories as undocumented.
- `15_Reverse_Engineering/08_Bringup.md` - Records management initialization, EEPROM access, firmware loading, health checks, reset sequence, power sequencing, and PCIe enumeration as undocumented.
- `15_Reverse_Engineering/09_Block_Diagram.md` - Shows Management / BMC / MCU / EEPROM as an unknown architecture block.
- `15_Reverse_Engineering/10_Minimal_Carrier.md` - Lists carrier-side management MCU, EEPROM/FRU, firmware flashing hardware, fan controller, and sensors as optional until proven required.
- `17_System_Architecture/02_System_Block_Diagram.md` - Shows Management MCU / BMC, EEPROM / FRU EEPROM, sensors, and fan controller as support blocks with requirements undocumented.
- `17_System_Architecture/03_Minimal_Carrier_Requirements.md` - Lists management access as an investigation provision and management MCU, EEPROM, sensors, fan controller, and firmware flashing hardware as unknown or optional until sourced.
- `17_System_Architecture/05_Component_Selection.md` - Contains an empty Management MCU candidate-parts section.
- `18_Component_Research/README.md` - Defines `05_Management_MCU.md` as management MCU or BMC-side hardware research and marks the carrier-side MCU/BMC requirement as unknown.
- `18_Component_Research/02_Power_Converters.md` - Records PMBus, telemetry, sequencing, enables, Power Good, GPIO-adjacent, and fault-handling requirements as unresolved.
- `18_Component_Research/04_EEPROM_FRU.md` - Records EEPROM/FRU, SMBus/I2C, firmware storage, and management access as unresolved.
- `18_Component_Research/06_Temperature_Sensors.md` - Records voltage/current/fault monitoring, telemetry, and sensor ownership as unresolved.
- `18_Component_Research/07_Fan_Control.md` - Records fan-control ownership, PWM, tachometer, fan fault, and firmware requirements as unresolved.
- `18_Component_Research/10_BOM.md` - Tracks Management MCU, BMC, PMBus device, EEPROM/FRU, firmware storage, sensors, and fan controller as unknown component categories.