if grep -q -w int $TASK
then
   print "your script may not contain \"int\""
   exit 1
fi

if grep -q -w abs $TASK
then
   print "your script may not contain \"abs\""
   exit 1
fi

if grep -q -w float $TASK
then
   print "your script may not contain \"float\""
   exit 1
fi

if grep -q '%' $TASK
then
   print "your script may not contain \"%\""
   exit 1
fi

print ok
