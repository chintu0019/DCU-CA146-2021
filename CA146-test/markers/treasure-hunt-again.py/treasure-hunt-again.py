#!/usr/bin/env python

import sys

words = sys.stdin.read().split()
d = {}

i = 0
while i < len(words)/2:
   d[words[2*i]] = words[2*i+1]
   i = i + 1

word = sys.argv[1]
while word in d:
   word = d[word]

print word
