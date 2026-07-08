# Purpose

Research REFCLK, clock generators, oscillators, PLLs, clock buffers, PCIe clocks, synchronization, jitter, skew, and clock distribution for an open-source AMD Instinct MI250X OAM carrier board using only repository information.

This document is not a clock-tree design, PCIe routing guide, oscillator recommendation, PLL recommendation, schematic source, or purchasable BOM. The repository does not currently contain verified MI250X OAM clock frequency, REFCLK topology, REFCLK source, clock-generator part number, oscillator part number, PLL requirement, clock-buffer part number, jitter budget, skew budget, spread-spectrum rule, synchronization scheme, AC-coupling rule, termination rule, clock-routing constraint, or OAM clock pin assignment. Sources: `15_Reverse_Engineering/03_Clock_Tree.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `18_Component_Research/10_BOM.md`.

# Verified

Only facts directly supported by repository documents are included here.

| Topic | Verified repository fact | Sources |
|---|---|---|
| Project evidence workflow | The repository is organized as a reverse-engineering knowledge base where unknown behavior is tracked rather than assumed. | `README.md`; `AI_TASKS.md` |
| REFCLK document gap | `REFCLK Guide` is marked missing under PCIe. | `Wanted_Documents.md`; `09_AI_Notes/05_Clock_Architecture.md`; `15_Reverse_Engineering/03_Clock_Tree.md` |
| PCIe routing document gap | `PCIe Routing Guide` is marked missing. | `Wanted_Documents.md`; `09_AI_Notes/03_PCIe_Interface.md`; `15_Reverse_Engineering/05_PCIe.md` |
| Clock-tree research scope | The clock-tree note is intended to document required clock sources, reference clocks, clock buffers, and clock distribution paths used by MI250X. | `15_Reverse_Engineering/03_Clock_Tree.md` |
| PCIe research scope | The PCIe note is intended to document PCIe lane count, reference clocks, reset signals, enumeration requirements, and optional PCIe switches. | `15_Reverse_Engineering/05_PCIe.md` |
| Component-identification scope | Component identification lists clock generators as a component category to identify. | `15_Reverse_Engineering/07_Component_ID.md`; `18_Component_Research/10_BOM.md` |
| Project hardware goal | Reliable clock generation is listed as a hardware goal. | `17_System_Architecture/01_System_Goals.md`; `18_Component_Research/README.md` |
| Current clock unknown | Clock topology is listed as a current high-priority engineering unknown. | `AI_TASKS.md`; `README.md` |
| System diagram status | The system block diagram shows a Clock Subsystem connected to the OAM connector, with REFCLK source, frequency, and topology undocumented. | `17_System_Architecture/02_System_Block_Diagram.md`; `15_Reverse_Engineering/09_Block_Diagram.md` |
| Block diagram clock source | The reverse-engineering block diagram includes a Clock Source block labeled REFCLK etc. and marks it unknown. | `15_Reverse_Engineering/09_Block_Diagram.md` |
| Minimal carrier status | Minimal carrier requirements list reference clocks as required only after source, frequency, topology, jitter, and routing rules are verified. | `15_Reverse_Engineering/10_Minimal_Carrier.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| Bring-up dependency | Bring-up notes list clock startup as a dependency before reset release and PCIe enumeration, while clock prerequisites remain undocumented. | `15_Reverse_Engineering/08_Bringup.md`; `15_Reverse_Engineering/03_Clock_Tree.md` |
| PCIe context | MI210 is described as a PCIe 4.0 x16 card, and MI200 SDMA engines are described as tuned for PCIe 4.0 x16. | `13_Reference_Docs/ROCm/Overview.md`; `15_Reverse_Engineering/05_PCIe.md` |
| MI250X module context | MI250 and MI250X are described as OCP Accelerator Modules with two GCDs and 128 GB total memory. | `13_Reference_Docs/ROCm/Overview.md`; `15_Reverse_Engineering/07_Component_ID.md` |
| BOM status | `18_Component_Research/10_BOM.md` tracks PCIe REFCLK source, clock generator, oscillator, and clock buffer as unknown component categories. | `18_Component_Research/10_BOM.md` |

# Candidate Components

