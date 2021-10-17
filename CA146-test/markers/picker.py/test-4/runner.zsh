
if grep -q -w "if" $TASK
then
   print "You may not use an 'if' statement for this task." >&2
else
   print ok
fi
