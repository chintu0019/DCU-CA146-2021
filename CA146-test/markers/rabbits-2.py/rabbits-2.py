#!/usr/bin/env python

rabbits = rabbits * (2 ** 4) ** years

# 2 ** 4 is 16.
#
# Assume we start with 10 rabbits:
#
#     Years     Rabbits
#     0         10                            (multiply by 16 ** 0, which is 1)
#     1         10 * 16                       (multiply by 16 ** 1, which is 16)
#     2         10 * 16 * 16                  (multiply by 16 ** 2, which is 256)
#     3         10 * 16 * 16 * 16             (multiply by 16 ** 3)
#     4         10 * 16 * 16 * 16 * 16        (multiply by 16 ** 4)
#
# In the general case, the number of rabbits is:
#   - 10 * (16 ** years)
