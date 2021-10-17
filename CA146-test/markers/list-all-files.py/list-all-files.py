#!/usr/bin/env python3

import os
dirs = ["."]

while len(dirs) != 0:
   d = dirs.pop()
   entries = os.listdir(d)
   i = 0
   while i < len(entries):
      path = d + "/" + entries[i]
      if os.path.isfile(path):
         print(path)
      else:
         dirs.append(path)
      i = i + 1
