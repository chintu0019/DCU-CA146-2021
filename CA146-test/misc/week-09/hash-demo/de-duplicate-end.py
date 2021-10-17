#!/use/bin/env python3

import sys

words = sys.stdin.read().split()

n = 7
seen = []

i = 0
while i < n:
   seen.append([])
   i = i + 1

def contains(a, value):
   return value in a[hash(value) % n]

def add(a, value):
   a[hash(value) % n].append(value)

i = 0
while i < len(words):
   if not contains(seen, words[i]):
      add(seen, words[i])
      sys.stdout.write(words[i] + "\n")
   i = i + 1

print(seen)
