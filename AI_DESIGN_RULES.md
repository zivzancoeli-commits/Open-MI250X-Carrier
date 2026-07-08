# Open-MI250X Carrier Design Rules

## General

- Follow KiCad 9 conventions.

- Never invent undocumented OAM pins.

- Clearly mark unknown values as TBD.

- Prefer verified OCP OAM specifications over assumptions.

## PCIe

- Treat PCIe lanes as differential pairs.

- Preserve lane numbering.

- Do not rename reference clocks.

## Power

- Every IC requires local decoupling.

- Separate analog and digital supplies when documented.

- Include test points on all primary rails.

## Documentation

- Every generated sheet must include:

  - Purpose

  - Assumptions

  - Source documents

  - Open questions

## Safety

- Never overwrite existing KiCad files.

- Always generate into a new folder.