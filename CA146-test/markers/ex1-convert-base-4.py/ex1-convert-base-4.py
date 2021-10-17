#!/usr/bin/env python

import sys

number = sys.argv[1]
base = int(sys.argv[2])
base2 = int(sys.argv[3])
v = 0

for d in number:
   v *= base
   v += int(d)

ds = []

while 0 < v:
   ds.append(v % base2)
   v = v / base2

for i in range(len(ds)):
   print ds[len(ds)-1-i]

