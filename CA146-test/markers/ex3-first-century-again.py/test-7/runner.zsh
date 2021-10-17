#!/usr/bin/zsh

print "Piping an 'infinite' number of integers through your script..."
print

{
	seq -10000 99
	print 98978
	while true
	do
		print 99 2> /dev/null || exit 0
	done
} | python $TASK

