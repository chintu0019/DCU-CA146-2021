#!/usr/bin/env python

import sys

# Here, book is a list of pages, where each page is a list of lines.
#
book = []
n = 10

i = 0
while i < n:
   file_name = "page-" + str(i) + ".txt"
   with open(file_name) as f:
      page = f.readlines()
   book.append(page)
   i = i + 1

triplets = sys.stdin.readlines()

i = 0
while i < len(triplets):
   triplet = triplets[i].split()
   page = int(triplet[0])
   line = int(triplet[1])
   char = int(triplet[2])
   # This isn't very efficient, but it's concise and correct,
   # which is enough here.
   sys.stdout.write(book[page][line][char])
   i = i + 1
