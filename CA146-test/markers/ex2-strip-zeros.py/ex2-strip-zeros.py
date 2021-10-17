#!/usr/bin/env python

s = raw_input()
while s != "end":
   # Approach...
   # We use linear search to find the position of the first
   # non-zero digit.  (So, we keep going while the digit is
   # in fact "0".)
   #
   # Tweak...
   # Every number contains at least one digit.  Therefore, we
   # continue while i < len(s)-1.  This means that i never
   # "falls entirely off of the end" of the number, which in
   # turn means that we do not have to treat "0" and "000"
   # specially.

   n = len(s) - 1
   i = 0
   while i < n and s[i] == "0":
      i = i + 1

   print s[i:]
   s = raw_input()
