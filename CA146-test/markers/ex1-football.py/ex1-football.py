#!/usr/bin/env python

hg = input()
hp = input()

ag = input()
ap = input()

hs = hg * 3 + hp
ws = ag * 3 + ap

if hs < ws:
   print "away win"
elif hs == ws:
   print "draw"
else:
   print "home win"

