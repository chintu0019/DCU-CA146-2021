
import sys
lines = sys.stdin.readlines()

d = {
   "one": "eins",
   "two": "zwei",
   "three": "drei",
   "four": "vier",
   "five": "funf",
   "six": "sechs",
   "seven": "sieben",
   "eight": "acht",
   "nine": "neun",
   "ten": "zehn",
}

i = 0
while i < len(lines):
   print d[lines[i].strip()]
   i = i + 1
