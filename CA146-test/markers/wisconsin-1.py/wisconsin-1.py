#!/usr/bin/env python3

state = "WI"

# Discard the header line.
s = input()

s = input()
while s != "end":
   # Linear search to find the dirst comma; this is the start of the
   # "state" field.
   i = 0
   while i < len(s) and s[i] != ",":
      i = i + 1

   if i < len(s):
      # Pick out the state code.  They are all two-letter codes (but that
      # actually doesn't matter, all that matters is "WI" is a two-leter
      # code).
      code = s[i + 1:i + 3]
      if code == state:
         # The name of the city is everything up to but excluding the
         # position of the first comma.
         print(s[:i])

   s = input()
