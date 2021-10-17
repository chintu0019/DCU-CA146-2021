
if grep -w abs $TASK
then
   print "You may not use the built-in absolute-value function." >&2
else
   print "ok"
fi
