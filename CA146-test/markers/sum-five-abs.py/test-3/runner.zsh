#!/usr/bin/zsh

set -e

for banned in abs
do
   if grep -q -w $banned $TASK
   then
      print "You may not use the built-in $banned() function."
      false
   fi
done

print "ok"
