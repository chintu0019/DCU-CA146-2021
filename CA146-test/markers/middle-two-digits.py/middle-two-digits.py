#!/usr/bin/env python3

n = int(input())

n = n // 100 % 100
print(n)

# Example:
#
#   123456
#   123456 // 100 -> 1234
#   1234 % 100 -> 34 (which are the middle two digits).
