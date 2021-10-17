#!/usr/bin/env python3

vowel_as = 0  # Count of the number of "a"-s encountered.
vowel_es = 0  # Count of the number of "e"-s encountered.
vowel_is = 0  # Count of the number of "i"-s encountered.
vowel_os = 0  # Count of the number of "o"-s encountered.
vowel_us = 0  # Count of the number of "u"-s encountered.
others = 0    # Count of every other character.

s = input()
while s != "end":
   i = 0
   while i < len(s):
      if s[i] == "a" or s[i] == "A":
         vowel_as = vowel_as + 1
      elif s[i] == "e" or s[i] == "E":
         vowel_es = vowel_es + 1
      elif s[i] == "i" or s[i] == "I":
         vowel_is = vowel_is + 1
      elif s[i] == "o" or s[i] == "O":
         vowel_os = vowel_os + 1
      elif s[i] == "u" or s[i] == "U":
         vowel_us = vowel_us + 1
      else:
         others += 1
      i = i + 1
   #
   s = input()

print("a:", vowel_as)
print("e:", vowel_es)
print("i:", vowel_is)
print("o:", vowel_os)
print("u:", vowel_us)
print("other:", others)
