#!/usr/bin/env python3

import os
task = os.environ["TASK"]

s = "dog  cat   mouse hen"

print("s =", '"{}"'.format(s))
print("running your script...")
print()

exec(open(task).read())
