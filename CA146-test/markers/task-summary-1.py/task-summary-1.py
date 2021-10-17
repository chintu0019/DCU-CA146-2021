#!/usr/bin/env python3

import sys

# status is dictionary mapping task names to either
# True or False.
status = {}
lines = sys.stdin.read().split()

i = 0
while i < len(lines):
   tokens = lines[i].split(".")
   task = ".".join(tokens[:2])
   result = tokens[2]
   # Update the status of "task" to it's most-recent
   # state. The expression below will either be True
   # or False.
   status[task] = result == "correct"
   i = i + 1

# There is no need to sort the tasks.  The Einstein
# marker does the sorting.
for task in status:
   if status[task]:
      print(task)
