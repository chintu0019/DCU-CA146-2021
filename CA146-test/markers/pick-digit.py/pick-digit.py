#!/usr/bin/env python3

n = int(input())
p = int(input())

print(n // (10 ** p) % 10)

# Example:
#
#     98765
#     3
#
# Dividing by (10 ** p) removes the digits which we don't care
# about, leaving:
#
#     98
#
# Then, modulus 10 picks off the last digit:
#
#     8
