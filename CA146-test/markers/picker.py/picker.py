#!/usr/bin/env python3

a = int(input())
b = int(input())
c = int(input())

print((1 + c) % 2 * a + c % 2 * b)
#     |         |       |   |
#     -----------       -----
#     A                 B
#
# Expressions A and B both use modulus two.
#
# One of them will be 0, and the other will be 1.
#
# Multiplying by 0 makes the value "go away", whereas multiplying
# by 1 leaves the value unchanged.
