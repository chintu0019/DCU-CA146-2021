#!/usr/bin/env python

import os

extension = ".py"
files = os.listdir(".")

i = 0
while i < len(files):
   if files[i][len(files[i])-len(extension):] == extension:
      with open(files[i]) as f:
         if len(f.read()) != 0:
            print files[i]
   i = i + 1
