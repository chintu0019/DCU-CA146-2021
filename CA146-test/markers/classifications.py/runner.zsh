
{
   seq 38 42
   seq 48 52
   seq 68 72
}  |
   while read mark
   do
      print "test $mark:"
      print $mark | python3 $TASK | sed 's/^/  /'
   done
