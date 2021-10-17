#!/usr/bin/env zsh -f

if grep -w with $TASK | grep -w open | grep -w -q as
then
   print ok
else
   print "Your solution must use a with-open-as statement." >&2
   exit 1
fi
