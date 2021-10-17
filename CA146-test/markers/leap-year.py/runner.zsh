
{
   seq 1995 2005
   seq 1895 1910
}  |
   while read year
   do
      print -n "test $year:"
      print $year | python $TASK
   done
