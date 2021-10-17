#!/usr/bin/env python

import sys

n = int(sys.argv[1])
iterations = 10

def is_palindrome(n):
   s = str(n)
   return s == s[::-1]

while not is_palindrome(n) and 0 < iterations:
   a = n
   b = int(str(n)[::-1])
   n = a + b
   iterations -= 1

if is_palindrome(n):
   print n
else:
   print "none", n
