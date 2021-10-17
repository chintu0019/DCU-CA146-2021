#!/usr/bin/zsh

error=0

if grep -q -w sys $TASK
then
   print "Your solution may not use the sys module." >&2
   error=1
fi

if grep -q -w raw_input $TASK
then
   print "Your solution may not use the raw_input() function." >&2
   error=1
fi

if [[ $error == 0 ]]
then
   print ok
else
   print error
fi

exit $error
