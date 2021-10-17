#!/usr/bin/env python3

import sys
a = sys.stdin.readlines()

i = 0
while i < len(a):
   tokens = a[i].rstrip().split("/")
   print(tokens[len(tokens) - 1])
   i = i + 1
