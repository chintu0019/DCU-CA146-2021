#!/usr/bin/env python

n = input()

print n * (n % 2)
#         |     |
#         -------
#
# For even n, this term will be 0, and we'll print 0.
#
# For odd n, this term will be 1, and we'll print the original number.
