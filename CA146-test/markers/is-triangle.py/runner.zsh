#!/usr/bin/env zsh

n=60

run_test ()
{
   a=$((1 + RANDOM % 50))
   b=$((1 + RANDOM % 50))
   c=$((1 + RANDOM % 50))
   expected=$( print -l $a $b $c | python3 is-triangle-reference.py )
   actual=$( print -l $a $b $c | python3 is-triangle.py )

   if [[ $actual != $expected ]]
   then
      print "test case failed: $a, $b, $c"
      print "        expected: $expected"
      print "          actual: $actual"
      false
   else
      true
   fi
}

print "running $n random test cases..."
for dummy in $(seq $n)
do
   run_test || exit 1
done
print "ok"
