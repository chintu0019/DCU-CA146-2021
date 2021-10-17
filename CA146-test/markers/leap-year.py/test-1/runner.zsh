
{
   seq 798 805
   seq 998 1005
}  |
   while read year
   do
      print -n "test $year:"
      print $year | python $TASK
   done
