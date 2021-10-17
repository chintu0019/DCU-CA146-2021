#!/usr/bin/env python3

n = int(input())
base = 16
s = ""

# We use the position i in the following string to map i to the
# required hexadecimal digit.  So, the "a" below, is at
# position 10, and the f is at position 15.
#
digits = "0123456789abcdef"

while 0 < n:
   s = digits[n % base] + s
   n = n // base

print(s)
