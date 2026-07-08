# Purpose

Research PCIe retimers, redrivers, switches, equalization, Gen4/Gen5 assumptions, and signal-integrity requirements for an open-source AMD Instinct MI250X OAM carrier board using only repository-supported information.

This document is not a PCIe topology selection, routing guide, loss budget, equalization plan, schematic, or BOM. The repository does not currently contain verified MI250X OAM PCIe generation, lane width, lane mapping, sideband pinout, retimer requirement, redriver requirement, insertion-loss budget, equalization settings, Gen5 requirement, or signal-integrity constraints. Sources: `15_Reverse_Engineering/05_PCIe.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `Wanted_Documents.md`; `18_Component_Research/README.md`.

# Verified

Only facts directly supported by repository documents are included here.

| Topic | Verified repository fact | Sources |
|---|---|---|
| PCIe research scope | The PCIe reverse-engineering note is intended to document generation, lane width, REFCLK, PERST#, WAKE#, CLKREQ#, enumeration, switches, retimers, signal integrity, OAM PCIe requirements, and AMD-specific PCIe behavior. | `15_Reverse_Engineering/05_PCIe.md` |
| Component research scope | `08_PCIe_Retimers.md` is defined as PCIe retimer and signal-conditioning research. | `18_Component_Research/README.md` |
| Missing PCIe guide | PCIe Routing Guide is marked missing. | `Wanted_Documents.md`; `15_Reverse_Engineering/05_PCIe.md`; `09_AI_Notes/03_PCIe_Interface.md` |
| Missing REFCLK guide | REFCLK Guide is marked missing. | `Wanted_Documents.md`; `15_Reverse_Engineering/03_Clock_Tree.md`; `18_Component_Research/03_Clock_Generators.md` |
| MI250X module context | MI250 and MI250X are documented as OCP Accelerator Modules with two GCDs and 128 GB total memory, exposed to software as two devices with separate 64 GB VRAM blocks. | `13_Reference_Docs/ROCm/Overview.md`; `15_Reverse_Engineering/05_PCIe.md`; `15_Reverse_Engineering/07_Component_ID.md` |
| MI210 PCIe context | MI210 is documented as a standard PCIe 4.0 x16 card with one GCD and 64 GB HBM2e. | `13_Reference_Docs/ROCm/Overview.md`; `09_AI_Notes/03_PCIe_Interface.md`; `15_Reverse_Engineering/05_PCIe.md` |
| MI200 SDMA context | MI200 SDMA engines are described as mainly tuned for PCIe 4.0 x16 and designed to operate at bandwidths up to 32 GB/s. | `13_Reference_Docs/ROCm/Overview.md`; `15_Reverse_Engineering/05_PCIe.md`; `15_Reverse_Engineering/08_Bringup.md` |
| Infinity Fabric context | On MI250X systems using Infinity Fabric, SDMA may not max out the faster interconnect. | `13_Reference_Docs/ROCm/Overview.md`; `15_Reverse_Engineering/05_PCIe.md` |
| Project hardware goal | PCIe Gen4 is listed as a hardware goal, and stable PCIe enumeration is listed as a project priority. | `17_System_Architecture/01_System_Goals.md`; `15_Reverse_Engineering/08_Bringup.md` |
| Architecture diagram status | System diagrams show Host -> PCIe -> optional PCIe Switch / Retimer -> OAM Connector -> MI250X, with switch/retimer and OAM interface details undocumented. | `17_System_Architecture/02_System_Block_Diagram.md`; `15_Reverse_Engineering/09_Block_Diagram.md` |
| Minimal carrier status | PCIe switch and PCIe retimer are optional until a verified topology, routing guide, or signal-integrity analysis requires them. | `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `15_Reverse_Engineering/10_Minimal_Carrier.md` |
| Component-identification status | PCIe switches and retimers are listed as undocumented component categories. | `15_Reverse_Engineering/07_Component_ID.md`; `18_Component_Research/README.md` |
| BOM status | PCIe switch, PCIe retimer, and PCIe redriver are listed as unknown categories. | `18_Component_Research/10_BOM.md` |

