#!/usr/bin/env python

import os

rabbits = 10
years = 2

print "rabbits:", rabbits
print "years:", years
print "  executing..."
execfile(os.environ.get("TASK"))
print "  variable rabbits is now", rabbits

print

rabbits = 123
years = 5

print "rabbits:", rabbits
print "years:", years
print "  executing..."
execfile(os.environ.get("TASK"))
print "  variable rabbits is now", rabbits
print "  that's a lot of rabbits!"

