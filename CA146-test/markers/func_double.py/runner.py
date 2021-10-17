#!/usr/bin/env python

import sys

try:
   import func_double
except Exception as e:
   sys.stderr.write("error: failed to import test file func_double\n")
   sys.stderr.write(str(e))
   sys.stderr.write("\n")
   sys.exit(1)

for v in [7, 10, 0, -2, -5]:
   print "testing integer double:", v
   print "  ", func_double.double(v)

for v in ["twit twoo, ", "choo choo "]:
   print "testing string double:", v
   print "  ", func_double.double(v)

for v in [3.14, 1.0, 0.0]:
   print "testing float double:", v
   print "  ", func_double.double(v)

import random
n = random.randint(1,2000000000)
m = n * 2

print "testing a random integer:"
print "  ", func_double.double(n) == m
