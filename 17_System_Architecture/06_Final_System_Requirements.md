# Open-MI250X Carrier System Requirements

## Purpose

This document is the project-level engineering specification for the Open-MI250X Carrier. It consolidates repository-supported requirements for schematic capture and preserves unresolved information as `Unknown` instead of converting it into schematic nets, rail values, part numbers, timing values, connector pins, dimensions, or thermal limits.

| Item | Requirement | Evidence status | Sources |
|---|---|---|---|
| Specification authority | Treat this document as the top-level requirements and release-gate document for schematic capture. | Verified project need from current work request and existing architecture flow. | `AI_PROJECT_CONTEXT.md`; `AI_TASKS.md`; `README.md`; `15_Reverse_Engineering/README.md` |
| Evidence rule | Every hardware requirement must be classified as `Verified`, `Inferred`, or `Unknown`; missing information must remain explicit. | Verified | `AI_PROJECT_CONTEXT.md`; `AI_TASKS.md`; `README.md`; `AI_DESIGN_RULES.md` |
| Schematic safety rule | This specification does not authorize guessed OAM pins, power rails, currents, clocks, bus addresses, routing values, mechanical dimensions, or thermal limits. | Verified | `AI_DESIGN_RULES.md`; `09_AI_Notes/10_Design_Checklist.md`; `15_Reverse_Engineering/08_Bringup.md` |
| Schematic capture status | A safe final schematic is blocked until connector, power, clock, PCIe, management, thermal, mechanical, and component evidence is verified. | Verified blocker | `15_Reverse_Engineering/README.md`; `15_Reverse_Engineering/10_Minimal_Carrier.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |

## Evidence Definitions

| Label | Meaning in this specification |
|---|---|
| Verified | Directly supported by readable repository documents. |
| Inferred | Required by engineering dependency or project scope, but implementation details are not directly documented. |
| Unknown | Not documented well enough for schematic, layout, BOM, firmware, or validation use. |
| Candidate | Named research lead only; not a requirement unless promoted by verified evidence. |

## System Context

| Topic | Verified | Inferred | Unknown | Sources |
|---|---|---|---|---|
| Project goal | The project goal is an open hardware carrier board for AMD Instinct MI250X OAM accelerator modules, documented with public evidence. | The first useful carrier should focus on one MI250X before scale-out features. | Exact supported MI250X module revision is not documented. | `AI_PROJECT_CONTEXT.md`; `README.md`; `15_Reverse_Engineering/10_Minimal_Carrier.md` |
| Target accelerator | MI250 and MI250X are documented as OCP Accelerator Modules; MI250/MI250X are described as two-GCD modules with 128 GB total memory and two software-visible devices. | The carrier must mechanically and electrically support the MI250X OAM module class. | The repository does not contain a local MI250X OAM hardware datasheet or full connector specification. | `13_Reference_Docs/ROCm/Overview.md`; `15_Reverse_Engineering/07_Component_ID.md`; `18_Component_Research/10_BOM.md` |
| Host platform planning | The system BOM planning target includes Supermicro X11DPH-T, dual Intel Xeon Gold 6258R, Intel Optane Persistent Memory, AMD MI250X OAM, and a custom OAM carrier. | Host planning should guide test-environment expectations, not connector pinout or carrier routing. | Exact host-to-carrier electrical path, riser/cable/baseboard arrangement, BIOS configuration, and slot assignment are not documented. | `20_System_BOM/README.md`; `20_System_BOM/Host_Platform.md`; `15_Reverse_Engineering/05_PCIe.md` |
| BOM status | The system BOM is revision 0.1, planning status, with no hardware purchased yet. | BOM entries should not become carrier schematic requirements unless tied to verified MI250X/OAM evidence. | Final purchased components, carrier BOM, and procurement status are not documented. | `20_System_BOM/README.md`; `18_Component_Research/10_BOM.md` |
| Schematic planning files | The `21_Schematic_Planning` files are empty RTF shells in the current repository state. | They provide no additional schematic authority yet. | Detailed schematic page requirements are still to be generated after requirement gates close. | `21_Schematic_Planning/README.md`; `21_Schematic_Planning/01_Power_System.md`; `21_Schematic_Planning/05_OAM_Interface.md` |

## Functional Requirements

### Verified

| ID | Requirement | Sources |
|---|---|---|
| FR-V-001 | The carrier project shall target AMD Instinct MI250X OAM accelerator modules. | `AI_PROJECT_CONTEXT.md`; `README.md`; `17_System_Architecture/01_System_Goals.md`; `15_Reverse_Engineering/10_Minimal_Carrier.md` |
| FR-V-002 | The project shall use public evidence, open documentation, and explicitly tracked unknowns rather than assumptions. | `AI_PROJECT_CONTEXT.md`; `README.md`; `AI_TASKS.md` |
| FR-V-003 | The first schematic scope shall support one MI250X module before multi-module scale-out is treated as a design driver. | `15_Reverse_Engineering/10_Minimal_Carrier.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `17_System_Architecture/04_Future_Expansion.md` |
| FR-V-004 | The completed platform vision includes low cost, modularity, serviceability, commodity components where practical, KiCad documentation, and open-source release. | `AI_PROJECT_CONTEXT.md`; `AI_TASKS.md`; `17_System_Architecture/01_System_Goals.md` |
| FR-V-005 | Software validation context includes ROCm inspection after hardware enumeration; `rocminfo` and XNACK checks are documented as software-context tools. | `13_Reference_Docs/ROCm/Overview.md`; `15_Reverse_Engineering/08_Bringup.md` |

### Inferred

| ID | Requirement | Basis | Sources |
|---|---|---|---|
| FR-I-001 | The minimal carrier shall provide only the functions needed to mate to, power, cool, communicate with, and mechanically support one MI250X OAM module. | Hardware cannot operate without these functions, and the minimal-carrier notebook defines these as required categories. | `15_Reverse_Engineering/10_Minimal_Carrier.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| FR-I-002 | Optional blocks shall be omitted from the smallest carrier unless verified evidence proves they are required. | The repository classifies switches, retimers, redrivers, MCU/BMC, EEPROM/FRU, sensors, fan controller, firmware flashing hardware, debug LEDs, USB debug, and generic debug headers as optional or unknown. | `15_Reverse_Engineering/10_Minimal_Carrier.md`; `15_Reverse_Engineering/07_Component_ID.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| FR-I-003 | Bring-up shall be gated in dependency order: evidence, power, clocks, management if required, reset, PCIe enumeration, ROCm, health checks, validation. | The bring-up notebook defines these dependencies and stop conditions. | `15_Reverse_Engineering/08_Bringup.md` |

### Unknown

