#!/usr/bin/env python3

n = 10000000  # Ten million.
a = []

i = 0
while i < n:
   b = a                # <-- This is needed to disable an optimisation implemented
   a = a + [i]          #     by the Python interpreter.
   #
   if i % 1000 == 0:    # One thousand.
      print(i)
   #
   i = i + 1
