#usr/bin/env zsh

if grep -q -w strip $TASK || grep -q -w lstrip $TASK || grep -q -w rstrip $TASK
then
   print "You may not use Python's built in strip methods."
   false
else
   print ok
   true
fi
