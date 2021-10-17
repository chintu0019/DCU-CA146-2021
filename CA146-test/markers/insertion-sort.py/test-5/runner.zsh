#!/usr/bin/env zsh

print "This test will pass for insertion sort, but should time out if selection\nsort were used instead."
print

{
   seq 200000
   print "end"
} | python $TASK | md5sum
