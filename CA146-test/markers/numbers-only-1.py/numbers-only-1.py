#!/usr/bin/env python

import sys
words = sys.stdin.read().split()

i = 0
while i < len(words):
   if words[i].isdigit():
      print words[i]
   i = i + 1
