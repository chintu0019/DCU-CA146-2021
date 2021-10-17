#!/usr/bin/env python

import sys

with open("words-1.txt") as f:
   words = f.read().split()

d = {}

i = 0
while i < len(words):
   d[words[i]] = True
   i = i + 1

with open("words-2.txt") as f:
   words = f.read().split()

e = {}

i = 0
while i < len(words):
   if words[i] in d:
      e[words[i]] = True
   i = i + 1

for word in sorted(e):
   print word
