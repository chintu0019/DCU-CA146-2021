#!/usr/bin/env python

import os

rabbits = 10

print "rabbits:", rabbits
print "  executing..."
execfile(os.environ.get("TASK"))
print "  variable rabbits is now", rabbits

print

rabbits = 123

print "rabbits:", rabbits
print "  executing..."
execfile(os.environ.get("TASK"))
print "  variable rabbits is now", rabbits

