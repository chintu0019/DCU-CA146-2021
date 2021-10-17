#!/usr/bin/env python3

import os
task = os.environ["TASK"]

a = range(12)
a = map(str, a)
s = " ".join(a)

print("s =", '"{}"'.format(s))
print("running your script...")
print()

exec(open(task).read())
