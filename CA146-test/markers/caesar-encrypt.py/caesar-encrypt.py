#!/usr/bin/env python3

n = 13
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

import sys

# Set up src and dst; src[i] is encrypted as dst[i].
#
# src: "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
# dst: "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM"

src = lower + upper
dst = lower[n:] + lower[:n] + upper[n:] + upper[:n]
cipher = {}

i = 0
while i < len(src):
   cipher[src[i]] = dst[i]
   i = i + 1

# Simply read the entire input as a single string.
#
message = sys.stdin.read()

# We build the output as a list (output) and then join the characters
# together later.
#
output = []

i = 0
while i < len(message):
   if message[i] in cipher:
      output.append(cipher[message[i]])
   else:
      output.append(message[i])
   i = i + 1

sys.stdout.write("".join(output))
