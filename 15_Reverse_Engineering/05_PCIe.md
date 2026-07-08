# PCIe

# Purpose

| Label | Statement | Sources |
|---|---|---|
| Verified | This notebook collects repository-supported PCIe evidence for the AMD Instinct MI250X OAM carrier effort. | `README.md`; `AI_TASKS.md`; `15_Reverse_Engineering/README.md` |
| Verified | The repository requires undocumented hardware behavior to remain `Unknown` rather than becoming schematic nets, routing rules, component selections, or inferred pin assignments. | `README.md`; `AI_TASKS.md`; `09_AI_Notes/10_Design_Checklist.md` |
| Verified | No readable repository document provides verified MI250X OAM PCIe generation, lane count, lane routing, lane mapping, REFCLK frequency, REFCLK topology, PERST# behavior, CLKREQ# behavior, WAKE# behavior, lane polarity rules, retimer requirement, switch requirement, equalization settings, loss budget, AC-coupling rule, impedance, or length-matching constraint. | `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `18_Component_Research/08_PCIe_Retimers.md` |

# Verified Evidence

| Topic | Verified repository fact | Design limitation | Sources |
|---|---|---|---|
| Missing PCIe guide | PCIe Routing Guide is marked missing. | PCIe lane routing, lane mapping, polarity, loss budget, equalization, AC-coupling, impedance, and routing limits remain unresolved. | `Wanted_Documents.md`; `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `18_Component_Research/08_PCIe_Retimers.md` |
| Missing REFCLK guide | REFCLK Guide is marked missing. | REFCLK frequency, source, topology, electrical standard, jitter, skew, termination, and connector pins remain unresolved. | `Wanted_Documents.md`; `15_Reverse_Engineering/03_Clock_Tree.md`; `18_Component_Research/03_Clock_Generators.md` |
| Missing connector/baseboard sources | Connector Specification and Baseboard Specification are marked missing. | OAM connector PCIe pins, sideband pins, host/baseboard topology, connector pinout, and baseboard routing expectations remain unresolved. | `Wanted_Documents.md`; `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| MI210 PCIe context | MI210 is described as a standard PCIe-4.0 x16 card with one GCD and 64 GB HBM2e. | This is a reference-card fact and must not be used as an MI250X OAM connector pinout, lane count, lane map, or routing rule. | `13_Reference_Docs/ROCm/Overview.md`; `18_Component_Research/08_PCIe_Retimers.md`; `15_Reverse_Engineering/01_OAM_Pin_Mapping.md` |
| MI250/MI250X OAM context | MI250 and MI250X are described as OCP Accelerator Modules with two GCDs and 128 GB total memory, exposed to software as two devices with separate 64 GB VRAM blocks. | This identifies the target module class but does not define PCIe electrical requirements. | `13_Reference_Docs/ROCm/Overview.md`; `15_Reverse_Engineering/07_Component_ID.md`; `18_Component_Research/10_BOM.md` |
| MI200 SDMA PCIe context | MI200 SDMA engines are described as tuned for PCIe-4.0 x16 and designed to operate up to 32 GB/s. | This is software/data-movement context and not an MI250X OAM lane map, signal-integrity rule, or routing constraint. | `13_Reference_Docs/ROCm/Overview.md`; `15_Reverse_Engineering/08_Bringup.md`; `18_Component_Research/08_PCIe_Retimers.md` |
| Infinity Fabric contrast | The ROCm overview discusses MI250X platforms using Infinity Fabric and contrasts that with standard PCIe-4.0 behavior. | This is platform/data-movement context and does not define custom carrier PCIe routing. | `13_Reference_Docs/ROCm/Overview.md`; `08_Research_Papers/01_Architecture/notes.rtf`; `15_Reverse_Engineering/10_Minimal_Carrier.md` |
| Project PCIe goal | PCIe Gen4 is listed as a hardware goal, and stable PCIe enumeration is listed as a project priority. | The goal does not verify MI250X OAM connector generation, lane width, or compliance target. | `17_System_Architecture/01_System_Goals.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `18_Component_Research/08_PCIe_Retimers.md` |
| Architecture path | The system block diagram shows Host -> PCIe -> optional PCIe Switch / Retimer -> OAM Connector -> MI250X. | The diagram is a dependency map; PCIe lane mapping and switch/retimer need are marked undocumented. | `17_System_Architecture/02_System_Block_Diagram.md`; `15_Reverse_Engineering/10_Minimal_Carrier.md`; `18_Component_Research/08_PCIe_Retimers.md` |
| Host platform context | The selected host-platform BOM says the Supermicro X11DPH-T supports multiple PCIe x16 slots. | Host-slot availability does not define MI250X OAM lane routing, bifurcation, connector mapping, or retimer/switch requirements. | `20_System_BOM/Host_Platform.md`; `20_System_BOM/GPU_Subsystem.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| Bring-up context | Bring-up notes include clock startup, reset release, PCIe enumeration, and ROCm detection as dependency steps. | Enumeration is a goal; hardware requirements, reset timing, and sideband behavior remain unknown. | `15_Reverse_Engineering/08_Bringup.md`; `15_Reverse_Engineering/03_Clock_Tree.md`; `15_Reverse_Engineering/02_Power_Rails.md` |

