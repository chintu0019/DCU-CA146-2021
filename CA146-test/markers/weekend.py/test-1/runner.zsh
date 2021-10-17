#!/usr/bin/zsh

error=0

for word in or elif
do
   if grep -q -w $word $TASK
   then
      print "A good solution to this task will not use $word."
      error=1
   fi
done >&2

if ! grep -w if $TASK | wc -l | grep -q -w 1
then
   print "A good solution involves only one if statement."
   error=1
fi >&2

if [[ $error == 0 ]]
then
   print ok
fi

exit $error
