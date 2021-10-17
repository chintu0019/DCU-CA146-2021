#!/usr/bin/env python3

x = int(input())
y = int(input())
r = int(input())

print(x * x + y * y < r * r)

# We're using Pythagoras' Theorem, here.  There's no need to take the square roots,
# because that does not change the relative magnitudes.
#
# This task is best solved by first sketching a couple of cases on paper.
