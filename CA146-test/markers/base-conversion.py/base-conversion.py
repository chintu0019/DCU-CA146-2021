#!/usr/bin/env python

n = input()
base = input()

digits = 1
while base ** digits <= n:
   digits = digits + 1

i = 0
while i < digits:
   power = base ** (digits - i - 1)
   print n / power
   n = n % power
   i = i + 1

