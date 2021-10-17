#!/usr/bin/env python

# Example input line:
# Write a Python script named +pp-extract-lines.py+ which copies ...
#                              |                  |
#                              | i                | j

line = raw_input()
while line != "end":

   i = 0                                    # Linear search.
   while i < len(line) and line[i] != "+":  #
      i = i + 1                             #
   i = i + 1                                # Advance to first char. of task name.

   j = i                                    # Linear search, again.
   while j < len(line) and line[j] != "+":  #
      j = j + 1                             #

   if j < len(line):                        # Did we find an apparent task name?
      text = line[i:j]

      if 4 <= len(text) and text[len(text)-3:] == ".py":
         print text

   line = raw_input()
