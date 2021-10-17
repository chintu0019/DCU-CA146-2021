#!/usr/bin/env python3

import os
task = os.environ["TASK"]

d = {}
for k in range(6):
   d[k] = k * k

print("d =", d)
print("running your script...")
print()

exec(open(task).read())
