# Purpose

Research carrier input-power connectors, power-entry architecture, PSU assumptions, high-current handling, ATX/server-power possibilities, cable assemblies, and connector ratings for an open-source AMD Instinct MI250X OAM carrier board using only repository-supported information.

This document is not a connector selection, PSU selection, cable-harness design, current-rating calculation, schematic source, safety approval, or purchasable BOM. The repository does not currently contain verified carrier input voltage, input current, total power budget, PSU type, ATX requirement, server-power requirement, cable-assembly requirement, connector manufacturer, connector part number, connector rating, fusing requirement, hot-swap requirement, wire gauge, busbar requirement, or baseboard power-entry architecture. Sources: `15_Reverse_Engineering/02_Power_Rails.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `18_Component_Research/10_BOM.md`; `18_Component_Research/README.md`.

# Verified

Only facts directly supported by repository documents are included here.

| Topic | Verified repository fact | Sources |
|---|---|---|
| Project evidence workflow | The repository is organized as a reverse-engineering knowledge base where undocumented behavior is tracked rather than assumed. | `README.md`; `AI_TASKS.md` |
| Target module | MI250 and MI250X are documented as OCP Accelerator Modules with two GCDs and 128 GB total memory, exposed to software as two devices with separate 64 GB VRAM blocks. | `13_Reference_Docs/ROCm/Overview.md`; `15_Reverse_Engineering/07_Component_ID.md` |
| OAM power relevance | The OAM specification link is described as useful for power specification. | `02_AMD_Docs/GitHub_Links.rtf`; `15_Reverse_Engineering/02_Power_Rails.md`; `18_Component_Research/02_Power_Converters.md` |
| Missing connector/baseboard sources | Connector Specification and Baseboard Specification are marked missing. | `Wanted_Documents.md`; `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| Missing power sources | PMBus Controller Datasheet and VRM Datasheet are marked missing. | `Wanted_Documents.md`; `15_Reverse_Engineering/02_Power_Rails.md`; `09_AI_Notes/04_Power_Architecture.md` |
| Minimal carrier power need | A minimal carrier must provide the module's required input power and ground paths once verified. | `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `15_Reverse_Engineering/10_Minimal_Carrier.md`; `15_Reverse_Engineering/02_Power_Rails.md` |
| Power implementation gap | Rail names, input voltages, current requirements, power pins, ground pins, standby rails, protection, and monitoring are not yet defined. | `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `15_Reverse_Engineering/02_Power_Rails.md` |
| Power-entry BOM status | `Carrier input-power connector` is tracked as an unknown BOM category whose purpose is to bring input power onto the carrier once baseboard power architecture is known. | `18_Component_Research/10_BOM.md`; `18_Component_Research/README.md` |
| OAM connector current-rating gap | MI250X OAM connector current rating, power-pin grouping, and current-sharing requirements are not documented. | `18_Component_Research/01_OAM_Connector.md`; `15_Reverse_Engineering/02_Power_Rails.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| Power converter report status | Carrier input-power connector, protection, hot-swap behavior, fusing, current limiting, and baseboard power architecture are documented as unknown. | `18_Component_Research/02_Power_Converters.md`; `15_Reverse_Engineering/02_Power_Rails.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| System diagram status | The system block diagram shows a Power Subsystem connected to the OAM connector while marking rails, sequencing, Power Good, and telemetry as undocumented. | `17_System_Architecture/02_System_Block_Diagram.md`; `15_Reverse_Engineering/09_Block_Diagram.md` |
| Bring-up dependency | Bring-up notes list standby power, main power, power sequencing, enable signals, Power Good signals, clock startup, reset release, and PCIe enumeration as dependencies with undocumented hardware details. | `15_Reverse_Engineering/08_Bringup.md`; `15_Reverse_Engineering/02_Power_Rails.md` |
| Current engineering unknowns | Project tasks include reverse engineering power rails, sequencing, telemetry, power-up testing, voltage validation, and cable routing. | `AI_TASKS.md`; `15_Reverse_Engineering/02_Power_Rails.md` |
| BOM guardrail | The BOM intentionally omits quantities, approved manufacturers, approved part numbers, packages, voltage/current ratings, footprints, and alternates until supported by readable source documents or verified measurements. | `18_Component_Research/10_BOM.md` |

# Candidate Components

No carrier input-power connector, PSU connector, ATX connector, EPS connector, server-power connector, CRPS connector, cable assembly, busbar, or connector rating is verified as selected, required, or present.

| Connector or category | Manufacturer | Part number | Status | Repository-supported information | Design position | Sources |
|---|---|---|---|---|---|---|
| Carrier input-power connector | Unknown | Unknown | Unknown category | The BOM tracks carrier input-power connector as an unknown category for bringing input power onto the carrier once baseboard power architecture is known. | Do not select a connector until input voltage, input current, power budget, protection, mechanical constraints, and baseboard requirements are verified. | `18_Component_Research/10_BOM.md`; `18_Component_Research/README.md`; `18_Component_Research/02_Power_Converters.md` |
| OAM connector power pins | Unknown | Unknown | Unknown implementation | Power delivery depends on verified OAM connector power and ground pins, but pin assignments and connector current rating are undocumented. | Do not assign power pins, ground pins, current sharing, or connector ratings until a verified connector/power source exists. | `18_Component_Research/01_OAM_Connector.md`; `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `15_Reverse_Engineering/02_Power_Rails.md` |
| ATX / EPS power connector | Unknown | Unknown | No verified requirement | Current power and minimal-carrier documents do not define ATX or EPS as the carrier input-power interface. | Treat ATX/EPS only as a research question, not a recommendation. | `09_AI_Notes/04_Power_Architecture.md`; `15_Reverse_Engineering/02_Power_Rails.md`; `18_Component_Research/README.md` |
| Server PSU / CRPS / server-power connector | Unknown | Unknown | No verified requirement | Current power and architecture documents do not define a server PSU, CRPS connector, rack PSU interface, or server-power connector for the carrier. | Treat server-power entry as a research question until baseboard and power-entry evidence exists. | `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `18_Component_Research/10_BOM.md`; `15_Reverse_Engineering/02_Power_Rails.md` |
| Cable assembly / harness | Unknown | Unknown | No verified requirement | Cable routing is listed as a low-priority project unknown, but no readable source defines a cable assembly, wire gauge, pinout, connector family, or current rating. | Do not design cable assemblies or harnesses until connector, current, and mechanical constraints are verified. | `AI_TASKS.md`; `18_Component_Research/10_BOM.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| High-current busbar or power blade | Unknown | Unknown | No verified requirement | Current requirements, total power budget, input voltage, return-current strategy, and power-entry architecture are undocumented. | Do not assume busbars, blades, or high-current connector families from current repository evidence. | `15_Reverse_Engineering/02_Power_Rails.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `09_AI_Notes/10_Design_Checklist.md` |
| Protection / fuse / hot-swap connector-adjacent hardware | Unknown | Unknown | Unknown category | Protection, hot-swap behavior, fusing, and current limiting are documented as unknown. | Do not select fuses, hot-swap controllers, current limiters, or protected connector schemes until requirements are sourced. | `18_Component_Research/02_Power_Converters.md`; `15_Reverse_Engineering/02_Power_Rails.md`; `09_AI_Notes/04_Power_Architecture.md` |

# Unknown

- **Unknown:** Carrier input-power connector manufacturer, family, part number, footprint, mating connector, pin count, pinout, voltage rating, current rating, derating, safety approvals, and mechanical retention. Sources: `18_Component_Research/10_BOM.md`; `18_Component_Research/README.md`; `18_Component_Research/02_Power_Converters.md`.
- **Unknown:** Whether the carrier should use ATX, EPS, PCIe auxiliary power, server PSU, CRPS, rack power, backplane power, external bench supply, cable harness, busbar, direct-wire input, or another power-entry topology. Sources: `15_Reverse_Engineering/02_Power_Rails.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `09_AI_Notes/04_Power_Architecture.md`.
- **Unknown:** Required input voltage, input-voltage range, total power budget, input current, peak current, transient current, and power margin. Sources: `15_Reverse_Engineering/02_Power_Rails.md`; `18_Component_Research/02_Power_Converters.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`.
- **Unknown:** OAM connector power-pin assignments, ground-pin assignments, return-current strategy, connector current rating, power-pin grouping, and current-sharing requirements. Sources: `18_Component_Research/01_OAM_Connector.md`; `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `15_Reverse_Engineering/02_Power_Rails.md`.
- **Unknown:** Required connector ratings for any carrier input connector, OAM connector, cable connector, PSU connector, or intermediate connector. Sources: `18_Component_Research/01_OAM_Connector.md`; `18_Component_Research/02_Power_Converters.md`; `18_Component_Research/10_BOM.md`.
- **Unknown:** Cable assembly requirements, including wire gauge, conductor count, cable length, mating connector, pinout, strain relief, shielding, thermal derating, and manufacturing method. Sources: `AI_TASKS.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `18_Component_Research/10_BOM.md`.
- **Unknown:** Protection, fusing, current limiting, hot-swap, inrush control, precharge, fault isolation, and shutdown behavior. Sources: `18_Component_Research/02_Power_Converters.md`; `15_Reverse_Engineering/02_Power_Rails.md`; `09_AI_Notes/04_Power_Architecture.md`.
- **Unknown:** Whether input-power entry is carrier-side, baseboard-side, host-side, chassis-side, rack-side, or external-supply-side. Sources: `17_System_Architecture/02_System_Block_Diagram.md`; `15_Reverse_Engineering/09_Block_Diagram.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`.
- **Unknown:** Which power-entry and connector requirements are OAM-defined, AMD-specific for MI250X, baseboard-specific, PSU-specific, chassis-specific, or implementation-specific. Sources: `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `15_Reverse_Engineering/10_Minimal_Carrier.md`; `Wanted_Documents.md`.

# Design Implications

- Do not invent connector ratings, current ratings, voltage ratings, current capacity, cable gauge, connector count, PSU type, ATX/EPS/server-power choice, busbar requirement, or cable-assembly design from the current repository alone.
- Do not select carrier input-power connectors, OAM power connector variants, cable assemblies, fuses, hot-swap controllers, current limiters, busbars, or PSU interfaces until input voltage, current, power budget, mechanical constraints, protection requirements, and baseboard power architecture are verified.
- Treat the `Carrier input-power connector` BOM row as an unresolved research category, not as a part recommendation.
- Treat ATX, EPS, CRPS/server PSU, rack power, direct-wire input, and busbar options as research questions only; no readable local source currently supports choosing one.
- Do not size copper, fuses, power pins, cables, connectors, regulators, or cooling from assumed MI250X power consumption; current requirements are not documented.
- Keep power connector research linked to OAM connector, power converters, power rails, mechanical, cooling, management, and bring-up documents because connector ratings depend on current, voltage, thermal, sequencing, and fault behavior.
- For two-, four-, and eight-module goals, do not extrapolate connector count, PSU capacity, cable routing, or rack-power architecture until the one-module power-entry requirement is verified.

# Future Research

| Priority | Research task | Required output | Sources |
|---|---|---|---|
| High | Obtain and extract OAM power and connector requirements. | Verified power pins, ground pins, input voltage, current requirements, connector current rating, current-sharing requirements, and OAM-vs-AMD-specific classification. | `02_AMD_Docs/GitHub_Links.rtf`; `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `15_Reverse_Engineering/02_Power_Rails.md` |
| High | Obtain the missing Connector Specification and Baseboard Specification. | Verified carrier/baseboard power-entry topology, connector family, pinout, mechanical constraints, mating connector, and rating requirements. | `Wanted_Documents.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `18_Component_Research/01_OAM_Connector.md` |
| High | Determine carrier input voltage and current. | Verified input voltage range, total power budget, steady-state current, peak current, transient behavior, margin, and PSU sizing basis. | `15_Reverse_Engineering/02_Power_Rails.md`; `18_Component_Research/02_Power_Converters.md`; `09_AI_Notes/04_Power_Architecture.md` |
| High | Determine protection and hot-swap requirements. | Verified fusing, current limiting, inrush control, hot-swap or no-hot-swap decision, precharge, reverse protection, and fault behavior. | `18_Component_Research/02_Power_Converters.md`; `15_Reverse_Engineering/02_Power_Rails.md`; `15_Reverse_Engineering/08_Bringup.md` |
| High | Determine whether ATX, EPS, server PSU, CRPS, rack power, cable harness, busbar, or another input topology is appropriate. | Verified power-entry topology with source evidence, connector requirements, cable requirements, and mechanical constraints. | `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `18_Component_Research/10_BOM.md`; `09_AI_Notes/04_Power_Architecture.md` |
| High | Identify input-power connector candidates only after requirements are known. | Verified manufacturer, part number, footprint, mating connector, ratings, derating rules, availability, safety approvals, and BOM status. | `18_Component_Research/10_BOM.md`; `18_Component_Research/README.md`; `09_AI_Notes/10_Design_Checklist.md` |
| Medium | Define cable assemblies after connector and current data are verified. | Verified wire gauge, conductor count, cable length, pinout, mating connectors, strain relief, derating, and assembly drawings. | `AI_TASKS.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `18_Component_Research/10_BOM.md` |
| Medium | Add power-entry validation steps to bring-up. | Pre-power inspection, continuity checks, connector temperature checks, standby validation, main-power validation, sequencing validation, Power Good validation, and fault-response validation. | `15_Reverse_Engineering/08_Bringup.md`; `AI_TASKS.md`; `09_AI_Notes/10_Design_Checklist.md` |
| Medium | Define scale-out power entry after one-module requirements are verified. | Verified power-entry architecture for dual-, four-, and eight-MI250X revisions, including PSU count, connector count, cable routing, distribution, protection, and serviceability. | `17_System_Architecture/04_Future_Expansion.md`; `AI_TASKS.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |

