#!/usr/bin/env python

import sys

def is_terminator(word):
   return word[len(word) - 1] in [".", "?", "!"]

def output_paragraph(words):
   i = 0
   while i < len(words):
      j = i
      while j < len(words) and not is_terminator(words[j]):
         j = j + 1

      j = j + 1
      words[i] = words[i].capitalize()
      print " ".join(words[i:j])

      i = j

paragraphs = sys.stdin.read().strip().split("\n\n")

i = 0
while i < len(paragraphs):
   words = paragraphs[i].strip().split()
   if 0 < i:
      print
   output_paragraph(words)
   i = i + 1