# PCIe Generation

| Item | Status | Repository-supported information | What remains unknown | Sources |
|---|---|---|---|---|
| MI250X OAM PCIe generation | Unknown | PCIe Gen4 is listed as a project hardware goal. | Verified MI250X OAM connector generation, compliance target, fallback behavior, and whether any other generation applies. | `17_System_Architecture/01_System_Goals.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `18_Component_Research/08_PCIe_Retimers.md` |
| MI210 reference generation | Verified reference | MI210 is described as a standard PCIe-4.0 x16 card. | Whether MI250X OAM exposes the same generation, lane count, or routing model. | `13_Reference_Docs/ROCm/Overview.md`; `18_Component_Research/08_PCIe_Retimers.md`; `15_Reverse_Engineering/01_OAM_Pin_Mapping.md` |
| Gen5 applicability | Unknown | The retimer research file treats Gen5 as unknown and no readable source identifies a Gen5 requirement. | Whether Gen5 is required, supported, irrelevant, or prohibited for this carrier. | `18_Component_Research/08_PCIe_Retimers.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `18_Component_Research/10_BOM.md` |

# Lane Count

| Item | Status | Repository-supported information | What remains unknown | Sources |
|---|---|---|---|---|
| MI250X OAM lane count / width | Unknown | The repository does not provide a verified MI250X OAM lane count or lane width. | Link width, bifurcation, multiple links, per-GCD mapping, connector pin count, and host-side allocation. | `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `18_Component_Research/08_PCIe_Retimers.md` |
| Host slot width context | Verified host-planning fact | The selected host-platform BOM lists multiple PCIe x16 slots. | Which slot, lane source, bifurcation mode, cable/riser path, and OAM lane mapping are used for the carrier. | `20_System_BOM/Host_Platform.md`; `20_System_BOM/GPU_Subsystem.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| MI210 lane count reference | Verified reference | MI210 is described as PCIe-4.0 x16. | Whether MI250X OAM exposes the same lane count or any other lane topology. | `13_Reference_Docs/ROCm/Overview.md`; `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `18_Component_Research/08_PCIe_Retimers.md` |

# Lane Routing

| Item | Status | Repository-supported information | What remains unknown | Sources |
|---|---|---|---|---|
| OAM connector PCIe lane pins | Unknown | No readable source provides verified MI250X OAM PCIe pin numbers, signal names, or lane assignments. | Lane order, TX/RX direction at connector, connector pin numbers, pair naming, polarity, and OAM-vs-AMD-specific classification. | `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `18_Component_Research/01_OAM_Connector.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| Lane mapping | Unknown | PCIe lane assignment is listed as a high-priority unknown, and the OAM pin map leaves PCIe lane mapping undocumented. | Host-to-OAM lane map, per-GCD mapping, lane reversal support, bifurcation, and assignment table. | `AI_TASKS.md`; `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `09_AI_Notes/03_PCIe_Interface.md` |
| Routing topology | Unknown | Architecture diagrams show a host PCIe path and optional switch/retimer block, but do not verify a topology. | Direct host link, switch topology, retimer topology, redriver topology, riser/cable path, connector route, and scale-out topology. | `17_System_Architecture/02_System_Block_Diagram.md`; `15_Reverse_Engineering/10_Minimal_Carrier.md`; `18_Component_Research/08_PCIe_Retimers.md` |

