#!/usr/bin/env python3

if __name__ == "__main__":
   a = ["", "", "dog", "", "", "cat", "", "", "", "mouse"]

count = 0

i = 0
while i < len(a):
   if 0 < len(a[i]):
      count = count + 1
   i = i + 1

print(count)
