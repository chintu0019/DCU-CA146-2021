#!/usr/bin/zsh

args=(
   "Mary had 1 little lamb"
   "9 little lamb"
   "And everywhere that 45 Marys went"
   "g"
   "Z"
   "9"
   "321"
   ""
)

for arg in $args
do
   print "$ echo \"$arg\" | python3 ex2-first.py"
   print $arg | python3 $TASK
done
