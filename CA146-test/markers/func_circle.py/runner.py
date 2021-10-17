#!/usr/bin/env python

import sys
import os

try:
   import func_circle
except Exception as e:
   sys.stderr.write("error: failed to import func_circle\n")
   sys.stderr.write(str(e))
   sys.stderr.write("\n")
   sys.exit(1)

for r in range(20):
   print "testing circumference:", r
   print "  ", func_circle.circumference(r)
   print "testing area:", r
   print "  ", func_circle.area(r)
   r = r + 0.5
   print "testing circumference:", r
   print "  ", func_circle.circumference(r)
   print "testing area:", r
   print "  ", func_circle.area(r)

