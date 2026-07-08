# Purpose

Research fan control, cooling-control ownership, PWM, tachometer feedback, airflow, thermal feedback, and cooling-related monitoring for an open-source AMD Instinct MI250X OAM carrier board using only repository-supported information.

This document is not a fan selection, airflow design, thermal simulation, cooling-loop design, schematic, or BOM. The repository does not currently contain verified fan part numbers, fan-controller part numbers, PWM frequencies, tachometer wiring, fan header pinouts, airflow targets, pressure targets, thermal limits, cooling-loop requirements, fan-control policy, or carrier-vs-module fan-control ownership. Sources: `15_Reverse_Engineering/04_Management.md`; `09_AI_Notes/07_Cooling.md`; `15_Reverse_Engineering/06_Mechanical.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`.

# Verified

Only facts directly supported by repository documents are included here.

| Topic | Verified repository fact | Sources |
|---|---|---|
| Project evidence workflow | The repository tracks unknown behavior instead of assuming it. | `README.md`; `AI_TASKS.md` |
| Fan-control research scope | `07_Fan_Control.md` is defined as fan controller and cooling-control research in the component-research index. | `18_Component_Research/README.md` |
| Management research scope | The management note includes fan control, temperature sensors, voltage monitoring, firmware management, and health monitoring. | `15_Reverse_Engineering/04_Management.md` |
| Management interface status | Fan control is undocumented in readable local files. | `15_Reverse_Engineering/04_Management.md` |
| Thermal evidence gap | OAM Thermal Guidelines are marked missing. | `Wanted_Documents.md`; `09_AI_Notes/07_Cooling.md`; `18_Component_Research/06_Temperature_Sensors.md` |
| Cooling references | Cold Plate Requirements, Cold Plate Development, Rack Manifold, Reservoir & Pumping Unit, Water Cooling, Glycol Cooling, and Immersion Cooling are indexed. | `13_Reference_Docs/Reference_Index.rtf`; `09_AI_Notes/07_Cooling.md`; `15_Reverse_Engineering/06_Mechanical.md` |
| Photo tracking | Front, back, and connector photos are marked found; heatsink and baseboard photos are not marked found. | `Wanted_Documents.md`; `15_Reverse_Engineering/06_Mechanical.md`; `18_Component_Research/06_Temperature_Sensors.md` |
| Cooling note status | Cooling references are indexed, but local notes do not provide MI250X thermal design power, cold plate interface, mounting force, keepouts, heatsink geometry, coolant requirements, or sensor locations. | `09_AI_Notes/07_Cooling.md`; `15_Reverse_Engineering/06_Mechanical.md` |
| System diagram status | The system block diagram shows Fan Controller and Cooling System support blocks with carrier role or implementation undocumented. | `17_System_Architecture/02_System_Block_Diagram.md` |
| Minimal carrier status | A minimal carrier system must provide cooling for MI250X operation, but cooling implementation and fan-control responsibility are undocumented. | `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `09_AI_Notes/07_Cooling.md`; `15_Reverse_Engineering/06_Mechanical.md` |
| Fan controller status | Fan controller is optional until the cooling method and fan-control ownership are verified. | `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `15_Reverse_Engineering/10_Minimal_Carrier.md` |
| Component-identification status | Fan controllers are listed as undocumented component categories. | `15_Reverse_Engineering/07_Component_ID.md`; `18_Component_Research/README.md` |
| BOM status | The BOM lists Fan, Fan controller, heatsink or cold plate, reservoir / pump unit, and rack manifold as unknown cooling categories. | `18_Component_Research/10_BOM.md` |
| Health and validation references | Health Checks, System Validation, MI250 Acceptance, AMD Lab Notes, and GPU Accelerator Management Interfaces are indexed. | `13_Reference_Docs/Reference_Index.rtf`; `15_Reverse_Engineering/04_Management.md`; `15_Reverse_Engineering/08_Bringup.md` |

# Candidate Components

