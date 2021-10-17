#!/usr/bin/env python3

import sys

try:
   exec(sys.stdin.read())
except BrokenPipeError:
   pass
