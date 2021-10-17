#!/usr/bin/env python3

import os, sys
task = os.environ["TASK"]

print("running your script with various combinations of goals and points...")
print()

for home_goals in range(3):
   for home_points in range(3):
      for away_goals in range(3):
         for away_points in range(3):
            print(home_goals, home_points, away_goals, away_points, "", end="")
            with open(task) as f:
               exec(f.read())
