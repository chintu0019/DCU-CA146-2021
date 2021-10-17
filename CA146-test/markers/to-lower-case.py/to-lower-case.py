#!/usr/bin/env python3

upper = "ABCDEFGHIFKLMNOPQRSTUVWXYZ"
lower = "abcdefghifklmnopqrstuvwxyz"

s = input()
while s != "end":
   t = ""

   i = 0
   while i < len(s):
      if "A" <= s[i] and s[i] <= "Z":
         # Upper case.
         # Linear search to find the position of this letter in upper,
         # then append the corresponmding letter from lower.
         j = 0
         while s[i] != upper[j]:
            j = j + 1
         t = t + lower[j]
      else:
         # Anything else.
         # Just append the current character.
         t = t + s[i]

      i = i + 1

   print(t)
   s = input()
