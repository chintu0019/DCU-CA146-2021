print -n "Check for use of %, the remainder operator: "
if grep -q "%" $TASK
then
   print "error."
   print "Your solution may not use % (see the task statement); this line:"
   grep "%" $TASK | sed 's/^/  /'
   false
else
   print "ok."
   print 

   seq -5 10 |
      while read n
      do
         print -n "test $n: "
         print $n | python3 $TASK
      done
   true
fi
