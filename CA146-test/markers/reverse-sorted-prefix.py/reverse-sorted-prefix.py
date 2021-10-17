#!/usr/bin/env python

ns = []

line = raw_input()
while line != "end" and (len(ns) == 0 or ns[len(ns)-1] <= int(line)):
   ns.append(int(line))
   line = raw_input()

i = 0
while i < len(ns):
   print ns[len(ns) - i - 1]
   i = i + 1

