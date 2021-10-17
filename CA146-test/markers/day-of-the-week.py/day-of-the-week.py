#!/usr/bin/env python3

# Externally, all ranges start from 1; for example, the months go from 1 to
# 12, the days from 1 to 7.
#
# Internally, the arithmetic turns out to be easier if all of the ranges start
# from 0; for example, 0 to 11.  This is not uncommon.
#
# To achieve this, we subtract one from each value as it is read in, and add
# one at the end, when the result is printed.

month = int(input()) - 1
day = int(input()) - 1

print((month * 30 + day) % 7 + 1)
