#!/usr/bin/env python

import sys
import os

try:
   import func_selection_sort
except Exception as e:
   sys.stderr.write("error: failed to import func_selection_sort\n")
   sys.stderr.write(str(e))
   sys.stderr.write("\n")
   sys.exit(1)

b = []
c = [1]
d = [3,6,423,45,87,2,4]
e = ["one", "two", "three", "four", "five"]
f = "Mary had a little lamb its fleece was white as snow".split()

for a in [b,c,d,e,f]:
   print "testing selection_sort:", a
   func_selection_sort.selection_sort(a)
   print "  ", a

import random
a = [random.randint(0,100) for v in range(20)]
b = tuple(sorted(a[:]))
func_selection_sort.selection_sort(a)
a = tuple(a)

print "Blind test:", a == b


