# Mechanical

# Purpose

Create a mechanical engineering reference for the AMD Instinct MI250X OAM carrier-board effort using only repository-supported evidence. This notebook covers module dimensions, connector locations, mounting holes, PCB thickness, cooling envelope, weight, heatsink, keepouts, connector height, mechanical tolerances, photographs, drawings, and specifications.

This file is not a board outline, assembly drawing, connector footprint, mechanical CAD source, heatsink design, or cooling-envelope approval. No dimensions are estimated from photos, names, indexed references, or unrelated standards.

# Verified

Only facts directly supported by readable repository documents are listed as `Verified`.

| Topic | Verified repository fact | Sources |
|---|---|---|
| Evidence rule | The project workflow tracks undocumented behavior as open questions instead of assumptions. | `README.md`; `AI_TASKS.md` |
| Target hardware | The carrier project targets AMD Instinct MI250X OAM modules, and MI250/MI250X are documented as OCP Accelerator Modules. | `README.md`; `13_Reference_Docs/ROCm/Overview.md`; `15_Reverse_Engineering/07_Component_ID.md` |
| OAM specification link | The repository tracks `https://github.com/oam-dev/spec` as the official Open Accelerator Module specification source. | `02_AMD_Docs/GitHub_Links.rtf`; `09_AI_Notes/02_OAM_Interface.md`; `15_Reverse_Engineering/01_OAM_Pin_Mapping.md` |
| Mechanical relevance of OAM link | The OAM specification link is described as useful for mechanical drawings, connector specification, and power specification. | `02_AMD_Docs/GitHub_Links.rtf`; `02_AMD_Docs/README.md`; `15_Reverse_Engineering/01_OAM_Pin_Mapping.md` |
| OAM document tracking | `Wanted_Documents.md` marks OAM Specification as found. | `Wanted_Documents.md`; `09_AI_Notes/02_OAM_Interface.md`; `15_Reverse_Engineering/01_OAM_Pin_Mapping.md` |
| Missing mechanical documents | `Wanted_Documents.md` marks Mechanical Specification, Baseboard Specification, and Connector Specification as not found. | `Wanted_Documents.md`; `09_AI_Notes/08_Mechanical.md`; `15_Reverse_Engineering/01_OAM_Pin_Mapping.md` |
| Missing thermal document | `Wanted_Documents.md` marks OAM Thermal Guidelines as not found. | `Wanted_Documents.md`; `09_AI_Notes/07_Cooling.md`; `18_Component_Research/07_Fan_Control.md` |
| Photo tracking | Front, back, and connector photos are marked found; heatsink and baseboard photos are not marked found. | `Wanted_Documents.md`; `09_AI_Notes/08_Mechanical.md`; `18_Component_Research/01_OAM_Connector.md` |
| Local photo gap | Repository notes state that no image files are currently present and that the front, back, and connector photos marked found are not present as readable image files in the repository. | `README.md`; `09_AI_Notes/01_Project_Overview.md`; `09_AI_Notes/09_Unknowns.md` |
| Planned photo evidence | The reference-library README describes planned high-resolution photographs of PCB, heatsink, package, connectors, and related items. | `13_Reference_Docs/README.rtf`; `13_Reference_Docs/README.md` |
| Planned mechanical evidence | The reference-library README describes planned mechanical measurements and dimensions. | `13_Reference_Docs/README.rtf`; `13_Reference_Docs/README.md` |
| Planned teardown and PCB-analysis evidence | The reference-library README describes planned teardown photos and board analysis areas. | `13_Reference_Docs/README.rtf`; `13_Reference_Docs/README.md` |
| Indexed OAM/OCP references | OAM Base Spec, OCP Accelerator Spec, Universal Baseboard, and OAI EXP are indexed under OCP/OAM references. | `13_Reference_Docs/Reference_Index.rtf`; `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `18_Component_Research/01_OAM_Connector.md` |
| Indexed connector references | Mirror Mezz Datasheet, Mirror Mezz Brochure, and Mirror Mezz Product Guide are indexed under Molex. | `13_Reference_Docs/Reference_Index.rtf`; `09_AI_Notes/08_Mechanical.md`; `18_Component_Research/01_OAM_Connector.md` |
| Mirror Mezz limitation | Molex Mirror Mezz is a candidate connector reference only; no readable local source confirms Mirror Mezz as the MI250X OAM connector. | `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `15_Reverse_Engineering/07_Component_ID.md`; `18_Component_Research/01_OAM_Connector.md` |
| Indexed cooling references | Cold Plate Requirements, Cold Plate Development, Rack Manifold, Reservoir & Pumping Unit, Water Cooling, Glycol Cooling, and Immersion Cooling are indexed. | `13_Reference_Docs/Reference_Index.rtf`; `09_AI_Notes/07_Cooling.md`; `18_Component_Research/07_Fan_Control.md` |
| Connector mechanical gap | The OAM pin-mapping reference states that module dimensions, connector coordinates, mounting pattern, keepouts, PCB thickness, standoff height, and mating height are undocumented. | `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `09_AI_Notes/08_Mechanical.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| Cooling mechanical gap | Thermal design power, cold plate or heatsink interface, airflow/coolant requirements, thermal keepouts, mounting force, fan-control responsibility, and sensor placement are undocumented. | `09_AI_Notes/07_Cooling.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `18_Component_Research/07_Fan_Control.md` |
| Layout gating | PCB layout should wait for mechanical, connector, cooling, and high-speed routing constraints because local readable files do not provide those details. | `09_AI_Notes/10_Design_Checklist.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `15_Reverse_Engineering/10_Minimal_Carrier.md` |
| Cooling intent | System goals include a replaceable cooling solution, and the system BOM states air cooling initially with future liquid-cooling possibility. | `17_System_Architecture/01_System_Goals.md`; `20_System_BOM/GPU_Subsystem.md`; `20_System_BOM/Cooling.md` |
| Mechanical reverse-engineering status | `AI_TASKS.md` lists reverse engineering mechanical dimensions as a Phase 4 task and board outline and connector placement as Phase 6 layout tasks. | `AI_TASKS.md` |

