#!/usr/bin/env python

import sys

haystack = sys.argv[1]
needle = sys.argv[2]

print haystack[:len(needle)] == needle

