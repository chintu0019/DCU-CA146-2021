#!/usr/bin/env python3

import os

x = 5

print("variable x is", x)
for v in range(10):
   print("executing", os.environ.get("TASK"), "...")
   exec(open(os.environ.get("TASK")).read())
   print("variable x is", x)
