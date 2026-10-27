import sys

CANONICAL_ORDER = ["setup", "lint", "build", "test", "security", "artifact", "deploy"]
order = {val: i for i, val in enumerate(CANONICAL_ORDER)}
for raw in sys.stdin:
    line = raw.rstrip("\n").strip()
    if not line: continue
    if line.startswith("ORDER "):
        stages = line[6:].split(",")
        res = sorted(stages, key=lambda x: order.get(x, len(CANONICAL_ORDER)))
        print(",".join(res))
