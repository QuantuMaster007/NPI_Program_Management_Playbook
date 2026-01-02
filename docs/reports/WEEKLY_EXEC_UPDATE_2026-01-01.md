# Weekly Exec Update — 1 pager

**Week of:** 2026-01-01  
**Program health (RAG):** 🟡

## 1) Headlines (top 3)
- **Program stood up + baseline plan created:** Charter, cadence, and initial IMS baseline are in place; critical path is established for Requirements → Design Freeze → Build → FAT → Install/SAT → Qualification.
- **Facilities readiness is the primary near-term blocker:** Network/VLAN readiness is currently blocked and can impact the **Move-in & Install** gate if not resolved before facilities minimum readiness completes.
- **Decision needed to protect schedule:** Propose a **controls “release lock” for FAT** (pin PLC/FW/HMI + IO map rev) to reduce churn and prevent late integration surprises.

## 2) Milestones (next 4–6 weeks)
| Milestone | Plan date | Forecast date | Delta | Owner | Notes |
|---|---:|---:|---:|---|---|
| Finalize Charter | 2026-01-06 | 2026-01-06 | 0d | PM | Charter template complete; align sponsor signoff |
| Requirements Baseline | 2026-01-20 | 2026-01-20 | 0d | Eng Lead | Freeze v0.1 requirements + RTM baseline |
| Site Survey & Utilities Plan | 2026-01-22 | 2026-01-22 | 0d | Facilities Lead | Confirms power/network/utilities + constraints |
| ICD v0.1 Draft | 2026-01-24 | 2026-01-24 | 0d | Controls Lead | Initial IO map + protocols for integration |
| Long-Lead Orders Placed | 2026-01-16 | 2026-01-16 | 0d | SCM | Confirm PO placement + supplier commit dates |
| Design Freeze (HW) | 2026-02-05 | 2026-02-05 | 0d | HW Lead | Change control becomes mandatory after freeze |

## 3) Critical path blockers
| Blocker | Domain | Owner | ETA | Escalation needed |
|---|---|---|---:|---|
| VLAN / network approval not complete (risk to site readiness minimum) | Facilities | Facilities Lead | 2026-01-10 | Yes — IT escalation if not approved by ETA |
| Controls version churn risk before FAT (need release lock policy) | Controls | Controls Lead | 2026-02-01 | Yes — approve “FAT release lock” decision |
| Supplier lead time uncertainty for long-lead components | HW/Supplier | SCM | 2026-01-16 | No (monitor) — trigger expedite if slip forecasted |

## 4) Top risks (top 5)
| Risk | Severity | Mitigation | Owner | Due |
|---|---|---|---|---:|
| Facilities network/VLAN approval delays site readiness minimum | High | Escalate IT ticket; implement temporary isolated switch if approved; update readiness checklist | Facilities Lead | 2026-01-10 |
| Long-lead parts slip build start | High | Dual source where possible; confirm supplier capacity; expedite plan + alternates | SCM | 2026-01-16 |
| Controls release churn causes late integration defects | Medium | Establish release lock candidate by 2026-02-10; changes via change control only | Controls Lead | 2026-02-10 |
| Safety interlock validation expands scope late | Medium | Review safety chain early; pre-test interlock logic; align EHS signoff checklist | EHS Lead | 2026-01-20 |
| Install window conflict / site access limitations | Medium | Lock install window; pre-stage tooling; align contractors + site services | Ops | 2026-03-10 |

## 5) Change control summary
- **CRs opened this week:** CR-001 (Proposed) — Pin Controls versions for FAT (“release lock”)  
- **CRs approved:** None  
- **Net schedule/cost impact:** Expected **schedule protection** (reduced integration churn). Minimal cost impact unless emergency re-test required.

## 6) Metrics
- **Readiness score (HW / Controls / Facilities):** HW **100%**, Controls **50%**, Facilities **0%** *(Facilities blocked by network approval)*  
- **Open Sev-1/Sev-2 issues:** Sev-1 **0**, Sev-2 **1** (Facilities network readiness)  
- **Supplier OTD for LLTs:** Baseline pending; initial PO confirmation due **2026-01-16**