# Reference Clocks

| Item | Status | Repository-supported information | What remains unknown | Sources |
|---|---|---|---|---|
| REFCLK documentation | Verified gap | REFCLK Guide is missing. | Frequency, source, topology, electrical standard, spread-spectrum behavior, termination, AC-coupling, connector pins, jitter, skew, and reset interaction. | `Wanted_Documents.md`; `15_Reverse_Engineering/03_Clock_Tree.md`; `18_Component_Research/03_Clock_Generators.md` |
| REFCLK source ownership | Unknown | No readable source documents whether REFCLK is supplied by host, baseboard, carrier, module, clock generator, oscillator, buffer, PLL, or another source. | Source owner, fanout, buffering, valid-before-reset rule, and measurement points. | `15_Reverse_Engineering/03_Clock_Tree.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `18_Component_Research/03_Clock_Generators.md` |
| REFCLK connector pins | Unknown | REFCLK is named only as an undocumented clock topic in the OAM pin map. | Pin names, pin numbers, differential pair assignment, polarity, termination, and routing requirements. | `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `15_Reverse_Engineering/03_Clock_Tree.md`; `18_Component_Research/03_Clock_Generators.md` |

# PERST#

| Item | Status | Repository-supported information | What remains unknown | Sources |
|---|---|---|---|---|
| PERST# presence | Unknown | PERST# is named as an undocumented PCIe sideband/reset topic. | Whether PERST# is present, required, optional, OAM-defined, AMD-specific, or baseboard-specific. | `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `15_Reverse_Engineering/08_Bringup.md`; `18_Component_Research/08_PCIe_Retimers.md` |
| PERST# pin and polarity | Unknown | No readable source provides an OAM pin assignment, polarity, voltage level, pullup, or timing for PERST#. | Pin number, direction, electrical standard, assertion timing, deassertion timing, and reset owner. | `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `15_Reverse_Engineering/08_Bringup.md`; `15_Reverse_Engineering/03_Clock_Tree.md` |
| PERST# dependency | Unknown | Bring-up notes infer reset release before PCIe enumeration, but MI250X timing is undocumented. | Relationship to Power Good, REFCLK validity, clock startup, management initialization, and PCIe enumeration. | `15_Reverse_Engineering/08_Bringup.md`; `15_Reverse_Engineering/02_Power_Rails.md`; `15_Reverse_Engineering/03_Clock_Tree.md` |

# CLKREQ#

| Item | Status | Repository-supported information | What remains unknown | Sources |
|---|---|---|---|---|
| CLKREQ# presence | Unknown | CLKREQ# is named as an undocumented PCIe sideband topic. | Whether CLKREQ# is present, required, optional, OAM-defined, AMD-specific, or unused. | `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `18_Component_Research/08_PCIe_Retimers.md`; `15_Reverse_Engineering/08_Bringup.md` |
| CLKREQ# behavior | Unknown | No readable source provides requirement or behavior for CLKREQ#. | Pin assignment, polarity, voltage level, pullups, clock power-management role, host ownership, and reset interaction. | `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `15_Reverse_Engineering/03_Clock_Tree.md`; `18_Component_Research/03_Clock_Generators.md` |

# WAKE#

| Item | Status | Repository-supported information | What remains unknown | Sources |
|---|---|---|---|---|
| WAKE# presence | Unknown | WAKE# is named as an undocumented PCIe sideband topic. | Whether WAKE# is present, required, optional, OAM-defined, AMD-specific, or unused. | `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `18_Component_Research/08_PCIe_Retimers.md`; `15_Reverse_Engineering/08_Bringup.md` |
| WAKE# behavior | Unknown | No readable source provides requirement or behavior for WAKE#. | Pin assignment, polarity, voltage level, pullups, wake behavior, power-state relationship, and host/baseboard ownership. | `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `15_Reverse_Engineering/02_Power_Rails.md`; `18_Component_Research/08_PCIe_Retimers.md` |

# Lane Polarity

