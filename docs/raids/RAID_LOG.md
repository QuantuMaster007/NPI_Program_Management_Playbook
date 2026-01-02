# RAID Log (Template)

> One line per item. Keep it current. Review every week.

| ID | Type (R/A/I/D) | Title | Domain | Severity | Owner | Due date | Status | Mitigation / Next step | Link / Evidence |
|---|---|---|---|---|---|---:|---|---|---|
| I-001 | Issue | Facilities readiness blocked (0%) due to network/VLAN approval | Facilities | High | <Facilities Lead> | 2026-01-10 | Open | Escalate IT ticket; define temporary isolated network workaround; update readiness checklist weekly | docs/evidence/readiness_score_output.md |
| R-002 | Risk | Controls readiness at 50% may cause churn during integration if versions not locked | Controls | Med | <Controls Lead> | 2026-02-10 | Open | Establish “FAT Release Lock” by Controls Release Lock Candidate date; require change control for any post-lock changes | docs/evidence/readiness_score_output.md |
| R-003 | Risk | Design Freeze (HW) is on the critical path; late changes will directly slip Build Assembly (EVT) | Hardware | High | <HW Lead> | 2026-02-05 | Open | Enforce change control; prioritize closure of open design issues; daily burn-down on freeze blockers | docs/evidence/critical_path_output.md |
| R-004 | Risk | Long-lead parts / supplier delivery slip may compress EVT build window and jeopardize FAT start | HW/Supplier | High | <SCM Lead> | 2026-01-16 | Open | Confirm supplier commit dates; dual-source where feasible; prepare expedite triggers + alternates | data/sample/ims_tasks.csv |
| I-005 | Issue | FAT Execute is critical-path; test readiness gaps could delay FAT start or reduce evidence quality | Test | Med | <Test Lead> | 2026-02-25 | Open | Finalize FAT plan + staffing; pre-stage instruments; define “minimum evidence” checklist for FAT exit | docs/evidence/critical_path_output.md |
| R-006 | Risk | Move-in & Install is critical-path; facilities “minimum readiness” may not align with install window | Facilities/Ops | High | <Ops Lead> | 2026-03-15 | Open | Weekly joint readiness review (Facilities+Ops); lock install window; contingency install plan if readiness slips | docs/evidence/critical_path_output.md |
| R-007 | Risk | SAT/Commissioning on critical path; safety/EHS signoff timing could block power-on | EHS/Safety | Med | <EHS Lead> | 2026-03-25 | Open | Pre-review LOTO + interlock validation plan; schedule EHS walkdown early; create SAT safety checklist evidence pack | docs/gates/checklists/G5_SAT_COMMISSIONING_CHECKLIST.md |
| D-008 | Decision | Proceed with “release lock” policy for FAT to prevent late churn (PLC/FW/HMI + IO map) | Controls | Med | <PM> | 2026-02-10 | Proposed | Publish release lock rules; create CR template usage; communicate rollback + retest scope | docs/raids/DECISION_LOG.md |

