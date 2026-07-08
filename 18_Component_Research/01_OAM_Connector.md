# Purpose

Research the AMD Instinct MI250X OAM connector using every repository document that contains connector, OAM, mechanical, baseboard, Molex, pinout, signal, PCIe, clock, power, management, cooling, BOM, or project-rule evidence.

This file is not a connector pinout, schematic source, footprint, mechanical drawing, or approved BOM. The repository does not currently contain a verified MI250X OAM connector manufacturer, connector family, part number, pin count, pin assignment, pitch, mating height, stack-up, footprint, current rating, or placement dimension. Sources: `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `15_Reverse_Engineering/06_Mechanical.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `18_Component_Research/10_BOM.md`.

# Verified

Only facts directly supported by repository documents are included here.

| Topic | Verified repository fact | Sources |
|---|---|---|
| Project goal | The project goal is to design an open hardware carrier board capable of operating AMD Instinct MI250X OAM accelerator modules. | `AI_PROJECT_CONTEXT.md`; `README.md` |
| Evidence rules | Project rules require `Verified`, `Inferred`, and `Unknown` labels. | `AI_PROJECT_CONTEXT.md`; `AI_TASKS.md` |
| Pinout evidence rule | Pinouts should only be marked verified if supported by documentation. | `AI_PROJECT_CONTEXT.md`; `15_Reverse_Engineering/01_OAM_Pin_Mapping.md` |
| Target module | MI250 and MI250X are OCP Accelerator Modules with two GCDs and 128 GB total memory, exposed to software as two devices with separate 64 GB VRAM blocks. | `13_Reference_Docs/ROCm/Overview.md`; `15_Reverse_Engineering/07_Component_ID.md` |
| OAM specification link | The repository tracks `https://github.com/oam-dev/spec` as the official Open Accelerator Module specification. | `02_AMD_Docs/GitHub_Links.rtf`; `09_AI_Notes/02_OAM_Interface.md`; `15_Reverse_Engineering/01_OAM_Pin_Mapping.md` |
| OAM specification usefulness | The OAM specification link is described as useful for mechanical drawings, connector specification, and power specification. | `02_AMD_Docs/GitHub_Links.rtf`; `02_AMD_Docs/README.md`; `15_Reverse_Engineering/06_Mechanical.md` |
| Document availability | `Wanted_Documents.md` marks OAM Specification as found. | `Wanted_Documents.md`; `09_AI_Notes/02_OAM_Interface.md`; `09_AI_Notes/10_Design_Checklist.md` |
| Missing source documents | `Wanted_Documents.md` marks Mechanical Specification, Baseboard Specification, and Connector Specification as not found. | `Wanted_Documents.md`; `09_AI_Notes/02_OAM_Interface.md`; `15_Reverse_Engineering/06_Mechanical.md` |
| Indexed OAM/OCP references | OAM Base Spec, OCP Accelerator Spec, Universal Baseboard, and OAI EXP are indexed under OCP/OAM references. | `13_Reference_Docs/Reference_Index.rtf`; `15_Reverse_Engineering/01_OAM_Pin_Mapping.md` |
| Indexed connector references | Mirror Mezz Datasheet, Mirror Mezz Brochure, and Mirror Mezz Product Guide are indexed under Molex. | `13_Reference_Docs/Reference_Index.rtf`; `09_AI_Notes/08_Mechanical.md`; `15_Reverse_Engineering/07_Component_ID.md` |
| Mirror Mezz limitation | Molex Mirror Mezz documents are indexed, but no readable local source confirms Mirror Mezz as the MI250X OAM connector. | `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `15_Reverse_Engineering/07_Component_ID.md`; `18_Component_Research/10_BOM.md` |
| Photo tracking | Front, back, and connector photos are marked found; heatsink and baseboard photos are not marked found. | `Wanted_Documents.md`; `15_Reverse_Engineering/06_Mechanical.md`; `09_AI_Notes/08_Mechanical.md` |
| Local photo gap | Repository notes state that the front, back, and connector photos marked found are not present as readable image files in the repository. | `09_AI_Notes/01_Project_Overview.md`; `09_AI_Notes/09_Unknowns.md`; `15_Reverse_Engineering/01_OAM_Pin_Mapping.md` |
| Planned reference-library scope | The reference-library README lists planned folders for photos, measurements/dimensions, teardown photos, PCB analysis, and vendor documentation. | `13_Reference_Docs/README.rtf` |
| Planned connector reference | The reference-library README lists Mirror Mezz Connector Documentation as a main reference. | `13_Reference_Docs/README.rtf` |
| Architecture diagram status | System diagrams show Host -> PCIe -> optional PCIe Switch/Retimer -> OAM Connector -> MI250X. | `17_System_Architecture/02_System_Block_Diagram.md`; `15_Reverse_Engineering/09_Block_Diagram.md` |
| Architecture diagram gap | System diagrams mark OAM connector pinout, mechanics, and sidebands as undocumented. | `17_System_Architecture/02_System_Block_Diagram.md`; `15_Reverse_Engineering/09_Block_Diagram.md` |
| Current engineering unknown | `AI_TASKS.md` lists OAM connector pinout as a current high-priority engineering unknown. | `AI_TASKS.md`; `15_Reverse_Engineering/01_OAM_Pin_Mapping.md` |

# Candidate Components

| Candidate manufacturer or family | Status | Repository evidence | Limitations | Sources |
|---|---|---|---|---|
| Molex | Candidate manufacturer | Molex is named in the reference index, and Mirror Mezz documents are indexed under Molex. | No readable local source confirms Molex as the actual MI250X OAM connector manufacturer. No Molex connector part number is documented. | `13_Reference_Docs/Reference_Index.rtf`; `15_Reverse_Engineering/07_Component_ID.md`; `18_Component_Research/10_BOM.md` |
| Molex Mirror Mezz | Candidate connector family/reference | Mirror Mezz Datasheet, Mirror Mezz Brochure, and Mirror Mezz Product Guide are indexed. `15_Reverse_Engineering/07_Component_ID.md` lists Mirror Mezz as a possible connector reference family for OAM/mezzanine interconnect research. | Not confirmed as the MI250X OAM connector. Exact part number, pitch, pin count, mating height, stack-up, footprint, current rating, and signal-integrity characteristics are unknown. | `13_Reference_Docs/Reference_Index.rtf`; `09_AI_Notes/08_Mechanical.md`; `15_Reverse_Engineering/07_Component_ID.md`; `18_Component_Research/10_BOM.md` |
| MI250X OAM mating connector | Unknown actual connector | A minimal carrier must include the physical and electrical mating interface for the MI250X OAM module once verified. | Actual manufacturer, family, part number, pinout, and mechanical implementation are not documented in readable local files. | `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `15_Reverse_Engineering/10_Minimal_Carrier.md` |
| OAM/OCP indexed references | Source set, not connector selection | OAM Base Spec, OCP Accelerator Spec, Universal Baseboard, and OAI EXP are indexed under OCP/OAM references. | The index does not by itself identify an MI250X connector manufacturer, family, part number, pinout, or dimensions. | `13_Reference_Docs/Reference_Index.rtf`; `09_AI_Notes/02_OAM_Interface.md` |

