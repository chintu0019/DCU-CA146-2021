#!/usr/bin/env zsh

if grep -w while $TASK
then
   print "Your solution to this task may not involve a loop."
   exit 1
fi >&2

print ok
