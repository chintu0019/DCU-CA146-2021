#!/usr/bin/env python3

timetable = []

line = input()
while line != "end":
   timetable.append(line)
   line = input()

i = 0
while i < len(timetable):
   parse = timetable[i].split()
   print(" ".join(parse[5:]))
   i = i + 1
