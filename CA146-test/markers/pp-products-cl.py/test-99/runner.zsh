#!/usr/bin/env zsh

if grep -w while $TASK | wc -l | grep -q -w 1
then
   print "ok"
   true
else
   print "The solution to this task must involve only one while loop." >&2
   false
fi
