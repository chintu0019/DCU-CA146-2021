#!/usr/bin/env python3

import sys

with open("irish-dobs.txt") as f_in:
   lines = f_in.readlines()

with open("american-dobs.txt", "w") as f_out:
   i = 0
   while i < len(lines):
      tokens = lines[i].split()
      date = tokens[0].split("/")
      tokens[0] = "/".join([date[1], date[0], date[2]])  # Replace the date.
      f_out.write(" ".join(tokens) + "\n")
      i = i + 1
