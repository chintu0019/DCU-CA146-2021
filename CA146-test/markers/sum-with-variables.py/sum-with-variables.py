#!/usr/bin/env python

import sys

lines = sys.stdin.readlines()

variables = {}
total = 0

i = 0
while i < len(lines):
   term = lines[i].strip()
   tokens = term.split("=")
   # Assignments.
   if len(tokens) == 2:
      variable = tokens[0].strip()
      variables[variable] = int(tokens[1])
   else:
      # Negative numbers.
      if 2 <= len(term) and term[0] == "-" and term[1:].isdigit():
         total += int(term)
      # Non-negative numbers.
      elif term.isdigit():
         total += int(term)
      # Variables.
      elif 0 < len(term):
         total += variables[term]
      # Only an empty line is left over.

   i = i + 1

print total

