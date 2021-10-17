
if grep -q -w if $TASK
then
   print "Error: script uses an if statement."
fi
