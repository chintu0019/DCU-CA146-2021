#!/usr/bin/env python

import sys
name = sys.argv[1]

with open(name) as f:
   sys.stdout.write(f.read())