| Item | Status | Repository-supported information | What remains unknown | Sources |
|---|---|---|---|---|
| Lane polarity rules | Unknown | The OAM pin map and retimer research list lane polarity as undocumented. | Polarity inversion allowance, connector pin polarity, pair naming, swap rules, and validation method. | `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `18_Component_Research/08_PCIe_Retimers.md`; `Wanted_Documents.md` |
| Lane reversal or bifurcation rules | Unknown | No readable source describes lane reversal, bifurcation, or mapping flexibility. | Allowed lane ordering, per-link grouping, per-GCD split, host slot bifurcation, and BIOS/platform requirements. | `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `20_System_BOM/Host_Platform.md`; `09_AI_Notes/03_PCIe_Interface.md` |

# Retimers

| Item | Status | Repository-supported information | What remains unknown | Sources |
|---|---|---|---|---|
| Retimer requirement | Unknown | PCIe retimer is optional until signal-integrity analysis or a verified routing guide requires it. | Whether any retimer is required for one MI250X module, where it would sit, lane count, generation support, insertion loss, equalization, and reset behavior. | `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `15_Reverse_Engineering/10_Minimal_Carrier.md`; `18_Component_Research/08_PCIe_Retimers.md` |
| Retimer component | Unknown | PCIe retimers are listed as undocumented component categories, and the BOM tracks PCIe retimer as unknown. | Manufacturer, part number, package, power rails, reference-clock needs, management bus, EEPROM/configuration needs, and firmware requirements. | `15_Reverse_Engineering/07_Component_ID.md`; `18_Component_Research/08_PCIe_Retimers.md`; `18_Component_Research/10_BOM.md` |
| Retimer settings | Unknown | No readable source provides equalization or retimer settings. | Presets, CTLE/DFE behavior, link training, compliance, register map, firmware, and validation method. | `18_Component_Research/08_PCIe_Retimers.md`; `09_AI_Notes/10_Design_Checklist.md`; `Wanted_Documents.md` |

# Switches

| Item | Status | Repository-supported information | What remains unknown | Sources |
|---|---|---|---|---|
| PCIe switch requirement | Unknown | PCIe switch is optional until a verified topology requires it. | Whether one MI250X module needs a switch, whether scale-out needs a switch, port widths, upstream/downstream topology, clocking, reset, and management. | `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `15_Reverse_Engineering/10_Minimal_Carrier.md`; `17_System_Architecture/02_System_Block_Diagram.md` |
| PCIe switch component | Unknown | PCIe switches are listed as undocumented component categories, and the BOM tracks PCIe switch as unknown. | Manufacturer, part number, package, generation support, lane count, power rails, EEPROM, firmware, thermal, and management interface. | `15_Reverse_Engineering/07_Component_ID.md`; `18_Component_Research/08_PCIe_Retimers.md`; `18_Component_Research/10_BOM.md` |
| Scale-out switch role | Unknown | Future goals include 1, 2, 4, and 8 MI250X modules. | Whether scale-out uses PCIe switches, fabric, direct host lanes, external baseboard, retimers, or another topology. | `17_System_Architecture/01_System_Goals.md`; `17_System_Architecture/04_Future_Expansion.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |

# Equalization

| Item | Status | Repository-supported information | What remains unknown | Sources |
|---|---|---|---|---|
| Equalization requirements | Unknown | Equalization is in the PCIe retimer research scope, but no settings or requirements are documented. | Presets, equalization phases, CTLE/DFE, transmitter settings, receiver settings, retimer/redriver settings, and compliance method. | `18_Component_Research/08_PCIe_Retimers.md`; `Wanted_Documents.md`; `09_AI_Notes/10_Design_Checklist.md` |
| Link training behavior | Unknown | PCIe enumeration is a bring-up goal, but link training requirements are not documented. | Training sequence, failure modes, recovery, measurement points, and required software/firmware checks. | `15_Reverse_Engineering/08_Bringup.md`; `18_Component_Research/08_PCIe_Retimers.md`; `13_Reference_Docs/ROCm/Overview.md` |

# Routing Constraints

| Item | Status | Repository-supported information | What remains unknown | Sources |
|---|---|---|---|---|
| PCIe routing guide | Verified gap | PCIe Routing Guide is marked missing. | Routing topology, impedance, loss budget, insertion loss, return path, via rules, layer transitions, length matching, skew, and spacing. | `Wanted_Documents.md`; `09_AI_Notes/03_PCIe_Interface.md`; `18_Component_Research/08_PCIe_Retimers.md` |
| AC coupling | Unknown | AC-coupling requirements are undocumented. | Capacitor values, footprint, placement, ownership, per-lane requirements, and whether REFCLK or sidebands need related treatment. | `18_Component_Research/08_PCIe_Retimers.md`; `15_Reverse_Engineering/03_Clock_Tree.md`; `09_AI_Notes/10_Design_Checklist.md` |
| Impedance and length matching | Unknown | High-speed routing constraints are documented as blockers before PCB layout, but values are not provided. | Differential impedance, tolerance, lane-to-lane skew, pair matching, connector compensation, and simulation requirements. | `09_AI_Notes/10_Design_Checklist.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `18_Component_Research/08_PCIe_Retimers.md` |
| Loss budget and connector loss | Unknown | No readable source provides loss budget or connector loss. | Board length limits, connector insertion loss, cable/riser loss, retimer trigger point, redriver trigger point, and compliance margin. | `Wanted_Documents.md`; `18_Component_Research/08_PCIe_Retimers.md`; `18_Component_Research/01_OAM_Connector.md` |

