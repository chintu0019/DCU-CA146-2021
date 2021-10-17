#!/usr/bin/env python3

# Calculate greatest common divisor of two integers (read from standard
# input) using Euclid's algorithm.

a = int(input())
b = int(input())

while b != 0:
   old_a = a
   a = b
   b = old_a % b

print(a)
