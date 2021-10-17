#!/usr/bin/env python3

s = input()

i = 0
while i < len(s) and s[i] != '*':
   i = i + 1

j = i + 1
while j < len(s) and s[j] != '*':
   j = j + 1

if j < len(s):
   print(s[i + 1:j])