| ID | Unknown requirement | Why it blocks schematic capture | Sources |
|---|---|---|---|
| FR-U-001 | Exact MI250X OAM hardware revision and supported module variants. | Schematic and mechanical constraints may depend on exact module revision. | `15_Reverse_Engineering/07_Component_ID.md`; `15_Reverse_Engineering/06_Mechanical.md` |
| FR-U-002 | Exact host electrical topology for one module. | Direct host link, cable/riser, switch, retimer, baseboard path, and slot mapping affect schematic structure. | `15_Reverse_Engineering/05_PCIe.md`; `17_System_Architecture/02_System_Block_Diagram.md` |
| FR-U-003 | Complete pass/fail requirements for prototype operation. | The repository has gated bring-up procedures but lacks rail limits, timing limits, thermal limits, and health criteria. | `15_Reverse_Engineering/08_Bringup.md`; `13_Reference_Docs/Reference_Index.rtf` |

## Mechanical Requirements

### Verified

| ID | Requirement | Sources |
|---|---|---|
| MR-V-001 | The OAM specification is tracked as a relevant source for mechanical drawings, connector specification, and power specification. | `02_AMD_Docs/GitHub_Links.rtf`; `02_AMD_Docs/README.md`; `15_Reverse_Engineering/06_Mechanical.md` |
| MR-V-002 | Mechanical Specification, Baseboard Specification, and Connector Specification are marked missing. | `Wanted_Documents.md`; `15_Reverse_Engineering/06_Mechanical.md`; `15_Reverse_Engineering/01_OAM_Pin_Mapping.md` |
| MR-V-003 | Front, back, and connector photos are marked found in tracking, but no readable local image files are present; heatsink and baseboard photos are not marked found. | `Wanted_Documents.md`; `README.md`; `09_AI_Notes/09_Unknowns.md`; `15_Reverse_Engineering/06_Mechanical.md` |
| MR-V-004 | Molex Mirror Mezz is only a candidate connector reference; it is not confirmed as the MI250X OAM connector. | `13_Reference_Docs/Reference_Index.rtf`; `15_Reverse_Engineering/07_Component_ID.md`; `18_Component_Research/01_OAM_Connector.md` |

### Inferred

| ID | Requirement | Basis | Sources |
|---|---|---|---|
| MR-I-001 | The carrier shall mechanically support the MI250X OAM module, mating connector, PCB, retention hardware, and cooling hardware after verified dimensions are available. | A minimal carrier must physically support the module and cooling assembly. | `15_Reverse_Engineering/06_Mechanical.md`; `15_Reverse_Engineering/10_Minimal_Carrier.md` |
| MR-I-002 | Connector footprint, board outline, mounting, 3D models, keepouts, and assembly drawings shall wait for verified connector and mechanical data. | The mechanical notebook and design checklist identify these as layout blockers. | `15_Reverse_Engineering/06_Mechanical.md`; `09_AI_Notes/10_Design_Checklist.md` |
| MR-I-003 | Thermal and mechanical work shall be resolved together. | Cooling interface, mounting force, keepouts, sensor placement, and retention are linked. | `15_Reverse_Engineering/06_Mechanical.md`; `18_Component_Research/07_Fan_Control.md` |

### Unknown

| ID | Unknown requirement | Why it blocks schematic/layout | Sources |
|---|---|---|---|
| MR-U-001 | Module length, width, installed height, component-side and backside height limits. | Board outline, enclosure fit, keepouts, and cooling envelope cannot be defined. | `15_Reverse_Engineering/06_Mechanical.md`; `09_AI_Notes/08_Mechanical.md` |
| MR-U-002 | Connector manufacturer, family, part number, footprint, pin-1 datum, center coordinates, mating height, stack-up, body height, and placement tolerance. | Connector symbol, footprint, placement, and pin map cannot be created. | `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `18_Component_Research/01_OAM_Connector.md` |
| MR-U-003 | Mounting hole count, hole diameter, coordinates, fasteners, standoff height, retention hardware, and mounting force. | The module and cooling hardware cannot be safely retained. | `15_Reverse_Engineering/06_Mechanical.md`; `15_Reverse_Engineering/10_Minimal_Carrier.md` |
| MR-U-004 | Module PCB thickness, carrier PCB thickness, carrier stack-up, board-to-board spacing, and tolerances. | Connector selection, fabrication stack-up, and mechanical fit are blocked. | `15_Reverse_Engineering/06_Mechanical.md`; `18_Component_Research/10_BOM.md` |
| MR-U-005 | Heatsink/cold-plate keepouts, weight, service clearances, chassis constraints, and cable routing. | Mechanical integration and safe thermal operation cannot be completed. | `15_Reverse_Engineering/06_Mechanical.md`; `20_System_BOM/Cooling.md` |

## Electrical Requirements

### Verified

| ID | Requirement | Sources |
|---|---|---|
| ER-V-001 | No readable repository document provides verified MI250X/OAM rail names, voltages, currents, enable names, Power Good names, PMBus addresses, telemetry registers, protection requirements, or startup order. | `15_Reverse_Engineering/02_Power_Rails.md`; `18_Component_Research/02_Power_Converters.md` |
| ER-V-002 | No readable repository document provides verified OAM connector pin numbers, signal names, or electrical assignments. | `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| ER-V-003 | KiCad design rules require unknown values to be marked `TBD`, undocumented OAM pins not to be invented, local decoupling for ICs, and test points on primary rails. | `AI_DESIGN_RULES.md` |
| ER-V-004 | Candidate components such as MP2975 and Molex Mirror Mezz are not verified schematic or BOM items. | `15_Reverse_Engineering/07_Component_ID.md`; `18_Component_Research/10_BOM.md` |

### Inferred

| ID | Requirement | Basis | Sources |
|---|---|---|---|
| ER-I-001 | The carrier shall implement only verified electrical connections, rails, clocks, resets, management nets, and sidebands. | Project rules forbid invented electrical connections. | `AI_PROJECT_CONTEXT.md`; `AI_DESIGN_RULES.md`; `15_Reverse_Engineering/08_Bringup.md` |
| ER-I-002 | All primary rails shall have test access once rail names and safe measurement points are verified. | The design rules call for test points on primary rails, and bring-up requires measurement logging. | `AI_DESIGN_RULES.md`; `15_Reverse_Engineering/08_Bringup.md` |
| ER-I-003 | Electrical schematic capture shall be organized around connector, power, clock/reset, PCIe, management, and validation dependencies. | The reverse-engineering README and block diagrams define these dependency groups. | `15_Reverse_Engineering/README.md`; `15_Reverse_Engineering/09_Block_Diagram.md` |

### Unknown