# Candidate Components

No PCIe switch, retimer, redriver, clock buffer, AC-coupling network, connector, or other signal-conditioning component is verified as selected, required, or present for the MI250X OAM carrier.

| Component category | Manufacturer | Part number | Status | Repository-supported information | Design position | Sources |
|---|---|---|---|---|---|---|
| PCIe retimer | Unknown | Unknown | Unknown category | Retimers are listed as undocumented, and no readable source proves that a retimer is required for one MI250X OAM module. | Do not select or place a retimer until topology, loss budget, lane count, generation, clocking, management, and part number are verified. | `18_Component_Research/08_PCIe_Retimers.md`; `15_Reverse_Engineering/07_Component_ID.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| PCIe redriver | Unknown | Unknown | Unknown category | The BOM lists PCIe redriver as an unknown signal-conditioning category, but no redriver requirement or candidate device is documented. | Do not select or place a redriver until verified routing or signal-integrity evidence requires one. | `18_Component_Research/10_BOM.md`; `18_Component_Research/08_PCIe_Retimers.md`; `18_Component_Research/README.md` |
| PCIe switch | Unknown | Unknown | Unknown category | PCIe switch is optional until a verified topology requires it. | Do not select or place a switch until host topology, lane mapping, port width, clocking, reset, management, and scale-out requirements are verified. | `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `17_System_Architecture/02_System_Block_Diagram.md`; `18_Component_Research/08_PCIe_Retimers.md` |
| PCIe REFCLK source or clock buffer | Unknown | Unknown | Unknown dependency | REFCLK topology, frequency, jitter, skew, routing, and clock-buffer requirements are undocumented. | Do not add PCIe clock support for switches, retimers, redrivers, or OAM connector pins until clock requirements are verified. | `15_Reverse_Engineering/03_Clock_Tree.md`; `18_Component_Research/03_Clock_Generators.md`; `Wanted_Documents.md` |
| PCIe passives / AC-coupling | Unknown | Unknown | Unknown category | AC-coupling capacitor requirements, termination, impedance constraints, and routing rules are undocumented. | Do not choose values, footprints, placement, or topology from current repository evidence. | `18_Component_Research/08_PCIe_Retimers.md`; `09_AI_Notes/10_Design_Checklist.md`; `Wanted_Documents.md` |

# Inferred Requirements

