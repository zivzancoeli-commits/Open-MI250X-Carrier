# Management

# Purpose

| Label | Statement | Sources |
|---|---|---|
| Verified | This document collects repository-supported management evidence for the AMD Instinct MI250X OAM carrier effort. | `README.md`; `AI_TASKS.md`; `15_Reverse_Engineering/README.md` |
| Verified | The repository tracks unknown hardware behavior instead of assigning unsourced schematic nets, part numbers, addresses, or firmware behavior. | `README.md`; `AI_TASKS.md`; `09_AI_Notes/10_Design_Checklist.md` |
| Verified | No readable repository source provides verified SMBus addresses, I2C addresses, PMBus addresses, bus speeds, bus topology, pullups, voltage levels, connector pins, telemetry registers, firmware-update wiring, health-monitoring procedure, BMC part number, MCU part number, EEPROM contents, FRU contents, temperature-sensor part number, voltage-monitor part number, reset wiring, enable wiring, or interrupt wiring. | `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `15_Reverse_Engineering/08_Bringup.md`; `18_Component_Research/05_Management_MCU.md` |

# Verified Management Evidence

| Topic | Verified repository fact | Design limitation | Sources |
|---|---|---|---|
| Target module | MI250 and MI250X are documented as OCP Accelerator Modules with two GCDs and 128 GB total memory, exposed to software as two devices with separate 64 GB VRAM blocks. | This establishes the target module class but does not define carrier management interfaces. | `13_Reference_Docs/ROCm/Overview.md`; `15_Reverse_Engineering/07_Component_ID.md`; `18_Component_Research/10_BOM.md` |
| Indexed firmware references | Firmware Tool v2.3, Firmware Tool v2.2, AMD FW Flash Guide, and Firmware Update Guide are listed in the reference index. | The index names research leads but does not provide firmware wiring, update protocol, storage role, or controller requirements. | `13_Reference_Docs/Reference_Index.rtf`; `09_AI_Notes/06_Management_Controller.md`; `18_Component_Research/04_EEPROM_FRU.md` |
| Indexed health and validation references | MI250 Acceptance, Health Checks, System Validation, AMD Lab Notes, and GPU Accelerator Management Interfaces are indexed. | The index does not provide health-check procedures or carrier hardware dependencies. | `13_Reference_Docs/Reference_Index.rtf`; `15_Reverse_Engineering/08_Bringup.md`; `18_Component_Research/06_Temperature_Sensors.md` |
| Missing PMBus source | PMBus Controller Datasheet is marked missing. | PMBus controller identity, topology, addresses, commands, telemetry registers, fault registers, pullups, isolation, and ownership remain unknown. | `Wanted_Documents.md`; `15_Reverse_Engineering/02_Power_Rails.md`; `18_Component_Research/02_Power_Converters.md` |
| Missing VRM source | VRM Datasheet is marked missing. | VRM controller behavior, power-stage pairing, telemetry, rail mapping, and sequencing behavior remain unknown. | `Wanted_Documents.md`; `15_Reverse_Engineering/02_Power_Rails.md`; `18_Component_Research/02_Power_Converters.md` |
| MP2975 candidate | MP2975 is listed as a Monolithic Power Systems digital multiphase VRM controller, believed present on MI250X and not visually confirmed. | MP2975 is not verified as a carrier component, BMC, MCU, PMBus device, or address source. | `13_Reference_Docs/Component_Index.rtf`; `15_Reverse_Engineering/07_Component_ID.md`; `18_Component_Research/02_Power_Converters.md` |
| MP2975 datasheet gap | No public MP2975 datasheet is available in the repository. | MP2975 pinout, PMBus behavior, telemetry registers, fault registers, sequencing features, and power-stage pairings cannot be inferred. | `13_Reference_Docs/Component_Index.rtf`; `15_Reverse_Engineering/02_Power_Rails.md`; `18_Component_Research/02_Power_Converters.md` |
| Software inspection context | `rocminfo` is used in readable ROCm material to inspect platform information, memory pools, and XNACK state. | `rocminfo` is software validation context after enumeration, not a hardware management bus, address map, or firmware-update path. | `13_Reference_Docs/ROCm/Overview.md`; `15_Reverse_Engineering/08_Bringup.md`; `15_Reverse_Engineering/10_Minimal_Carrier.md` |
| System diagram status | The architecture block diagram shows Management MCU / BMC, EEPROM / FRU EEPROM, Temperature / Voltage Sensors, and Fan Controller as support blocks with requirements undocumented. | Diagram blocks are dependency placeholders, not verified schematic blocks. | `17_System_Architecture/02_System_Block_Diagram.md`; `18_Component_Research/05_Management_MCU.md`; `18_Component_Research/10_BOM.md` |
| Minimal-carrier status | Management MCU, EEPROM or FRU EEPROM, temperature/voltage/current/fault sensors, fan controller, and firmware flashing hardware remain optional or unknown until requirements prove they are needed. | Do not select or place these parts until role, bus, pins, and constraints are verified. | `15_Reverse_Engineering/10_Minimal_Carrier.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `18_Component_Research/10_BOM.md` |

