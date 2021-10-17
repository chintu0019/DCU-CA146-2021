#!/usr/bin/env python3

filename = "./translation.txt"

import sys

# This implementation uses a slightly unusual method for reading in
# the data; it is not necessary to read the input dictionary in this way.
#
# We read the translations into a single list.  The word pairs are at
# positions:
#    0 1
#    2 3
#    4 5
#
# The i-th English word is at position 2*i, and the i-th translated word
# is at position 2*i+1
#
# E.g.:
#    0   1    2   3    4     5    6    7
#    one eins two zwei three drei four vier
#    |        |        |          |            positions 2*i
#    |        |        |          |
#        |        |          |         |       positions 2*i+1
#        |        |          |         |

with open(filename) as f:
   words = f.read().split()

d = {}

i = 0
while i < len(words) / 2:
   d[words[i * 2]] = words[i * 2 + 1]
   i = i + 1

words = sys.stdin.read().split()

i = 0
while i < len(words):
   print(d[words[i]])
   i = i + 1
