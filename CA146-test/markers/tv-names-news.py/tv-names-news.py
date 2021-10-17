#!/usr/bin/env python

import sys

lines = sys.stdin.readlines()

search_string = "BBC News"
search_terms = search_string.split()

for line in lines:
   details = line.split()
   leading_words = details[1:][:len(search_terms)]
   if " ".join(leading_words) == search_string:
      print details[0], " ".join(details[1:])

