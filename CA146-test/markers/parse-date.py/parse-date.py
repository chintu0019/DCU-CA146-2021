#!/usr/bin/env python3

s = input()

day_end = 0
while day_end < len(s) and s[day_end] != " ":
   day_end += 1

date_start = day_end + 1
date_end = date_start + 1
while date_end < len(s) and s[date_end] != " ":
   date_end += 1

month_start = date_end + 1
month_end = month_start + 1
while month_end < len(s) and s[month_end] != ",":
   month_end = month_end + 1

year_start = month_end + 2

month = s[month_start:month_end]
date = s[date_start:date_end]
year = s[year_start:]
day = s[0:day_end]

print(month, date + ",", year, "(" + day + ")")
