#!/usr/bin/env python3

n = 10
base = 10
accumulator = 0

i = 0
while i < n:
   accumulator = accumulator * base + int(input())
   i = i + 1

i = 0
while i < n:
   print(accumulator % base)
   accumulator = accumulator // base
   i = i + 1
