#!/usr/bin/env python3

# Read the input, printing out the even numbers as they are encountered, and
# appending the odd numbers to a list (odd_numbers), which we iterate over
# subsequently.

odd_numbers = []

s = input()
while s != "end":
   n = int(s)
   if n % 2 == 0:
      # Print the even numbers.
      print(n)
   else:
      # Save the odd numbers for later.
      odd_numbers.append(n)
   s = input()

# We have now read (and output) all of the even numbers.
# Next, output the odd numbers.
i = 0
while i < len(odd_numbers):
   print(odd_numbers[i])
   i = i + 1
