# Purpose

Research EEPROM, FRU EEPROM, I2C EEPROM, board identification, SMBus, configuration EEPROM, and board metadata requirements for an open-source AMD Instinct MI250X OAM carrier board using only repository information.

This document is not an EEPROM selection, FRU data map, address map, firmware plan, schematic source, or BOM. The repository does not currently contain verified EEPROM or FRU EEPROM part numbers, required contents, bus topology, SMBus/I2C addresses, write-protect behavior, board-identification format, board metadata format, configuration data, ownership model, or OAM connector pin mapping for the MI250X OAM carrier. Sources: `15_Reverse_Engineering/04_Management.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `18_Component_Research/README.md`.

# Verified

Only facts directly supported by repository documents are included here.

| Topic | Verified repository fact | Sources |
|---|---|---|
| Project evidence workflow | The repository is organized as a reverse-engineering knowledge base where unknown behavior is tracked rather than assumed. | `README.md`; `AI_TASKS.md` |
| EEPROM engineering unknown | `AI_TASKS.md` lists EEPROM requirements as a current engineering unknown and includes EEPROM validation as a future bring-up task. | `AI_TASKS.md` |
| Management research scope | The management note includes SMBus, I2C, PMBus, EEPROM, FRU EEPROM, BMC interaction, management MCU, firmware management, and health monitoring in its research scope. | `15_Reverse_Engineering/04_Management.md` |
| Management interface status | SMBus, I2C, PMBus, EEPROM, FRU EEPROM, BMC interaction, management MCU, firmware-management hardware, and health-monitoring hardware are undocumented in readable local files. | `15_Reverse_Engineering/04_Management.md`; `15_Reverse_Engineering/08_Bringup.md` |
| Component-identification status | EEPROMs and FRU EEPROMs are listed as undocumented component categories. | `15_Reverse_Engineering/07_Component_ID.md`; `18_Component_Research/README.md` |
| Component-selection status | The component-selection document contains an EEPROM candidate-parts section, but no candidate parts are filled in. | `17_System_Architecture/05_Component_Selection.md` |
| BOM status | `18_Component_Research/10_BOM.md` lists EEPROM, FRU EEPROM, and SPI flash / firmware storage device as unknown categories. | `18_Component_Research/10_BOM.md` |
| BOM meaning | Empty manufacturer and part-number cells in the BOM mean the repository does not currently provide that information. | `18_Component_Research/10_BOM.md` |
| Minimal carrier status | EEPROM or FRU EEPROM is optional until a readable source proves that the carrier must provide one. | `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `15_Reverse_Engineering/10_Minimal_Carrier.md` |
| Block diagram status | The system block diagram shows EEPROM / FRU EEPROM as a support block with requirement undocumented. | `17_System_Architecture/02_System_Block_Diagram.md`; `15_Reverse_Engineering/09_Block_Diagram.md` |
| Connector-level status | EEPROM or FRU EEPROM requirement, address, contents, ownership, and OAM pin mapping are undocumented. | `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `18_Component_Research/01_OAM_Connector.md` |
| Bring-up status | EEPROM access is undocumented in readable local files. | `15_Reverse_Engineering/08_Bringup.md`; `15_Reverse_Engineering/04_Management.md` |
| Firmware references | Firmware Tool v2.3, Firmware Tool v2.2, AMD FW Flash Guide, and Firmware Update Guide are indexed. | `13_Reference_Docs/Reference_Index.rtf`; `15_Reverse_Engineering/04_Management.md`; `09_AI_Notes/06_Management_Controller.md` |
| Validation references | MI250 Acceptance, Health Checks, System Validation, AMD Lab Notes, and GPU Accelerator Management Interfaces are indexed. | `13_Reference_Docs/Reference_Index.rtf`; `15_Reverse_Engineering/04_Management.md`; `09_AI_Notes/06_Management_Controller.md` |
| MI250X module context | MI250 and MI250X are described as OCP Accelerator Modules with two GCDs and 128 GB total memory, exposed to software as two devices with separate 64 GB VRAM blocks. | `13_Reference_Docs/ROCm/Overview.md`; `15_Reverse_Engineering/07_Component_ID.md` |

# Candidate Components

No EEPROM or FRU EEPROM device is verified as selected, required, or present. The table below records only repository-supported candidate categories.

| Device or category | Manufacturer | Part number | Status | Repository-supported information | Design position | Sources |
|---|---|---|---|---|---|---|
| Carrier EEPROM | Unknown | Unknown | Unknown category | The BOM lists EEPROM as a possible identity or configuration storage category if required, but no readable source proves the carrier must include one. | Do not select or place a carrier EEPROM until requirement, role, bus, contents, and part number are verified. | `18_Component_Research/10_BOM.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `15_Reverse_Engineering/04_Management.md` |
| FRU EEPROM | Unknown | Unknown | Unknown category | FRU EEPROM is listed as an unknown identity / storage category and as an undocumented management topic. | Do not define FRU format, address, stored contents, or device part number from current repository evidence. | `18_Component_Research/10_BOM.md`; `15_Reverse_Engineering/04_Management.md`; `15_Reverse_Engineering/07_Component_ID.md` |
| I2C EEPROM | Unknown | Unknown | Unknown category | I2C is named as an undocumented management interface, but no source proves an I2C EEPROM requirement. | Treat as a research category only; do not assign an I2C address, size, voltage, write protect, or contents. | `15_Reverse_Engineering/04_Management.md`; `09_AI_Notes/06_Management_Controller.md`; `18_Component_Research/README.md` |
| Configuration EEPROM | Unknown | Unknown | Unknown category | The BOM describes EEPROM as carrier, module, identity, or configuration storage if required; exact configuration role is not documented. | Do not assume configuration data exists or define its contents. | `18_Component_Research/10_BOM.md`; `18_Component_Research/README.md` |
| Module EEPROM | Unknown | Unknown | Unknown category | No readable local source proves that a module EEPROM is exposed to, required by, or readable from the carrier. | Do not add module-EEPROM nets or access logic until connector and management sources prove it. | `15_Reverse_Engineering/04_Management.md`; `15_Reverse_Engineering/10_Minimal_Carrier.md`; `18_Component_Research/01_OAM_Connector.md` |
| Firmware storage device | Unknown | Unknown | Unknown category | Firmware tools and update guides are indexed, and the BOM lists SPI flash / firmware storage device as unknown. | Do not treat firmware storage as EEPROM/FRU or add firmware storage until hardware dependencies are verified. | `13_Reference_Docs/Reference_Index.rtf`; `15_Reverse_Engineering/04_Management.md`; `18_Component_Research/10_BOM.md` |

