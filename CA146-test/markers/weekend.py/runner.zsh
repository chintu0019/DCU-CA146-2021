
seq 0 6 |
   while read day
   do
      print -n "testing $day: "
      print $day | python $TASK
   done
