#!/usr/bin/env python

ns = []
total = 0.0

line = raw_input()
while line != "end":
   n = int(line)
   total = total + n
   ns.append(n)
   line = raw_input()

if 0 < len(ns):
   average = total / len(ns)

   i = 0
   while i < len(ns):
      if average < ns[i]:
         print ns[i]
      i = i + 1
