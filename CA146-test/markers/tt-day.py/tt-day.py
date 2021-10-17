#!/usr/bin/env python3

timetable = []

line = input()
while line != "end":
   timetable.append(line)
   line = input()

day = input()

i = 0
while i < len(timetable):
   parse = timetable[i].split()
   if parse[0] == day:
      print(timetable[i])
   i = i + 1
