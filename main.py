import sys

CANONICAL_ORDER = ["setup", "lint", "build", "test", "security", "artifact", "deploy"]

for raw in sys.stdin:
    line = raw.rstrip("\n").strip()
    if not line: continue
    if line.startswith("ORDER "):
        stages = line[6:].split(",")
        # TODO: reorder `stages` to follow CANONICAL_ORDER.
        # - Stages that appear in CANONICAL_ORDER should come first, sorted by
        #   their position in CANONICAL_ORDER.
        # - Any stage NOT in CANONICAL_ORDER goes at the end, keeping its
        #   original relative order from the input.
        # - Print the result as a comma-separated list.
        print(",".join(stages))