# SMBus

| Item | Status | Repository-supported information | Unknowns that must not be invented | Sources |
|---|---|---|---|---|
| SMBus presence | Unknown | SMBus is included in management research scope and connector-level management signals, but no readable source confirms a required SMBus implementation. | Required or optional status, connector pins, bus owner, topology, voltage level, pullups, muxing, isolation, hot-plug behavior, and devices. | `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `18_Component_Research/05_Management_MCU.md`; `18_Component_Research/04_EEPROM_FRU.md` |
| SMBus addresses | Unknown | No readable source provides SMBus addresses. | Device addresses, address straps, reserved addresses, scan procedure, and address ownership. | `18_Component_Research/04_EEPROM_FRU.md`; `18_Component_Research/05_Management_MCU.md`; `15_Reverse_Engineering/01_OAM_Pin_Mapping.md` |
| SMBus protocol behavior | Unknown | The repository names SMBus only as an unresolved management topic. | Transaction types, command set, alert behavior, timeout behavior, firmware ownership, and validation method. | `09_AI_Notes/06_Management_Controller.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `18_Component_Research/05_Management_MCU.md` |

# I2C

| Item | Status | Repository-supported information | Unknowns that must not be invented | Sources |
|---|---|---|---|---|
| I2C presence | Unknown | I2C is included in management and EEPROM/sensor research, but no readable source proves a required I2C bus. | Required or optional status, bus topology, bus owner, voltage level, pullups, muxing, isolation, connector pins, and device list. | `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `18_Component_Research/04_EEPROM_FRU.md`; `18_Component_Research/06_Temperature_Sensors.md` |
| I2C addresses | Unknown | No readable source provides I2C EEPROM, sensor, management, or controller addresses. | Device addresses, strap pins, conflict handling, bus scan procedure, and address map. | `18_Component_Research/04_EEPROM_FRU.md`; `18_Component_Research/06_Temperature_Sensors.md`; `18_Component_Research/05_Management_MCU.md` |
| I2C devices | Unknown | I2C EEPROMs and I2C sensors are tracked only as unknown categories. | EEPROM requirement, sensor requirement, part number, package, voltage, bus speed, write-protect behavior, and validation method. | `15_Reverse_Engineering/07_Component_ID.md`; `18_Component_Research/04_EEPROM_FRU.md`; `18_Component_Research/06_Temperature_Sensors.md` |

# PMBus

| Item | Status | Repository-supported information | Unknowns that must not be invented | Sources |
|---|---|---|---|---|
| PMBus source status | Verified gap | PMBus Controller Datasheet is marked missing. | Controller identity, topology, addresses, commands, telemetry registers, fault registers, pullups, isolation, ownership, and firmware behavior. | `Wanted_Documents.md`; `15_Reverse_Engineering/02_Power_Rails.md`; `18_Component_Research/02_Power_Converters.md` |
| PMBus relationship to MP2975 | Candidate-only | MP2975 is listed as a candidate digital multiphase VRM controller and is not visually confirmed. | Whether MP2975 is present, whether it uses PMBus in this design, address, commands, rails controlled, telemetry, faults, sequencing, and power-stage pairings. | `13_Reference_Docs/Component_Index.rtf`; `15_Reverse_Engineering/07_Component_ID.md`; `18_Component_Research/02_Power_Converters.md` |
| PMBus telemetry | Unknown | PMBus is a power-management research area, and telemetry/monitoring are unresolved. | Voltage, current, temperature, fault, status, limit, and protection registers; polling owner; alert behavior; validation procedure. | `15_Reverse_Engineering/02_Power_Rails.md`; `18_Component_Research/02_Power_Converters.md`; `18_Component_Research/06_Temperature_Sensors.md` |
| PMBus schematic use | Not supported yet | Current evidence does not support assigning PMBus nets, devices, addresses, commands, or firmware behavior. | Net names, pullups, bus owner, isolation, muxes, connectors, and controller firmware. | `18_Component_Research/05_Management_MCU.md`; `15_Reverse_Engineering/02_Power_Rails.md`; `09_AI_Notes/10_Design_Checklist.md` |

# BMC

| Item | Status | Repository-supported information | Unknowns that must not be invented | Sources |
|---|---|---|---|---|
| BMC requirement | Unknown | BMC interaction is tracked as undocumented, and system diagrams show Management MCU / BMC as a support block with requirement undocumented. | Whether a BMC is carrier-side, baseboard-side, host-side, external, module-side, or not required. | `17_System_Architecture/02_System_Block_Diagram.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `18_Component_Research/05_Management_MCU.md` |
| BMC part number | Unknown | No BMC manufacturer or part number is verified in readable local files. | Manufacturer, part number, package, power rails, memory, boot, debug, peripherals, and firmware environment. | `15_Reverse_Engineering/07_Component_ID.md`; `18_Component_Research/05_Management_MCU.md`; `18_Component_Research/10_BOM.md` |
| BMC interfaces | Unknown | Management buses, GPIO, resets, enables, interrupts, firmware wiring, fan control, and telemetry are unresolved. | SMBus, I2C, PMBus, SPI, JTAG, UART, GPIO, interrupt, reset, enable, Power Good, PWM, tachometer, fault, and alert wiring. | `09_AI_Notes/06_Management_Controller.md`; `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `18_Component_Research/05_Management_MCU.md` |

# MCU

| Item | Status | Repository-supported information | Unknowns that must not be invented | Sources |
|---|---|---|---|---|
| Management MCU requirement | Unknown | Minimal carrier requirements state that a carrier-side management MCU is not proven required. | Whether management belongs to a carrier MCU, BMC, host/baseboard, module, external controller, or no carrier-visible controller. | `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `15_Reverse_Engineering/10_Minimal_Carrier.md`; `18_Component_Research/05_Management_MCU.md` |
| MCU candidate parts | Unknown | The component-selection document has a Management MCU candidate-parts section, but repository component research records no verified MCU part. | Manufacturer, family, part number, package, supply voltage, peripherals, memory, programming, debug, boot, and lifecycle. | `17_System_Architecture/05_Component_Selection.md`; `15_Reverse_Engineering/07_Component_ID.md`; `18_Component_Research/05_Management_MCU.md` |
| MCU firmware role | Unknown | Firmware tools and health references are indexed, but no readable source defines a carrier MCU firmware architecture. | Firmware update flow, firmware state machine, polling loops, telemetry ownership, health-check participation, reset control, fan-control policy, and fault handling. | `13_Reference_Docs/Reference_Index.rtf`; `09_AI_Notes/06_Management_Controller.md`; `15_Reverse_Engineering/08_Bringup.md` |
| MCU GPIO and sidebands | Unknown | Required GPIO list, reset lines, interrupts, enable lines, Power Good lines, fan-control pins, telemetry pins, and connector pins are undocumented. | Signal names, directions, voltage levels, pullups, polarity, timing, ownership, and validation procedure. | `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `15_Reverse_Engineering/02_Power_Rails.md`; `18_Component_Research/05_Management_MCU.md` |

# EEPROM

| Item | Status | Repository-supported information | Unknowns that must not be invented | Sources |
|---|---|---|---|---|
| EEPROM requirement | Unknown | EEPROM is optional until a readable source proves that the carrier must provide one. | Carrier-side, module-side, baseboard-side, host-side, BMC-side, MCU-side, or no-carrier EEPROM responsibility. | `15_Reverse_Engineering/10_Minimal_Carrier.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `18_Component_Research/04_EEPROM_FRU.md` |
| EEPROM part number | Unknown | EEPROMs are listed as undocumented component categories. | Manufacturer, part number, density, package, voltage, interface, temperature rating, endurance, address pins, and footprint. | `15_Reverse_Engineering/07_Component_ID.md`; `18_Component_Research/04_EEPROM_FRU.md`; `18_Component_Research/10_BOM.md` |
| EEPROM bus and address | Unknown | No readable source provides EEPROM bus topology or address. | SMBus/I2C/SPI choice, address, write-protect, pullups, bus ownership, connector pins, isolation, and access sequencing. | `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `18_Component_Research/04_EEPROM_FRU.md`; `18_Component_Research/05_Management_MCU.md` |
| EEPROM contents | Unknown | No readable source defines EEPROM contents, board metadata, configuration data, provisioning, or update behavior. | Stored fields, format, checksum, ownership, write policy, factory programming, field update, and validation use. | `18_Component_Research/04_EEPROM_FRU.md`; `15_Reverse_Engineering/08_Bringup.md`; `13_Reference_Docs/Reference_Index.rtf` |

# FRU EEPROM

| Item | Status | Repository-supported information | Unknowns that must not be invented | Sources |
|---|---|---|---|---|
| FRU EEPROM requirement | Unknown | FRU EEPROM is listed as an unresolved management and BOM category, but no readable source proves a carrier FRU requirement. | Whether FRU storage is required, where it resides, who owns it, and whether it is accessible to host, baseboard, module, BMC, or MCU. | `18_Component_Research/04_EEPROM_FRU.md`; `18_Component_Research/10_BOM.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| FRU format and contents | Unknown | No readable source defines FRU contents or board-identification format. | FRU fields, board metadata, serial number, manufacturer fields, checksums, update flow, write-protect, and provisioning. | `18_Component_Research/04_EEPROM_FRU.md`; `15_Reverse_Engineering/08_Bringup.md`; `13_Reference_Docs/Reference_Index.rtf` |
| FRU bus and address | Unknown | No readable source provides FRU bus topology, address, pins, or voltage level. | SMBus/I2C/SPI choice, device address, pullups, bus owner, muxing, isolation, and connector pins. | `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `18_Component_Research/04_EEPROM_FRU.md`; `18_Component_Research/05_Management_MCU.md` |

# Temperature Sensors

| Item | Status | Repository-supported information | Unknowns that must not be invented | Sources |
|---|---|---|---|---|
| Temperature-sensor requirement | Unknown | Temperature sensors are named as management and component-research topics, but carrier-visible temperature-sensor requirements are undocumented. | Whether sensors are module-side, carrier-side, baseboard-side, host-side, external, MCU/BMC-side, or not required. | `18_Component_Research/06_Temperature_Sensors.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `17_System_Architecture/02_System_Block_Diagram.md` |
| Temperature-sensor part number | Unknown | Temperature sensors are listed as undocumented component categories, and no sensor part number is verified. | Manufacturer, part number, package, sensor technology, interface, address, accuracy, range, resolution, supply rail, and footprint. | `15_Reverse_Engineering/07_Component_ID.md`; `18_Component_Research/06_Temperature_Sensors.md`; `18_Component_Research/10_BOM.md` |
| Junction temperature | Unknown | No readable source defines a junction-temperature access path, telemetry source, register, limit, or validation use. | Access method, owner, register, polling rate, alert behavior, limits, and health-check dependency. | `18_Component_Research/06_Temperature_Sensors.md`; `15_Reverse_Engineering/08_Bringup.md`; `13_Reference_Docs/Reference_Index.rtf` |
| Board temperature | Unknown | No readable source defines board-temperature sensing, sensor placement, or board-temperature limits. | Sensor count, location, thermal coupling, mechanical attachment, limits, test method, and ownership. | `18_Component_Research/06_Temperature_Sensors.md`; `09_AI_Notes/07_Cooling.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| Thermal feedback | Unknown | Fan control is named as a management topic, but thermal feedback and cooling-control ownership are undocumented. | Whether temperature sensors feed fan control, firmware, BMC, MCU, external cooling, host software, or health checks. | `18_Component_Research/07_Fan_Control.md`; `18_Component_Research/06_Temperature_Sensors.md`; `18_Component_Research/05_Management_MCU.md` |

# Voltage Monitoring

| Item | Status | Repository-supported information | Unknowns that must not be invented | Sources |
|---|---|---|---|---|
| Voltage-monitoring requirement | Unknown | Voltage monitoring is tracked as unresolved in management, power, sensor, and minimal-carrier documents. | Which rails are monitored, required accuracy, thresholds, owner, access bus, telemetry path, and health-check role. | `15_Reverse_Engineering/02_Power_Rails.md`; `18_Component_Research/06_Temperature_Sensors.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| Voltage-monitoring components | Unknown | Voltage/current/fault sensors are unknown component categories, and no voltage monitor part number is verified. | Manufacturer, part number, package, input range, interface, address, thresholds, alerts, power rail, and footprint. | `18_Component_Research/06_Temperature_Sensors.md`; `18_Component_Research/10_BOM.md`; `15_Reverse_Engineering/07_Component_ID.md` |
| PMBus/VRM telemetry | Unknown | Telemetry and voltage monitoring may overlap with PMBus/VRM work, but PMBus and VRM details are undocumented. | PMBus addresses, commands, telemetry registers, fault registers, polling owner, alert behavior, and voltage limits. | `15_Reverse_Engineering/02_Power_Rails.md`; `18_Component_Research/02_Power_Converters.md`; `18_Component_Research/05_Management_MCU.md` |
| Power Good and enable relationship | Unknown | Power Good signal names, thresholds, timing, reset-gating relationships, enable names, locations, polarity, and timing are undocumented. | Signal names, controller ownership, voltage levels, timing, fault behavior, and reset release dependency. | `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `15_Reverse_Engineering/02_Power_Rails.md`; `18_Component_Research/02_Power_Converters.md` |

# Firmware Update

| Item | Status | Repository-supported information | Unknowns that must not be invented | Sources |
|---|---|---|---|---|
| Firmware references | Indexed only | Firmware Tool v2.3, Firmware Tool v2.2, AMD FW Flash Guide, and Firmware Update Guide are indexed. | Actual guide contents, procedure, required hardware, wiring, storage, protocol, controller role, and validation steps. | `13_Reference_Docs/Reference_Index.rtf`; `09_AI_Notes/06_Management_Controller.md`; `18_Component_Research/04_EEPROM_FRU.md` |
| Firmware-update hardware | Unknown | Firmware flashing hardware is optional until firmware-update path and hardware dependencies are verified. | Whether carrier hardware is required, whether firmware storage exists, whether EEPROM/SPI flash participates, and whether MCU/BMC/host/baseboard owns update. | `15_Reverse_Engineering/10_Minimal_Carrier.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `18_Component_Research/04_EEPROM_FRU.md` |
| Firmware storage | Unknown | SPI flash / firmware storage device is tracked as an unknown BOM category, and EEPROM/FRU storage roles are unresolved. | Storage type, contents, address, protocol, update process, write-protect, power sequencing, and ownership. | `18_Component_Research/04_EEPROM_FRU.md`; `18_Component_Research/10_BOM.md`; `09_AI_Notes/06_Management_Controller.md` |
| Firmware flow | Unknown | No readable source defines firmware loading sequence or hardware dependencies. | State machine, order, security, recovery, update trigger, interface, reset dependency, health-check relationship, and pass/fail criteria. | `15_Reverse_Engineering/08_Bringup.md`; `09_AI_Notes/06_Management_Controller.md`; `13_Reference_Docs/Reference_Index.rtf` |

