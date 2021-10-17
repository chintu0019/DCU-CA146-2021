#!/usr/bin/env zsh

print -l "testing values 1 through 19..." ""
for a in $( seq 0 3 )
do
   for b in $( seq 0 3 )
   do
      print -n "testing $a $b: "
      print -l $a $b | python3 $TASK
   done
done
