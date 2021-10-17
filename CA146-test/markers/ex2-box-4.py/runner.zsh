#!/usr/bin/zsh

for n in 1 2 3 4 5 10 12 15
do
   print "$ python3 $TASK $n"
   python3 $TASK $n
done