No clock component is verified as selected, required, or present. The table below records only repository-supported candidate categories.

| Component or category | Manufacturer | Part number | Status | Repository-supported information | Design position | Sources |
|---|---|---|---|---|---|---|
| PCIe REFCLK source | Unknown | Unknown | Unknown category | A minimal carrier must provide whatever reference clocks are required once verified, and the REFCLK Guide is missing. | Do not choose source, frequency, topology, or electrical standard yet. | `Wanted_Documents.md`; `15_Reverse_Engineering/03_Clock_Tree.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| Clock generator | Unknown | Unknown | Unknown category | Clock generators are listed as a component category to identify and as an unknown BOM category. | Do not select a clock generator until part number, input source, outputs, power rails, configuration method, and constraints are verified. | `15_Reverse_Engineering/07_Component_ID.md`; `18_Component_Research/10_BOM.md`; `18_Component_Research/README.md` |
| Oscillator | Unknown | Unknown | Unknown category | Oscillator research is part of the clock-generator component scope, but no oscillator requirement is documented. | Do not select oscillator frequency, tolerance, output standard, voltage, package, or part number. | `15_Reverse_Engineering/03_Clock_Tree.md`; `18_Component_Research/10_BOM.md`; `18_Component_Research/README.md` |
| Clock buffer | Unknown | Unknown | Unknown category | Clock buffers are included in the clock-tree research scope and unknown BOM categories. | Do not select fanout count, output standard, skew, additive jitter, or part number. | `15_Reverse_Engineering/03_Clock_Tree.md`; `18_Component_Research/10_BOM.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| PLL | Unknown | Unknown | Unknown category | No readable local source documents a verified PLL requirement or PLL part number. | Do not add a PLL unless a verified clocking source proves it is required. | `15_Reverse_Engineering/03_Clock_Tree.md`; `18_Component_Research/10_BOM.md` |
| PCIe switch or retimer clocking support | Unknown | Unknown | Unknown dependency | PCIe switch, retimer, and related clocking needs are undocumented, and no readable source proves a switch or retimer is required. | Do not add clocking circuitry for switches or retimers until topology and signal-integrity evidence require it. | `18_Component_Research/08_PCIe_Retimers.md`; `15_Reverse_Engineering/05_PCIe.md`; `17_System_Architecture/02_System_Block_Diagram.md` |

# Unknown

- **Unknown:** REFCLK frequency, source, topology, electrical standard, spread-spectrum requirement, termination, AC-coupling, connector pins, and routing constraints. Sources: `15_Reverse_Engineering/03_Clock_Tree.md`; `09_AI_Notes/05_Clock_Architecture.md`; `Wanted_Documents.md`.
- **Unknown:** Whether REFCLK is supplied by the host, baseboard, carrier, OAM module, clock generator, oscillator, buffer, PLL, or another source. Sources: `15_Reverse_Engineering/03_Clock_Tree.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`.
- **Unknown:** Clock generator manufacturer, part number, input source, output count, output standards, configuration method, power rails, package, programming interface, and validation method. Sources: `15_Reverse_Engineering/07_Component_ID.md`; `18_Component_Research/10_BOM.md`.
- **Unknown:** Oscillator manufacturer, part number, frequency, tolerance, output standard, supply rail, enable behavior, package, and placement. Sources: `15_Reverse_Engineering/03_Clock_Tree.md`; `18_Component_Research/10_BOM.md`.
- **Unknown:** PLL requirement, location, part number, input/output frequencies, bandwidth, jitter behavior, configuration method, and whether a PLL is needed at all. Sources: `15_Reverse_Engineering/03_Clock_Tree.md`; `18_Component_Research/10_BOM.md`.
- **Unknown:** Clock-buffer requirement, fanout count, output standard, additive jitter, skew, enable behavior, power rails, topology, and part number. Sources: `15_Reverse_Engineering/03_Clock_Tree.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`.
- **Unknown:** PCIe clock requirements for MI250X OAM at the connector level, including REFCLK pins, reset interaction, sideband interaction, and enumeration timing. Sources: `15_Reverse_Engineering/05_PCIe.md`; `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `15_Reverse_Engineering/08_Bringup.md`.
- **Unknown:** Jitter budget, allowed additive jitter, skew budget, clock length-matching constraints, and clock-quality validation criteria. Sources: `09_AI_Notes/05_Clock_Architecture.md`; `18_Component_Research/08_PCIe_Retimers.md`; `09_AI_Notes/10_Design_Checklist.md`.
- **Unknown:** Synchronization scheme between host, carrier, OAM module, PCIe link, management hardware, and future multi-module configurations. Sources: `15_Reverse_Engineering/03_Clock_Tree.md`; `17_System_Architecture/04_Future_Expansion.md`.
- **Unknown:** Whether any non-PCIe clocks are required by MI250X OAM, management hardware, firmware hardware, sensors, fans, retimers, switches, or other carrier subsystems. Sources: `09_AI_Notes/05_Clock_Architecture.md`; `15_Reverse_Engineering/04_Management.md`; `18_Component_Research/08_PCIe_Retimers.md`.
- **Unknown:** Which clock requirements are OAM-defined, AMD-specific to MI250X, baseboard-specific, host-topology-specific, or implementation-specific. Sources: `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `15_Reverse_Engineering/03_Clock_Tree.md`; `15_Reverse_Engineering/10_Minimal_Carrier.md`.

