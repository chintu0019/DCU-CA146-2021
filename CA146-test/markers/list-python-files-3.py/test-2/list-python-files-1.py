#!/usr/bin/env python3

import os

extension = ".py"
files = os.listdir(".")

i = 0
while i < len(files):
   if files[i][len(files[i])-len(extension):] == extension:
      print files[i]
   i = i + 1
