#!/usr/bin/env python

import sys

lines = sys.stdin.readlines()

for line in lines:
   details = line.split()
   hm = details[0].split(":")
   duration = int(details[1])
   h = int(hm[0])
   m = int(hm[1])
   m += duration
   h += m / 60
   m = m % 60

   if h < 10:
      details[1] = "0" + str(h)
   else:
      details[1] = str(h)

   details[1] += ":"

   if m < 10:
      details[1] += "0" + str(m)
   else:
      details[1] += str(m)

   print " ".join(details)
