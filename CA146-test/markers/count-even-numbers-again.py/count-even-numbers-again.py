#!/usr/bin/env python3

count = 0

n = int(input())
while n != 0:
   count = count + (1 - n % 2)
   n = int(input())

print(count)
