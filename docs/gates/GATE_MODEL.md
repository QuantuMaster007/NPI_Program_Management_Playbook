# Gate Model (EVT/DVT/PVT example)

> Adapt names to your environment (FAT/SAT, Alpha/Beta, Pilot/MP, etc.)

## Gate definitions
| Gate | Intent | Required evidence (examples) | Decision authority |
|---|---|---|---|
| G0 — Charter Approved | Program is real | charter, scope, success metrics | Sponsor |
| G1 — Requirements Locked | Agree what “done” means | requirements + RTM baseline + ICD draft | Eng + PM |
| G2 — Design Freeze | Minimize churn | drawings/BOM frozen, change control active | Eng |
| G3 — Build Ready | Parts + facilities ready | LLT in-hand, site readiness minimum | PM |
| G4 — FAT Complete | System works offsite | FAT report, issues triaged, release lock | Eng/Test |
| G5 — SAT/Commissioning Complete | Safe & functional onsite | SAT checklist, EHS signoff, alarms validated | Facilities+EHS |
| G6 — Qualification Complete | Meets performance | qual report, RTM evidence, reliability (if req.) | Quality |
| G7 — Handoff | Ops owns it | training, spares, docs, acceptance | Ops |

See checklists in `docs/gates/checklists/`.
