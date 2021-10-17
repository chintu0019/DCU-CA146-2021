#!/usr/bin/zsh

{
   seq -3 5
   echo 50
   seq 97 103
} |
   while read n
   do
      echo -n "testing $n "
      echo $n | python $TASK
   done
