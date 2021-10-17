#!/usr/bin/env python3

# The data structure here is a dictionary of dictionaries.
#
# The keys for the outer dictionary are user names.
#
# The keys for the inner dictionaries are task names.
#
# The values for the task names are Booleans. Example:
#
# {
#    "john": {
#               "some-task.py": True,
#               "some-other-task.py": False,
#            },
# }
#
# Other approaches are possible.

import sys

students = {}
lines = sys.stdin.read().split()

i = 0
while i < len(lines):
   tokens = lines[i].strip().split("/")
   student = tokens[0]
   tokens = tokens[1].split(".")
   task = ".".join(tokens[:2])
   result = tokens[2]
   # If this is the first time that we've seen this student, then
   # create an entry for them.
   if student not in students:
      students[student] = {}
   # Set the task status to either True or False.
   students[student][task] = result == "correct"
   i = i + 1

for student in students:
   # Add up the number of correct tasks for this student.
   count = 0
   for task in students[student]:
      if students[student][task]:
         count = count + 1

   print(student, count)