# Source Availability

| Source category | Repository status | Mechanical information available now | Mechanical information still missing | Sources |
|---|---|---|---|---|
| OAM Specification | Link / tracked source | Identified as relevant to mechanical drawings, connector specification, and power specification. | Extracted mechanical drawings, dimensions, datum scheme, connector coordinates, mounting pattern, stack-up, keepouts, and tolerances are not present in readable local files. | `02_AMD_Docs/GitHub_Links.rtf`; `02_AMD_Docs/README.md`; `15_Reverse_Engineering/01_OAM_Pin_Mapping.md` |
| Mechanical Specification | Marked not found | None. | Module dimensions, mounting, PCB thickness, standoff height, keepouts, connector height, and tolerances. | `Wanted_Documents.md`; `09_AI_Notes/08_Mechanical.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| Baseboard Specification | Marked not found | None. | Baseboard outline, connector placement assumptions, mounting interface, baseboard keepouts, power-entry mechanical constraints, and integration envelope. | `Wanted_Documents.md`; `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| Connector Specification | Marked not found | None. | Connector manufacturer, family, part number, footprint, pitch, pin count, mating height, stack-up, mechanical envelope, and retention requirements. | `Wanted_Documents.md`; `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `18_Component_Research/01_OAM_Connector.md` |
| OAM Thermal Guidelines | Marked not found | None. | Cooling envelope, thermal keepouts, heatsink or cold-plate interface, mounting force, airflow/coolant requirements, and validation criteria. | `Wanted_Documents.md`; `09_AI_Notes/07_Cooling.md`; `18_Component_Research/07_Fan_Control.md` |
| Photos | Front, back, and connector photos marked found; heatsink and baseboard photos marked not found | Photo categories are tracked. | Usable image files, provenance, scale references, measurement method, heatsink image, and baseboard image are not present in readable local evidence. | `Wanted_Documents.md`; `README.md`; `09_AI_Notes/01_Project_Overview.md`; `09_AI_Notes/09_Unknowns.md` |
| Drawings / CAD / PCB layout | Planned but not present as design authority | The project roadmap includes future board outline, connector placement, assembly drawings, and fabrication package work. | Board outline, drawing files, CAD models, footprint files, assembly drawings, and fabrication mechanical data are not available as verified design sources. | `AI_TASKS.md`; `13_Reference_Docs/README.rtf`; `13_Reference_Docs/README.md` |
| Molex Mirror Mezz documents | Indexed only | Mirror Mezz Datasheet, Brochure, and Product Guide are named as reference leads. | Actual documents, part number, pitch, height, footprint, stack-up, and proof that Mirror Mezz is used by MI250X OAM. | `13_Reference_Docs/Reference_Index.rtf`; `15_Reverse_Engineering/07_Component_ID.md`; `18_Component_Research/01_OAM_Connector.md` |
| Cooling documents | Indexed only | Cold-plate, manifold, pump, water, glycol, and immersion-cooling reference names are listed. | Extracted cooling-envelope dimensions, cold-plate geometry, interface pressure, mounting, coolant requirements, and service envelope. | `13_Reference_Docs/Reference_Index.rtf`; `09_AI_Notes/07_Cooling.md`; `18_Component_Research/10_BOM.md` |
| Local PDFs | Present but not usable for mechanical evidence | Repository notes report invalid PDF structure for three local PDFs. | No mechanical measurements can be extracted from those PDFs in their current state. | `09_AI_Notes/09_Unknowns.md`; `README.md` |

# Measurement Tables

The tables below intentionally preserve unknowns rather than filling values from assumptions. `Verified value` is left as `Unknown` unless a readable repository document provides a direct measurement or requirement.

## Module Dimensions

| Measurement | Verified value | Datum / measurement method | Status | Sources |
|---|---:|---|---|---|
| Overall length | Unknown | Unknown | No verified dimension in readable local files. | `09_AI_Notes/08_Mechanical.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `15_Reverse_Engineering/01_OAM_Pin_Mapping.md` |
| Overall width | Unknown | Unknown | No verified dimension in readable local files. | `09_AI_Notes/08_Mechanical.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `15_Reverse_Engineering/01_OAM_Pin_Mapping.md` |
| Overall installed height | Unknown | Unknown | No verified module, connector, or cooling stack height in readable local files. | `09_AI_Notes/08_Mechanical.md`; `09_AI_Notes/07_Cooling.md`; `18_Component_Research/01_OAM_Connector.md` |
| Component-side height limit | Unknown | Unknown | No verified envelope or keepout drawing in readable local files. | `09_AI_Notes/07_Cooling.md`; `09_AI_Notes/10_Design_Checklist.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| Back-side height limit | Unknown | Unknown | No verified envelope or keepout drawing in readable local files. | `09_AI_Notes/08_Mechanical.md`; `09_AI_Notes/10_Design_Checklist.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |

## Connector Locations

| Measurement | Verified value | Datum / measurement method | Status | Sources |
|---|---:|---|---|---|
| OAM connector manufacturer | Unknown | Not a dimension; required before footprint work. | No readable local source confirms the connector manufacturer. | `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `15_Reverse_Engineering/07_Component_ID.md`; `18_Component_Research/01_OAM_Connector.md` |
| OAM connector family | Unknown | Not a dimension; required before footprint work. | Mirror Mezz is a candidate reference only, not verified as MI250X OAM. | `13_Reference_Docs/Reference_Index.rtf`; `15_Reverse_Engineering/07_Component_ID.md`; `18_Component_Research/01_OAM_Connector.md` |
| Connector part number | Unknown | Not a dimension; required before footprint work. | No connector part number is documented. | `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `18_Component_Research/01_OAM_Connector.md`; `18_Component_Research/10_BOM.md` |
| Connector center X coordinate | Unknown | Unknown | No verified connector placement drawing. | `Wanted_Documents.md`; `09_AI_Notes/08_Mechanical.md`; `15_Reverse_Engineering/01_OAM_Pin_Mapping.md` |
| Connector center Y coordinate | Unknown | Unknown | No verified connector placement drawing. | `Wanted_Documents.md`; `09_AI_Notes/08_Mechanical.md`; `15_Reverse_Engineering/01_OAM_Pin_Mapping.md` |
| Connector orientation / pin-1 datum | Unknown | Unknown | No verified connector drawing or pinout. | `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `18_Component_Research/01_OAM_Connector.md`; `09_AI_Notes/10_Design_Checklist.md` |
| Connector-to-board-edge offsets | Unknown | Unknown | No verified mechanical drawing. | `Wanted_Documents.md`; `09_AI_Notes/08_Mechanical.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |

## Mounting Holes And Support

| Measurement | Verified value | Datum / measurement method | Status | Sources |
|---|---:|---|---|---|
| Mounting hole count | Unknown | Unknown | No verified mounting pattern. | `09_AI_Notes/08_Mechanical.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `15_Reverse_Engineering/10_Minimal_Carrier.md` |
| Mounting hole diameter | Unknown | Unknown | No verified hole geometry. | `09_AI_Notes/08_Mechanical.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `15_Reverse_Engineering/10_Minimal_Carrier.md` |
| Mounting hole X/Y coordinates | Unknown | Unknown | No verified coordinate table or drawing. | `09_AI_Notes/08_Mechanical.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `09_AI_Notes/10_Design_Checklist.md` |
| Standoff height | Unknown | Unknown | No verified standoff or stack-up requirement. | `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `09_AI_Notes/08_Mechanical.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| Retention hardware | Unknown | Unknown | No verified retention or fastener requirement. | `15_Reverse_Engineering/10_Minimal_Carrier.md`; `18_Component_Research/10_BOM.md`; `09_AI_Notes/08_Mechanical.md` |
| Mounting force | Unknown | Unknown | Cooling notes identify mounting force as undocumented. | `09_AI_Notes/07_Cooling.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `18_Component_Research/07_Fan_Control.md` |

## PCB Thickness And Stack-Up

| Measurement | Verified value | Datum / measurement method | Status | Sources |
|---|---:|---|---|---|
| Module PCB thickness | Unknown | Unknown | No verified module board thickness. | `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `09_AI_Notes/08_Mechanical.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| Carrier PCB thickness | Unknown | Unknown | No verified carrier stack-up or fabrication constraint. | `09_AI_Notes/10_Design_Checklist.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `18_Component_Research/10_BOM.md` |
| Connector stack-up | Unknown | Unknown | No verified connector stack-up or mating system. | `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `18_Component_Research/01_OAM_Connector.md`; `15_Reverse_Engineering/10_Minimal_Carrier.md` |
| Board-to-board spacing | Unknown | Unknown | No verified mating height or board spacing. | `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `09_AI_Notes/08_Mechanical.md`; `18_Component_Research/01_OAM_Connector.md` |