# Unknown

- **Unknown:** Exact MI250X OAM connector manufacturer, connector family, part number, pin count, pitch, row/column arrangement, mating height, stack-up, footprint, current rating, and placement. Sources: `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `15_Reverse_Engineering/06_Mechanical.md`; `18_Component_Research/10_BOM.md`.
- **Unknown:** Full connector pinout, including power, ground, PCIe, REFCLK, reset, management, sideband, telemetry, sensor, fan-control, optional, reserved, no-connect, and vendor-specific pins. Sources: `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`.
- **Unknown:** Which connector requirements are OAM-defined, AMD-specific to MI250X, baseboard-specific, host-topology-specific, or implementation-specific. Sources: `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `15_Reverse_Engineering/10_Minimal_Carrier.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`.
- **Unknown:** Whether Molex Mirror Mezz is the actual connector family used by MI250X OAM. Sources: `13_Reference_Docs/Reference_Index.rtf`; `15_Reverse_Engineering/07_Component_ID.md`; `18_Component_Research/10_BOM.md`.
- **Unknown:** Whether the front, back, and connector photos marked found can verify connector markings, orientation, pitch, placement, or visible vendor clues because the image files are not present as readable repository evidence. Sources: `Wanted_Documents.md`; `09_AI_Notes/01_Project_Overview.md`; `09_AI_Notes/09_Unknowns.md`.
- **Unknown:** Connector electrical performance, including high-speed loss, impedance, crosstalk, reference-clock constraints, return-current requirements, and management/sideband electrical levels. Sources: `15_Reverse_Engineering/03_Clock_Tree.md`; `15_Reverse_Engineering/05_PCIe.md`; `18_Component_Research/08_PCIe_Retimers.md`.
- **Unknown:** Mechanical constraints needed for PCB layout, including module outline, board outline, connector coordinates, mounting holes, keepouts, PCB thickness, standoff height, cold-plate/heatsink clearance, and module weight. Sources: `15_Reverse_Engineering/06_Mechanical.md`; `09_AI_Notes/08_Mechanical.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`.

