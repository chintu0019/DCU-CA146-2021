#!/usr/bin/env python3

import os

extension = "py"
files = os.listdir(".")

i = 0
while i < len(files):
   tokens = files[i].split(".")
   if tokens[len(tokens) - 1] == extension:
      print(files[i])
   i = i + 1
