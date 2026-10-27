import sys, json

# CANONICAL_ORDER = ["setup", "lint", "build", "test", "security", "artifact", "deploy"]
# order = {val: i for i, val in enumerate(CANONICAL_ORDER)}
# for raw in sys.stdin:
#     line = raw.rstrip("\n").strip()
#     if not line: continue
#     if line.startswith("ORDER "):
#         stages = line[6:].split(",")
#         res = sorted(stages, key=lambda x: order.get(x, len(CANONICAL_ORDER)))
#         print(",".join(res))

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