# Design Implications

- Do not create a connector symbol, footprint, pin map, 3D model, board outline, placement constraint, or routing constraint from the current repository alone.
- Do not assign OAM connector pin numbers, signal names, rail names, PCIe lanes, REFCLK pins, reset pins, sideband pins, management pins, EEPROM pins, sensor pins, fan-control pins, reserved pins, or no-connect pins until a verified pinout source exists.
- Do not treat Molex or Molex Mirror Mezz as the MI250X connector without direct evidence from a readable source or verified physical inspection.
- Do not infer pitch, mating height, stack-up, footprint, keepouts, current rating, loss, impedance, skew, or connector placement from indexed reference names alone.
- Treat the current system diagrams as dependency maps only; they show that an OAM connector is needed, but they do not define a schematic interface.
- Treat MI210 PCIe 4.0 x16 and MI200 SDMA context as software/data-movement context, not as connector pinout, lane mapping, or signal-integrity evidence for MI250X OAM.
- A safe schematic is blocked until connector, power, PCIe/REFCLK, reset, management, mechanical, baseboard, and cooling evidence are recovered and extracted.

# Future Research

| Priority | Research task | Required output | Sources |
|---|---|---|---|
| High | Obtain and extract the missing Connector Specification or another verified MI250X OAM connector source. | Verified connector manufacturer, family, part number, pin count, pin numbering, footprint, mating height, stack-up, and full pinout. | `Wanted_Documents.md`; `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| High | Extract the OAM Specification sections relevant to connector, power, mechanical, and sideband interfaces. | Separate OAM-standard requirements from MI250X-specific unknowns. | `02_AMD_Docs/GitHub_Links.rtf`; `13_Reference_Docs/Reference_Index.rtf`; `09_AI_Notes/02_OAM_Interface.md` |
| High | Obtain or recover baseboard and mechanical specifications. | Verified board outline, connector placement, module dimensions, mounting pattern, keepouts, PCB thickness, standoff height, cooling clearance, and baseboard constraints. | `Wanted_Documents.md`; `15_Reverse_Engineering/06_Mechanical.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| High | Verify or reject Molex Mirror Mezz as the MI250X OAM connector family. | Evidence-backed connector vendor/family decision and, if applicable, exact part number and footprint data. | `13_Reference_Docs/Reference_Index.rtf`; `15_Reverse_Engineering/07_Component_ID.md`; `18_Component_Research/10_BOM.md` |
| High | Locate the front, back, and connector photos marked found. | Photo files, provenance, scale/reference method, and any verified connector markings, orientation, placement, or visible vendor clues. | `Wanted_Documents.md`; `09_AI_Notes/01_Project_Overview.md`; `09_AI_Notes/09_Unknowns.md` |
| High | Map electrical categories only after a verified pinout source is available. | Separate tables for power, ground, PCIe, REFCLK, reset, management, EEPROM/FRU, PMBus, telemetry, sensors, fan control, optional, reserved, no-connect, and vendor-specific pins. | `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `15_Reverse_Engineering/02_Power_Rails.md`; `15_Reverse_Engineering/03_Clock_Tree.md`; `15_Reverse_Engineering/04_Management.md`; `15_Reverse_Engineering/05_PCIe.md` |
| High | Determine connector electrical constraints. | Verified current rating, return-current strategy, impedance/loss constraints, clock constraints, routing rules, and sideband electrical levels. | `15_Reverse_Engineering/02_Power_Rails.md`; `15_Reverse_Engineering/03_Clock_Tree.md`; `15_Reverse_Engineering/05_PCIe.md`; `18_Component_Research/08_PCIe_Retimers.md` |
| Medium | Update the BOM after connector confirmation. | Move the OAM mating connector and any related hardware from `Unknown` or `Candidate` to `Verified` only after manufacturer, family, part number, and constraints are sourced. | `18_Component_Research/10_BOM.md`; `15_Reverse_Engineering/07_Component_ID.md` |

# Sources

- `AI_PROJECT_CONTEXT.md` - Defines the project goal, evidence labels, and rule that pinouts should only be marked verified when supported by documentation.
- `AI_TASKS.md` - Lists OAM connector pinout as a high-priority engineering unknown and includes future connector-related KiCad tasks.
- `README.md` - States the public-evidence workflow and says undocumented behavior should be tracked as open questions rather than assumed.
- `Wanted_Documents.md` - Tracks found and missing OAM, mechanical, baseboard, connector, PCIe, REFCLK, power, cooling, and photo evidence.
- `02_AMD_Docs/README.md` - States that the OAM link is useful for mechanical drawings, connector specification, and power specification.
- `02_AMD_Docs/GitHub_Links.rtf` - Links the official Open Accelerator Module specification and describes its connector, mechanical, and power relevance.
- `13_Reference_Docs/README.rtf` - Describes the MI250X research library, planned photos/mechanical/teardown/PCB-analysis folders, and Mirror Mezz connector documentation as a main reference.
- `13_Reference_Docs/Reference_Index.rtf` - Indexes OAM/OCP references and Molex Mirror Mezz references.
- `13_Reference_Docs/Component_Index.rtf` - Provides component-confidence context for the repository and reinforces that component claims need source support.
- `13_Reference_Docs/ROCm/Overview.md` - Identifies MI250 and MI250X as OCP Accelerator Modules and provides MI210/MI200 PCIe context that is not a connector pinout.
- `09_AI_Notes/01_Project_Overview.md` - Records the project evidence workflow and local photo/PDF limitations.
- `09_AI_Notes/02_OAM_Interface.md` - Summarizes OAM interface evidence and connector/mechanical/baseboard gaps.
- `09_AI_Notes/03_PCIe_Interface.md` - Summarizes PCIe lane mapping, sideband, routing, and REFCLK gaps.
- `09_AI_Notes/04_Power_Architecture.md` - Summarizes power-pin, power-rail, and OAM power-specification gaps.
- `09_AI_Notes/05_Clock_Architecture.md` - Summarizes REFCLK and clock-interface gaps.
- `09_AI_Notes/06_Management_Controller.md` - Summarizes management, firmware, health, bus, and sideband gaps.
- `09_AI_Notes/07_Cooling.md` - Summarizes cooling, heatsink, baseboard-photo, and thermal-guideline gaps.
- `09_AI_Notes/08_Mechanical.md` - Summarizes mechanical connector, board outline, mounting, keepout, and Mirror Mezz reference gaps.
- `09_AI_Notes/09_Unknowns.md` - Consolidates missing specifications, photo location gaps, and invalid/unreadable PDF limitations.
- `09_AI_Notes/10_Design_Checklist.md` - States that schematic capture and PCB layout must wait for connector, PCIe/REFCLK, power, management, mechanical, baseboard, and high-speed constraints.
- `15_Reverse_Engineering/README.md` - Defines the reverse-engineering goal to identify required interfaces, separate OAM-standard and AMD-specific features, and identify undocumented hardware.
- `15_Reverse_Engineering/01_OAM_Pin_Mapping.md` - Main connector, pinout, signal-category, OAM-vs-AMD-specific, and unknown tracking source.
- `15_Reverse_Engineering/02_Power_Rails.md` - Current power-pin, ground-pin, rail, sequencing, telemetry, and PMBus gaps.
- `15_Reverse_Engineering/03_Clock_Tree.md` - Current REFCLK, clock-interface, jitter, skew, termination, and reset-clock gaps.
- `15_Reverse_Engineering/04_Management.md` - Current management-bus, EEPROM, PMBus, firmware, health, and sensor gaps.
- `15_Reverse_Engineering/05_PCIe.md` - Current PCIe lane, sideband, REFCLK, reset, routing, and enumeration gaps.
- `15_Reverse_Engineering/06_Mechanical.md` - Current mechanical connector placement, pitch, mating-height, stack-up, keepout, photo, and baseboard gaps.
- `15_Reverse_Engineering/07_Component_ID.md` - Lists Molex Mirror Mezz as a low-confidence connector reference and OAM connectors as an unknown component category.
- `15_Reverse_Engineering/08_Bringup.md` - Records reset, clock startup, PCIe enumeration, power, and management bring-up dependencies as undocumented.
- `15_Reverse_Engineering/09_Block_Diagram.md` - Shows the OAM connector as an undocumented architecture block with power, reset, sideband, clock, management, and PCIe dependencies.
- `15_Reverse_Engineering/10_Minimal_Carrier.md` - Describes the OAM connector as required only after connector type, pin count, pinout, and mechanical stack-up are verified.
- `17_System_Architecture/02_System_Block_Diagram.md` - Shows OAM connector, clock, power, management, sensors, fan, cooling, PCIe, and optional switch/retimer blocks with details undocumented.
- `17_System_Architecture/03_Minimal_Carrier_Requirements.md` - Lists OAM connector implementation and signal classification as schematic blockers.
- `18_Component_Research/README.md` - Defines the component-research workflow and states that connector part selection must wait for sourced evidence.
- `18_Component_Research/02_Power_Converters.md` - Records connector power-pin and ground-pin gaps that affect power design.
- `18_Component_Research/03_Clock_Generators.md` - Records REFCLK and clock pin assignment gaps at the connector.
- `18_Component_Research/04_EEPROM_FRU.md` - Records EEPROM/FRU requirement and OAM pin mapping as unresolved.
- `18_Component_Research/05_Management_MCU.md` - Records management bus and sideband ownership as unresolved.
- `18_Component_Research/06_Temperature_Sensors.md` - Records sensor and telemetry connector-level requirements as unresolved.
- `18_Component_Research/07_Fan_Control.md` - Records fan-control and cooling-control connector-level requirements as unresolved.
- `18_Component_Research/08_PCIe_Retimers.md` - Records PCIe lane, REFCLK, reset, sideband, and signal-integrity gaps.
- `18_Component_Research/10_BOM.md` - Tracks MI250X OAM mating connector as unknown and Molex Mirror Mezz as a candidate reference only.