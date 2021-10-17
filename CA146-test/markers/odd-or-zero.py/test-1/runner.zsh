#!/usr/bin/zsh

if grep -w -q "if" $TASK
then
   print "Your solution may not use an if statement."
else
   print ok
fi
