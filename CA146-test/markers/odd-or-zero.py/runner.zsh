#!/usr/bin/zsh

set -e

seq -5 20 |
  while read v
  do
     print -n "testing $v: "
     print $v | python $TASK
  done