## Cooling Envelope And Heatsink

| Measurement | Verified value | Datum / measurement method | Status | Sources |
|---|---:|---|---|---|
| Cooling method | Unknown for MI250X OAM requirement | Unknown | System BOM states air cooled initially and future liquid cooling possible, but no OAM requirement is verified. | `20_System_BOM/GPU_Subsystem.md`; `20_System_BOM/Cooling.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| Thermal design power | Unknown | Unknown | No verified MI250X OAM thermal design power in readable local files. | `09_AI_Notes/07_Cooling.md`; `18_Component_Research/07_Fan_Control.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| Heatsink dimensions | Unknown | Unknown | Heatsink photo is marked not found and no heatsink geometry is documented. | `Wanted_Documents.md`; `09_AI_Notes/07_Cooling.md`; `18_Component_Research/10_BOM.md` |
| Cold-plate interface | Unknown | Unknown | Cold-plate references are indexed only; no local interface dimensions are extracted. | `13_Reference_Docs/Reference_Index.rtf`; `09_AI_Notes/07_Cooling.md`; `18_Component_Research/10_BOM.md` |
| Cooling envelope height | Unknown | Unknown | No verified cooling-envelope drawing or height limit. | `09_AI_Notes/07_Cooling.md`; `17_System_Architecture/02_System_Block_Diagram.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| Airflow path | Unknown for MI250X OAM requirement | Unknown | System BOM mentions high airflow ducting and front-to-rear airflow as goals, not measured MI250X OAM constraints. | `20_System_BOM/Cooling.md`; `18_Component_Research/07_Fan_Control.md`; `09_AI_Notes/07_Cooling.md` |
| Coolant requirements | Unknown | Unknown | Water, glycol, and immersion references are indexed only. | `13_Reference_Docs/Reference_Index.rtf`; `09_AI_Notes/07_Cooling.md`; `18_Component_Research/07_Fan_Control.md` |

## Weight And Handling

| Measurement | Verified value | Datum / measurement method | Status | Sources |
|---|---:|---|---|---|
| Bare module weight | Unknown | Unknown | No verified module weight. | `09_AI_Notes/08_Mechanical.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `18_Component_Research/10_BOM.md` |
| Module plus heatsink weight | Unknown | Unknown | No verified heatsink or cooling assembly weight. | `Wanted_Documents.md`; `09_AI_Notes/07_Cooling.md`; `18_Component_Research/10_BOM.md` |
| Carrier support load | Unknown | Unknown | No verified mass, fastener, retention, or shipping-load data. | `15_Reverse_Engineering/10_Minimal_Carrier.md`; `09_AI_Notes/08_Mechanical.md`; `AI_TASKS.md` |

