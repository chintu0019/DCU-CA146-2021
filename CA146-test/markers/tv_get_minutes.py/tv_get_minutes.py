#!/usr/bin/env python

def get_minutes(s):
   hm = s.split(":")
   return int(hm[0]) * 60 + int(hm[1])

def main():
   for s in ["0:7", "10:30", "24:00"]:
      print "testing:", s
      print get_minutes(s)

if __name__ == "__main__":
   main()

