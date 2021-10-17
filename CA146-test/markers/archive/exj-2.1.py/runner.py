#!/usr/bin/env python3

import os
task = os.environ["TASK"]

lists = []
lists.append([7, 12, 20, 14, 20])
lists.append([20, 12, 20, 14, 20])
lists.append([20, 12, 20, 14, 21])
lists.append([20])
lists.append([1, 1, 1, 1, 1, 1, 1, 1])
lists.append([1, 1, 1, 1, 1, 2, 1, 1])
lists.append([1, 1, 3, 1, 1, 2, 1, 1])
lists.append([4, 1, 3, 1, 1, 2, 1, 1])
lists.append([4, 1, 3, 1, 1, 2, 1, 5])
lists.append([-10, -5, -5])

for a in lists:
   print("a =", a)
   with open(task) as f:
      exec(f.read())
