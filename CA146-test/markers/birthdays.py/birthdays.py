#!/usr/bin/env python

import sys

dates = {}

def get_date(text):
    return "/".join(text.split("/")[:2])

with open("birthdays.txt") as f:
    lines = f.readlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        date = get_date(line)
        if date not in dates:
            dates[date] = []
        dates[date].append(" ".join(line.split()[1:]))
        i = i + 1

lines = sys.stdin.readlines()

i = 0
while i < len(lines):
    line = lines[i]
    date = get_date(line.strip())
    if date in dates:
        people = dates[date]
        j = 0
        while j < len(people):
            print people[j]
            j = j + 1
    i = i + 1
