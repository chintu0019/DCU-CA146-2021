#!/usr/bin/zsh

if grep -w input $TASK | wc -l | grep -q -w 1
then
   print "ok"
else
   print "error: the word input must appear exactly once in your solution"
fi
