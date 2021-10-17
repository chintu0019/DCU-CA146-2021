#!/usr/bin/env python

import sys

banned = {}
with open("banned.txt") as f:
   words = f.read().split()

i = 0
while i < len(words):
   banned[words[i]] = True
   i = i + 1

lines = sys.stdin.readlines()

i = 0
while i < len(lines):
   tokens = lines[i].split()
   j = 0
   while j < len(tokens):
      if tokens[j] in banned:
         tokens[j] = "*" * len(tokens[j])
      j = j + 1

   print " ".join(tokens)
   i = i + 1
