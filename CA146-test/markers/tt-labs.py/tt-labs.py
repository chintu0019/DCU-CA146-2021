#!/usr/bin/env python3

timetable = []

line = input()
while line != "end":
   timetable.append(line)
   line = input()

i = 0
while i < len(timetable):
   parse = timetable[i].split()
   if 1 < int(parse[2]):
      print(timetable[i])
   i = i + 1
