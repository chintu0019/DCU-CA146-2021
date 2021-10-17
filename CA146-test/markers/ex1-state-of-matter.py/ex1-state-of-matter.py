#!/usr/bin/env python3

temperature = int(input())

if temperature < 0:
   print("solid")
elif 100 < temperature:
   print("gas")
else:
   print("liquid")
