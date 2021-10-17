#!/usr/bin/env python

words = {
   "one":    "eins",
   "two":    "zwei",
   "three":  "drei",
   "four":   "vier",
   "five":   "funf",
   "six":    "sechs",
   "seven":  "sieben",
   "eight":  "acht",
   "nine":   "neun",
   "ten":   "zehn",
}

import sys

ws = sys.argv[1:]

i = 0
while i < len(ws):
   if ws[i] in words:
      ws[i] = words[ws[i]]
   i = i + 1

print " ".join(ws)
