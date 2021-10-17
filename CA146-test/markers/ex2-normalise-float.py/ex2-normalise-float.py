#!/usr/bin/env python

s = raw_input()

# Find the position of the decimal point.
#
i = 0
while i < len(s) and s[i] != ".":
   i = i + 1

# If there's no decimal point, then add one.
#
if len(s) <= i:
   s = s + "."

# Strip leading zeros.
#
i = 0
while i < len(s) and s[i] == "0":
   i = i + 1

s = s[i:]

# Strip trailing zeros.
#
i = 0
while i < len(s) and s[len(s) - i - 1] == "0":
   i = i + 1

s = s[:len(s) - i]

# If there's no integer part, then add one.
#
if s[0] == ".":
   s = "0" + s

# If there's no fractional part, then add one.
#
if s[len(s) - 1] == ".":
   s = s + "0"

print s
