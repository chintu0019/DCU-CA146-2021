#!/usr/bin/env python3

n = int(input())
smallest = n

n = int(input())
while n != 0:
   if n < smallest:
      smallest = n
   n = int(input())

print(smallest)
