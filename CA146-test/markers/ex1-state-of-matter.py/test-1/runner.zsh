#!/usr/bin/zsh

while read n
do
   echo -n "testing $n: "
   echo $n | python $TASK
done < input.txt
