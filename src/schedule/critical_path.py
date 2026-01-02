#!/usr/bin/env python3

"""
Compute a simple critical path for a task list in CSV form.

CSV columns:
task_id, task_name, domain, owner, start_date, end_date, depends_on

depends_on can be empty or a semicolon-separated list of task_ids.

This script:
- Parses tasks
- Builds a dependency DAG
- Computes earliest finish / latest finish
- Prints critical tasks (zero slack)
"""
import csv
from dataclasses import dataclass
from datetime import datetime
from typing import Dict, List, Optional, Set

DATE_FMT = "%Y-%m-%d"

@dataclass
class Task:
    task_id: str
    name: str
    start: datetime
    end: datetime
    deps: List[str]

    @property
    def duration_days(self) -> int:
        return max(1, (self.end - self.start).days + 1)

def parse_csv(path: str) -> Dict[str, Task]:
    tasks: Dict[str, Task] = {}
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            tid = row["task_id"].strip()
            deps_raw = (row.get("depends_on") or "").strip()
            deps = [d.strip() for d in deps_raw.split(";") if d.strip()]
            start = datetime.strptime(row["start_date"].strip(), DATE_FMT)
            end = datetime.strptime(row["end_date"].strip(), DATE_FMT)
            tasks[tid] = Task(task_id=tid, name=row["task_name"].strip(), start=start, end=end, deps=deps)
    return tasks

def topo_sort(tasks: Dict[str, Task]) -> List[str]:
    # Kahn
    incoming = {t: set(tasks[t].deps) for t in tasks}
    for t in list(incoming):
        incoming[t] = {d for d in incoming[t] if d in tasks}
    order: List[str] = []
    ready = [t for t, deps in incoming.items() if not deps]
    while ready:
        n = ready.pop()
        order.append(n)
        for m, deps in incoming.items():
            if n in deps:
                deps.remove(n)
                if not deps and m not in order and m not in ready:
                    ready.append(m)
    if len(order) != len(tasks):
        missing = set(tasks) - set(order)
        raise ValueError(f"Cycle or missing deps detected; unresolved: {sorted(missing)}")
    return order

def critical_path(tasks: Dict[str, Task]) -> None:
    order = topo_sort(tasks)

    # Earliest start/finish in days offset from project start
    project_start = min(tasks[t].start for t in tasks)
    es: Dict[str, int] = {}
    ef: Dict[str, int] = {}
    for t in order:
        deps = [d for d in tasks[t].deps if d in tasks]
        es[t] = max((ef[d] for d in deps), default=0)
        ef[t] = es[t] + tasks[t].duration_days

    project_duration = max(ef.values(), default=0)

    # Latest start/finish
    ls: Dict[str, int] = {}
    lf: Dict[str, int] = {}
    for t in reversed(order):
        # successors: tasks that depend on t
        succ = [s for s in tasks if t in tasks[s].deps]
        lf[t] = min((ls[s] for s in succ), default=project_duration)
        ls[t] = lf[t] - tasks[t].duration_days

    print(f"Project start: {project_start.date()}  |  Duration (days): {project_duration}")
    print("\nTasks (sorted by earliest start):")
    rows = []
    for t in sorted(tasks, key=lambda x: es[x]):
        slack = ls[t] - es[t]
        rows.append((t, es[t], ef[t], ls[t], lf[t], slack, tasks[t].name))
    for r in rows:
        tid, _es, _ef, _ls, _lf, slack, name = r
        flag = "CRITICAL" if slack == 0 else ""
        print(f"{tid:>4}  ES:{_es:>3} EF:{_ef:>3}  LS:{_ls:>3} LF:{_lf:>3}  Slack:{slack:>3}  {flag:>8}  {name}")

    critical = [tid for tid, *_ in rows if (ls[tid] - es[tid]) == 0]
    print("\nCritical path tasks:", " -> ".join(critical))

if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("csv_path", help="Path to ims_tasks.csv")
    args = ap.parse_args()
    tasks = parse_csv(args.csv_path)
    critical_path(tasks)
