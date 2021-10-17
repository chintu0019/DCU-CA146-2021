#!/usr/bin/zsh

set -e

for n in $( seq -12 12 )
do
   if (( n ))
   then
      print -n "testing your script with $n: "
      print $n | python3 $TASK
   fi
done
