#!/usr/bin/env python3

import sys
field = sys.argv[1]

s = input()
position = 0
start = 0

# First find the start and end of the first header field.
#
end = 0
while end < len(s) and s[end] != ",":
   end = end + 1

# Keep going while we have not yet found the field which
# we are looking for.
#
while s[start:end] != field:
   # Find the start and end of the next header field.
   #
   position = position + 1
   start = end + 1

   end = start + 1
   while end < len(s) and s[end] != ",":
      end = end + 1

print(position)
