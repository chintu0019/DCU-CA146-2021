#!/usr/bin/env python

a = []

line = raw_input()
while line != "end":
   a.append(line)
   line = raw_input()

text = ""
line = raw_input()
while line != "end":
   if len(line) == 0:
      print text
      text = ""
   else:
      if len(text) != 0:
         text = text + " "
      text = text + a[int(line)]

   line = raw_input()

if 0 < len(text):
   print text