# Design Implications

- Do not select clock generators, oscillators, PLLs, clock buffers, termination networks, AC-coupling components, fanout topology, or synchronization topology from the current repository alone.
- Do not route PCIe REFCLK or assign clock pins until the REFCLK guide, PCIe routing guide, OAM connector pinout, and baseboard requirements are verified.
- Treat `PCIe Gen4` and `reliable clock generation` as project goals, not as complete clocking specifications.
- Treat MI210 PCIe 4.0 x16 and MI200 SDMA information as software/data-movement context, not as an MI250X OAM clocking specification.
- Do not assume a standard PCIe REFCLK frequency, clock electrical standard, spread-spectrum setting, jitter budget, skew budget, or reset-clock timing from general PCIe knowledge.
- Keep clock, PCIe, power, reset, connector, management, retimer, and bring-up documents linked because reset release and PCIe enumeration may depend on verified clock startup.
- Defer multi-module clock fanout and synchronization until the one-module REFCLK and host-interface requirements are verified.

# Future Research

| Priority | Research task | Required output | Sources |
|---|---|---|---|
| High | Obtain and extract the REFCLK Guide. | Verified REFCLK frequency, topology, source, electrical standard, jitter budget, skew budget, spread-spectrum rule, termination, AC-coupling, and routing requirements. | `Wanted_Documents.md`; `15_Reverse_Engineering/03_Clock_Tree.md`; `09_AI_Notes/05_Clock_Architecture.md` |
| High | Obtain and extract the PCIe Routing Guide. | Verified PCIe clock routing, length matching, loss, impedance, skew, termination, validation, and signal-integrity constraints. | `Wanted_Documents.md`; `15_Reverse_Engineering/05_PCIe.md`; `18_Component_Research/08_PCIe_Retimers.md` |
| High | Obtain verified OAM connector and baseboard clock information. | Verified REFCLK pins, clock-related sideband pins, host/baseboard clock ownership, and OAM-defined versus AMD-specific classification. | `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `18_Component_Research/01_OAM_Connector.md`; `15_Reverse_Engineering/10_Minimal_Carrier.md` |
| High | Determine reset-clock-power timing. | Verified sequence for standby power, main power, clock startup, Power Good, reset release, and PCIe enumeration. | `15_Reverse_Engineering/08_Bringup.md`; `15_Reverse_Engineering/02_Power_Rails.md`; `18_Component_Research/02_Power_Converters.md` |
| High | Determine whether clock components are required. | Verified need or non-need for oscillator, clock generator, PLL, clock buffer, and related passives. | `15_Reverse_Engineering/03_Clock_Tree.md`; `18_Component_Research/10_BOM.md`; `18_Component_Research/README.md` |
| Medium | Identify clock components only after requirements are known. | Verified manufacturer, part number, package, power rail, output standard, jitter/skew performance, configuration method, and BOM status for any required clock component. | `15_Reverse_Engineering/07_Component_ID.md`; `18_Component_Research/10_BOM.md` |
| Medium | Define scale-out clocking after one-module clocking is verified. | Verified fanout, synchronization, and clock ownership approach for two-, four-, and eight-module goals if needed. | `17_System_Architecture/01_System_Goals.md`; `17_System_Architecture/04_Future_Expansion.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| Medium | Add bring-up validation steps after clock requirements are sourced. | Clock-valid checks, reset-release checks, PCIe enumeration checks, and measurement points tied to verified clock nets. | `15_Reverse_Engineering/08_Bringup.md`; `AI_TASKS.md`; `09_AI_Notes/10_Design_Checklist.md` |

