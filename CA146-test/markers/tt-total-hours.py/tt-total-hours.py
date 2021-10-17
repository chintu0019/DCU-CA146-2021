#!/usr/bin/env python3

timetable = []

line = input()
while line != "end":
   timetable.append(line)
   line = input()

total_hours = 0

i = 0
while i < len(timetable):
   parse = timetable[i].split()
   total_hours = total_hours + int(parse[2])
   i = i + 1

print(total_hours)
