#!/usr/bin/env python

def strip_suffix(fname, suffix):
   return fname[:len(fname)-len(suffix)]

if __name__ == '__main__':
   correct = {}
   slist = []

   with open("uploads.txt") as f:
      uploads = map(str.strip,f.readlines())

   for upload in uploads:
      details = upload.split("/")
      name = details[2]
      fname = details[3]

      if name not in correct:
         correct[name] = {}
         slist.append(name)

      if fname.startswith("bl-"):
         if fname.endswith(".correct"):
            key = strip_suffix(fname,".correct")
            correct[name][key] = 1

         if fname.endswith(".incorrect"):
            key = strip_suffix(fname,".incorrect")
            correct[name][key] = 0

   for name in slist:
      count = 0
      for key in correct[name]:
         count += correct[name][key]
      print name, count
