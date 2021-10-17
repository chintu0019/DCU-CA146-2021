#!/usr/bin/env python

import sys

employee_file = "employees.txt"
employees = {}

with open(employee_file) as f:
   lines = f.readlines()

i = 0
while i < len(lines):
   parse = lines[i].split()
   employees[parse[0]] = {
         "id": parse[0],
         "dob": parse[1],
         "name": " ".join(parse[2:])
         }
   i = i + 1

lines = sys.stdin.readlines()

i = 0
while i < len(lines):
   print employees[lines[i].strip()]["name"]
   i = i + 1

