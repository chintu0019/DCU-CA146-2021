#!/usr/bin/env python3

n = int(input())

# The following is layed out specifically to make the symmetry of
# how we use arithmetic to extract individual digits clear.
#
# We're using base 10 here; bit with a little thought, to might be
# clear how this approach can be generalised to other bases
# (including binary).

print(n // 100 % 10)
print(n // 10 % 10)
print(n // 1 % 10)
