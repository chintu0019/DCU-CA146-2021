#!/usr/bin/env python

import os

sweets = 78
children = 5

print "sweets:", sweets
print "children:", children
print "  executing..."
execfile(os.environ.get("TASK"))
print "  variable sweets_left_over is now", sweets_left_over

print

sweets = 6796
children = 56

print "sweets:", sweets
print "children:", children
print "  executing..."
execfile(os.environ.get("TASK"))
print "  variable sweets_left_over is now", sweets_left_over