| ID | Unknown requirement | Why it blocks schematic capture | Sources |
|---|---|---|---|
| ER-U-001 | Connector pinout, pin numbering, signal names, power pins, ground pins, clock pins, sideband pins, management pins, reserved pins, no-connect pins, optional pins, and vendor-specific pins. | No connector symbol or schematic nets can be assigned. | `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `18_Component_Research/01_OAM_Connector.md` |
| ER-U-002 | Electrical standards, voltage levels, polarity, pullups, termination, AC-coupling, impedance, and signal directions for connector signals. | Interfaces cannot be connected safely or routed correctly. | `15_Reverse_Engineering/05_PCIe.md`; `15_Reverse_Engineering/04_Management.md` |
| ER-U-003 | Final carrier component set, packages, footprints, datasheets, ratings, and lifecycle status. | KiCad symbols and footprints cannot be finalized. | `15_Reverse_Engineering/07_Component_ID.md`; `18_Component_Research/10_BOM.md` |

## Thermal Requirements

### Verified

| ID | Requirement | Sources |
|---|---|---|
| TR-V-001 | OAM Thermal Guidelines are marked missing. | `Wanted_Documents.md`; `15_Reverse_Engineering/06_Mechanical.md`; `18_Component_Research/07_Fan_Control.md` |
| TR-V-002 | System goals include a replaceable cooling solution. | `17_System_Architecture/01_System_Goals.md`; `15_Reverse_Engineering/06_Mechanical.md` |
| TR-V-003 | The system BOM records air cooling initially, high airflow ducting, future liquid cooling possibility, industrial PWM fans, front-to-rear airflow, positive pressure, redundant cooling, and easy maintenance as system-level planning goals. | `20_System_BOM/GPU_Subsystem.md`; `20_System_BOM/Cooling.md` |
| TR-V-004 | No readable local source provides MI250X OAM thermal design power, thermal limits, cooling envelope, heatsink geometry, cold-plate interface, airflow/coolant requirement, or fan-control ownership. | `15_Reverse_Engineering/06_Mechanical.md`; `18_Component_Research/07_Fan_Control.md`; `18_Component_Research/06_Temperature_Sensors.md` |

### Inferred

| ID | Requirement | Basis | Sources |
|---|---|---|---|
| TR-I-001 | The carrier system shall provide a verified thermal solution before sustained MI250X operation. | Operation without verified cooling is unsafe. | `15_Reverse_Engineering/10_Minimal_Carrier.md`; `15_Reverse_Engineering/08_Bringup.md` |
| TR-I-002 | Thermal validation shall precede stress or long-duration testing. | Bring-up procedures stop before sustained load if thermal limits and cooling ownership are unknown. | `15_Reverse_Engineering/08_Bringup.md`; `AI_TASKS.md` |
| TR-I-003 | Carrier fan control shall be omitted unless verified cooling requirements prove carrier-side fan control is required. | Fan control ownership is undocumented. | `18_Component_Research/07_Fan_Control.md`; `15_Reverse_Engineering/04_Management.md` |

### Unknown

| ID | Unknown requirement | Why it blocks design | Sources |
|---|---|---|---|
| TR-U-001 | Thermal design power, allowable temperatures, junction-temperature access path, board-temperature limits, and health thresholds. | Cooling sizing and health checks cannot be defined. | `18_Component_Research/06_Temperature_Sensors.md`; `15_Reverse_Engineering/04_Management.md` |
| TR-U-002 | Cooling method required for MI250X OAM: air, heatsink, cold plate, liquid, immersion, or other. | Mechanical envelope and cooling hardware cannot be selected. | `15_Reverse_Engineering/06_Mechanical.md`; `20_System_BOM/Cooling.md` |
| TR-U-003 | Heatsink/cold-plate geometry, thermal interface, mounting force, airflow/coolant rate, coolant type, pump/manifold/reservoir need, and validation method. | Sustained operation cannot be authorized. | `15_Reverse_Engineering/06_Mechanical.md`; `18_Component_Research/07_Fan_Control.md` |
| TR-U-004 | Fan quantity, fan voltage, fan current, fan header, PWM, tachometer, fan fault, presence detection, and firmware ownership. | Carrier fan-control circuitry cannot be specified. | `18_Component_Research/07_Fan_Control.md`; `18_Component_Research/10_BOM.md` |

## PCIe Requirements

### Verified

| ID | Requirement | Sources |
|---|---|---|
| PR-V-001 | PCIe Gen4 is listed as a project hardware goal, and stable PCIe enumeration is listed as a project priority. | `17_System_Architecture/01_System_Goals.md`; `15_Reverse_Engineering/05_PCIe.md` |
| PR-V-002 | MI210 is documented as a standard PCIe 4.0 x16 card; this is reference context only, not MI250X OAM pinout evidence. | `13_Reference_Docs/ROCm/Overview.md`; `15_Reverse_Engineering/05_PCIe.md` |
| PR-V-003 | MI200 SDMA context is described as tuned for PCIe 4.0 x16 and up to 32 GB/s; this is software/data-movement context, not a carrier routing requirement. | `13_Reference_Docs/ROCm/Overview.md`; `15_Reverse_Engineering/05_PCIe.md` |
| PR-V-004 | PCIe Routing Guide and REFCLK Guide are marked missing. | `Wanted_Documents.md`; `15_Reverse_Engineering/05_PCIe.md`; `15_Reverse_Engineering/03_Clock_Tree.md` |
| PR-V-005 | No readable repository document verifies MI250X OAM PCIe generation, lane count, lane map, REFCLK, sidebands, polarity, retimer/switch need, equalization, or routing constraints. | `15_Reverse_Engineering/05_PCIe.md`; `18_Component_Research/08_PCIe_Retimers.md` |

### Inferred

| ID | Requirement | Basis | Sources |
|---|---|---|---|
| PR-I-001 | The carrier shall provide the verified host-facing communication path needed for enumeration and ROCm/software use. | A usable accelerator carrier requires host communication. | `15_Reverse_Engineering/10_Minimal_Carrier.md`; `13_Reference_Docs/ROCm/Overview.md` |
| PR-I-002 | PCIe and REFCLK requirements shall be resolved before schematic capture and PCB layout. | Missing routing and REFCLK guides block high-speed design. | `Wanted_Documents.md`; `09_AI_Notes/10_Design_Checklist.md`; `15_Reverse_Engineering/05_PCIe.md` |
| PR-I-003 | Switches, retimers, and redrivers shall remain optional until topology and signal-integrity evidence proves they are required. | No readable source proves they are needed for one MI250X module. | `15_Reverse_Engineering/05_PCIe.md`; `18_Component_Research/08_PCIe_Retimers.md`; `15_Reverse_Engineering/10_Minimal_Carrier.md` |

### Unknown

| ID | Unknown requirement | Why it blocks schematic/layout | Sources |
|---|---|---|---|
| PR-U-001 | MI250X OAM PCIe generation, lane width, lane count, per-GCD mapping, bifurcation, and host slot mapping. | Host link topology cannot be designed. | `15_Reverse_Engineering/05_PCIe.md`; `09_AI_Notes/03_PCIe_Interface.md` |
| PR-U-002 | Lane order, TX/RX direction, connector pins, pair polarity, lane reversal support, and sideband pins. | Connector symbol and high-speed nets cannot be assigned. | `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `18_Component_Research/08_PCIe_Retimers.md` |
| PR-U-003 | PERST#, CLKREQ#, WAKE#, reset signal names, polarity, timing, voltage levels, pullups, and ownership. | Reset and enumeration sequencing cannot be defined. | `15_Reverse_Engineering/05_PCIe.md`; `15_Reverse_Engineering/08_Bringup.md` |
| PR-U-004 | REFCLK frequency, source, topology, electrical standard, jitter, skew, termination, connector pins, and reset interaction. | PCIe clocking cannot be implemented or validated. | `15_Reverse_Engineering/03_Clock_Tree.md`; `18_Component_Research/03_Clock_Generators.md` |
| PR-U-005 | Impedance, loss budget, AC-coupling, length matching, via rules, return path, equalization, compliance, and simulation requirements. | PCB layout and signal-integrity validation are blocked. | `15_Reverse_Engineering/05_PCIe.md`; `18_Component_Research/08_PCIe_Retimers.md`; `Wanted_Documents.md` |

