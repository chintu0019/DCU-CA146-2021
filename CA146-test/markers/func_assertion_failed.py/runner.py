#!/usr/bin/env python

import sys
import os

try:
   import func_assertion_failed
except Exception as e:
   sys.stderr.write("error: failed to import test file\n")
   sys.stderr.write(str(e))
   sys.stderr.write("\n")
   sys.exit(1)

try:
   func_assertion_failed.failed()
except AssertionError:
   print "The exception was correctly raised, as expected."