| Inferred requirement | Evidence basis | What is not verified | Sources |
|---|---|---|---|
| Host communication must be resolved for a minimal carrier. | Minimal carrier documents require a host-facing communication path for enumeration and ROCm/software use. | PCIe generation, lane width, lane map, sidebands, routing, and topology. | `15_Reverse_Engineering/10_Minimal_Carrier.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `13_Reference_Docs/ROCm/Overview.md` |
| PCIe and REFCLK are schematic blockers. | PCIe Routing Guide and REFCLK Guide are missing, and the design checklist says PCIe/REFCLK must be verified before schematic/layout. | Routing rules, clock topology, sideband pins, reset timing, and validation criteria. | `Wanted_Documents.md`; `09_AI_Notes/10_Design_Checklist.md`; `15_Reverse_Engineering/03_Clock_Tree.md` |
| Clock startup may precede reset release and enumeration. | Bring-up notes infer clock startup, reset release, and PCIe enumeration as dependency steps. | Signal names, timing, Power Good dependency, REFCLK valid criteria, and reset polarity. | `15_Reverse_Engineering/08_Bringup.md`; `15_Reverse_Engineering/02_Power_Rails.md`; `15_Reverse_Engineering/03_Clock_Tree.md` |
| Switches, retimers, and redrivers are optional until evidence proves they are required. | Minimal-carrier and component-research documents list them as optional or unknown categories. | Requirement, topology, placement, part number, equalization settings, management interface, and power rails. | `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `15_Reverse_Engineering/10_Minimal_Carrier.md`; `18_Component_Research/08_PCIe_Retimers.md` |
| MI210/MI200 PCIe facts are validation context only. | ROCm notes document MI210 PCIe-4.0 x16 and MI200 SDMA behavior; OAM notes separately mark MI250X lane mapping unknown. | MI250X OAM generation, lane count, lane routing, sideband behavior, and signal-integrity constraints. | `13_Reference_Docs/ROCm/Overview.md`; `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `18_Component_Research/08_PCIe_Retimers.md` |

# Unknown Summary

| Requested topic | Status | Unknown details | Sources |
|---|---|---|---|
| PCIe generation | Unknown for MI250X OAM | Actual connector generation, compliance target, Gen4/Gen5 applicability, fallback behavior, and host compatibility. | `17_System_Architecture/01_System_Goals.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `18_Component_Research/08_PCIe_Retimers.md` |
| Lane count | Unknown | Link width, bifurcation, per-GCD mapping, host slot mapping, and multi-link topology. | `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `09_AI_Notes/03_PCIe_Interface.md`; `18_Component_Research/08_PCIe_Retimers.md` |
| Lane routing | Unknown | Lane order, TX/RX direction, connector pins, pair naming, route topology, length matching, and topology through host/switch/retimer/redriver. | `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `Wanted_Documents.md`; `17_System_Architecture/02_System_Block_Diagram.md` |
| Reference clocks | Unknown | REFCLK frequency, source, topology, fanout, jitter, skew, termination, connector pins, and reset-clock interaction. | `15_Reverse_Engineering/03_Clock_Tree.md`; `18_Component_Research/03_Clock_Generators.md`; `Wanted_Documents.md` |
| PERST# | Unknown | Presence, pin, polarity, voltage, timing, owner, and relationship to Power Good and REFCLK. | `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `15_Reverse_Engineering/08_Bringup.md`; `15_Reverse_Engineering/02_Power_Rails.md` |
| CLKREQ# | Unknown | Presence, pin, polarity, voltage, clock-power role, owner, and timing. | `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `15_Reverse_Engineering/03_Clock_Tree.md`; `18_Component_Research/08_PCIe_Retimers.md` |
| WAKE# | Unknown | Presence, pin, polarity, voltage, power-state role, owner, and timing. | `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `15_Reverse_Engineering/02_Power_Rails.md`; `18_Component_Research/08_PCIe_Retimers.md` |
| Lane polarity | Unknown | Pair polarity, allowed inversion, lane reversal, pair swap, connector polarity, and validation method. | `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `18_Component_Research/08_PCIe_Retimers.md`; `Wanted_Documents.md` |
| Retimers | Unknown requirement | Need, placement, part number, lane count, clocking, equalization, reset, management, power, and configuration. | `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `15_Reverse_Engineering/07_Component_ID.md`; `18_Component_Research/08_PCIe_Retimers.md` |
| Switches | Unknown requirement | Need, topology, port widths, part number, management, EEPROM, reset, clocking, and scale-out role. | `17_System_Architecture/02_System_Block_Diagram.md`; `17_System_Architecture/04_Future_Expansion.md`; `18_Component_Research/10_BOM.md` |
| Equalization | Unknown | Presets, CTLE/DFE settings, link training, retimer/redriver configuration, eye-mask targets, and compliance method. | `18_Component_Research/08_PCIe_Retimers.md`; `Wanted_Documents.md`; `09_AI_Notes/10_Design_Checklist.md` |
| Routing constraints | Unknown | Impedance, loss budget, insertion loss, AC coupling, length matching, skew, via rules, layer stack, connector loss, and simulation requirements. | `Wanted_Documents.md`; `09_AI_Notes/10_Design_Checklist.md`; `18_Component_Research/08_PCIe_Retimers.md` |

