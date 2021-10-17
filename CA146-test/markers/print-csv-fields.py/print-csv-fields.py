#!/usr/bin/env python3

lines = []

line = input()
while line != "end":
   lines.append(line)
   line = input()

column = int(input())

i = 0
while i < len(lines):
   line = lines[i]

   j = 0    # This counts the columns.
   k = 0    # The indexes into the line.
   while j < column:
      while k < len(line) and line[k] != ",":
         k = k + 1
      j = j + 1

      if 0 < k:
         k = k + 1

   start_position = k
   while k < len(line) and line[k] != ",":
      k = k + 1

   if start_position < k:
      print(line[start_position:k])

   i = i + 1
