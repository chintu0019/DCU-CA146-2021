#!/usr/bin/env python

import sys
tries = int(sys.argv[1])
conversions = int(sys.argv[2])
penalties = int(sys.argv[3])

score = tries * 5 + conversions * 2 + penalties * 3
print score

