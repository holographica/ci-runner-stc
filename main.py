from itertools import product
import sys, json

"""
# stage 01
CANONICAL_ORDER = ["setup", "lint", "build", "test", "security", "artifact", "deploy"]
order = {val: i for i, val in enumerate(CANONICAL_ORDER)}
for raw in sys.stdin:
    line = raw.rstrip("\n").strip()
    if not line: continue
    if line.startswith("ORDER "):
        stages = line[6:].split(",")
        res = sorted(stages, key=lambda x: order.get(x, len(CANONICAL_ORDER)))
        print(",".join(res))
"""

"""
# stage 02
text = sys.stdin.read()
out_jobs = []
name = ""
runs_on = ""
for line in text.splitlines():
    line = line.strip()
    if line.startswith("job:"):
        name = line[5:]
    elif line.startswith("runs-on: "):
        runs_on = line[9:]
    elif line.startswith("- run: "):
        out_jobs.append(f"  STEP RUN {line[7:]}")
    elif line.startswith("- uses: "):
        out_jobs.append(f"  STEP USES {line[8:]}")

print(f"JOB {name} ON {runs_on}")
for job in out_jobs:
    print(job)
"""


# stage 03
matrix = {}
exclusions = []
for raw in sys.stdin:
    line = raw.rstrip("\n").strip()
    if not line: continue
    if line.startswith("EXCLUDE "):
        exclusions.append(dict(
            item.strip().split("=",1)
            for item in line[8:].split(",")
        ))
    else:
        k, vals = line.split(":", 1)
        matrix[k] = [v.strip() for v in vals.split(",")]

combos = []
for values in product(*matrix.values()):
    combo = dict(zip(matrix, values))

    if any(
        all(combo.get(k) == v for k, v in exc.items())
        for exc in exclusions
    ):
        continue
    combos.append(combo)

combos.sort(key=lambda c: (
    c.get("os", ""),
    c.get("python",""),
    c.get("arch", ""),
))

for combo in combos:
    print(",".join(f"{k}={v}" for k, v in combo.items()))