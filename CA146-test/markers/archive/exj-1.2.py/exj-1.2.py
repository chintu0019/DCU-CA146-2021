#!/usr/bin/env python3

home_score = home_goals * 3 + home_points
away_score = away_goals * 3 + away_points

if home_score < away_score:
   print("away win")
elif away_score < home_score:
   print("home win")
else:
   print("draw")
