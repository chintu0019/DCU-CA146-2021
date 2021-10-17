#!/usr/bin/env python3

import sys

# cypher will be a dictionary which, for every character
# encountered in the pages, maps that character to a list
# of triplets which could be used to encode that character.
#
# E.g.
# {
#    "z":  ["6 5 12", "3 9 20"]
#    "\n": ["8 2 0", "9 12 20", "1 45 23"]
# }
#
# Note that spaces, punctuation and newline characters are all
# treated exactly the same.

cypher = {}
n = 10

i = 0
while i < n:
   file_name = "page-" + str(i) + ".txt"
   with open(file_name) as f:
      lines = f.readlines()
   #
   j = 0
   while j < len(lines):
      line = lines[j]
      k = 0
      while k < len(line):
         ch = line[k]
         if ch not in cypher:
            cypher[ch] = []
         triplet = str(i) + " " + str(j) + " " + str(k)
         cypher[ch].append(triplet)
         k = k + 1
      j = j + 1
   i = i + 1

# Next, we shuffle each list of triplets.  This is not necessary,
# and I do not expect student solutions to do this, but it generates
# better test data for the Einstein tests.
from random import shuffle
for ch in cypher:
   shuffle(cypher[ch])

text = sys.stdin.read()

i = 0
while i < len(text):
   print(cypher[text[i]].pop())
   i = i + 1
