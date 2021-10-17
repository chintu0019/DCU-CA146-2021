#!/usr/bin/env python3

import sys

text = sys.stdin.read()
count = 0

i = 0
while i < len(text):
   if "A" <= text[i] and text[i] <= "Z":
      count = count + 1
   i = i + 1

print(count)
