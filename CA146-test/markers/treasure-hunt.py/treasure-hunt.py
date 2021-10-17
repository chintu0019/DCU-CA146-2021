#!/usr/bin/env python3

import os

filename = "start.txt"

while os.path.isfile(filename):
   with open(filename) as f:
      filename = f.read().rstrip()

print(filename)
