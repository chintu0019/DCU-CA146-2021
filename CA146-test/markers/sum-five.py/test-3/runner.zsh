#!/usr/bin/zsh

error=0

if ! grep -w "while" $TASK | wc -l | grep -q -w 1
then
   print "Your script does not appear to use exactly one while loop."
   error=1
fi >&2

if ! grep -w "input" $TASK | wc -l | grep -q -w 1
then
   print "Your script does not appear to contain exactly one use of the input() function."
   error=1
fi >&2

if [[ $error == 0 ]]
then
   print ok
fi
