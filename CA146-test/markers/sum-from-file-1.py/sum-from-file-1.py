#!/usr/bin/env python3

with open("numbers.txt") as f:
   lines = f.readlines()

total = 0

i = 0
while i < len(lines):
   total = total + int(lines[i])
   i = i + 1

print(total)
