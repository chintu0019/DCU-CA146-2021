#!/usr/bin/env python

def strip_suffix(fname, suffix):
   return fname[:len(fname)-len(suffix)]

if __name__ == '__main__':
   counts = {}
   slist = []

   with open("uploads.txt") as f:
      uploads = map(str.strip,f.readlines())

   for upload in uploads:
      details = upload.split("/")
      name = details[2]

      if name not in counts:
         counts[name] = 0
         slist.append(name)

      counts[name] = counts[name] + 1

   for name in slist:
      print name, counts[name]
