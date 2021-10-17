#!/usr/bin/env python3

a = [17421, 9455, 13834, 16724, 18498]
total = 0

i = 0
while i < len(a):
   total = total + (int(input()) - a[i])
   i = i + 1

print(total)
