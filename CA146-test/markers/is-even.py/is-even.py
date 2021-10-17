#!/usr/bin/env python3

n = int(input())

print(n // 2 * 2 == n)

# The task statement states that we may not use the modulus operator.
#
# Instead, we take advantage of the fact that, for odd numbers, integer
# division discards the remainder.  So, if we divide by 2 then multiply by 2,
# we do not get back to where we started.
