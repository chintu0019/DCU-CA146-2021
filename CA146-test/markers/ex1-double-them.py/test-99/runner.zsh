#!/usr/bin/zsh

if grep -w input $TASK | wc -l | grep -w -q 1
then
   if grep -w raw_input $TASK | wc -l | grep -w -q 0
   then
      print ok
   else
      print "The word 'raw_input' may not occur in your solution."
   fi
else
   print "The word 'input' may occur at most once in your solution."
fi

