#!/usr/bin/zsh

for word in sort sorted
do
   if grep -w -q $word $TASK
   then
      print "The word $word may not appear in your solution." >&2
      exit 1
   fi
done

print "ok"