# Health Monitoring

| Item | Status | Repository-supported information | Unknowns that must not be invented | Sources |
|---|---|---|---|---|
| Health references | Indexed only | MI250 Acceptance, Health Checks, System Validation, AMD Lab Notes, and GPU Accelerator Management Interfaces are indexed. | Actual procedure, hardware dependencies, telemetry inputs, pass/fail criteria, logging, and required management buses. | `13_Reference_Docs/Reference_Index.rtf`; `15_Reverse_Engineering/08_Bringup.md`; `18_Component_Research/06_Temperature_Sensors.md` |
| Software inspection | Verified software context | `rocminfo` and XNACK checks are documented as software inspection aids after hardware can enumerate. | These tools do not define SMBus, I2C, PMBus, BMC, MCU, EEPROM, FRU, sensor, or firmware-update wiring. | `13_Reference_Docs/ROCm/Overview.md`; `15_Reverse_Engineering/08_Bringup.md`; `15_Reverse_Engineering/10_Minimal_Carrier.md` |
| Telemetry inputs | Unknown | Required voltage, current, temperature, fan, fault, and health telemetry ownership and bus path are undocumented. | Sensors, registers, polling owner, alert/fault behavior, thresholds, health-check dependencies, and validation method. | `15_Reverse_Engineering/02_Power_Rails.md`; `18_Component_Research/06_Temperature_Sensors.md`; `18_Component_Research/07_Fan_Control.md` |
| Health-monitoring hardware | Unknown | No readable source identifies required health-monitoring hardware. | BMC/MCU requirement, PMBus device, sensor set, fan feedback, firmware storage, interrupt lines, fault lines, and logging path. | `18_Component_Research/05_Management_MCU.md`; `17_System_Architecture/02_System_Block_Diagram.md`; `18_Component_Research/10_BOM.md` |

