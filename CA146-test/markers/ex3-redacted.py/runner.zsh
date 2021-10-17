#!/usr/bin/zsh

print "showing banned.txt:"
sed 's/^/   |/' banned.txt
print

print "running your script:"
python $TASK | sed 's/^/   |/'
