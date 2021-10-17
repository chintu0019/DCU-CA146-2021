#!/usr/bin/env python

ht = input()
hc = input()
hp = input()

at = input()
ac = input()
ap = input()

hs = ht * 5 + hc * 2 + hp * 3
aws = at * 5 + ac * 2 + ap * 3

if hs < aws:
   print "away win"
elif hs == aws:
   print "draw"
else:
   print "home win"
