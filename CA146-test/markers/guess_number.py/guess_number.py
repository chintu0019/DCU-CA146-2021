#!/usr/bin/env python

import secret_number

def play():
   low = 0
   high = 1024
   mid = low + ((high - low) / 2)
   result = secret_number.guess(mid)
   while result != "correct":
      if result == "too-high":
         high = mid
      else:
         low = mid + 1
      mid = low + ((high - low) / 2)
      result = secret_number.guess(mid)
