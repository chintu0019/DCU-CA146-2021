#!/usr/bin/env zsh

for w in break continue exit quit for range search find startswith endswith replace int float split
do
   if grep -q -w $w $TASK
   then
      print "Your solution make not contain the word \"$w\"." >&2
      exit 1
   fi
done

print ok
