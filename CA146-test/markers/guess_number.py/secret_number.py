#!/usr/bin/env python

import random

N = 10
maximum = 999

guesses = 0
number = 0
correct = False

def reset():
   global guesses, number, correct
   guesses = 10
   number = random.randint(1,maximum)
   correct = False

def is_correct():
   return correct

def guess(n):
   global guesses, correct
   if guesses == 0:
      raise Exception("too many guesses")
   guesses -= 1
   if n < number:
      return "too-low"
   elif number < n:
      return "too-high"
   else:
      correct = True
      return "correct"