# Sources

- `README.md` - States the evidence workflow and that undocumented behavior should be tracked as an open question rather than assumed.
- `AI_TASKS.md` - Lists clock topology as a high-priority unknown and includes clock sheet, clock routing, and clock validation tasks.
- `Wanted_Documents.md` - Marks `REFCLK Guide` and `PCIe Routing Guide` as missing.
- `09_AI_Notes/03_PCIe_Interface.md` - Summarizes PCIe and REFCLK evidence gaps.
- `09_AI_Notes/05_Clock_Architecture.md` - Summarizes missing REFCLK frequency, topology, source, fanout, jitter budget, AC-coupling, termination, and enable/reset relationships.
- `09_AI_Notes/10_Design_Checklist.md` - States that PCIe/REFCLK routing and high-speed constraints need verification before schematic capture and PCB layout.
- `13_Reference_Docs/ROCm/Overview.md` - Provides MI210 PCIe 4.0 x16 and MI200 SDMA context; does not provide MI250X OAM clocking requirements.
- `15_Reverse_Engineering/01_OAM_Pin_Mapping.md` - Records REFCLK, clocks, and OAM connector clock pin assignments as undocumented.
- `15_Reverse_Engineering/02_Power_Rails.md` - Records power sequencing and clock-startup dependencies as unresolved.
- `15_Reverse_Engineering/03_Clock_Tree.md` - Main clock evidence document for REFCLK, clock sources, clock buffers, routing, jitter, skew, synchronization, and unknowns.
- `15_Reverse_Engineering/05_PCIe.md` - Records PCIe REFCLK, sideband, enumeration, routing, and signal-integrity gaps.
- `15_Reverse_Engineering/07_Component_ID.md` - Lists clock generators as an unknown component category.
- `15_Reverse_Engineering/08_Bringup.md` - Records clock startup, reset sequence, and PCIe enumeration as bring-up dependencies with undocumented hardware details.
- `15_Reverse_Engineering/09_Block_Diagram.md` - Shows a clock source block with REFCLK marked unknown.
- `15_Reverse_Engineering/10_Minimal_Carrier.md` - Records reference clocks and reset signals as required only after source, frequency, topology, jitter, and routing rules are verified.
- `17_System_Architecture/01_System_Goals.md` - Lists reliable clock generation and PCIe Gen4 as hardware goals.
- `17_System_Architecture/02_System_Block_Diagram.md` - Shows a Clock Subsystem connected to the OAM connector, with REFCLK source, frequency, and topology undocumented.
- `17_System_Architecture/03_Minimal_Carrier_Requirements.md` - Lists REFCLK frequency, source, topology, clock generator, oscillator, and buffer requirements as unknown.
- `17_System_Architecture/04_Future_Expansion.md` - Records future one-, two-, four-, and eight-module goals that may affect later clock fanout and synchronization research.
- `18_Component_Research/README.md` - Defines clock generator, buffer, oscillator, REFCLK, jitter, skew, fanout, and termination as component research scope.
- `18_Component_Research/01_OAM_Connector.md` - Records REFCLK pins and connector clock details as unknown.
- `18_Component_Research/02_Power_Converters.md` - Records reset-clock-power timing as unresolved.
- `18_Component_Research/08_PCIe_Retimers.md` - Records REFCLK, jitter, skew, routing, and signal-integrity gaps.
- `18_Component_Research/10_BOM.md` - Tracks PCIe REFCLK source, clock generator, oscillator, and clock buffer as unknown component categories.