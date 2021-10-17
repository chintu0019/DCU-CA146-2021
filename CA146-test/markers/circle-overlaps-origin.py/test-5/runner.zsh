#!/usr/bin/zsh

for a in 1 2 3 4 5
do
   for b in 1 2 3 4 5
   do
      for c in 1 2 3 4 5
      do
         print -n "x=$a y=$b r=$c: "
         print -l $a $b $c | python $TASK
      done
   done
done
