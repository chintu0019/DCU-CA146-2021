#!/usr/bin/zsh

args=( 2 800 4 5 87 3 400 701 50 )
print "$ python3 ex2-big-arguments.py" $args
python3 $TASK $args
args=( 900 51 5 201 700 )
print "$ python3 ex2-big-arguments.py" $args
python3 $TASK $args
args=( 678 2 44 49 50 198 199 499 500 699 700 )
print "$ python3 ex2-big-arguments.py" $args
python3 $TASK $args
