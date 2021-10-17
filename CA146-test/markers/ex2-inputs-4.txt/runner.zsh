#!/usr/bin/zsh

user=$( python3 ./script.py < $TASK )
expected=$( < ./output.txt )

if [[ $user == $expected ]]
then
   print "correct"
else
   print "incorrect"
   exit 1
fi
