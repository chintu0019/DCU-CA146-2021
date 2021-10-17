#!/usr/bin/zsh

for word in input int float
do
   if grep -w $word $TASK
   then
      print
      print "The word $word may not occur in your solution."
      exit 1
   fi
done >&2

print "ok"