# Unknown

- **Unknown:** Whether the minimal carrier must include EEPROM, FRU EEPROM, I2C EEPROM, configuration EEPROM, SPI flash, firmware storage, or any other identity or metadata storage device. Sources: `15_Reverse_Engineering/04_Management.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `18_Component_Research/10_BOM.md`.
- **Unknown:** EEPROM/FRU manufacturer, part number, density, package, voltage, bus type, write-protect behavior, address pins, pullup requirements, endurance, temperature rating, and footprint. Sources: `15_Reverse_Engineering/07_Component_ID.md`; `17_System_Architecture/05_Component_Selection.md`; `18_Component_Research/README.md`.
- **Unknown:** EEPROM contents, FRU contents, configuration contents, board metadata contents, data format, checksum behavior, provisioning process, update process, and field ownership. Sources: `15_Reverse_Engineering/04_Management.md`; `18_Component_Research/README.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`.
- **Unknown:** Board identification requirement, board-identification format, metadata format, and whether any board metadata is required for power-up, PCIe enumeration, firmware loading, driver initialization, ROCm detection, health checks, or validation. Sources: `15_Reverse_Engineering/08_Bringup.md`; `15_Reverse_Engineering/04_Management.md`; `13_Reference_Docs/Reference_Index.rtf`.
- **Unknown:** Whether board identification or metadata belongs to the carrier, MI250X module, host/baseboard, BMC, management MCU, firmware storage, or no carrier-visible device. Sources: `17_System_Architecture/02_System_Block_Diagram.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `15_Reverse_Engineering/10_Minimal_Carrier.md`.
- **Unknown:** SMBus, I2C, PMBus, SPI, JTAG, UART, reset, interrupt, enable, GPIO, and firmware-update topology. Sources: `09_AI_Notes/06_Management_Controller.md`; `15_Reverse_Engineering/04_Management.md`; `18_Component_Research/05_Management_MCU.md`.
- **Unknown:** SMBus/I2C/PMBus addresses, address straps, bus ownership, voltage levels, pullups, muxing, isolation, hot-plug behavior, connector pins, and bus access sequencing. Sources: `15_Reverse_Engineering/04_Management.md`; `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `18_Component_Research/05_Management_MCU.md`.
- **Unknown:** Firmware update hardware dependencies, including whether EEPROM/FRU/configuration storage participates in firmware update, identity reporting, health checks, or validation. Sources: `13_Reference_Docs/Reference_Index.rtf`; `09_AI_Notes/06_Management_Controller.md`; `15_Reverse_Engineering/04_Management.md`.
- **Unknown:** Whether a carrier-side management MCU or BMC is required, and whether either would access EEPROM/FRU data. Sources: `15_Reverse_Engineering/04_Management.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `18_Component_Research/05_Management_MCU.md`.

