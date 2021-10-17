#!/usr/bin/env python

# To swap the values in two variables, we need a temporary variable.
#
# To help think about the order:
#   1. begin by taking a copy of n; that can do no harm,
#   2. now we have a copy of n, it's safe to overwrite n with m,
#   3. lastly, install the original value of n (or, rather, the copy in tmp) in m.

tmp = n      # tmp: a temporary variable
n = m
m = tmp
