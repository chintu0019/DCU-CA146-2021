#!/usr/bin/env zsh

if grep -w round $TASK
then
   {
      print "Your solution may not include the word 'round'."
      print
      print "A simple (and elegant) solution exists involving only integer arithmetic."
   } >&2
   false
else
   print ok
   true
fi
