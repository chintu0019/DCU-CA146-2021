#!/usr/bin/zsh

print "Piping a large number of small numbers through your script..."
print

seq -10000 99 | python $TASK
