#!/usr/bin/env python3

# Approach...
# Maintain a count of the number of times that we've seen
# each word.  When we're done, print out each word for
# which the count is 1.
#
# This is very similar to one of the tasks in the notes.

import sys

words = sys.stdin.read().split()
counts = {}

i = 0
while i < len(words):
   word = words[i]
   if word not in counts:
      counts[word] = 0
   counts[word] += 1
   i = i + 1

for word in counts:
   if counts[word] == 1:
      print(word)
