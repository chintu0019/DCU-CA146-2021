#!/usr/bin/env python

import sys

words = sys.argv[1:]
max_len = 0

# Calculate max_len, the length of the longest "word".
i = 0
while i < len(words):
   word = words[i]
   if max_len < len(word):
      max_len = len(word)
   i = i + 1

# Output the "words", one per line, in a frame.
print "*" * (max_len + 4)

i = 0
while i < len(words):
   word = words[i]
   text = "* " + word + " " * (max_len - len(word)) + " *"
   print text
   i = i + 1

print "*" * (max_len + 4)
