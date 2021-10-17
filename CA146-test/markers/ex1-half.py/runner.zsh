#!/usr/bin/zsh

set -e

for n in $( seq 20 )
do
   print -n "testing your script with $n: "
   print $n | python3 $TASK
done