# Design Implications

| Rule | Status | Engineering implication | Sources |
|---|---|---|---|
| Do not assign management nets. | Inferred | Do not assign SMBus, I2C, PMBus, EEPROM, FRU, reset, interrupt, enable, Power Good, GPIO, telemetry, fan, sensor, firmware, or health-check nets from the current repository alone. | `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `09_AI_Notes/10_Design_Checklist.md`; `18_Component_Research/05_Management_MCU.md` |
| Do not invent addresses or protocols. | Inferred | Do not invent SMBus/I2C/PMBus addresses, bus speeds, PMBus commands, telemetry registers, EEPROM contents, FRU contents, firmware protocol, or health-check procedure. | `18_Component_Research/04_EEPROM_FRU.md`; `15_Reverse_Engineering/02_Power_Rails.md`; `18_Component_Research/05_Management_MCU.md` |
| Treat controller blocks as placeholders. | Inferred | Management MCU / BMC blocks in diagrams are unresolved dependencies, not verified schematic requirements or BOM lines. | `17_System_Architecture/02_System_Block_Diagram.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `18_Component_Research/10_BOM.md` |
| Keep power and management linked. | Inferred | PMBus, telemetry, voltage monitoring, enable, Power Good, reset, sequencing, and fault behavior cross power and management documents. | `15_Reverse_Engineering/02_Power_Rails.md`; `18_Component_Research/02_Power_Converters.md`; `18_Component_Research/05_Management_MCU.md` |
| Keep thermal and management linked. | Inferred | Temperature sensors, voltage/current/fault sensors, fan control, thermal feedback, health checks, and validation cross sensor, cooling, fan, and management documents. | `18_Component_Research/06_Temperature_Sensors.md`; `18_Component_Research/07_Fan_Control.md`; `13_Reference_Docs/Reference_Index.rtf` |

