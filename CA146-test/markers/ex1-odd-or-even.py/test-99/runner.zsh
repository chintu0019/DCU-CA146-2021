#!/usr/bin/env zsh

tr -c "a-z" "\n" < $TASK |
   grep -w input |
   wc -l |
   read n

print "The word 'input' occurs $n time(s)."
