#!/use/bin/env python3

import sys

words = sys.stdin.read().split()
seen = []

def contains(a, value):
   return value in a

def add(a, value):
   a.append(value)

i = 0
while i < len(words):
   if not contains(seen, words[i]):
      add(seen, words[i])
      sys.stdout.write(words[i] + "\n")
   i = i + 1
