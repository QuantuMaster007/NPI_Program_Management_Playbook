# Decision Log (Template)

| Decision ID | Date | Decision | Options considered | Why (tradeoffs) | Impact (Schedule/Cost/Quality/Risk) | Approver | Follow-ups |
|---|---:|---|---|---|---|---|---|
| D-001 | 2026-01-01 | Establish “FAT Release Lock” (pin PLC/FW/HMI + IO map revision before FAT) | (A) Keep iterating versions through FAT (B) Lock versions for FAT + change control only | Prevents integration churn and improves evidence quality; may defer non-critical features | ↓ schedule risk on FAT; may require planned backport process; improves test repeatability | <Eng Dir> | Add release-lock note to weekly update; require CR for post-lock changes |
| D-002 | 2026-01-01 | Treat Facilities Network/VLAN as a gated prerequisite for Move-in/Install readiness | (A) Wait for full VLAN approval (B) Approve temporary isolated network workaround (C) Start install without network | Facilities is currently blocked; avoid last-minute install slip | Protects install window; may add small cost for temporary gear; reduces idle time risk | <Ops + Facilities> | Define acceptable workaround + security approval; update site readiness checklist |
| D-003 | 2026-01-01 | Enforce strict Change Control after HW Design Freeze (no “silent changes”) | (A) Informal changes allowed (B) Change control required + impact assessment | Design Freeze is on critical path; untracked changes create late surprises | ↓ risk of EVT/FAT slips; ↑ visibility; small process overhead | <HW Lead> | Publish CR workflow; add PR template impact fields; weekly review of CRs |

