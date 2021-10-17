#!/usr/bin/env python3

import os
task = os.getenv("TASK")

a = list(range(10))
print("a =", a)
with open(task) as f:
   exec(f.read())

print()
a = list(range(-10, 0))
print("a =", a)
with open(task) as f:
   exec(f.read())

print()
a = [3, 32, 33, -333]
print("a =", a)
with open(task) as f:
   exec(f.read())

print()
a = [313, 3132, 3133, -31333, -107]
print("a =", a)
with open(task) as f:
   exec(f.read())
