#!/usr/bin/env python

import sys

names = {}
count = 1

for line in sys.stdin.readlines():
   parse = line.strip().split("/")
   if parse[0] not in names:
      names[parse[0]] = "user-{}".format(count)
      count += 1
   parse[0] = names[parse[0]]
   print "/".join(parse)


