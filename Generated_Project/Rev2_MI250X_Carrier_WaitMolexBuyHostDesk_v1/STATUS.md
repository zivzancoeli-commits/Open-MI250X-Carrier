# STATUS — 2026-08-17

## Waiting (do not close)

**Brian Park’s answer on Molex 218910-1115 / 2189101115 60 V and skip-pin.**

OCP Accelerator Module Design Spec **v1.5 Table 3** (already extracted): connector max **30 V AC**, with parenthetical *“OAM supports 60V after Molex’s pin assignment review.”* Farnell/Molex catalog sheets still **30 V / 29.9 V RMS**. Product spec **`2189100001-PS-000` was not retrieved** (molex.com timeout in PR #4).

This run:

- Did **not** reload old chats for an answer.
- Gmail MCP was **needsAuth** — cannot see whether Brian Park replied.
- Did **not** invent skip-pin numbers or re-rate the catalog 30 V line.

Until a citable reply or the PS PDF is filed here: **no P48V tape-out, no PCBWay, no energize.**

Questions to remain unanswered until then: [`docs/MOLEX_2189101115_QUESTIONS.md`](docs/MOLEX_2189101115_QUESTIONS.md).

## OK to buy now (will work without OAMs)

- Host: X11DPH-T, 2× Gold 6230 SRF8W, 8× SNPHVY68C/128G, 8× MEM-DR432L-SL01-ER29, NH-U14S DX-3647, ATX/EPS PSU, boot SSD.
- Desk: B550M + Ryzen 5 5500, desk RAM/PSU, optional RX 470.
- Local: square tube + weld consumables (SendCutSend does **sheet**, not tube).
- **SendCutSend:** [`cad/dxf/`](cad/dxf/) skins and trays. Not a bolster, not a heatsink, not an OAM hole pattern.

Details: [`docs/BUY_NOW_HOST_DESK_SENDCUTSEND.md`](docs/BUY_NOW_HOST_DESK_SENDCUTSEND.md).

## Forbidden

- PCBWay or any fab of in-repo KiCad (named-net stub; 30 V vs 48 V open; AMD overlay NDA).
- Energize MI250X. Mate an OAM to a random PCB. Apply 48 V to 218910-1115 pads.
- Invent pins. Mix r2.0 (P3V3=6). Strap TEST*/RFU/DO_NOT_USE. Drive PVREF.
- SendCutSend **M3.5** PEM (not in their metric nut list). Do not put OAM M3.5 NPTH on these DXFs.
- Drill 8-GPU **412 × 332 mm** Inferred tiling as if it were a UBB.

## What this tree does *not* change

- No production schematic/PCB edits.
- No new OCP pad names.
- No claim that host/desk POST implies HBM works.
