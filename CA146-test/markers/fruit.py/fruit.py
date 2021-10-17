#!/usr/bin/env python3

import sys

fruit = {
   "apple": True,
   "pear": True,
   "orange": True,
   "banana": True,
   "cherry": True,
}

words = sys.stdin.read().split()

i = 0
while i < len(words):
   if words[i] in fruit:
      print(words[i])
   i = i + 1
