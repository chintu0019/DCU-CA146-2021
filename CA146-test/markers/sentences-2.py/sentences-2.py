#!/usr/bin/env python3

import sys
words = sys.stdin.read().split()

terminators = {
   ".": True,
   "?": True,
   "!": True,
}

i = 0
while i < len(words):
   j = i
   while j < len(words) and words[j][len(words[j]) - 1] not in terminators:
      j = j + 1

   j = j + 1
   sentence = " ".join(words[i:j])
   sentence = sentence[0].capitalize() + sentence[1:]
   print(sentence)

   i = j
