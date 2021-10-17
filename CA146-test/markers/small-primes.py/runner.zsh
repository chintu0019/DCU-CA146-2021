#!/usr/bin/env zsh

print -l "testing values 1 through 19..." ""
for v in $( seq 19 )
do
   print -n "testing $v: "
   print $v | python small-primes.py
done
