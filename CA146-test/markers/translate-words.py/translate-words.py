#!/usr/bin/env python

import sys

words = {}
file = sys.argv[1]

with open(file) as f:
   for line in f.readlines():
      details = line.split()
      words[details[0]] = details[1]

for line in sys.stdin.readlines():
   ws = line.split()
   i = 0
   while i < len(ws):
      word = ws[i]
      if word in words:
         ws[i] = words[word]
      i = i + 1
   sys.stdout.write(" ".join(ws) + "\n")


