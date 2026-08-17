# Molex 2189101115 — 60 V / skip-pin questions (WAITING)

**Status:** No answer in this tree. Do not fill this file with a guessed skip-pin table.

**Who:** Brian Park (named by the project owner for this question). Affiliation is **not** re-derived here. Do not substitute a different Molex contact and call it resolved.

**Inbox this run:** Gmail MCP **needsAuth**. If a reply already exists, it was **not** read. File any future reply under `docs/received/` with date, quote, and whether it cites `2189100001-PS-000`.

**Do not reload old chats** for “what he said.” Only a message or a Molex PDF in this repo counts.

---

## Why this is a wait, not a public close

Already in-repo (PR #4 `FINDINGS.md`):

| Claim | Label | Source |
|---|---|---|
| Catalog max **30 V AC (RMS)/DC** | Verified | Farnell sheet https://www.farnell.com/datasheets/3919676.pdf (HTTP 200 in prior trees) |
| Family flyer **29.9 V AC RMS** | Verified | Molex Mirror Mezz 15×11 OCP PDF |
| Marketing “12 V or **48 V** … **500 W (48 V)**” | Verified marketing | Molex *Supports OCP Open Standards* PDF |
| OCP Table 3: “Max Voltage Application **30V AC (OAM supports 60V after Molex’s pin assignment review)**.” | Verified OCP text | OAM Design Spec v1.5 Table 3 |
| OCP Table 5: P48V **44–60 V**, 16 pins, **16 A at 44 V** | Verified OCP text | same spec §8.4.1 |
| `2189100001-PS-000` / `2189101115-SD-000` PDFs | **Not retrieved** | molex.com timeout / distributor 403 in PR #4 |

OCP’s parenthetical is a **review caveat**, not a retrieved Molex skip-pin table. Catalog 30 V still wins “what does the connector sheet say?” until Molex answers.

---

## Questions that must be answered (send as-is)

Part: Molex **218910-1115** / **2189101115**, Mirror Mezz Pro, 688 circuits, 15 pair × 11 row, hermaphroditic, 5.00 mm stack. Carrier mates with the same MPN on AMD Instinct **MI250X OAM** (OCP OAM v1.x, not r2.0).

1. After Molex’s **pin assignment review**, may the **16 OCP-named P48V contacts** on Conn0 run at **48–60 V DC** (OCP Table 5 window 44–60 V; shipping UBB cables are 54 V class)? Yes / no / only if listed pins are left open.

2. What is the **skip-pin / isolation rule** for 60 V? List **Molex ball IDs** (PIN A3 family on `2189101115-SD-000`) that must be **NC**, deleted, or kept as creepage barriers. Do not point at an unnamed “review.”

3. Is the OCP generic v1.0 map’s **16 P48V pads** (Conn0 H59, K59, H60, K60, H61, J61, K61, L61, H62, J62, K62, L62, H63, J63, H64, J64 in `OAM Pin map rev 1.0.xlsx`) that reviewed set — or a different set? **Do not invent a different set in the reply path; confirm or deny this list.**

4. Current rating **per P48V contact at 48–54 V**, 80 °C, after the 20 % derating OCP Table 3 cites (catalog 0.75 / 1.0 / 1.2 A by Cu oz is a **30 V** sheet).

5. Please send **`2189100001-PS-000`** and **`2189101115-SD-000`** (or a public URL that is not a JS shell).

6. BGA-attach: is **218910-1115** rated only for factory reflow, or is there an authorized prototype attach note?

Until 1–3 are answered with Molex IDs or a PS table: **do not energize P48V through these pads. Do not send the carrier to PCBWay.**

---

## What is *not* an answer

- Molex marketing “supports 48 V / 500 W”
- SuperMicro **CBL-PWEX-1280** 54 V **UBB cable** (not the mezz)
- UBB BOM Amphenol **10028917-001LF** “54 V connector” (UBB **input**, not 218910-1115)
- Forum posts
- Reciting OCP Table 3 without the skip-pin list