## Keepouts

| Measurement | Verified value | Datum / measurement method | Status | Sources |
|---|---:|---|---|---|
| Module outline keepout | Unknown | Unknown | No verified module outline or keepout drawing. | `09_AI_Notes/08_Mechanical.md`; `09_AI_Notes/10_Design_Checklist.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| Connector keepout | Unknown | Unknown | No verified connector drawing, placement data, or mechanical envelope. | `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `18_Component_Research/01_OAM_Connector.md`; `09_AI_Notes/10_Design_Checklist.md` |
| Heatsink / cold-plate keepout | Unknown | Unknown | No verified heatsink, cold-plate, or thermal guideline data. | `Wanted_Documents.md`; `09_AI_Notes/07_Cooling.md`; `18_Component_Research/07_Fan_Control.md` |
| Component keepout above carrier PCB | Unknown | Unknown | No verified carrier board envelope or component-height constraints. | `09_AI_Notes/10_Design_Checklist.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `18_Component_Research/10_BOM.md` |
| Chassis / service keepout | Unknown | Unknown | No verified enclosure, cable routing, service, or installation envelope. | `AI_TASKS.md`; `17_System_Architecture/04_Future_Expansion.md`; `20_System_BOM/Cooling.md` |

## Connector Height

| Measurement | Verified value | Datum / measurement method | Status | Sources |
|---|---:|---|---|---|
| Connector mating height | Unknown | Unknown | No verified mating-height requirement. | `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `18_Component_Research/01_OAM_Connector.md`; `09_AI_Notes/08_Mechanical.md` |
| Connector body height | Unknown | Unknown | No verified connector part number or datasheet. | `13_Reference_Docs/Reference_Index.rtf`; `15_Reverse_Engineering/07_Component_ID.md`; `18_Component_Research/01_OAM_Connector.md` |
| OAM module-to-carrier spacing | Unknown | Unknown | No verified connector stack-up or standoff data. | `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `15_Reverse_Engineering/10_Minimal_Carrier.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| Connector compression / engagement allowance | Unknown | Unknown | No verified connector specification. | `Wanted_Documents.md`; `18_Component_Research/01_OAM_Connector.md`; `09_AI_Notes/10_Design_Checklist.md` |

