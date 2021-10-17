#!/usr/bin/env python

import sys

s = sys.argv[1]

if len(s) < 5:
   s = "0" + s

sh = int(s[:2])
sm = int(s[3:])

print 60 * sh + sm
