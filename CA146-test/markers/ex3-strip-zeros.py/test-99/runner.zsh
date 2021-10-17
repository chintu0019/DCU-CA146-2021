#!/usr/bin/env zsh

for word in int float long complex
do
   if grep -w $word $TASK
   then
      print "Your solution may not use $word()."
      exit 1
   fi
done >&2

print ok
