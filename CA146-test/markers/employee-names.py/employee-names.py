#!/usr/bin/env python

people = []

s = raw_input()
while s != "end":
   people.append(s)
   s = raw_input()

s = raw_input()
while s != "end":
   i = 0                                         # Linear search.
   while i < len(people) and people[i][:8] != s: #
      i = i + 1                                  #

   if i < len(people):
      print people[i][9:]                        # Print the name.
   s = raw_input()