# Design Implications

| Rule | Status | Engineering implication | Sources |
|---|---|---|---|
| Do not route PCIe yet. | Inferred | Do not route lanes, assign lane mapping, define polarity, choose lane width, or assign sidebands until connector, baseboard, PCIe routing, and REFCLK evidence is recovered. | `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `Wanted_Documents.md`; `09_AI_Notes/10_Design_Checklist.md` |
| Do not infer MI250X OAM from MI210. | Inferred | Treat MI210 PCIe-4.0 x16 and MI200 SDMA behavior as software/data-movement context, not as MI250X OAM carrier electrical requirements. | `13_Reference_Docs/ROCm/Overview.md`; `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `18_Component_Research/08_PCIe_Retimers.md` |
| Do not select signal-conditioning parts. | Inferred | Do not choose switches, retimers, redrivers, clock buffers, AC-coupling values, or equalization settings until topology and signal-integrity evidence exist. | `18_Component_Research/08_PCIe_Retimers.md`; `18_Component_Research/10_BOM.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| Keep reset, clock, power, and PCIe linked. | Inferred | PCIe enumeration depends on unresolved REFCLK, reset release, Power Good, power sequencing, and host-interface requirements. | `15_Reverse_Engineering/08_Bringup.md`; `15_Reverse_Engineering/03_Clock_Tree.md`; `15_Reverse_Engineering/02_Power_Rails.md` |
| Treat host-platform PCIe slots as planning context. | Inferred | Multiple host PCIe x16 slots do not define carrier pinout, lane assignment, bifurcation, cable/riser topology, or OAM connector routing. | `20_System_BOM/Host_Platform.md`; `20_System_BOM/GPU_Subsystem.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |

# Future Research

| Priority | Research task | Required output | Sources |
|---|---|---|---|
| High | Obtain and extract the PCIe Routing Guide. | Verified PCIe generation, lane routing, lane mapping, polarity rules, loss budget, impedance, length matching, skew, equalization, AC-coupling, and validation constraints. | `Wanted_Documents.md`; `09_AI_Notes/03_PCIe_Interface.md`; `18_Component_Research/08_PCIe_Retimers.md` |
| High | Obtain and extract the REFCLK Guide. | Verified REFCLK frequency, source, topology, electrical standard, jitter, skew, termination, connector pins, and reset interaction. | `Wanted_Documents.md`; `15_Reverse_Engineering/03_Clock_Tree.md`; `18_Component_Research/03_Clock_Generators.md` |
| High | Obtain connector and baseboard PCIe data. | Verified OAM connector lane pins, sideband pins, REFCLK pins, lane order, baseboard ownership, host topology, and OAM-vs-AMD-specific classification. | `Wanted_Documents.md`; `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md` |
| High | Determine reset and sideband requirements. | Verified PERST#, CLKREQ#, WAKE#, reset timing, polarity, voltage levels, Power Good dependency, REFCLK dependency, and enumeration sequence. | `15_Reverse_Engineering/01_OAM_Pin_Mapping.md`; `15_Reverse_Engineering/08_Bringup.md`; `15_Reverse_Engineering/02_Power_Rails.md` |
| Medium | Determine switch/retimer/redriver need. | Verified direct-connect, switch, retimer, redriver, or other topology decision supported by signal-integrity evidence. | `17_System_Architecture/02_System_Block_Diagram.md`; `17_System_Architecture/03_Minimal_Carrier_Requirements.md`; `18_Component_Research/08_PCIe_Retimers.md` |
| Medium | Add PCIe bring-up validation after requirements are sourced. | Verified link-speed checks, lane-width checks, enumeration checks, equalization/compliance checks, and ROCm validation tied to verified hardware requirements. | `15_Reverse_Engineering/08_Bringup.md`; `13_Reference_Docs/ROCm/Overview.md`; `09_AI_Notes/10_Design_Checklist.md` |
| Medium | Define scale-out topology after single-module PCIe is verified. | Verified one-, two-, four-, and eight-module host-link topology and implications for switches, retimers, redrivers, routing, and management. | `17_System_Architecture/01_System_Goals.md`; `17_System_Architecture/04_Future_Expansion.md`; `20_System_BOM/GPU_Subsystem.md` |