## OAM Requirements

### Verified

| ID | Requirement | Sources |
|---|---|---|
| OR-V-001 | MI250 and MI250X are described as OCP Accelerator Modules. | `13_Reference_Docs/ROCm/Overview.md`; `15_Reverse_Engineering/01_OAM_Pin_Mapping.md` |
| OR-V-002 | The official Open Accelerator Module specification source is tracked at `https://github.com/oam-dev/spec`. | `02_AMD_Docs/GitHub_Links.rtf`; `09_AI_Notes/02_OAM_Interface.md`; `18_Component_Research/01_OAM_Connector.md` |
| OR-V-003 | The OAM Specification is marked found, while Mechanical Specification, Baseboard Specification, and Connector Specification are marked not found. | `Wanted_Documents.md`; `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `15_Reverse_Engineering/06_Mechanical.md` |
| OR-V-004 | No verified MI250X OAM connector pin map, pin numbers, signal names, electrical assignments, or AMD-specific signal list is present in readable repository files. | `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |

### Inferred

| ID | Requirement | Basis | Sources |
|---|---|---|---|
| OR-I-001 | The carrier shall include the physical and electrical mating interface for the MI250X OAM module after connector type, pin count, pinout, mating height, stack-up, and footprint are verified. | The target module is OAM. | `15_Reverse_Engineering/10_Minimal_Carrier.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| OR-I-002 | OAM-standard and AMD-specific signals shall be separated only after verified sources support the classification. | Current documents identify the need but not the actual signal lists. | `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `15_Reverse_Engineering/README.md` |
| OR-I-003 | Reserved, optional, vendor-specific, and no-connect pins shall not be connected until verified. | Pin handling is undocumented. | `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `AI_DESIGN_RULES.md` |

### Unknown

| ID | Unknown requirement | Why it blocks schematic capture | Sources |
|---|---|---|---|
| OR-U-001 | Connector manufacturer, family, part number, pin count, pin numbering, pin names, signal roles, and footprint. | OAM connector symbol and footprint cannot be created. | `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `18_Component_Research/01_OAM_Connector.md` |
| OR-U-002 | OAM-standard signal set and AMD-specific MI250X signal set. | Required, optional, reserved, vendor-specific, and no-connect handling cannot be determined. | `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `15_Reverse_Engineering/10_Minimal_Carrier.md` |
| OR-U-003 | OAM connector power, ground, PCIe, clock, sideband, management, telemetry, and thermal-related pins. | All major schematic sheets depend on the connector pin map. | `15_Reverse_Engineering/README.md`; `15_Reverse_Engineering/09_Block_Diagram.md` |
| OR-U-004 | OAM mechanical stack-up, mating height, connector current rating, and baseboard integration expectations. | Footprint, current distribution, and board mechanics are blocked. | `15_Reverse_Engineering/06_Mechanical.md`; `18_Component_Research/09_Power_Connectors.md` |

## Management Requirements

### Verified

| ID | Requirement | Sources |
|---|---|---|
| MGR-V-001 | Firmware tools, firmware update guides, MI250 acceptance, health checks, system validation, AMD lab notes, and GPU management references are indexed. | `13_Reference_Docs/Reference_Index.rtf`; `15_Reverse_Engineering/04_Management.md` |
| MGR-V-002 | No readable source provides verified SMBus/I2C/PMBus addresses, bus speeds, bus topology, pullups, voltage levels, connector pins, telemetry registers, firmware wiring, health procedure, BMC/MCU part number, EEPROM/FRU contents, or sensor part numbers. | `15_Reverse_Engineering/04_Management.md`; `18_Component_Research/05_Management_MCU.md` |
| MGR-V-003 | Management MCU/BMC, EEPROM/FRU, sensors, fan controller, and firmware flashing hardware are shown as support blocks or research categories, but their requirements are undocumented. | `17_System_Architecture/02_System_Block_Diagram.md`; `15_Reverse_Engineering/04_Management.md`; `18_Component_Research/10_BOM.md` |

### Inferred

| ID | Requirement | Basis | Sources |
|---|---|---|---|
| MGR-I-001 | Management ownership shall be determined before adding carrier-side MCU/BMC hardware. | Management may be carrier-side, host-side, baseboard-side, module-side, external, or absent. | `15_Reverse_Engineering/04_Management.md`; `15_Reverse_Engineering/10_Minimal_Carrier.md` |
| MGR-I-002 | PMBus, telemetry, voltage monitoring, enable, Power Good, reset, sequencing, and fault behavior shall be treated as cross-functional power and management requirements. | These categories overlap in the power and management notebooks. | `15_Reverse_Engineering/02_Power_Rails.md`; `15_Reverse_Engineering/04_Management.md` |
| MGR-I-003 | Health monitoring shall be defined only after telemetry sources, limits, buses, and procedures are available. | Health references are indexed but not extracted into executable procedures. | `15_Reverse_Engineering/08_Bringup.md`; `13_Reference_Docs/Reference_Index.rtf` |

### Unknown

| ID | Unknown requirement | Why it blocks schematic/firmware | Sources |
|---|---|---|---|
| MGR-U-001 | Whether SMBus, I2C, PMBus, SPI, JTAG, UART, GPIO expanders, interrupts, reset lines, or enable lines are required on the carrier. | Management nets cannot be assigned. | `15_Reverse_Engineering/04_Management.md`; `18_Component_Research/05_Management_MCU.md` |
| MGR-U-002 | Bus topology, owner, addresses, voltage levels, pullups, isolation, muxing, and hot-plug behavior. | Bus wiring and firmware cannot be designed. | `15_Reverse_Engineering/04_Management.md`; `18_Component_Research/04_EEPROM_FRU.md` |
| MGR-U-003 | EEPROM, FRU EEPROM, I2C EEPROM, SPI flash, firmware storage, board metadata, contents, provisioning, write protection, and validation role. | Identity/configuration/firmware storage cannot be added or omitted safely. | `18_Component_Research/04_EEPROM_FRU.md`; `15_Reverse_Engineering/04_Management.md` |
| MGR-U-004 | Sensor requirements for temperature, voltage, current, fault, fan, and health telemetry. | Health checks and safe operation limits cannot be implemented. | `18_Component_Research/06_Temperature_Sensors.md`; `18_Component_Research/07_Fan_Control.md` |
| MGR-U-005 | Firmware update path, recovery path, commands, required hardware, and pass/fail procedure. | Firmware-related schematic hardware cannot be justified. | `13_Reference_Docs/Reference_Index.rtf`; `15_Reverse_Engineering/08_Bringup.md` |

## Power Requirements

### Verified

| ID | Requirement | Sources |
|---|---|---|
| PWR-V-001 | The current readable repository contains no verified MI250X/OAM module rail table. | `15_Reverse_Engineering/02_Power_Rails.md`; `18_Component_Research/02_Power_Converters.md` |
| PWR-V-002 | The OAM specification is tracked as relevant to power specification, but extracted OAM power requirements are not present in readable local files. | `02_AMD_Docs/GitHub_Links.rtf`; `09_AI_Notes/04_Power_Architecture.md`; `15_Reverse_Engineering/02_Power_Rails.md` |
| PWR-V-003 | PMBus Controller Datasheet and VRM Datasheet are marked missing. | `Wanted_Documents.md`; `15_Reverse_Engineering/04_Management.md`; `15_Reverse_Engineering/02_Power_Rails.md` |
| PWR-V-004 | MP2975 is a low-confidence candidate digital multiphase VRM controller believed present on MI250X, not visually confirmed, and without a public datasheet in the repository. | `13_Reference_Docs/Component_Index.rtf`; `15_Reverse_Engineering/07_Component_ID.md`; `18_Component_Research/02_Power_Converters.md` |
| PWR-V-005 | System-level power planning includes three redundant 3000W CRPS supplies, N+1, hot swap, 12V distribution, eight MI250X modules, and dual host systems; final PSU model awaits chassis design. | `20_System_BOM/Power.md` |

### Inferred

| ID | Requirement | Basis | Sources |
|---|---|---|---|
| PWR-I-001 | The carrier shall provide the MI250X/OAM input power and ground paths only after rail and connector requirements are verified. | The target module cannot operate without power and ground. | `15_Reverse_Engineering/02_Power_Rails.md`; `15_Reverse_Engineering/10_Minimal_Carrier.md` |
| PWR-I-002 | Power sequencing, enables, Power Good, reset gating, telemetry, and protection shall be implemented only from verified source requirements. | Incorrect sequencing could prevent operation or damage hardware. | `15_Reverse_Engineering/02_Power_Rails.md`; `15_Reverse_Engineering/08_Bringup.md` |
| PWR-I-003 | System-BOM power targets shall remain planning context unless mapped by evidence to one-module carrier requirements. | CRPS and 12V distribution are system plans, not verified MI250X rails. | `20_System_BOM/Power.md`; `15_Reverse_Engineering/02_Power_Rails.md`; `18_Component_Research/09_Power_Connectors.md` |

### Unknown

| ID | Unknown requirement | Why it blocks schematic/BOM | Sources |
|---|---|---|---|
| PWR-U-001 | Rail names, voltages, tolerances, current limits, input voltage, standby rails, auxiliary rails, main rails, and total power budget. | Regulators, power planes, copper sizing, fusing, and connector ratings cannot be selected. | `15_Reverse_Engineering/02_Power_Rails.md`; `18_Component_Research/02_Power_Converters.md` |
| PWR-U-002 | Power pins, ground pins, current sharing, return-current strategy, connector current rating, and OAM power grouping. | OAM connector power implementation cannot be drawn. | `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `18_Component_Research/09_Power_Connectors.md` |
| PWR-U-003 | Startup order, shutdown order, enables, Power Good thresholds, reset release dependency, fault behavior, retry behavior, and safe power-down. | Bring-up and protection cannot be defined. | `15_Reverse_Engineering/02_Power_Rails.md`; `15_Reverse_Engineering/08_Bringup.md` |
| PWR-U-004 | Regulator topology, VRM controller, power stages, phase count, compensation, switching behavior, telemetry, PMBus behavior, and power-stage pairings. | Power components and firmware cannot be selected. | `15_Reverse_Engineering/07_Component_ID.md`; `18_Component_Research/02_Power_Converters.md` |
| PWR-U-005 | Carrier input-power connector, cable assembly, busbar if any, fusing, hot-swap, inrush, current limiting, and protection hardware. | Input power implementation cannot be specified. | `18_Component_Research/09_Power_Connectors.md`; `18_Component_Research/10_BOM.md` |

