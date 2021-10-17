#!/usr/bin/env zsh

for v in $( seq 50 )
do
   print -n "testing $v -> "
   print $v | python $TASK
done
