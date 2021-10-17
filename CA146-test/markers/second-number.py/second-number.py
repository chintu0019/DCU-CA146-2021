#!/usr/bin/env python3

s = input()

# k is the outer loop variable.
# i is the potential start of a word (the first Linear Search).
# j is the potential end of a word (the second Linear Search).

j = 0
k = 0
while k < 2:
   i = j
   while i < len(s) and not ("0" <= s[i] and s[i] <= "9"):
      i = i + 1

   j = i
   while j < len(s) and ("0" <= s[j] and s[j] <= "9"):
      j = j + 1

   k = k + 1

if i < len(s):
   print(s[i:j], i)
