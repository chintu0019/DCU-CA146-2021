#!/usr/bin/env python3

import sys

n = int(sys.argv[1])
s = input()

# Find the position of the start of the nth field.
#
start = 0
i = 0
while i < n:
   while start < len(s) and s[start] != ",":
      start = start + 1

   start = start + 1  # Jump over the comma.
   i = i + 1

# Find the position of the end of the nth field.
#
end = start + 1
while end < len(s) and s[end] != ",":
   end = end + 1

print(s[start:end])