No fan controller, fan-control IC, PWM source, tachometer monitor, fan header, pump controller, or cooling controller is verified as selected, required, or present.

| Controller or category | Manufacturer | Part number | Status | Repository-supported information | Design position | Sources |
|---|---|---|---|---|---|---|
| Fan controller IC | Unknown | Unknown | Unknown category | Fan controllers are listed as undocumented component categories; no manufacturer, part number, interface, channel count, or electrical limits are documented. | Do not select or place a fan-controller IC until cooling method, ownership, fan type, interface, and part number are verified. | `15_Reverse_Engineering/07_Component_ID.md`; `18_Component_Research/10_BOM.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| Carrier-side fan controller | Unknown | Unknown | Unknown category | Fan controller is optional until the cooling method and fan-control ownership are verified. | Treat as a research category only, not a schematic requirement. | `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `15_Reverse_Engineering/10_Minimal_Carrier.md`; `15_Reverse_Engineering/04_Management.md` |
| Management MCU / BMC fan control | Unknown | Unknown | Unknown category | The repository does not prove a carrier-side management MCU or BMC requirement, and it does not define fan-control firmware or GPIO/PWM wiring. | Do not assign fan control to MCU/BMC until management architecture is verified. | `15_Reverse_Engineering/04_Management.md`; `18_Component_Research/05_Management_MCU.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| External chassis or host fan control | Unknown | Unknown | Unknown category | No readable local source states whether fans are controlled by the carrier, host chassis, external cooling unit, baseboard, or MI250X module. | Do not assume external fan-control ownership without a verified platform source. | `17_System_Architecture/02_System_Block_Diagram.md`; `15_Reverse_Engineering/04_Management.md`; `09_AI_Notes/07_Cooling.md` |
| Liquid-cooling support controller | Unknown | Unknown | Unknown category | Cooling references are indexed, and BOM lists reservoir / pump unit and rack manifold as unknown categories, but no pump, valve, manifold, or coolant-control requirement is extracted. | Do not add pump, valve, manifold, flow, leak, or coolant-control hardware until cooling method is verified. | `13_Reference_Docs/Reference_Index.rtf`; `09_AI_Notes/07_Cooling.md`; `18_Component_Research/10_BOM.md` |
| Fan header | Unknown | Unknown | Unknown category | No readable local source defines fan headers, pinout, voltage, current, PWM, tachometer, fault, or presence pins. | Do not add fan headers until fan requirement and electrical interface are verified. | `15_Reverse_Engineering/04_Management.md`; `15_Reverse_Engineering/07_Component_ID.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |

# Unknown

- **Unknown:** Fan quantity, fan size, connector type, fan header type, fan voltage, current, power budget, airflow target, static pressure target, acoustic requirement, redundancy requirement, and mechanical placement. Sources: `09_AI_Notes/07_Cooling.md`; `15_Reverse_Engineering/06_Mechanical.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`.
- **Unknown:** Fan-control ownership, including whether control belongs to a carrier MCU, BMC, host system, baseboard, chassis controller, external cooling system, liquid-cooling unit, or MI250X module. Sources: `15_Reverse_Engineering/04_Management.md`; `17_System_Architecture/02_System_Block_Diagram.md`; `18_Component_Research/05_Management_MCU.md`.
- **Unknown:** PWM requirement, PWM source, PWM voltage level, PWM frequency, PWM polarity, pullups, fan-header pinout, channel count, fail-safe behavior, and default duty cycle. Sources: `15_Reverse_Engineering/04_Management.md`; `15_Reverse_Engineering/07_Component_ID.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`.
- **Unknown:** Tachometer requirement, tachometer signal electrical details, fan RPM sensing, fan fault signaling, fan-present detection, fan failure reporting, and health-check use. Sources: `15_Reverse_Engineering/04_Management.md`; `15_Reverse_Engineering/07_Component_ID.md`; `18_Component_Research/05_Management_MCU.md`.
- **Unknown:** Thermal design power, thermal limits, heatsink or cold-plate geometry, cold-plate interface, mounting force, cooling envelope, thermal keepouts, airflow/coolant requirements, coolant type, and coolant-flow requirements. Sources: `Wanted_Documents.md`; `09_AI_Notes/07_Cooling.md`; `15_Reverse_Engineering/06_Mechanical.md`.
- **Unknown:** Whether liquid-cooling references imply required carrier-side pump, reservoir, manifold, coolant-flow, leak-detection, coolant-temperature, pressure, valve, or control hardware. Sources: `13_Reference_Docs/Reference_Index.rtf`; `09_AI_Notes/07_Cooling.md`; `18_Component_Research/10_BOM.md`.
- **Unknown:** Fan-controller IC manufacturer, part number, package, bus interface, channel count, PWM/tachometer limits, alert behavior, power rail, GPIO wiring, firmware requirements, and BOM status. Sources: `15_Reverse_Engineering/07_Component_ID.md`; `18_Component_Research/README.md`; `18_Component_Research/10_BOM.md`.

