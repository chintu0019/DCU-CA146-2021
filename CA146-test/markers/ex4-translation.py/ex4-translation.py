#!/usr/bin/env python

import sys

translation = {}
filename = "translation.txt"

with open(filename) as f:
   lines = f.readlines()

i = 0
while i < len(lines):
   line = lines[i]
   details = line.split()
   translation[details[0]] = details[1]
   i = i + 1

lines = sys.stdin.readlines()

i = 0
while i < len(lines):
   words = lines[i].split()
   j = 0
   while j < len(words):
      word = words[j]
      if word in translation:
         words[j] = translation[word]
      j = j + 1
   sys.stdout.write(" ".join(words) + "\n")
   i = i + 1