Important distinction: PCIe 4.0 x16 is verified for MI210 and MI200 SDMA context, and PCIe Gen4 is a project goal. It is not verified in the readable repository as the MI250X OAM connector generation, lane width, lane assignment, topology, or routing specification. Sources: `13_Reference_Docs/ROCm/Overview.md`; `15_Reverse_Engineering/05_PCIe.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`.

# Candidate Components

No PCIe retimer, redriver, switch, clock buffer, equalization device, or other signal-conditioning component is verified as selected, required, or present.

| Component category | Manufacturer | Part number | Status | Repository-supported information | Design position | Sources |
|---|---|---|---|---|---|---|
| PCIe retimer | Unknown | Unknown | Unknown category | Retimers are listed as undocumented, and no readable local source proves that a retimer is required for one MI250X OAM module. | Do not recommend, select, or place a retimer until topology, loss budget, lane count, generation, clocking, management, and part number are verified. | `15_Reverse_Engineering/05_PCIe.md`; `15_Reverse_Engineering/07_Component_ID.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| PCIe redriver | Unknown | Unknown | Unknown category | The BOM lists PCIe redriver as an unknown signal-conditioning category, but no redriver requirement or candidate device is documented. | Do not recommend, select, or place a redriver until verified routing or signal-integrity evidence requires one. | `18_Component_Research/10_BOM.md`; `15_Reverse_Engineering/05_PCIe.md`; `18_Component_Research/README.md` |
| PCIe switch | Unknown | Unknown | Unknown category | A PCIe switch is optional until a verified topology requires it; no readable local source proves a switch is required for one MI250X module. | Do not recommend, select, or place a switch until host topology and lane mapping are verified. | `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `15_Reverse_Engineering/05_PCIe.md`; `17_System_Architecture/02_System_Block_Diagram.md` |
| PCIe REFCLK source or clock buffer | Unknown | Unknown | Unknown dependency | Clock generators, oscillators, buffers, REFCLK topology, frequency, jitter, skew, and routing requirements are not documented. | Do not add PCIe clock support for switches, retimers, or redrivers until clock requirements are verified. | `15_Reverse_Engineering/03_Clock_Tree.md`; `18_Component_Research/03_Clock_Generators.md`; `Wanted_Documents.md` |
| AC-coupling / passives for PCIe | Unknown | Unknown | Unknown category | AC-coupling capacitor requirements, termination, impedance constraints, and routing rules are undocumented. | Do not choose values, footprints, placement, or topology from current repository evidence. | `15_Reverse_Engineering/05_PCIe.md`; `09_AI_Notes/10_Design_Checklist.md`; `Wanted_Documents.md` |

# Unknown