# Design Implications

- Do not invent cooling requirements, airflow targets, fan quantity, fan size, PWM frequency, tachometer behavior, fan-header pinout, thermal thresholds, coolant requirements, or control policy from the current repository.
- Do not select fans, fan-controller ICs, fan headers, pump controllers, valves, reservoirs, manifolds, pressure sensors, flow sensors, or coolant hardware until cooling method and ownership are verified.
- Do not assign PWM, tachometer, fan fault, fan-present, fan power, fan-control GPIO, I2C, SMBus, PMBus, telemetry, alert, or coolant-control nets from the current repository alone.
- Treat Fan Controller and Cooling System blocks in system diagrams as dependency placeholders, not verified schematic requirements.
- Treat indexed cooling references as research leads only; the index does not define MI250X airflow, liquid-cooling, or fan-control requirements.
- Keep fan-control research linked to temperature sensors, management MCU/BMC, power, mechanical, connector, and bring-up notes because thermal feedback, telemetry, management ownership, and safe operation cross subsystem boundaries.

# Future Research

| Priority | Research task | Required output | Sources |
|---|---|---|---|
| High | Obtain OAM Thermal Guidelines or another verified MI250X thermal source. | Verified cooling method, thermal limits, airflow/coolant requirements, heatsink/cold-plate interface, fan expectations, and validation criteria. | `Wanted_Documents.md`; `09_AI_Notes/07_Cooling.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| High | Determine fan-control ownership. | Verified carrier-side, module-side, baseboard-side, host-side, external cooling unit, chassis-controller, or no-carrier-fan-control responsibility. | `15_Reverse_Engineering/04_Management.md`; `17_System_Architecture/02_System_Block_Diagram.md`; `18_Component_Research/05_Management_MCU.md` |
| High | Determine whether fans or fan headers are required. | Verified fan requirement, fan quantity, fan connector/header, voltage/current, pinout, PWM/tachometer/fault/presence signals, and placement, or verified statement that carrier fans are not required. | `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `15_Reverse_Engineering/06_Mechanical.md`; `18_Component_Research/10_BOM.md` |
| High | Determine PWM and tachometer requirements. | Verified PWM source, frequency, voltage level, polarity, tachometer behavior, fan fault behavior, fan-present behavior, and monitoring owner if required. | `15_Reverse_Engineering/04_Management.md`; `15_Reverse_Engineering/07_Component_ID.md`; `18_Component_Research/05_Management_MCU.md` |
| High | Determine airflow or coolant requirements. | Verified airflow target, static pressure, ducting, coolant flow, pressure, coolant type, manifold/pump/reservoir requirements, and acceptable operating ranges. | `09_AI_Notes/07_Cooling.md`; `15_Reverse_Engineering/06_Mechanical.md`; `13_Reference_Docs/Reference_Index.rtf` |
| Medium | Determine thermal feedback path. | Verified temperature sensor, PMBus, external controller, host, module, or other feedback path used for fan or coolant control. | `18_Component_Research/06_Temperature_Sensors.md`; `15_Reverse_Engineering/04_Management.md`; `18_Component_Research/05_Management_MCU.md` |
| Medium | Locate or recover thermal and photo evidence. | Usable heatsink/baseboard/front/back/connector photos or thermal drawings with provenance and measurement method. | `Wanted_Documents.md`; `15_Reverse_Engineering/06_Mechanical.md`; `09_AI_Notes/09_Unknowns.md` |
| Medium | Identify candidate controllers only after requirements are known. | Verified manufacturer, part number, package, interface, channel count, power rail, PWM/tachometer capability, alert behavior, and BOM status for any required fan controller. | `15_Reverse_Engineering/07_Component_ID.md`; `18_Component_Research/10_BOM.md`; `17_System_Architecture/05_Component_Selection.md` |
| Medium | Add bring-up and validation fan checks after requirements are sourced. | Verified fan spin-up checks, tachometer checks, thermal feedback checks, health-check inputs, fault checks, pass/fail criteria, and logging method if required. | `AI_TASKS.md`; `15_Reverse_Engineering/08_Bringup.md`; `13_Reference_Docs/Reference_Index.rtf` |

