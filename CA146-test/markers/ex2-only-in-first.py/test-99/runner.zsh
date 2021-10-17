#!/usr/bin/zsh

if grep -w in $TASK
then
   print "The Python feature 'in' has not been covered in this module, and may."
   print "not be used for this task."
   exit 1
fi >&2

print ok
