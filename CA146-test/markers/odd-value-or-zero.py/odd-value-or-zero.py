#!/usr/bin/env python3

n = int(input())

print(n * (n % 2))
#         =======
#
# "%" is the modulus or remainder operator, it evaluates to the remainder
# after deviding one number by another (after dividing n by 2, here).
#
# Consider just the marked part of the expression.
#
# If n is odd, then the remainder after dividing by 2 will be 1, and
# multiplying n by 1 gives just n, as required.
#
# If n is even, then the remainder after dividing by 2 will be 0, and
# multiplying n by 0 gives just 0, as required.
