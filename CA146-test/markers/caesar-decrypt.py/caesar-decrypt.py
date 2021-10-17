#!/usr/bin/env python3

# Note:
# This is IDENTICAL to caesar-encrypt.py.  Because 13 is chosen as the rotaion,
# rotating a further 13 characters brings us back to where we started.

n = 13

import sys

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

src = lower + upper
dst = lower[n:] + lower[:n] + upper[n:] + upper[:n]
cipher = {}

i = 0
while i < len(src):
   cipher[src[i]] = dst[i]
   i = i + 1

message = sys.stdin.read()
output = []

i = 0
while i < len(message):
   if message[i] in cipher:
      output.append(cipher[message[i]])
   else:
      output.append(message[i])
   i = i + 1

sys.stdout.write("".join(output))
