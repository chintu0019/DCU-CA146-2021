#!/usr/bin/zsh

count=$( grep -w while $TASK | wc -l )
error=0

if (( 2 < count ))
then
   print "Your solution may not involve more than two while loops."
   error=1
fi

if grep -w while $TASK | grep "^[ \t]"
then
   print
   print "Your solution may not involve a nested while loop."
   error=1
fi

if [[ $error == 0 ]]
then
   print ok
fi

exit $error
