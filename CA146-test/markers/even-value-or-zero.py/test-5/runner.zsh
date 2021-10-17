#!/usr/bin/zsh

for v in $( seq 20 )
do
   print -n "testing $v:\n  "
   print $v | python3 $TASK
done
