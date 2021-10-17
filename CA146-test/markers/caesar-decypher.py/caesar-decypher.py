#!/usr/bin/env python

import sys

rotate = int(sys.argv[1])

# To decrypt, simply comlete the rotation.
rotate = 26 - rotate

alpha = "abcdefghijklmnopqrstuvwxyz"
rotated = alpha[rotate:] + alpha[:rotate]

encrypt = {}

i = 0
while i < len(alpha):
   encrypt[alpha[i]] = rotated[i]
   encrypt[alpha[i].upper()] = rotated[i].upper()
   i = i + 1

line = sys.stdin.readline()
while line:
   i = 0
   while i < len(line):
      if line[i] in encrypt:
         line = line[:i] + encrypt[line[i]] + line[i+1:]
      i = i + 1
   sys.stdout.write(line)
   line = sys.stdin.readline()