# Sources

| Source | Use in this reference |
|---|---|
| `README.md` | States the evidence workflow and project goal. |
| `AI_TASKS.md` | Lists PCIe lane assignment, PCIe routing, differential pair tuning, and validation as unresolved project work. |
| `Wanted_Documents.md` | Marks PCIe Routing Guide, REFCLK Guide, Connector Specification, and Baseboard Specification as missing. |
| `13_Reference_Docs/ROCm/Overview.md` | Provides MI210 PCIe-4.0 x16 context, MI250/MI250X OAM context, MI200 SDMA PCIe-4.0 x16 tuning, Infinity Fabric contrast, and software validation context. |
| `08_Research_Papers/01_Architecture/notes.rtf` | Lists Infinity Fabric, MI250X, RCCL, MPI, node topology, bandwidth matrix, and MPI bandwidth as research topics. |
| `09_AI_Notes/03_PCIe_Interface.md` | Summarizes missing lane mapping, lane count, polarity, routing constraints, REFCLK topology, reset signals, and sidebands. |
| `09_AI_Notes/10_Design_Checklist.md` | States schematic capture and PCB layout should wait for PCIe/REFCLK and high-speed constraints. |
| `15_Reverse_Engineering/01_OAM_Pin_Mapping.md` | Records PCIe lanes, PCIe sideband pins, clock pins, lane mapping, polarity, REFCLK, PERST#, WAKE#, and CLKREQ# as undocumented. |
| `15_Reverse_Engineering/02_Power_Rails.md` | Records Power Good, enable, sequencing, and reset dependency gaps that affect PCIe bring-up. |
| `15_Reverse_Engineering/03_Clock_Tree.md` | Records REFCLK, clock source, frequency, topology, jitter, skew, routing, and reset-clock relationships as unknown. |
| `15_Reverse_Engineering/07_Component_ID.md` | Lists PCIe switches and retimers as undocumented component categories. |
| `15_Reverse_Engineering/08_Bringup.md` | Records clock startup, reset release, PCIe enumeration, ROCm detection, and unresolved hardware prerequisites. |
| `15_Reverse_Engineering/10_Minimal_Carrier.md` | Defines the host communication path, PCIe design resolution, reset, and optional switch/retimer positions for the minimal carrier. |
| `17_System_Architecture/01_System_Goals.md` | Lists PCIe Gen4 as a hardware goal and stable PCIe enumeration as a project priority. |
| `17_System_Architecture/02_System_Block_Diagram.md` | Shows Host -> PCIe -> optional PCIe Switch / Retimer -> OAM Connector -> MI250X with details undocumented. |
| `17_System_Architecture/03_Minimal_Carrier_Requirements.md` | Lists PCIe implementation, lane mapping, sidebands, switches, retimers, signal-integrity rules, and REFCLK details as unresolved. |
| `17_System_Architecture/04_Future_Expansion.md` | Records future one-, two-, four-, and eight-MI250X goals that may later affect host-link topology. |
| `18_Component_Research/01_OAM_Connector.md` | Records connector and pinout unknowns that block PCIe lane assignment. |
| `18_Component_Research/03_Clock_Generators.md` | Records REFCLK, jitter, skew, routing, and PCIe clocking gaps. |
| `18_Component_Research/08_PCIe_Retimers.md` | Main related component research for PCIe retimers, redrivers, switches, Gen4/Gen5, equalization, REFCLK, lane mapping, and signal-integrity gaps. |
| `18_Component_Research/10_BOM.md` | Tracks PCIe switch, PCIe retimer, PCIe redriver, and related clock components as unknown categories. |
| `20_System_BOM/Host_Platform.md` | Records the selected host platform and multiple PCIe x16 slots as host planning context. |
| `20_System_BOM/GPU_Subsystem.md` | Records OAM, custom carrier board, PCIe host interface, and future expansion as system-BOM planning context. |