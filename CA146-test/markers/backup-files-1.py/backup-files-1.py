#!/usr/bin/env python3

import os

files = os.listdir(".")
backup_extension = "bak"

i = 0
while i < len(files):
   file_name = files[i]
   tokens = file_name.split(".")
   extension = tokens[len(tokens) - 1]
   if extension != backup_extension:
      with open(file_name) as f:
         content = f.read()

      backup_name = file_name + "." + backup_extension
      with open(backup_name, "w") as f:
         f.write(content)

   i = i + 1
