#!/usr/bin/env python

import sys

s = sys.argv[1]

while s and s[0].isspace():
   s = s[1:]

while s and s[len(s)-1].isspace():
   s = s[:len(s)-1]

print s
