#!/usr/bin/env python

punctuation = ". , : ; ? ! 's ( ) [ ] { } - _".split()
punctuation.append("'")
punctuation.append('"')

import sys
text = sys.stdin.read()

i = 0
while i < len(punctuation):
   text = " ".join(text.split(punctuation[i]))
   i = i + 1

words = text.split()
counts = {}

i = 0
while i < len(words):
   word = words[i]
   if 2 < len(word):
      if word not in counts:
         counts[word] = 0
      counts[word] += 1
   i = i + 1

maximum_word = None
maximum_count = 0

for word in counts:
   if maximum_count < counts[word]:
      maximum_word = word
      maximum_count = counts[word]

print maximum_word, maximum_count
