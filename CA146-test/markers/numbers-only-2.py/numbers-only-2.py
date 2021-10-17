#!/usr/bin/env python

import sys
words = sys.stdin.read().split()

i = 0
while i < len(words):
   word = words[i]
   if words[i][0] == "-":
      words[i] = words[i][1:]
   if words[i].isdigit():
      print word
   i = i + 1
