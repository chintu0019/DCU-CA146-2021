#!/usr/bin/env python

import sys

line = raw_input()
while line != "end":
   print line[::-1]
   line = raw_input()