# Future Research

| Priority | Research task | Required output | Sources |
|---|---|---|---|
| High | Recover or extract management-interface documentation. | Verified SMBus, I2C, PMBus, GPIO, reset, interrupt, enable, Power Good, telemetry, EEPROM, FRU, firmware, sensor, and health-monitoring pins or verified absence of each. | `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `18_Component_Research/05_Management_MCU.md`; `09_AI_Notes/10_Design_Checklist.md` |
| High | Obtain PMBus and VRM documentation. | Verified PMBus controller identity, topology, addresses, commands, telemetry registers, fault registers, pullups, isolation, ownership, and VRM relationship. | `Wanted_Documents.md`; `13_Reference_Docs/Component_Index.rtf`; `15_Reverse_Engineering/02_Power_Rails.md` |
| High | Determine management ownership. | Verified carrier-side, module-side, host-side, baseboard-side, external-controller, or no-carrier-controller ownership for BMC/MCU, buses, telemetry, firmware update, and health monitoring. | `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `15_Reverse_Engineering/10_Minimal_Carrier.md`; `18_Component_Research/05_Management_MCU.md` |
| High | Determine EEPROM and FRU requirements. | Verified requirement, owner, part type, bus, address, contents, write-protect behavior, update process, and validation role, or verified absence. | `18_Component_Research/04_EEPROM_FRU.md`; `15_Reverse_Engineering/08_Bringup.md`; `13_Reference_Docs/Reference_Index.rtf` |
| High | Determine monitoring requirements. | Verified temperature, voltage, current, fan, fault, and health telemetry sources, sensors, limits, bus path, owner, and pass/fail criteria. | `18_Component_Research/06_Temperature_Sensors.md`; `18_Component_Research/07_Fan_Control.md`; `15_Reverse_Engineering/02_Power_Rails.md` |
| Medium | Confirm or reject MP2975 on real MI250X hardware. | Visual or document-backed confirmation of presence, location, role, rails controlled, PMBus behavior, and related power stages. | `13_Reference_Docs/Component_Index.rtf`; `15_Reverse_Engineering/07_Component_ID.md`; `18_Component_Research/02_Power_Converters.md` |
| Medium | Convert indexed firmware and health references into readable notes. | Extracted procedures, hardware dependencies, validation steps, and evidence-backed management requirements. | `13_Reference_Docs/Reference_Index.rtf`; `15_Reverse_Engineering/08_Bringup.md`; `09_AI_Notes/06_Management_Controller.md` |

