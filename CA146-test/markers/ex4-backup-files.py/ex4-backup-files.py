#!/usr/bin/env python

backup_extension = "bak"

import os
files = os.listdir(".")

i = 0
while i < len(files):
   file_name = files[i]
   if file_name.split(".")[-1] != backup_extension:
      with open(file_name) as f:
         content = f.read()

      backup_name = file_name + "." + backup_extension
      with open(backup_name, "w") as f:
         f.write(content)

   i = i + 1