# Sources

- `README.md` - States the public-evidence workflow and that undocumented behavior should be tracked rather than assumed.
- `AI_TASKS.md` - Lists power-domain, power-up, voltage-validation, cable-routing, and evidence-label rules.
- `Wanted_Documents.md` - Marks Connector Specification, Baseboard Specification, PMBus Controller Datasheet, and VRM Datasheet as missing.
- `02_AMD_Docs/GitHub_Links.rtf` - Links the official Open Accelerator Module specification and describes its connector, mechanical, and power relevance.
- `09_AI_Notes/04_Power_Architecture.md` - Summarizes power input, connector, fusing, hot-plug, telemetry, PMBus, and VRM unknowns.
- `09_AI_Notes/07_Cooling.md` - Records that MI250X thermal design power is not documented locally.
- `09_AI_Notes/10_Design_Checklist.md` - States that schematic capture and PCB layout must wait for connector, power, management, mechanical, baseboard, and footprint-critical requirements.
- `13_Reference_Docs/ROCm/Overview.md` - Identifies MI250 and MI250X as OCP Accelerator Modules; provides module context but not connector ratings.
- `15_Reverse_Engineering/01_OAM_Pin_Mapping.md` - Records OAM connector power pins, ground pins, and pin assignments as unknown.
- `15_Reverse_Engineering/02_Power_Rails.md` - Main source for power rails, input voltage, current requirements, sequencing, connector dependency, fusing/hot-plug unknowns, and power research tasks.
- `15_Reverse_Engineering/07_Component_ID.md` - Lists power stages and PMBus devices as undocumented and reinforces that part numbers should not be guessed.
- `15_Reverse_Engineering/08_Bringup.md` - Records standby power, main power, sequencing, enable, Power Good, clock startup, reset release, and validation gaps.
- `15_Reverse_Engineering/09_Block_Diagram.md` - Shows power system and power/reset/sideband blocks as undocumented architecture dependencies.
- `15_Reverse_Engineering/10_Minimal_Carrier.md` - Describes minimum carrier power delivery and unresolved implementation details.
- `17_System_Architecture/02_System_Block_Diagram.md` - Shows Power Subsystem connected to OAM with rails, sequencing, Power Good, and telemetry undocumented.
- `17_System_Architecture/03_Minimal_Carrier_Requirements.md` - Lists power delivery, current, connector current rating, copper sizing, protection, and thermal design as blocked by missing requirements.
- `17_System_Architecture/04_Future_Expansion.md` - Records future single-, dual-, four-, and eight-MI250X system revisions.
- `18_Component_Research/README.md` - Defines `09_Power_Connectors.md` as carrier input-power connector, protection, current-capacity, and system-power-entry research.
- `18_Component_Research/01_OAM_Connector.md` - Records connector current rating, power-pin grouping, current sharing, and OAM connector electrical constraints as unknown.
- `18_Component_Research/02_Power_Converters.md` - Records carrier input-power connector, protection, hot-swap, fusing, current limiting, connector ratings, and baseboard power architecture as unknown.
- `18_Component_Research/10_BOM.md` - Tracks carrier input-power connector as an unknown BOM category and omits voltage/current ratings until supported by readable source documents or verified measurements.