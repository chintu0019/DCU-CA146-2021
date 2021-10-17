#!/usr/bin/env python3

import os
task = os.getenv("TASK")

tuples = [
      (4,4,4),
      (14,14,14),
      (1,1,1),
      (2,4,4),
      (4,2,4),
      (4,4,2),
      (2,4,2),
      (2,4,3),
      (5,6,44)
      ]

for tup in tuples:
   print("-----------------")
   (x, y, z) = tup
   print("x =", x)
   print("y =", y)
   print("z =", z)
   with open(task) as f: exec(f.read())
