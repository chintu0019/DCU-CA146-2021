#!/usr/bin/env python3

import os
task = os.environ["TASK"]

d = {}
d["fish"] = "school"
d["dogs"] = "pack"
d["sheep"] = "flock"
d["cows"] = "herd"

print("d =", d)
print("running your script...")
print()

exec(open(task).read())
