#!/usr/bin/zsh

error=0

if ! grep -w if $TASK | wc -l | grep -q -w 1
then
   print "A good solution involves only one if statement."
   error=1
fi >&2

if [[ $error == 0 ]]
then
   print ok
fi

exit $error
