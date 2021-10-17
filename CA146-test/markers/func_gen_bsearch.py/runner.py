#!/usr/bin/env python

import sys
import os

try:
   import func_gen_bsearch
except Exception as e:
   sys.stderr.write("error: failed to import test file\n")
   sys.stderr.write(str(e))
   sys.stderr.write("\n")
   sys.exit(1)

def reverse(s):
   return s[::-1]

def lt(a,b):
   return reverse(a) < reverse(b)

def ssort(a,lt):
   i = 0
   while i < len(a):
      p = i
      j = i + 1
      while j < len(a):
         if lt(a[j],a[p]):
            p = j
         j = j + 1

      # swap a[i] and a[p]
      tmp = a[p]
      a[p] = a[i]
      a[i] = tmp

      i = i + 1

#    0  1  2  3  4   5   6   7   8   9
a = [ "one", "two", "two", "three", "four", "four", "four", "five" ]
ssort(a,lt)

message = """A test failed.
Here's the SORTED test array:

{}

Can you work out the order that's being used?
It pretty unusual.
"""

message = message.format(a)

try:
   assert func_gen_bsearch.gen_bsearch(a, "one", lt) == 1
   assert func_gen_bsearch.gen_bsearch(a, "two", lt) == 3
   assert func_gen_bsearch.gen_bsearch(a, "three", lt) == 0
   assert func_gen_bsearch.gen_bsearch(a, "four", lt) == 5

   assert func_gen_bsearch.gen_bsearch(a, "aaa", lt) == 0
   assert func_gen_bsearch.gen_bsearch(a, "zzz", lt) == 8
except AssertionError as e:
   sys.stderr.write(message + "\n")
   raise e
