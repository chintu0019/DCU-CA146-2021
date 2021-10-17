#!/usr/bin/env python3

import os
task = os.environ["TASK"]

a = "".split()

print("a =", a)
print("running your script...")
print()

exec(open(task).read())
