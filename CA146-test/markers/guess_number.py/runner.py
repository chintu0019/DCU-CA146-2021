#!/usr/bin/env python

import sys
import guess_number
import secret_number

for i in range(10):
   print "trying play", i
   secret_number.reset()
   try:
      guess_number.play()
   except Exception as e:
      print "  play", i, "failed"
      print " ", str(e)
      continue
   if not secret_number.is_correct():
      print "  failed to guess number on round", i

