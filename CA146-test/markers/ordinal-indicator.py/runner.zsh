#!/usr/bin/env zsh

for v in $( seq 135 )
do
   print -n "testing $v: $v"
   print $v | python3 $TASK
done
