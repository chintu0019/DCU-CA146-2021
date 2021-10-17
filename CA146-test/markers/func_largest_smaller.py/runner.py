#!/usr/bin/env python

import sys
import os

try:
   import func_largest_smaller
except Exception as e:
   sys.stderr.write("error: failed to import test file\n")
   sys.stderr.write(str(e))
   sys.stderr.write("\n")
   sys.exit(1)

#    0  1  2  3  4   5   6   7   8   9
a = [2, 4, 4, 7, 7, 7, 10, 10, 11, 20, 25]

assert func_largest_smaller.largest_smaller(a, 3) == 2
assert func_largest_smaller.largest_smaller(a, 4) == 2
assert func_largest_smaller.largest_smaller(a, 5) == 4
assert func_largest_smaller.largest_smaller(a, 7) == 4
assert func_largest_smaller.largest_smaller(a, 8) == 7
assert func_largest_smaller.largest_smaller(a, 9) == 7
assert func_largest_smaller.largest_smaller(a, 10) == 7
assert func_largest_smaller.largest_smaller(a, 11) == 10
assert func_largest_smaller.largest_smaller(a, 20) == 11
assert func_largest_smaller.largest_smaller(a, 25) == 20
assert func_largest_smaller.largest_smaller(a, 30) == 25