# Design Implications

- Do not assume EEPROM contents, FRU contents, board metadata contents, configuration data, board-identification values, or any other stored fields from the current repository.
- Do not place EEPROM, FRU EEPROM, I2C EEPROM, SPI flash, firmware storage, pullups, address straps, write-protect circuits, or bus muxes into the schematic until requirement, ownership, contents, bus, address, and part number are verified.
- Do not assign SMBus, I2C, PMBus, SPI, EEPROM, FRU, write-protect, address, BMC, MCU, or management sideband nets from the current repository alone.
- Treat the EEPROM / FRU EEPROM block in architecture diagrams as a dependency placeholder, not a verified schematic requirement.
- Treat firmware and health-check references as research drivers only; indexed references do not prove an EEPROM, FRU EEPROM, or specific board metadata format.
- Keep EEPROM/FRU research linked to connector, management, power, firmware, and bring-up notes because bus ownership, power sequencing, reset behavior, and validation may cross subsystem boundaries.

# Future Research

| Priority | Research task | Required output | Sources |
|---|---|---|---|
| High | Determine whether EEPROM or FRU EEPROM is required. | Verified carrier-side, module-side, baseboard-side, or no-carrier EEPROM/FRU requirement. | `15_Reverse_Engineering/04_Management.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `15_Reverse_Engineering/10_Minimal_Carrier.md` |
| High | Determine EEPROM/FRU ownership and contents from a verified source. | Verified owner, storage role, data format, stored contents, update process, and validation responsibility, or verified statement that no such storage is required. | `15_Reverse_Engineering/04_Management.md`; `13_Reference_Docs/Reference_Index.rtf`; `15_Reverse_Engineering/08_Bringup.md` |
| High | Obtain verified management and OAM connector documentation. | Verified SMBus/I2C/PMBus/SPI pins, EEPROM/FRU pins, management pins, addresses, bus ownership, voltage levels, pullups, and write-protect requirements. | `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `18_Component_Research/01_OAM_Connector.md`; `15_Reverse_Engineering/04_Management.md` |
| High | Determine board-identification requirements. | Verified board identification path, metadata requirement, access method, and whether board metadata is required for bring-up, firmware, health checks, or software detection. | `15_Reverse_Engineering/08_Bringup.md`; `13_Reference_Docs/Reference_Index.rtf`; `18_Component_Research/05_Management_MCU.md` |
| Medium | Identify EEPROM devices only after requirements are known. | Verified manufacturer, part number, package, density, power rail, bus, address behavior, write-protect behavior, and BOM status for any required EEPROM/FRU device. | `15_Reverse_Engineering/07_Component_ID.md`; `17_System_Architecture/05_Component_Selection.md`; `18_Component_Research/10_BOM.md` |
| Medium | Determine firmware-storage relationship. | Verified whether indexed firmware tools require carrier storage, module storage, external programming, management MCU/BMC access, or no carrier-side storage. | `13_Reference_Docs/Reference_Index.rtf`; `09_AI_Notes/06_Management_Controller.md`; `15_Reverse_Engineering/04_Management.md` |
| Medium | Add bring-up validation steps after requirements are sourced. | Verified EEPROM/FRU access checks, board-ID checks, write-protect checks, bus scan procedure, and pass/fail criteria if required. | `AI_TASKS.md`; `15_Reverse_Engineering/08_Bringup.md`; `09_AI_Notes/10_Design_Checklist.md` |

