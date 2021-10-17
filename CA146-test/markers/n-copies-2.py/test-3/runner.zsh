
if grep -q -w "while" $TASK
then
   print "Your solution may not involve a while loop."
   false
elif grep -q -w "if" $TASK
then
   print "Your solution may not involve a if statement."
   false
else
   print ok
fi
