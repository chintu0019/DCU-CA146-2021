#!/usr/bin/env python

prev = raw_input()
curr = raw_input()
while curr != prev:
   prev = curr
   curr = raw_input()

print "snap:", curr