# Sources

| Source | Use in this reference |
|---|---|
| `README.md` | States the evidence workflow and that undocumented behavior should be tracked rather than assumed. |
| `AI_TASKS.md` | Lists management interface, EEPROM requirements, telemetry, fan control, power sequencing, validation, and bring-up tasks as unresolved project areas. |
| `Wanted_Documents.md` | Marks PMBus Controller Datasheet, VRM Datasheet, Connector Specification, Baseboard Specification, and OAM Thermal Guidelines as missing. |
| `13_Reference_Docs/Reference_Index.rtf` | Indexes firmware tools, firmware update guides, health checks, system validation, MI250 acceptance, AMD Lab Notes, and GPU accelerator management interfaces. |
| `13_Reference_Docs/Component_Index.rtf` | Identifies MP2975 as a Monolithic Power Systems digital multiphase VRM controller candidate, believed present but not visually confirmed, with no public datasheet. |
| `13_Reference_Docs/ROCm/Overview.md` | Provides MI250/MI250X OAM context and software inspection context such as `rocminfo` and XNACK checks. |
| `09_AI_Notes/06_Management_Controller.md` | Summarizes firmware, management, health-check, validation, SMBus/I2C, PMBus, JTAG, SPI flash, UART, reset, interrupt, and enable gaps. |
| `09_AI_Notes/10_Design_Checklist.md` | States schematic capture and PCB layout should wait for connector, PCIe/REFCLK, power, management, mechanical, baseboard, and high-speed constraints. |
| `15_Reverse_Engineering/01_OAM_Pin_Mapping.md` | Records management signals, SMBus, I2C, PMBus, EEPROM/FRU, GPIO, interrupts, firmware hardware, sensors, fan control, and OAM connector pins as undocumented. |
| `15_Reverse_Engineering/02_Power_Rails.md` | Records PMBus, telemetry, voltage monitoring, enable, Power Good, reset, sequencing, protection, and startup-order gaps. |
| `15_Reverse_Engineering/07_Component_ID.md` | Lists MP2975 as a low-confidence candidate and lists EEPROMs, FRU EEPROMs, temperature sensors, PMBus devices, fan controllers, and management controllers as undocumented categories. |
| `15_Reverse_Engineering/08_Bringup.md` | Records management initialization, EEPROM access, firmware loading, health checks, voltage validation, reset sequence, and hardware bring-up dependencies as unresolved. |
| `15_Reverse_Engineering/10_Minimal_Carrier.md` | Lists carrier-side management MCU, EEPROM/FRU, fan controller, sensors, and firmware flashing hardware as optional until proven required. |
| `17_System_Architecture/02_System_Block_Diagram.md` | Shows Management MCU / BMC, EEPROM / FRU EEPROM, Temperature / Voltage Sensors, and Fan Controller blocks with requirements undocumented. |
| `17_System_Architecture/03_Minimal_Carrier_Requirements.md` | Lists management access as an investigation provision and management MCU, EEPROM/FRU, sensors, fan controller, and firmware flashing hardware as unknown or optional until sourced. |
| `17_System_Architecture/05_Component_Selection.md` | Contains empty candidate sections for Management MCU, EEPROM, Temperature Sensors, and related component categories. |
| `18_Component_Research/02_Power_Converters.md` | Records PMBus, telemetry, sequencing, enables, Power Good, voltage/current monitoring, and fault behavior as unresolved. |
| `18_Component_Research/04_EEPROM_FRU.md` | Records EEPROM, FRU EEPROM, I2C EEPROM, configuration storage, board identification, SMBus/I2C addresses, contents, and ownership as unresolved. |
| `18_Component_Research/05_Management_MCU.md` | Main related component research for BMC, management MCU, PMBus, I2C, SMBus, GPIO, telemetry, firmware, fan control, and power sequencing. |
| `18_Component_Research/06_Temperature_Sensors.md` | Records temperature sensors, voltage/current/fault sensors, junction temperature, board temperature, PMBus telemetry, and monitoring ownership as unresolved. |
| `18_Component_Research/07_Fan_Control.md` | Records fan-control ownership, PWM, tachometer, fan fault, fan-present, firmware ownership, and cooling-control requirements as unresolved. |
| `18_Component_Research/10_BOM.md` | Tracks Management MCU, BMC, PMBus device, EEPROM/FRU, firmware storage, temperature sensors, voltage/current/fault sensors, fan controller, and related support hardware as unknown categories. |