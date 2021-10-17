#!/usr/bin/env python

# Pi should be defined as a constant; the literal should appear
# exactly once in the script.

pi = 3.141

def circumference(r):
   return 2 * pi * r

def area(r):
   return pi * r * r

if __name__ == "__main__":
   print "testing circumference..."
   print circumference(5)
   print "testing area..."
   print area(5)
