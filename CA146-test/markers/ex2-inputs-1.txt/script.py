#!/usr/bin/env python3

a = [4508, 22068, 26974, 20057, 30726]
total = 0

i = 0
while i < len(a):
   total = total + (int(input()) - a[i])
   i = i + 1

print(total)
