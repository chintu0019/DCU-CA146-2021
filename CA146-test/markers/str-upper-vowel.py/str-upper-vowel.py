#!/usr/bin/env python

import sys

line = raw_input()
vowels = "AEIOU"

while line != "end":
   i = 0
   while i < len(vowels):
      if 0 <= line.find(vowels[i]):
         print line
         i = len(vowels)
      i += 1
   line = raw_input()
