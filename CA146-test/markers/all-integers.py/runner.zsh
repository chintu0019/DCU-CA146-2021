#!/usr/bin/zsh

print "We will run your script twice."

print
print "Here are the first ten lines of output..."
python3 ./wrapper.py < $TASK | head -10

print
print "And here are the first 200 lines of output..."
python3 ./wrapper.py < $TASK | head -200
