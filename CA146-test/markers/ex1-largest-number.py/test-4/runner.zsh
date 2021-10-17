#!/usr/bin/zsh

error=0

for word in while input
do
   if ! grep -w $word $TASK | wc -l | grep -q -w 1
   then
      print "The word $word must occur exactly once in your solution."
      error=1
   fi >&2
done >&2

if [[ $error == 0 ]]
then
   print ok
fi

exit $error
