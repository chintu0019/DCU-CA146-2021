#!/usr/bin/env python3

da = {}
db = {}

with open("a.txt") as f:
   a = f.read().split()

i = 0
while i < len(a):
   da[a[i]] = True
   i = i + 1

with open("b.txt") as f:
   b = f.read().split()

i = 0
while i < len(b):
   db[b[i]] = True
   i = i + 1

# There is no need to sort the keys; the Einstein marker does that.
#
for key in da:
   if key in db:
      print(key)
