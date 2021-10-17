#!/usr/bin/env zsh

if grep -q -w "if" $TASK
then
   print "Your solution may not involve an if statement."
   exit 1
fi

if ! grep "=" $TASK | wc -l | grep -q -w 1
then
   print "Your solution must involve exactly one assignment statement."
   exit 1
fi

print ok
