#!/usr/bin/env zsh

run () {
   print -n "testing $@: "
   print -l $@ | python3 $TASK
}

run 1 1 10 2 2 10
run 1 1 1 10 10 1
run 0 0 1 2 2 1
run 0 0 1 2 0 1
run 0 0 1 2 0 2
run 0 0 1 2 0 2
run 1 1 2 4 5 3
run 1 1 3 4 5 3

run 55 26 3 50 20 1
run 55 26 3 50 20 2
run 55 26 3 50 20 3
run 55 26 3 50 20 4
run 55 26 3 50 20 5
run 55 26 3 50 20 6
run 55 26 3 50 20 7
run 55 26 3 50 20 8
