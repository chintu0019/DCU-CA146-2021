#!/usr/bin/zsh

error=0

if grep -q -w raw_input $TASK
then
   print "You must read the numbers are integers, using input()."
   print "Do not use raw_input()"
   error=1
fi

if grep -q -w sys $TASK
then
   print "Your solution may not use the sys module."
   error=1
fi

if [[ $error == 0 ]]
then
   print ok
fi

exit $error
