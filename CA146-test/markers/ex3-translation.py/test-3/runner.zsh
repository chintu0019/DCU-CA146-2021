#!/usr/bin/env zsh

n=6

for c in $( seq $n )
do
   print "Run number $c of $n..."
   python $TASK < text.txt | md5sum -
done
