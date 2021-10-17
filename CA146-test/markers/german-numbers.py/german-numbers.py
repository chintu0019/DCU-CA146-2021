#!/usr/bin/env python3

import sys

# It is not necessary to build the dictionary this way
# (but it's easier to type).
#
english = "one two three four five six seven eight nine ten".split()
german = "eins zwei drei vier funf sechs sieben acht neun zehn".split()
d = {}

i = 0
while i < len(english):
   d[english[i]] = german[i]
   i = i + 1

words = sys.stdin.read().split()

i = 0
while i < len(words):
   print(d[words[i]])
   i = i + 1
