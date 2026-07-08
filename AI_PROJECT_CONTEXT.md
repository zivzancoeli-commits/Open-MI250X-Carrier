{\rtf1\ansi\ansicpg1252\cocoartf2709
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # AI Project Context\
\
## Project Name\
\
Open MI250X Carrier Board\
\
---\
\
# Project Goal\
\
Design a completely open hardware carrier board capable of operating AMD Instinct MI250X OAM accelerator modules.\
\
The final objective is a practical carrier board that can be manufactured and assembled by individuals or small companies using publicly available documentation and reverse engineering.\
\
This project is intended to document every engineering decision.\
\
---\
\
# Long-Term System Goal\
\
The final system should support:\
\
- Up to 8 AMD Instinct MI250X OAM modules\
- Possibly 16 modules if practical\
- Two complete computers inside one enclosure\
- Lowest possible overall system cost\
- Commodity components whenever possible\
- Open-source hardware\
- Open-source software\
- Designed primarily in KiCad\
- Easy future upgrades\
\
---\
\
# Memory Goal\
\
The preferred host memory configuration uses:\
\
Dell SNPHVY68C/128G\
\
128 GB DDR4 Persistent Memory\
\
8 or 16 DIMMs depending on motherboard\
\
The system should support very large memory capacity.\
\
---\
\
# GPU Goal\
\
Primary accelerator:\
\
AMD Instinct MI250X OAM\
\
Desired scalability:\
\
- 1 GPU\
- 2 GPUs\
- 4 GPUs\
- 8 GPUs\
- Future investigation into 16 GPUs\
\
Carrier boards should remain as similar as possible across all configurations.\
\
---\
\
# Philosophy\
\
Never invent hardware requirements.\
\
Always separate information into:\
\
Verified\
\
Inferred\
\
Unknown\
\
Whenever documentation is incomplete, clearly mark assumptions.\
\
---\
\
# Documentation Rules\
\
Every engineering statement should include one of:\
\
Verified\
\
Inferred\
\
Unknown\
\
Whenever possible cite the original AMD document.\
\
Avoid speculation.\
\
---\
\
# Reverse Engineering Rules\
\
Unknown interfaces should be documented rather than guessed.\
\
Every unknown should become an engineering task.\
\
Pinouts should only be marked verified if supported by documentation.\
\
---\
\
# Repository Organization\
\
The repository is organized into:\
\
01-14\
\
Reference material\
\
15\
\
Reverse engineering notebooks\
\
16\
\
KiCad project\
\
17\
\
System architecture\
\
Future folders will include:\
\
PCB revisions\
\
Mechanical CAD\
\
Validation\
\
Firmware\
\
Manufacturing\
\
Testing\
\
---\
\
# Preferred Design Style\
\
Simple\
\
Modular\
\
Low cost\
\
Repairable\
\
Expandable\
\
Commodity components\
\
Avoid unnecessary complexity.\
\
---\
\
# KiCad Expectations\
\
The KiCad project should eventually include:\
\
Complete schematics\
\
PCB layout\
\
Library symbols\
\
Footprints\
\
3D models\
\
Manufacturing outputs\
\
ERC/DRC clean design\
\
---\
\
# AI Assistant Expectations\
\
Whenever generating documentation:\
\
Do not summarize entire documents.\
\
Extract engineering facts.\
\
Identify missing information.\
\
Highlight risks.\
\
Generate engineering TODO items.\
\
Keep documentation concise.\
\
Whenever generating KiCad work:\
\
Never invent electrical connections.\
\
Only use verified documentation.\
\
Flag every unknown for future validation.\
\
---\
\
# Current Project Phase\
\
Current Phase:\
\
System Architecture\
\
Next Phase:\
\
Reverse Engineering\
\
After that:\
\
KiCad schematic capture\
\
PCB layout\
\
Prototype\
\
Bring-up\
\
Validation\
\
---\
\
# Ultimate Goal\
\
Create the first fully documented open-source AMD Instinct MI250X carrier board that can realistically be built by hobbyists, researchers, and small companies.}