## Mechanical Tolerances

| Tolerance category | Verified value | Datum / measurement method | Status | Sources |
|---|---:|---|---|---|
| Module outline tolerance | Unknown | Unknown | No verified mechanical drawing. | `Wanted_Documents.md`; `09_AI_Notes/08_Mechanical.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| Connector placement tolerance | Unknown | Unknown | No verified connector placement drawing or footprint. | `Wanted_Documents.md`; `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `18_Component_Research/01_OAM_Connector.md` |
| Mounting hole positional tolerance | Unknown | Unknown | No verified mounting drawing. | `09_AI_Notes/08_Mechanical.md`; `09_AI_Notes/10_Design_Checklist.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| PCB thickness tolerance | Unknown | Unknown | No verified PCB stack-up. | `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `09_AI_Notes/10_Design_Checklist.md`; `18_Component_Research/10_BOM.md` |
| Cooling interface flatness / pressure tolerance | Unknown | Unknown | No verified OAM thermal guideline or cold-plate drawing. | `Wanted_Documents.md`; `09_AI_Notes/07_Cooling.md`; `18_Component_Research/07_Fan_Control.md` |

# Inferred

| Inferred requirement or dependency | Basis | Design implication | Sources |
|---|---|---|---|
| Mechanical source acquisition is a PCB-layout blocker. | Mechanical Specification, Baseboard Specification, Connector Specification, and OAM Thermal Guidelines are missing, and the design checklist says PCB layout should wait for mechanical, connector, cooling, and high-speed constraints. | Do not create board outline, connector placement, keepouts, mounting, footprint, or 3D model from current local evidence. | `Wanted_Documents.md`; `09_AI_Notes/10_Design_Checklist.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| Connector mechanical data is inseparable from electrical pin mapping. | The connector controls physical mating plus power, ground, PCIe, clock, reset, management, sideband, and reserved pins. | Do not create a mechanical footprint before connector part number, pinout, mating height, stack-up, and current/routing constraints are known. | `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `18_Component_Research/01_OAM_Connector.md`; `15_Reverse_Engineering/10_Minimal_Carrier.md` |
| Mirror Mezz is only a research lead. | Mirror Mezz documents are indexed and listed as possible connector references, but no local source confirms Mirror Mezz as the MI250X OAM connector. | Do not use Mirror Mezz pitch, height, footprint, or keepout data unless the actual documents and MI250X relevance are verified. | `13_Reference_Docs/Reference_Index.rtf`; `15_Reverse_Engineering/07_Component_ID.md`; `18_Component_Research/01_OAM_Connector.md` |
| Cooling envelope depends on missing thermal and mechanical evidence. | OAM Thermal Guidelines, heatsink photo, baseboard photo, and extracted cold-plate data are missing. | Do not set heatsink clearance, cold-plate interface, airflow duct geometry, mounting force, or thermal keepouts from current evidence. | `Wanted_Documents.md`; `09_AI_Notes/07_Cooling.md`; `18_Component_Research/07_Fan_Control.md` |
| Expansion planning affects mechanical architecture but not first-revision measurements. | The project targets 1, 2, 4, and 8 MI250X modules over future revisions. | Keep serviceability, airflow path, chassis, cable routing, and retention in future planning, but do not invent one-module dimensions. | `17_System_Architecture/01_System_Goals.md`; `17_System_Architecture/04_Future_Expansion.md`; `AI_TASKS.md` |

