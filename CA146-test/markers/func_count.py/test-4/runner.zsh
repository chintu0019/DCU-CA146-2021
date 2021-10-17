#!/usr/bin/zsh

if grep -w while $TASK
then
	print "Your solution may not contain the word \"while\"."
	exit 1
fi

if grep -w for $TASK
then
	print "Your solution may not contain the word \"for\"."
	exit 1
fi

print ok
