#!/usr/bin/env zsh

tester ()
{
   print "testing:" $argv
   for v in $argv
   do
      print $v
   done | python $TASK | sed 's/^/  /'
}

tester 1 2 3
tester 1 3 2
tester 2 1 3
tester 2 3 1
tester 3 1 2
tester 3 2 1

tester 90 100 100
tester 100 90 100
tester 100 100 90

for word in sort sorted
do
   if grep -q -w $word $TASK
   then
      print "Your solution may not contain the word $word." >&2
      exit 1
   fi
done