# Unknown

| Requested topic | Status | What must be obtained before design use | Sources |
|---|---|---|---|
| Module dimensions | Unknown | Verified length, width, height, module outline, datum references, and drawing revision. | `09_AI_Notes/08_Mechanical.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `15_Reverse_Engineering/01_OAM_Pin_Mapping.md` |
| Connector locations | Unknown | Verified connector coordinates, orientation, pin-1 datum, board-edge offsets, and mechanical drawing. | `Wanted_Documents.md`; `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `18_Component_Research/01_OAM_Connector.md` |
| Mounting holes | Unknown | Verified hole count, diameter, coordinates, hardware, datum references, and tolerances. | `09_AI_Notes/08_Mechanical.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `09_AI_Notes/10_Design_Checklist.md` |
| PCB thickness | Unknown | Verified module PCB thickness, carrier PCB thickness constraints, stack-up rules, and tolerances. | `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `09_AI_Notes/10_Design_Checklist.md`; `18_Component_Research/10_BOM.md` |
| Cooling envelope | Unknown | Verified heatsink or cold-plate envelope, airflow/coolant requirements, thermal keepouts, and mounting force. | `Wanted_Documents.md`; `09_AI_Notes/07_Cooling.md`; `18_Component_Research/07_Fan_Control.md` |
| Weight | Unknown | Verified bare-module weight, cooling assembly weight, retention load assumptions, and handling requirements. | `09_AI_Notes/08_Mechanical.md`; `18_Component_Research/10_BOM.md`; `15_Reverse_Engineering/10_Minimal_Carrier.md` |
| Heatsink | Unknown | Verified heatsink photo, geometry, interface, fasteners, weight, airflow path, and clearance. | `Wanted_Documents.md`; `09_AI_Notes/07_Cooling.md`; `18_Component_Research/10_BOM.md` |
| Keepouts | Unknown | Verified module, connector, component, heatsink, cold-plate, chassis, and service keepout drawings. | `09_AI_Notes/08_Mechanical.md`; `09_AI_Notes/10_Design_Checklist.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| Connector height | Unknown | Verified connector mating height, body height, engagement range, board spacing, and stack-up. | `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `18_Component_Research/01_OAM_Connector.md`; `09_AI_Notes/08_Mechanical.md` |
| Mechanical tolerances | Unknown | Verified drawing tolerances for connector placement, holes, outline, PCB thickness, and thermal interface. | `Wanted_Documents.md`; `09_AI_Notes/08_Mechanical.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| Photos / drawings / specifications | Needs verification | Local copies or links with provenance, revision, retrieval date, readable content, and measurement method. | `README.md`; `13_Reference_Docs/README.md`; `09_AI_Notes/09_Unknowns.md` |

# Design Implications

| Rule | Status | Engineering implication | Sources |
|---|---|---|---|
| Do not estimate dimensions. | Inferred | Leave module dimensions, hole coordinates, connector coordinates, connector height, PCB thickness, weight, keepouts, tolerances, and cooling envelope as `Unknown` until a readable source or verified measurement exists. | `README.md`; `AI_TASKS.md`; `09_AI_Notes/10_Design_Checklist.md` |
| Do not create final mechanical CAD yet. | Inferred | Board outline, connector placement, 3D models, enclosure planning, mounting hardware, and cooling interfaces are blocked. | `09_AI_Notes/10_Design_Checklist.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `15_Reverse_Engineering/10_Minimal_Carrier.md` |
| Do not create a final connector footprint yet. | Inferred | Connector manufacturer, family, part number, pin count, footprint, mating height, stack-up, and keepouts are not verified. | `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `18_Component_Research/01_OAM_Connector.md`; `18_Component_Research/10_BOM.md` |
| Do not use photo-derived measurements without provenance. | Inferred | Photos need local files, scale references, calibration or measurement method, and source provenance before any measurement can become design input. | `Wanted_Documents.md`; `09_AI_Notes/01_Project_Overview.md`; `09_AI_Notes/08_Mechanical.md` |
| Keep thermal and mechanical work linked. | Inferred | Heatsink, cold plate, airflow, fan control, sensor placement, mounting force, keepouts, and carrier mechanics must be resolved together. | `09_AI_Notes/07_Cooling.md`; `18_Component_Research/07_Fan_Control.md`; `17_System_Architecture/02_System_Block_Diagram.md` |
| Treat system-BOM cooling goals as goals only. | Inferred | "Air cooled initially", "high airflow ducting", and "front to rear airflow" do not define MI250X OAM envelope, heatsink, or keepout dimensions. | `20_System_BOM/GPU_Subsystem.md`; `20_System_BOM/Cooling.md`; `18_Component_Research/07_Fan_Control.md` |

# Future Research

| Priority | Research task | Required output | Sources |
|---|---|---|---|
| High | Obtain and extract the OAM Specification mechanical sections. | Verified module outline, datum scheme, connector placement rules, mounting pattern, keepouts, PCB thickness or stack-up requirements, connector height, tolerances, and source revision. | `02_AMD_Docs/GitHub_Links.rtf`; `02_AMD_Docs/README.md`; `15_Reverse_Engineering/01_OAM_Pin_Mapping.md` |
| High | Obtain the missing Mechanical Specification and Baseboard Specification. | Verified carrier/baseboard mechanical interface, mounting, module support, board outline constraints, keepouts, and baseboard integration envelope. | `Wanted_Documents.md`; `09_AI_Notes/08_Mechanical.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| High | Obtain the missing Connector Specification or verified MI250X connector source. | Verified connector manufacturer, family, part number, pitch, pin count, footprint, connector coordinates, mating height, stack-up, body height, and tolerances. | `Wanted_Documents.md`; `18_Component_Research/01_OAM_Connector.md`; `15_Reverse_Engineering/07_Component_ID.md` |
| High | Locate the front, back, and connector photos marked found. | Local image files with provenance, scale/reference method, visible connector markings, orientation evidence, and measurement limits. | `Wanted_Documents.md`; `README.md`; `09_AI_Notes/09_Unknowns.md` |
| High | Obtain heatsink, baseboard, and thermal evidence. | Heatsink/baseboard photos or drawings, cooling envelope, cold-plate interface, mounting force, airflow/coolant requirements, thermal keepouts, and validation criteria. | `Wanted_Documents.md`; `09_AI_Notes/07_Cooling.md`; `13_Reference_Docs/Reference_Index.rtf` |
| Medium | Recover indexed Mirror Mezz documents and verify relevance. | Evidence-backed confirmation or rejection of Mirror Mezz as the MI250X OAM connector, with extracted dimensions only if confirmed relevant. | `13_Reference_Docs/Reference_Index.rtf`; `15_Reverse_Engineering/07_Component_ID.md`; `18_Component_Research/01_OAM_Connector.md` |
| Medium | Add mechanical provenance metadata. | Source URL, document title, document version, retrieval date, local file path, extraction date, and measurement method for every future dimension. | `13_Reference_Docs/README.md`; `02_AMD_Docs/README.md`; `README.md` |
| Medium | Build CAD and layout artifacts after measurements are verified. | Board outline, connector footprint, 3D model, mounting hardware definition, keepout layers, and assembly drawing tied to source citations. | `AI_TASKS.md`; `09_AI_Notes/10_Design_Checklist.md`; `15_Reverse_Engineering/10_Minimal_Carrier.md` |

