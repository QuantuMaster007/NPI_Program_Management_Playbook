# Weekly Exec Update — 1 pager

**Week of:** 2026-01-01  
**Program health (RAG):** 🟡

## 1) Headlines (top 3)
- **Baseline established + critical path confirmed:** Project start is **2026-01-02** with **125 days** total duration. Critical path is **T001 → T010 → T050 → T070 → T080 → T100 → T110 → T120** (Charter → Requirements → HW Design Freeze → EVT Build → FAT → Install → SAT → Qual).  
- **Facilities is the current constraint (0% readiness):** Facilities readiness is blocked and remains the most likely driver of install risk unless network/VLAN is cleared (or a compliant temporary workaround is approved).  
- **Execution decision needed (controls churn):** Controls readiness is **50%**; we need to implement a **FAT “release lock”** (pin PLC/FW/HMI + IO map revision) to protect FAT evidence quality and reduce late integration surprises.

## 2) Milestones (next 4–6 weeks)
| Milestone | Plan date | Forecast date | Delta | Owner | Notes |
|---|---:|---:|---:|---|---|
| Finalize Charter (T001) | 2026-01-06 | 2026-01-06 | 0d | PM | Sponsor signoff + publish cadence/RAID |
| Requirements Baseline (T010) | 2026-01-20 | 2026-01-20 | 0d | Eng Lead | Freeze v0.1 requirements + RTM baseline |
| Site Survey & Utilities Plan (T030) | 2026-01-22 | 2026-01-22 | 0d | Facilities Lead | Confirm power/network/utilities; capture constraints |
| ICD v0.1 Draft (T020) | 2026-01-24 | 2026-01-24 | 0d | Controls Lead | Initial IO map + protocols for integration |
| Long-Lead Orders Placed (T040) | 2026-01-16 | 2026-01-16 | 0d | SCM | Confirm supplier commit dates + expedite triggers |
| Design Freeze (HW) (T050) | 2026-02-05 | 2026-02-05 | 0d | HW Lead | Change control mandatory after freeze |

## 3) Critical path blockers
| Blocker | Domain | Owner | ETA | Escalation needed |
|---|---|---|---:|---|
| **Network/VLAN approval not complete** (drives Facilities readiness = 0%) | Facilities | Facilities Lead | 2026-01-10 | Yes — IT escalation if not approved by ETA |
| **Controls version churn risk before FAT** (needs release lock policy before T080) | Controls | Controls Lead | 2026-02-01 | Yes — approve “FAT release lock” decision |
| **Supplier lead time uncertainty** for long-lead components (risk to T070 EVT build start) | HW/Supplier | SCM | 2026-01-16 | Monitor — trigger expedite/alternate sourcing if slip forecasted |

## 4) Top risks (top 5)
| Risk | Severity | Mitigation | Owner | Due |
|---|---|---|---|---:|
| Facilities network/VLAN approval delays site readiness minimum | High | Escalate IT ticket; pre-approve compliant temporary isolated network workaround if needed; track weekly | Facilities Lead | 2026-01-10 |
| Long-lead parts slip build start (impacts EVT build on critical path) | High | Confirm supplier capacity + commit dates; dual source where feasible; expedite triggers | SCM | 2026-01-16 |
| Controls release churn causes late integration defects / retest | Medium | Define FAT release lock; allow changes only via change control + defined retest scope | Controls Lead | 2026-02-10 |
| Safety interlock validation expands scope late (SAT/commissioning impacts) | Medium | Pre-test interlock logic; align EHS signoff checklist early; schedule walkdown | EHS Lead | 2026-01-20 |
| Install window conflict / site access limitations | Medium | Lock install window; pre-stage tooling; align contractors + site services | Ops | 2026-03-10 |

## 5) Change control summary
- **CRs opened this week:** CR-001 (Proposed) — Pin Controls versions for FAT (“release lock”)  
- **CRs approved:** None  
- **Net schedule/cost impact:** Expected schedule protection (reduced integration churn). Minimal cost unless emergency retest required.

## 6) Metrics
- **Readiness by domain:** Hardware **100%**; Controls **50%**; Facilities **0%**; EHS **100%**  
- **Overall readiness:** **62%**  
- **Open Sev-1/Sev-2 issues:** Sev-1 **0**, Sev-2 **1** (Facilities network readiness)  
- **Supplier OTD for LLTs:** Baseline pending; initial PO confirmation due **2026-01-16**

### Evidence
- Critical path output: `docs/evidence/critical_path_output.md`
- Readiness output: `docs/evidence/readiness_score_output.md`