- **Unknown:** MI250X OAM PCIe generation, lane width, lane mapping, lane polarity rules, sideband signals, REFCLK pins, reset pins, and enumeration hardware requirements. Sources: `15_Reverse_Engineering/05_PCIe.md`; `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`.
- **Unknown:** Whether the minimal carrier connects PCIe directly to the host, through a switch, through a retimer, through a redriver, or through a baseboard-specific topology. Sources: `15_Reverse_Engineering/05_PCIe.md`; `17_System_Architecture/02_System_Block_Diagram.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`.
- **Unknown:** Whether a PCIe switch, retimer, or redriver is required for one MI250X module; all remain optional until verified topology and signal-integrity evidence require them. Sources: `15_Reverse_Engineering/05_PCIe.md`; `15_Reverse_Engineering/10_Minimal_Carrier.md`; `18_Component_Research/README.md`.
- **Unknown:** PCIe equalization requirements, link-training behavior, compliance method, eye-mask targets, insertion-loss budget, routing length limits, connector loss, via strategy, AC-coupling capacitor values, and impedance constraints. Sources: `Wanted_Documents.md`; `09_AI_Notes/03_PCIe_Interface.md`; `09_AI_Notes/10_Design_Checklist.md`.
- **Unknown:** Retimer, redriver, or switch candidate manufacturers, part numbers, packages, power rails, reference-clock needs, management buses, EEPROM needs, firmware/configuration requirements, lane counts, and reset sequencing. Sources: `15_Reverse_Engineering/07_Component_ID.md`; `18_Component_Research/10_BOM.md`; `18_Component_Research/README.md`.
- **Unknown:** Whether Gen4, Gen5, or another topology-specific requirement applies to the MI250X OAM carrier interface. Sources: `17_System_Architecture/01_System_Goals.md`; `15_Reverse_Engineering/05_PCIe.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`.
- **Unknown:** Which PCIe requirements are OAM-defined, AMD-specific for MI250X, baseboard-specific, host-topology-specific, or implementation-specific. Sources: `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `15_Reverse_Engineering/05_PCIe.md`; `Wanted_Documents.md`.

# Design Implications

- Do not recommend PCIe retimers, redrivers, switches, clock buffers, AC-coupling values, connectors, or other signal-conditioning components without verified topology and signal-integrity evidence.
- Do not route PCIe lanes, assign lane mapping, define polarity rules, choose lane width, or assign PCIe sidebands from the current repository alone.
- Treat PCIe Gen4 as a project goal and MI210/MI200 PCIe 4.0 x16 as software/data-movement context, not as a verified MI250X OAM carrier electrical requirement.
- Treat Gen5 as unknown; no readable local source identifies a Gen5 requirement.
- Do not define equalization settings, loss budgets, skew budgets, impedance constraints, AC-coupling capacitor values, retimer settings, or compliance tests until the PCIe routing and connector evidence is available.
- Keep PCIe, REFCLK, OAM connector, reset, power sequencing, management, and bring-up documents linked because enumeration depends on verified host interface, clock, reset, and power behavior.

# Future Research

| Priority | Research task | Required output | Sources |
|---|---|---|---|
| High | Obtain and extract the PCIe Routing Guide. | Verified PCIe generation, routing topology, lane mapping, loss budget, impedance, length matching, skew, equalization, AC-coupling, and validation constraints. | `Wanted_Documents.md`; `15_Reverse_Engineering/05_PCIe.md`; `09_AI_Notes/03_PCIe_Interface.md` |
| High | Obtain verified OAM connector and baseboard PCIe information. | Verified PCIe pins, sideband pins, lane order, lane width, host/baseboard topology, and OAM-defined versus AMD-specific classification. | `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `Wanted_Documents.md` |
| High | Determine whether any PCIe switch, retimer, or redriver is required. | Verified direct-connect, switch, retimer, redriver, or other topology decision with supporting signal-integrity evidence. | `15_Reverse_Engineering/05_PCIe.md`; `17_System_Architecture/02_System_Block_Diagram.md`; `15_Reverse_Engineering/10_Minimal_Carrier.md` |
| High | Determine REFCLK and reset requirements. | Verified REFCLK source, frequency, topology, electrical standard, jitter/skew constraints, PERST#, WAKE#, CLKREQ#, reset timing, and enumeration dependencies. | `Wanted_Documents.md`; `15_Reverse_Engineering/03_Clock_Tree.md`; `18_Component_Research/03_Clock_Generators.md` |
| High | Determine Gen4 and Gen5 applicability. | Verified statement of MI250X OAM carrier PCIe generation, link width, compatibility requirements, and compliance target. | `17_System_Architecture/01_System_Goals.md`; `15_Reverse_Engineering/05_PCIe.md`; `13_Reference_Docs/ROCm/Overview.md` |
| Medium | Identify signal-conditioning components only after requirements are known. | Verified manufacturer, part number, package, lane count, protocol generation, clocking, reset, management interface, equalization behavior, and BOM status for any required switch, retimer, or redriver. | `15_Reverse_Engineering/07_Component_ID.md`; `18_Component_Research/10_BOM.md`; `18_Component_Research/README.md` |
| Medium | Add bring-up and validation steps after PCIe requirements are sourced. | Verified PCIe enumeration checks, link-speed checks, lane-width checks, equalization/compliance checks, and ROCm detection checks tied to verified hardware requirements. | `15_Reverse_Engineering/08_Bringup.md`; `09_AI_Notes/10_Design_Checklist.md`; `13_Reference_Docs/ROCm/Overview.md` |
| Medium | Define scale-out topology after one-module host interface is verified. | Verified one-, two-, four-, and eight-module topology implications for switches, retimers, redrivers, signal integrity, and host links. | `17_System_Architecture/01_System_Goals.md`; `17_System_Architecture/04_Future_Expansion.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |

# Sources

- `Wanted_Documents.md` - Marks PCIe Routing Guide, REFCLK Guide, Connector Specification, Baseboard Specification, and related integration documents as missing.
- `13_Reference_Docs/ROCm/Overview.md` - Provides MI210 PCIe 4.0 x16, MI250/MI250X OAM module context, MI200 SDMA tuning for PCIe 4.0 x16, and Infinity Fabric context.
- `09_AI_Notes/03_PCIe_Interface.md` - Summarizes PCIe evidence and gaps, including missing lane mapping, routing constraints, REFCLK topology, reset signals, and sidebands.
- `09_AI_Notes/10_Design_Checklist.md` - States that PCIe/REFCLK routing and high-speed constraints need verification before schematic capture and PCB layout.
- `15_Reverse_Engineering/01_OAM_Pin_Mapping.md` - Records OAM connector PCIe lanes, sidebands, REFCLK, and pin assignments as unknown.
- `15_Reverse_Engineering/03_Clock_Tree.md` - Records REFCLK, clock routing, jitter, skew, termination, and reset-clock relationships as unknown.
- `15_Reverse_Engineering/05_PCIe.md` - Main PCIe reverse-engineering source for generation, lane width, lane mapping, REFCLK, reset, switch, retimer, and signal-integrity gaps.
- `15_Reverse_Engineering/07_Component_ID.md` - Lists PCIe switches and retimers as undocumented component categories.
- `15_Reverse_Engineering/08_Bringup.md` - Records PCIe enumeration as a bring-up objective and PCIe prerequisites as undocumented.
- `15_Reverse_Engineering/09_Block_Diagram.md` - Shows an optional PCIe Switch/Retimer block and undocumented PCIe architecture dependency.
- `15_Reverse_Engineering/10_Minimal_Carrier.md` - Treats PCIe switch and retimer as optional until verified topology or signal-integrity constraints require them.
- `17_System_Architecture/01_System_Goals.md` - Lists PCIe Gen4 as a hardware goal and stable PCIe enumeration as a project priority.
- `17_System_Architecture/02_System_Block_Diagram.md` - Shows Host -> PCIe -> optional PCIe Switch/Retimer -> OAM Connector -> MI250X with implementation details undocumented.
- `17_System_Architecture/03_Minimal_Carrier_Requirements.md` - Lists MI250X OAM PCIe generation, lane width, lane mapping, sidebands, switches, retimers, and signal-integrity rules as unknown.
- `17_System_Architecture/04_Future_Expansion.md` - Records future single-, dual-, four-, and eight-MI250X system revisions.
- `18_Component_Research/README.md` - Defines PCIe retimer and signal-conditioning research and requires component choices to wait for sourced evidence.
- `18_Component_Research/03_Clock_Generators.md` - Records REFCLK, jitter, skew, routing, and PCIe clocking gaps.
- `18_Component_Research/10_BOM.md` - Tracks PCIe switch, PCIe retimer, and PCIe redriver as unknown component categories.