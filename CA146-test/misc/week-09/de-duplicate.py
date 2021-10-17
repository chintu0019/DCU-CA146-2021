#!/use/bin/env python3

import sys

words = sys.stdin.read().split()
seen = []

i = 0
while i < len(words):
   j = 0
   while j < len(seen) and seen[j] != words[i]:
      j = j + 1

   if j == len(seen):
      seen.append(words[i])
      sys.stdout.write(words[i] + "\n")
   i = i + 1