## Expandability

### Verified

| ID | Requirement | Sources |
|---|---|---|
| EX-V-001 | Long-term goals include support for 1, 2, 4, and 8 MI250X modules. | `AI_PROJECT_CONTEXT.md`; `17_System_Architecture/01_System_Goals.md`; `17_System_Architecture/04_Future_Expansion.md` |
| EX-V-002 | Future investigation into 16 modules is documented as possible if practical. | `AI_PROJECT_CONTEXT.md`; `AI_TASKS.md` |
| EX-V-003 | Future expansion revisions are documented as single MI250X prototype, dual MI250X carrier, four-MI250X system, and eight-MI250X system. | `17_System_Architecture/04_Future_Expansion.md` |
| EX-V-004 | The GPU subsystem BOM says current configuration is 2 MI250X, future expansion to 4 and 8, OAM, custom carrier board, and PCIe host interface; carrier board is not yet designed. | `20_System_BOM/GPU_Subsystem.md` |

### Inferred

| ID | Requirement | Basis | Sources |
|---|---|---|---|
| EX-I-001 | The first carrier shall remain single-module unless one-module verified requirements demand additional hardware. | Minimal-carrier document excludes scale-out-only hardware from the smallest design. | `15_Reverse_Engineering/10_Minimal_Carrier.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| EX-I-002 | Multi-module expansion shall be resolved after the one-module connector, power, PCIe, clock, management, thermal, and mechanical requirements are verified. | Scale-out affects all unresolved subsystems. | `15_Reverse_Engineering/README.md`; `17_System_Architecture/04_Future_Expansion.md` |
| EX-I-003 | Future revisions should preserve modularity, serviceability, documentation quality, and cost awareness. | These are project priorities and long-term vision items. | `AI_PROJECT_CONTEXT.md`; `AI_TASKS.md`; `17_System_Architecture/01_System_Goals.md` |

### Unknown

| ID | Unknown requirement | Why it blocks expansion design | Sources |
|---|---|---|---|
| EX-U-001 | Multi-module PCIe/fabric topology, host-lane allocation, switch/retimer/redriver role, and baseboard topology. | Scale-out host architecture cannot be designed. | `15_Reverse_Engineering/05_PCIe.md`; `17_System_Architecture/02_System_Block_Diagram.md` |
| EX-U-002 | Multi-module power distribution, PSU-to-carrier mapping, connector ratings, protection, cable routing, and fault isolation. | Eight-module power architecture cannot be specified. | `20_System_BOM/Power.md`; `15_Reverse_Engineering/02_Power_Rails.md` |
| EX-U-003 | Multi-module cooling, chassis airflow/liquid cooling, service envelope, and thermal telemetry. | Scale-out thermal design cannot be validated. | `20_System_BOM/Cooling.md`; `15_Reverse_Engineering/06_Mechanical.md` |
| EX-U-004 | Multi-module management, firmware update, health monitoring, and inventory/FRU architecture. | Fleet or chassis management cannot be defined. | `15_Reverse_Engineering/04_Management.md`; `18_Component_Research/04_EEPROM_FRU.md` |
| EX-U-005 | Whether 16 modules is practical. | The repository records it only as future investigation. | `AI_PROJECT_CONTEXT.md`; `AI_TASKS.md` |

## Future Upgrades

### Verified

| ID | Requirement | Sources |
|---|---|---|
| FU-V-001 | Future improvements include improved cooling, better management firmware, higher power efficiency, easier manufacturing, and community documentation. | `17_System_Architecture/04_Future_Expansion.md` |
| FU-V-002 | Future system goals include up to 8 MI250X modules, possibly 16, two complete computers inside one enclosure, lowest practical cost, open hardware/software, KiCad design, and easy future upgrades. | `AI_PROJECT_CONTEXT.md`; `AI_TASKS.md` |
| FU-V-003 | Host memory planning includes 8 Intel NMA1XXD128GPS 128 GB Optane DC Persistent Memory modules initially and future increase to 16 modules, with target capacity 1 TB initially and 2 TB future. | `20_System_BOM/Host_Platform.md` |
| FU-V-004 | Storage and networking BOM planning includes future storage expansion and NVIDIA Mellanox ConnectX-6 Dx 100 Gigabit Ethernet with future InfiniBand capability. | `20_System_BOM/Storage.md`; `20_System_BOM/Networking.md` |

### Inferred

| ID | Requirement | Basis | Sources |
|---|---|---|---|
| FU-I-001 | Future upgrades shall not drive first-revision schematic complexity unless they also satisfy a verified one-module requirement. | The minimal-carrier notebook prioritizes the smallest one-module carrier. | `15_Reverse_Engineering/10_Minimal_Carrier.md` |
| FU-I-002 | Future revisions should reuse requirements and subsystem documentation where possible. | The project goal is modular, documented, maintainable hardware. | `AI_PROJECT_CONTEXT.md`; `17_System_Architecture/01_System_Goals.md` |
| FU-I-003 | Future upgrades should be converted into explicit requirements only after source-backed topology, power, thermal, mechanical, and management data exist. | Current expansion details are not documented. | `15_Reverse_Engineering/README.md`; `17_System_Architecture/04_Future_Expansion.md` |

### Unknown

| ID | Unknown requirement | Why it remains unresolved | Sources |
|---|---|---|---|
| FU-U-001 | Upgrade path from one module to two, four, eight, and possible sixteen modules. | Electrical, mechanical, thermal, and management scale-out topology is undocumented. | `17_System_Architecture/04_Future_Expansion.md`; `15_Reverse_Engineering/09_Block_Diagram.md` |
| FU-U-002 | Future liquid-cooling implementation. | Liquid cooling is only a future possibility; cold-plate, manifold, pump, coolant, and chassis data are not extracted. | `20_System_BOM/Cooling.md`; `13_Reference_Docs/Reference_Index.rtf`; `18_Component_Research/07_Fan_Control.md` |
| FU-U-003 | Better management firmware architecture. | Firmware tools are indexed, but no firmware architecture, controller role, or update path is documented. | `13_Reference_Docs/Reference_Index.rtf`; `15_Reverse_Engineering/04_Management.md` |
| FU-U-004 | Manufacturing optimization path. | PCB stack-up, connector footprint, mechanical drawings, BOM, and fabrication constraints are not verified. | `15_Reverse_Engineering/06_Mechanical.md`; `18_Component_Research/10_BOM.md` |

## Constraints

### Verified

| ID | Constraint | Sources |
|---|---|---|
| CT-V-001 | Do not invent undocumented OAM pins. | `AI_DESIGN_RULES.md`; `15_Reverse_Engineering/01_OAM_Pin_Mapping.md` |
| CT-V-002 | Unknown values shall be marked `TBD` or `Unknown`. | `AI_DESIGN_RULES.md`; `AI_PROJECT_CONTEXT.md`; `AI_TASKS.md` |
| CT-V-003 | Prefer verified OCP OAM specifications over assumptions. | `AI_DESIGN_RULES.md`; `02_AMD_Docs/GitHub_Links.rtf` |
| CT-V-004 | Treat PCIe lanes as differential pairs, preserve lane numbering, and do not rename reference clocks once verified. | `AI_DESIGN_RULES.md` |
| CT-V-005 | Every IC requires local decoupling when an IC is added to the schematic. | `AI_DESIGN_RULES.md` |
| CT-V-006 | Include test points on all primary rails after primary rails are verified. | `AI_DESIGN_RULES.md`; `15_Reverse_Engineering/08_Bringup.md` |
| CT-V-007 | Do not overwrite existing KiCad files; generate into a new folder when creating KiCad work. | `AI_DESIGN_RULES.md` |
| CT-V-008 | The repository is not ready for final KiCad schematic capture until connector, power, clock, PCIe, management, cooling, mechanical, components, and bring-up gates close. | `15_Reverse_Engineering/README.md`; `15_Reverse_Engineering/10_Minimal_Carrier.md` |

### Inferred

| ID | Constraint | Basis | Sources |
|---|---|---|---|
| CT-I-001 | Use system BOM and host-platform documents as planning context unless they directly define carrier requirements. | BOM files are planning/no-hardware-purchased and several host files are empty shells. | `20_System_BOM/README.md`; `20_System_BOM/Power.md`; `20_System_BOM/Host_Platform.md` |
| CT-I-002 | Do not treat indexed-only references as extracted engineering requirements. | Many references are listed by name but not locally extracted. | `13_Reference_Docs/README.md`; `13_Reference_Docs/Reference_Index.rtf`; `15_Reverse_Engineering/04_Management.md` |
| CT-I-003 | Do not use invalid local PDFs as evidence. | Three local PDFs report invalid structure and could not support component or requirements extraction. | `09_AI_Notes/09_Unknowns.md`; `15_Reverse_Engineering/07_Component_ID.md` |
| CT-I-004 | Do not infer MI250X OAM PCIe requirements from MI210 or MI200 software context. | MI210/MI200 details are reference context only. | `13_Reference_Docs/ROCm/Overview.md`; `15_Reverse_Engineering/05_PCIe.md` |
| CT-I-005 | Do not promote MP2975, Molex Mirror Mezz, HBM references, PCIe switches/retimers/redrivers, EEPROMs, sensors, fan controllers, or management controllers into BOM lines without direct evidence. | They are candidate or unknown component categories. | `15_Reverse_Engineering/07_Component_ID.md`; `18_Component_Research/10_BOM.md` |

### Unknown

| ID | Unknown constraint | Required resolution | Sources |
|---|---|---|---|
| CT-U-001 | Legal/release constraints for open-source hardware manufacturing. | Define license, release files, documentation package, and compliance expectations. | `AI_PROJECT_CONTEXT.md`; `AI_TASKS.md` |
| CT-U-002 | Manufacturing constraints such as PCB layer count, stack-up, impedance process, copper weight, assembly capability, and inspection requirements. | Obtain schematic/layout requirements and fabrication constraints. | `09_AI_Notes/10_Design_Checklist.md`; `15_Reverse_Engineering/06_Mechanical.md` |
| CT-U-003 | Validation limits for release. | Define sourced pass/fail limits for power, clock, PCIe, thermal, management, firmware, ROCm, and stress tests. | `15_Reverse_Engineering/08_Bringup.md`; `AI_TASKS.md` |

## Engineering Assumptions

### Verified

| ID | Assumption / rule | Sources |
|---|---|---|
| EA-V-001 | The specification assumes evidence labels are mandatory project process, not optional documentation style. | `AI_PROJECT_CONTEXT.md`; `AI_TASKS.md`; `README.md` |
| EA-V-002 | The repository's current strongest verified hardware fact is the target module class and software-visible MI250X context, not the carrier pinout or electrical implementation. | `13_Reference_Docs/ROCm/Overview.md`; `15_Reverse_Engineering/07_Component_ID.md` |

### Inferred

| ID | Assumption | Rationale | Sources |
|---|---|---|---|
| EA-I-001 | The first schematic should be a one-MI250X carrier architecture unless verified evidence requires otherwise. | The minimal-carrier document defines one module as the smallest valid target. | `15_Reverse_Engineering/10_Minimal_Carrier.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| EA-I-002 | Schematic capture can begin only as placeholder hierarchy or documentation until the release gates close. | Final nets, pins, rails, components, and dimensions are unresolved. | `15_Reverse_Engineering/README.md`; `09_AI_Notes/10_Design_Checklist.md` |
| EA-I-003 | Host platform selections can guide validation setup but cannot define OAM connector signals or carrier electrical requirements. | Host BOM entries are planning context and do not contain connector-level requirements. | `20_System_BOM/Host_Platform.md`; `15_Reverse_Engineering/05_PCIe.md` |
| EA-I-004 | Future expansion should be protected through modular documentation and not through unsourced first-revision hardware. | Expansion topology is unknown. | `AI_PROJECT_CONTEXT.md`; `17_System_Architecture/04_Future_Expansion.md`; `15_Reverse_Engineering/10_Minimal_Carrier.md` |