# Sources

- `README.md` - States the evidence workflow and that undocumented behavior should be tracked as an open question rather than assumed.
- `AI_TASKS.md` - Lists EEPROM requirements as a current engineering unknown and includes EEPROM validation as a future bring-up task.
- `Wanted_Documents.md` - Tracks missing system evidence and does not list a found EEPROM/FRU-specific source in the readable document list.
- `13_Reference_Docs/Reference_Index.rtf` - Indexes firmware tools, firmware update guides, health checks, system validation, MI250 acceptance, and GPU accelerator management interfaces.
- `13_Reference_Docs/ROCm/Overview.md` - Provides MI250/MI250X OAM module context and `rocminfo` software-inspection context.
- `09_AI_Notes/06_Management_Controller.md` - Summarizes management, firmware, health-check, SMBus/I2C, PMBus, JTAG, SPI flash, UART, reset, interrupt, and enable gaps.
- `15_Reverse_Engineering/01_OAM_Pin_Mapping.md` - Records management buses, EEPROM/FRU, and OAM pin mapping as undocumented at connector level.
- `15_Reverse_Engineering/04_Management.md` - Main management evidence document for SMBus, I2C, PMBus, EEPROM, FRU EEPROM, BMC interaction, management MCU, firmware, and health monitoring.
- `15_Reverse_Engineering/07_Component_ID.md` - Lists EEPROMs / FRU EEPROMs and management controllers as undocumented component categories.
- `15_Reverse_Engineering/08_Bringup.md` - Records EEPROM access and management initialization as undocumented bring-up topics.
- `15_Reverse_Engineering/09_Block_Diagram.md` - Shows Management / BMC / MCU / EEPROM as an unknown architecture block.
- `15_Reverse_Engineering/10_Minimal_Carrier.md` - Lists EEPROM or FRU EEPROM as optional until a readable source proves one is required.
- `17_System_Architecture/02_System_Block_Diagram.md` - Shows EEPROM / FRU EEPROM with requirement undocumented.
- `17_System_Architecture/03_Minimal_Carrier_Requirements.md` - Lists EEPROM or FRU EEPROM as optional until a readable source proves carrier requirement, and management hardware as unknown.
- `17_System_Architecture/05_Component_Selection.md` - Contains an EEPROM candidate-parts section with no candidate parts filled in.
- `18_Component_Research/README.md` - Defines `04_EEPROM_FRU.md` as EEPROM and FRU EEPROM research and marks current EEPROM/FRU requirements as unknown.
- `18_Component_Research/01_OAM_Connector.md` - Records EEPROM/FRU requirement, contents, ownership, and OAM pin mapping as undocumented.
- `18_Component_Research/05_Management_MCU.md` - Records management bus, SMBus/I2C/PMBus, firmware, telemetry, reset, GPIO, and sideband ownership as unresolved.
- `18_Component_Research/10_BOM.md` - Tracks EEPROM, FRU EEPROM, and SPI flash / firmware storage as unknown component categories.