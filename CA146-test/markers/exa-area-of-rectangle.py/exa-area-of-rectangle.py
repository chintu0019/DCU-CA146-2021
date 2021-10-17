#!/usr/bin/env python3

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if x1 < x2:
   xd = x2 - x1
else:
   xd = x1 - x2

if y1 < y2:
   yd = y2 - y1
else:
   yd = y1 - y2

print(xd * yd)