### Unknown

| ID | Unknown assumption | Required resolution | Sources |
|---|---|---|---|
| EA-U-001 | Whether the carrier is a direct host adapter, baseboard-compatible OAM carrier, cable/riser assembly, switch-based board, or some other topology. | Recover connector/baseboard/PCIe evidence and define host topology. | `17_System_Architecture/02_System_Block_Diagram.md`; `15_Reverse_Engineering/05_PCIe.md` |
| EA-U-002 | Whether management is required on the carrier. | Determine carrier-side, host-side, baseboard-side, module-side, external, or absent management ownership. | `15_Reverse_Engineering/04_Management.md`; `18_Component_Research/05_Management_MCU.md` |
| EA-U-003 | Whether a carrier-side EEPROM/FRU/firmware storage device is required. | Determine storage ownership, bus, address, contents, and validation role or verified absence. | `18_Component_Research/04_EEPROM_FRU.md`; `15_Reverse_Engineering/04_Management.md` |
| EA-U-004 | Whether first-revision cooling is air-cooled, liquid-cooled, cold-plate-based, or another method. | Obtain OAM Thermal Guidelines or verified measurements. | `15_Reverse_Engineering/06_Mechanical.md`; `20_System_BOM/Cooling.md` |

## Schematic Capture Release Gates

