#!/usr/bin/env python3

total = 0

# n is always the most-recent number; the current number, if you like.
#
# (n % 2) will either be 0 (even) or 1 (odd).
#
# For each number, we multiply that term by either 0 or 1.  When we multiply by
# 0, the term disappears (even numbers), and when we multiply by 1 the term is
# added to the total (odd numbers).
#
# We add each term to the total as we go along, and print the total out when
# we're done.

n = int(input())
total = total + n * (n % 2)

n = int(input())
total = total + n * (n % 2)

n = int(input())
total = total + n * (n % 2)

n = int(input())
total = total + n * (n % 2)

n = int(input())
total = total + n * (n % 2)

n = int(input())
total = total + n * (n % 2)

n = int(input())
total = total + n * (n % 2)

n = int(input())
total = total + n * (n % 2)

n = int(input())
total = total + n * (n % 2)

n = int(input())
total = total + n * (n % 2)

print(total)
