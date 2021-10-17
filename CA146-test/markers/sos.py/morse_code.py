#!/usr/bin/env python

import sys

a = 0
b = 0

def dot():
   global a
   a += 1
   sys.stdout.write(".")

def dash():
   global b
   b += 1
   sys.stdout.write("-")

def check():
   sys.stdout.write("\n")
   return (a, b)
