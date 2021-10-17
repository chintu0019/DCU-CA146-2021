#!/usr/bin/env python3

n = 5

# Keep track of the total as we go along
total = 0

# The first number starts at position 0
start = 0

# Read the line
s = input()

# There are five numbers, so we need a loop which goes around n (5) times
i = 0
while i < n:
   # Begin searching for the "end" at the "start" of the current number
   end = start
   while end < len(s) and s[end] != "+":
      end = end + 1

   # Uncomment this line if you want to see how things are working
   # print start, end, s[start, end]

   # Add the current number
   total = total + int(s[start:end])

   # The next number starts after the "+" sign, so one position after "end"
   start = end + 1

   i = i + 1

print(total)