# Sources

- `README.md` - States the public-evidence workflow, says undocumented behavior should be tracked as an open question, and notes that no image files are currently present.
- `AI_TASKS.md` - Lists rules to never invent engineering facts, Phase 4 mechanical reverse engineering, Phase 6 board outline and connector placement, and future assembly/fabrication tasks.
- `Wanted_Documents.md` - Tracks OAM, mechanical, baseboard, connector, thermal, and photo availability.
- `02_AMD_Docs/README.md` - States that the OAM link is useful for mechanical drawings, connector specification, and power specification.
- `02_AMD_Docs/GitHub_Links.rtf` - Links the official Open Accelerator Module specification and describes its mechanical, connector, and power relevance.
- `13_Reference_Docs/README.md` - Describes the local reference library and notes that many indexed entries do not have matching local files.
- `13_Reference_Docs/README.rtf` - Describes planned photos, KiCad, schematics, datasheets, mechanical measurements, teardowns, PCB analysis, and vendor documentation.
- `13_Reference_Docs/Reference_Index.rtf` - Indexes OAM/OCP, Molex Mirror Mezz, and cooling references.
- `13_Reference_Docs/ROCm/Overview.md` - Identifies MI250 and MI250X as OCP Accelerator Modules.
- `09_AI_Notes/01_Project_Overview.md` - Records the project evidence workflow and local photo/PDF limitations.
- `09_AI_Notes/02_OAM_Interface.md` - Summarizes OAM interface source availability and connector/mechanical/baseboard gaps.
- `09_AI_Notes/07_Cooling.md` - Summarizes missing thermal guidelines, cooling photos/drawings, cold-plate/heatsink geometry, mounting force, and sensor-location gaps.
- `09_AI_Notes/08_Mechanical.md` - Summarizes mechanical connector, board outline, mounting, keepout, and Mirror Mezz reference gaps.
- `09_AI_Notes/09_Unknowns.md` - Consolidates missing specifications, photo location gaps, and invalid/unreadable PDF limitations.
- `09_AI_Notes/10_Design_Checklist.md` - States schematic capture and PCB layout should wait for connector, PCIe/REFCLK, power, management, mechanical, baseboard, and high-speed constraints.
- `15_Reverse_Engineering/01_OAM_Pin_Mapping.md` - Main source for OAM connector source availability, mechanical unknowns, Mirror Mezz limitations, and pinout blockers.
- `15_Reverse_Engineering/07_Component_ID.md` - Lists MI250X as the target OAM module and Mirror Mezz as a low-confidence connector reference.
- `15_Reverse_Engineering/10_Minimal_Carrier.md` - Defines mechanical support, connector, cooling, and PCB implementation as requirements that must wait for verified data.
- `17_System_Architecture/01_System_Goals.md` - Lists OAM compliance, PCIe Gen4, power sequencing, clock generation, management, and replaceable cooling as hardware goals.
- `17_System_Architecture/02_System_Block_Diagram.md` - Shows OAM connector mechanics and cooling envelope as undocumented system blocks.
- `17_System_Architecture/03_Minimal_Carrier_Requirements.md` - Lists mechanical implementation, cooling implementation, OAM connector implementation, and PCB implementation as design blockers.
- `17_System_Architecture/04_Future_Expansion.md` - Lists future one-, two-, four-, and eight-module expansion path and improved cooling as a future improvement.
- `18_Component_Research/01_OAM_Connector.md` - Related connector research documenting unknown connector manufacturer, family, part number, mating height, stack-up, footprint, and placement.
- `18_Component_Research/07_Fan_Control.md` - Related cooling-control research documenting unknown thermal limits, heatsink/cold-plate geometry, airflow/coolant requirements, and fan-control ownership.
- `18_Component_Research/10_BOM.md` - Tracks heatsink/cold plate, cooling hardware, carrier PCB, mounting hardware, retention, and OAM connector as unresolved component categories.
- `20_System_BOM/GPU_Subsystem.md` - Records system-level intent for initial air cooling and possible future liquid cooling.
- `20_System_BOM/Cooling.md` - Records system-level cooling goals such as high airflow ducting, front-to-rear airflow, positive pressure, redundant cooling, and maintenance.