# Management Controller

## Purpose
- Track firmware, management, health-check, and validation references that may affect carrier-board sideband interfaces and bring-up.

## Verified
- Firmware Tool v2.3, Firmware Tool v2.2, AMD FW Flash Guide, and Firmware Update Guide are indexed. Source: `13_Reference_Docs/Reference_Index.rtf`.
- Health Checks, System Validation, and GPU Accelerator Management Interfaces are indexed. Source: `13_Reference_Docs/Reference_Index.rtf`.
- `rocminfo` is referenced for inspecting memory pools and XNACK-related platform information. Source: `13_Reference_Docs/ROCm/Overview.md`.
- `Management.md` exists, but contains no visible plain Markdown engineering content. Source: `09_AI_Notes/Management.md`.

## Inferred
- Management and firmware behavior will matter during bring-up because firmware tools, health checks, validation, and GPU management interfaces are indexed. Source: `13_Reference_Docs/Reference_Index.rtf`.
- The carrier may need sideband paths for telemetry, reset, enable, firmware update, or health checks, but this is not defined in readable local files.

## Unknown
- Needs Verification: no management controller part number is identified in readable local files.
- Needs Verification: BMC, MCU, SMBus/I2C, PMBus, JTAG, SPI flash, UART, reset, interrupt, and enable topology are not verified.
- Needs Verification: firmware update flow and hardware dependencies are not available locally.

## Source Documents
- `13_Reference_Docs/Reference_Index.rtf`
- `13_Reference_Docs/ROCm/Overview.md`
- `09_AI_Notes/Management.md`

## Design Implications
- Do not assign management sideband signals until GPU management interface documentation is found.
- Keep PMBus and VRM control questions linked to `04_Power_Architecture.md`.
- Separate software health checks from electrical schematic requirements.

## Open Questions
- What management interface does the MI250X OAM expose?
- Is a carrier-side controller required?
- What hardware is required for firmware update or health checks?
