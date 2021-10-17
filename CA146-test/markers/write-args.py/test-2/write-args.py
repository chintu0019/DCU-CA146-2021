#!/usr/bin/env python

import sys

with open(sys.argv[1], "w") as f:
   f.write( "\n".join(sys.argv[2:]) + "\n"  )