The following gates must close before final schematic capture can assign concrete nets, values, part numbers, or footprints.

| Gate | Required verified output | Current status | Authority files |
|---|---|---|---|
| OAM connector | Connector manufacturer, part number, pin count, pin numbering, footprint, signal map, mating height, stack-up, current rating, and mechanical constraints. | Unknown / blocking | `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `15_Reverse_Engineering/06_Mechanical.md` |
| Power | Rail table, voltages, currents, input power, power pins, ground pins, sequencing, enables, Power Good, PMBus, telemetry, monitoring, protection, and fault behavior. | Unknown / blocking | `15_Reverse_Engineering/02_Power_Rails.md`; `18_Component_Research/02_Power_Converters.md` |
| Clock and reset | REFCLK source/frequency/topology, clock components if any, jitter/skew/routing, reset names, polarity, timing, and Power Good relationship. | Unknown / blocking | `15_Reverse_Engineering/03_Clock_Tree.md`; `15_Reverse_Engineering/08_Bringup.md` |
| PCIe | Generation, lane width, lane map, sidebands, topology, routing constraints, switch/retimer/redriver decision, equalization, and compliance method. | Unknown / blocking | `15_Reverse_Engineering/05_PCIe.md`; `18_Component_Research/08_PCIe_Retimers.md` |
| Management | Ownership, buses, addresses, voltage levels, pullups, PMBus/I2C/SMBus topology, EEPROM/FRU role, firmware path, telemetry, health, and fan-control role. | Unknown / blocking | `15_Reverse_Engineering/04_Management.md`; `18_Component_Research/05_Management_MCU.md` |
| Thermal/mechanical | Module dimensions, connector coordinates, board outline, mounting, keepouts, PCB thickness, thermal limits, cooling interface, airflow/coolant, fan ownership, and validation limits. | Unknown / blocking | `15_Reverse_Engineering/06_Mechanical.md`; `18_Component_Research/07_Fan_Control.md` |
| Components/BOM | Manufacturer, part number, package, datasheet, footprint, ratings, confidence level, and source for every schematic component. | Unknown / blocking | `15_Reverse_Engineering/07_Component_ID.md`; `18_Component_Research/10_BOM.md` |
| Bring-up and validation | Numbered procedure with measurement points, pass/fail limits, current limits, clock limits, reset timing, management commands, health criteria, thermal limits, debug flow, and recovery. | Template exists; values unknown | `15_Reverse_Engineering/08_Bringup.md` |

## Non-Requirements And Weak Evidence

| Item | Position in this specification | Sources |
|---|---|---|
| MI210 PCIe 4.0 x16 | Reference context only; not MI250X OAM lane or routing evidence. | `13_Reference_Docs/ROCm/Overview.md`; `15_Reverse_Engineering/05_PCIe.md` |
| MI200 SDMA up to 32 GB/s | Software/data-movement context only; not a carrier PCIe requirement. | `13_Reference_Docs/ROCm/Overview.md`; `15_Reverse_Engineering/05_PCIe.md` |
| MP2975 | Low-confidence candidate research lead only; not a verified rail, PMBus, or BOM requirement. | `13_Reference_Docs/Component_Index.rtf`; `15_Reverse_Engineering/07_Component_ID.md` |
| Molex Mirror Mezz | Candidate connector reference only; not confirmed as MI250X OAM connector. | `13_Reference_Docs/Reference_Index.rtf`; `18_Component_Research/01_OAM_Connector.md` |
| Three 3000W CRPS supplies / 12V distribution | System-level planning target; not a verified MI250X/OAM rail or carrier input requirement. | `20_System_BOM/Power.md`; `15_Reverse_Engineering/02_Power_Rails.md` |
| Air cooling initially / future liquid cooling | System-level planning goal; not a verified MI250X OAM thermal design. | `20_System_BOM/GPU_Subsystem.md`; `20_System_BOM/Cooling.md`; `15_Reverse_Engineering/06_Mechanical.md` |
| Indexed firmware, health, cooling, and OAM/OCP references | Research leads until extracted into readable requirements with citations. | `13_Reference_Docs/Reference_Index.rtf`; `15_Reverse_Engineering/04_Management.md` |
| Invalid local PDFs | Not usable as evidence until repaired or replaced. | `09_AI_Notes/09_Unknowns.md`; `15_Reverse_Engineering/07_Component_ID.md` |

## Repository Coverage

| Document area | Use in this specification |
|---|---|
| `README.md`, `AI_PROJECT_CONTEXT.md`, `AI_TASKS.md`, `AI_DESIGN_RULES.md`, `Wanted_Documents.md` | Project goal, evidence rules, design rules, roadmap, and missing-source tracker. |
| `02_AMD_Docs/` and `13_Reference_Docs/` | OAM/OCP links, reference indexes, ROCm overview, component index, and unreadable/placeholder reference limitations. |
| `08_Research_Papers/` | Data-movement/topology context and invalid PDF limitations; no carrier schematic facts promoted. |
| `09_AI_Notes/` | Topic notes for architecture, OAM, PCIe, power, clocking, management, cooling, mechanical, unknowns, and design checklist. |
| `15_Reverse_Engineering/` | Main schematic-preparation authority for OAM pin mapping, power rails, clock tree, management, PCIe, mechanical, component ID, bring-up, block diagram, and minimal carrier. |
| `17_System_Architecture/` | System goals, block diagram, minimal carrier requirements, future expansion, component-selection shell, and this final requirements specification. |
| `18_Component_Research/` | Component-selection notebooks for connector, power, clock, EEPROM/FRU, management, sensors, fan control, PCIe, power connectors, and BOM planning. |
| `19_Host_Platform/` | Empty RTF shells in the current repository state; no requirements promoted. |
| `20_System_BOM/` | System-planning context for host platform, GPU subsystem, storage, networking, power, cooling, cost, and procurement status. |
| `21_Schematic_Planning/` | Empty RTF shells in the current repository state; no requirements promoted. |

## Sources

- `AI_PROJECT_CONTEXT.md`
- `AI_TASKS.md`
- `AI_DESIGN_RULES.md`
- `README.md`
- `Wanted_Documents.md`
- `02_AMD_Docs/README.md`
- `02_AMD_Docs/GitHub_Links.rtf`
- `08_Research_Papers/README.md`
- `08_Research_Papers/01_Architecture/notes.rtf`
- `09_AI_Notes/01_Project_Overview.md`
- `09_AI_Notes/02_OAM_Interface.md`
- `09_AI_Notes/03_PCIe_Interface.md`
- `09_AI_Notes/04_Power_Architecture.md`
- `09_AI_Notes/05_Clock_Architecture.md`
- `09_AI_Notes/06_Management_Controller.md`
- `09_AI_Notes/07_Cooling.md`
- `09_AI_Notes/08_Mechanical.md`
- `09_AI_Notes/09_Unknowns.md`
- `09_AI_Notes/10_Design_Checklist.md`
- `13_Reference_Docs/README.md`
- `13_Reference_Docs/Reference_Index.rtf`
- `13_Reference_Docs/Component_Index.rtf`
- `13_Reference_Docs/ROCm/Overview.md`
- `13_Reference_Docs/ROCm/Matrix_Cores/README.md`
- `13_Reference_Docs/Memory_HBM/README.md`
- `15_Reverse_Engineering/README.md`
- `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`
- `15_Reverse_Engineering/02_Power_Rails.md`
- `15_Reverse_Engineering/03_Clock_Tree.md`
- `15_Reverse_Engineering/04_Management.md`
- `15_Reverse_Engineering/05_PCIe.md`
- `15_Reverse_Engineering/06_Mechanical.md`
- `15_Reverse_Engineering/07_Component_ID.md`
- `15_Reverse_Engineering/08_Bringup.md`
- `15_Reverse_Engineering/09_Block_Diagram.md`
- `15_Reverse_Engineering/10_Minimal_Carrier.md`
- `17_System_Architecture/01_System_Goals.md`
- `17_System_Architecture/02_System_Block_Diagram.md`
- `17_System_Architecture/03_Minimal_Carrier_Requirements.md`
- `17_System_Architecture/04_Future_Expansion.md`
- `17_System_Architecture/05_Component_Selection.md`
- `18_Component_Research/README.md`
- `18_Component_Research/01_OAM_Connector.md`
- `18_Component_Research/02_Power_Converters.md`
- `18_Component_Research/03_Clock_Generators.md`
- `18_Component_Research/04_EEPROM_FRU.md`
- `18_Component_Research/05_Management_MCU.md`
- `18_Component_Research/06_Temperature_Sensors.md`
- `18_Component_Research/07_Fan_Control.md`
- `18_Component_Research/08_PCIe_Retimers.md`
- `18_Component_Research/09_Power_Connectors.md`
- `18_Component_Research/10_BOM.md`
- `20_System_BOM/README.md`
- `20_System_BOM/Host_Platform.md`
- `20_System_BOM/GPU_Subsystem.md`
- `20_System_BOM/Power.md`
- `20_System_BOM/Cooling.md`
- `20_System_BOM/Storage.md`
- `20_System_BOM/Networking.md`
- `20_System_BOM/Cost_Estimate.md`
- `21_Schematic_Planning/README.md`
