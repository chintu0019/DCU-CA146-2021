#!/usr/bin/env python

__name__ = "einstein"

import os
task = os.environ["TASK"]

a = [1, 5, 6, 6, 10, 12]
v = 8

p = 0
while p < len(a) + 1:
   print "---"
   print "a =", a
   print "p =", p
   print "v =", v
   snap = (a[:], p, v)
   execfile(task)
   print "   ", a
   (a, p, v) = snap
   p = p + 1

a = []
p = 0
print "---"
print "a =", a
print "p =", p
print "v =", v
snap = (a[:], p, v)
execfile(task)
print "   ", a
