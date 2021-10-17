#!/usr/bin/zsh

if grep 3.141 $TASK | wc -l | grep -q -w 1
then
   print ok
   exit 0
fi

{
   print "pi should be defined as a constant."
} >&2
exit 1
