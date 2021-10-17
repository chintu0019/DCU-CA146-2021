#!/usr/bin/env python

import os

pi = 3
radius = 20

print "pi:", pi
print "radius:", radius
print "executing..."
execfile(os.environ.get("TASK"))
print "variable circumference is now", circumference

print

pi = 3.14
radius = 30

print "pi:", pi
print "radius:", radius
print "executing..."
execfile(os.environ.get("TASK"))
print "variable circumference is now", circumference



