#!/usr/bin/env python

import sys
import os
task = os.environ["TASK"]

try:
   execfile(task)
except IndexError as err:
   print "ok"
   sys.exit(0)
