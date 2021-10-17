#!/usr/bin/env zsh

vs=( 1 2 3 4 5 6 )

is_triangle ()
{
   local a=$argv[1]
   local b=$argv[2]
   local c=$argv[3]

   (( a < b + c )) && (( b < a + c )) && (( c < a + b ))
}

for a in $vs
do
   for b in $vs
   do
      for c in $vs
      do
	 if is_triangle $a $b $c
	 then
	    print -n "testing $a $b $c\n  "
	    print -l $a $b $c | python3 $TASK
	 fi
      done
   done
done
