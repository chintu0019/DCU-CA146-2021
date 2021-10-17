#!/usr/bin/env python

import sys

text = sys.stdin.read()
count = 0

i = 0
while i < len(text):
   if "0" <= text[i] and text[i] <= "9":
      count = count + 1
   i = i + 1

print count
