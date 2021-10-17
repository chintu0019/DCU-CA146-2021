#!/usr/bin/env python3

import os

files = os.listdir(".")
backup = "bak"

i = 0
while i < len(files):
   file_name = files[i]
   tokens = file_name.split(".")
   extension = tokens[len(tokens) - 1]
   if 1 < len(tokens) and extension == backup and os.path.isfile(file_name):
      os.unlink(file_name)
   i = i + 1
