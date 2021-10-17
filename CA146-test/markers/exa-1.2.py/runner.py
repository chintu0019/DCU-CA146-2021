#!/usr/bin/env python

import os
task = os.environ["TASK"]

print "running your script with various combinations of goals and points..."
print

for home_goals in range(3):
   for home_points in range(3):
      for away_goals in range(3):
         for away_points in range(3):
            print home_goals, home_goals, away_goals, away_points,
            execfile(task)
