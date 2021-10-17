#!/usr/bin/env python

import sys
import os


try:
   import tv_get_minutes
except Exception as e:
   sys.stderr.write("error: failed to import test file\n")
   sys.stderr.write(str(e))
   sys.stderr.write("\n")
   sys.exit(1)

for s in ["0:7", "10:30", "24:00"]:
   print "testing:", s
   print tv_get_minutes.get_minutes(s)
