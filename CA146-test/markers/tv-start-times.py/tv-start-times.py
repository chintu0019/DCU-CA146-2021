#!/usr/bin/env python

import sys

lines = sys.stdin.readlines()

for line in lines:
   details = line.split()
   start_stop_list = details[0].split("-")
   print start_stop_list[0], " ".join(details[1:])

