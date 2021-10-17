
seq 0 20 |
   while read days
   do
      print -n "testing $days: "
      print $days | python $TASK
   done
