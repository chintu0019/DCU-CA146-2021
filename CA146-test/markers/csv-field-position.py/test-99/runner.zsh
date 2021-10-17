#!/usr/bin/zsh

print "Checking for use of split..."

if grep -q -w split $TASK
then
   print
   grep -w split $TASK
   print
   print "Your solution must not include the word split."
else
   print ok
fi
