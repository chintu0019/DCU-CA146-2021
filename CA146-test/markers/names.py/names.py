#!/usr/bin/env python3

# Approach...
#
# One approach is to maintain two dictionaries, one for the boys names
# and one for the girls names.
#
# The approach here, though, uses just one dictionary.  That dictionary
# maps each name directly to the required sex for output (which we
# compute as the dictionary is constructed).

import sys

with open("boys.txt") as f:
   boys = f.read().split()

with open("girls.txt") as f:
   girls = f.read().split()

sex = {}

# First add all of the boys' names.
#
i = 0
while i < len(boys):
   sex[boys[i]] = "boy"
   i = i + 1

# Then add all of the girls' names.
#
i = 0
while i < len(girls):
   name = girls[i]
   if name in sex:
      sex[name] = "either"
   else:
      sex[name] = "girl"
   i = i + 1

names = sys.stdin.read().split()

i = 0
while i < len(names):
   print(names[i], sex[names[i]])
   i = i + 1
