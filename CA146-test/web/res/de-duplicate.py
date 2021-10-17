#!/use/bin/env python3

# This is a re-implementation of the week-09 task "de-duplicate.py.
#
# It demonstrates an approach to emulating hash tables with lists,
# thereby transforming an O(n^2) algorithm into an O(n) algorithm.

import sys

words = sys.stdin.read().split()

n = len(words) * 10 // 7  # This should give 70% occupancy.
seen = []

i = 0
while i < n:
   seen.append([])
   i = i + 1

def contains(value):
   return value in seen[hash(value) % n]

def add(value):
   seen[hash(value) % n].append(value)

i = 0
while i < len(words):
   if not contains(words[i]):
      add(words[i])
      sys.stdout.write(words[i] + "\n")
   i = i + 1
