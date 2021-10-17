#!/usr/bin/env python

import sys
import os

try:
   import func_reverse
except Exception as e:
   sys.stderr.write("error: failed to import func_reverse\n")
   sys.stderr.write(str(e))
   sys.stderr.write("\n")
   sys.exit(1)

a = [1,2,3,4,5]
print a
print "swap positions 0 and 4"
func_reverse.swap(a,0,4)
print a
print "swap positions 1 and 3"
func_reverse.swap(a,1,3)
print a
print "swap positions 2 and 2"
func_reverse.swap(a,2,2)
print a

a = []
b = [2]
c = [3,2,1]
d = [5,4,3,2,1]
e = ["apple", "orange", "pear"]
f = [True, False]
g = range(20)

for v in [a,b,c,d,e,f,g]:
   print "reversing:", v
   func_reverse.reverse(v)
   print "  ", v

import random
a = [random.randint(0,100) for v in range(20)]
b = sorted(a[:])
b.reverse()
b = tuple(b)

i = 0
while i < len(a):
   p = i
   j = i+1
   while j < len(a):
      if a[j] < a[p]:
         p = j
      j = j + 1
   func_reverse.swap(a,i,p)
   i = i + 1

a.reverse()
a = tuple(a)

print "Blind test:", a == b