# Sources

- `README.md` - States the evidence workflow and that undocumented behavior should be tracked rather than assumed.
- `AI_TASKS.md` - Lists fan control, thermal monitoring, cooling solution, thermal testing, sensor placement, telemetry, and validation tasks as unresolved project areas.
- `Wanted_Documents.md` - Marks OAM Thermal Guidelines, heatsink photo, baseboard photo, PMBus Controller Datasheet, and VRM Datasheet as missing.
- `13_Reference_Docs/Reference_Index.rtf` - Indexes Cold Plate Requirements, Cold Plate Development, Rack Manifold, Reservoir & Pumping Unit, Water Cooling, Glycol Cooling, Immersion Cooling, Health Checks, System Validation, MI250 Acceptance, and GPU Accelerator Management Interfaces.
- `09_AI_Notes/07_Cooling.md` - Summarizes cooling evidence and gaps, including missing OAM Thermal Guidelines, missing thermal photos/drawings, unknown cooling method, and unknown sensor locations.
- `15_Reverse_Engineering/04_Management.md` - Identifies fan control, temperature sensors, voltage monitoring, firmware management, and health monitoring as undocumented management topics.
- `15_Reverse_Engineering/06_Mechanical.md` - Records unknown cooling envelope, thermal keepout, heatsink geometry, mounting, dimensions, and baseboard evidence.
- `15_Reverse_Engineering/07_Component_ID.md` - Lists fan controllers and temperature sensors as undocumented component categories.
- `15_Reverse_Engineering/08_Bringup.md` - Records management initialization, voltage validation, health checks, and bring-up prerequisites as unresolved.
- `15_Reverse_Engineering/10_Minimal_Carrier.md` - Lists fan controller and sensors as optional until proven required.
- `17_System_Architecture/02_System_Block_Diagram.md` - Shows Fan Controller and Cooling System blocks with carrier role or implementation undocumented.
- `17_System_Architecture/03_Minimal_Carrier_Requirements.md` - Lists cooling as inferred for operation and fan controller as optional until cooling method and fan-control ownership are verified.
- `17_System_Architecture/05_Component_Selection.md` - Contains component-selection categories used only after requirements are sourced.
- `18_Component_Research/README.md` - Defines `07_Fan_Control.md` as fan controller and cooling-control research.
- `18_Component_Research/05_Management_MCU.md` - Records fan-control ownership, PWM, tachometer, fault, firmware ownership, and GPIO wiring as unresolved.
- `18_Component_Research/06_Temperature_Sensors.md` - Records thermal feedback, sensor placement, thermal monitoring, and carrier-vs-module monitoring ownership as unknown.
- `18_Component_Research/10_BOM.md` - Tracks Fan, Fan controller, heatsink or cold plate, reservoir / pump unit, and rack manifold as unknown component categories.