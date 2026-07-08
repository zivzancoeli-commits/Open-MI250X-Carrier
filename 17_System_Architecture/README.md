{\rtf1\ansi\ansicpg1252\cocoartf2709
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # System Architecture\
\
## Purpose\
\
This folder defines the complete hardware architecture of the Open MI250X Carrier project.\
\
Unlike the reverse engineering notes, these documents represent engineering decisions that will guide schematic capture, PCB layout, firmware development, and system integration.\
\
The goal is to design an open carrier board capable of operating surplus AMD Instinct MI250X OAM modules while remaining scalable from a single GPU prototype to an eight-GPU compute platform.\
\
---\
\
## Documents\
\
### 01_System_Goals.md\
\
Overall objectives and project requirements.\
\
### 02_System_Block_Diagram.md\
\
High-level architecture of the complete system.\
\
### 03_Minimal_Carrier_Requirements.md\
\
Hardware required to operate one MI250X.\
\
### 04_Future_Expansion.md\
\
Roadmap from one GPU to eight GPUs.\
\
### 05_Component_Selection.md\
\
Candidate components for every subsystem.\
\
---\
\
## Design Philosophy\
\
- Prefer open standards.\
- Prefer publicly documented components.\
- Minimize proprietary hardware.\
- Minimize cost using surplus enterprise hardware.\
- Design for future expansion.\
- Clearly distinguish verified facts from assumptions.}