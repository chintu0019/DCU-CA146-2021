#!/usr/bin/env zsh

print "Verifying that there is a single if statement..."
if grep -w -c "if" $TASK | grep -q -w 1
then
   print "  ... ok"
else
   print "  ... error"
fi

print
print "Verifying appropriate use of elif..."
if grep -w -c "elif" $TASK | grep -q -w 1
then
   print "  ... ok"
else
   print "  ... error"
fi

print
print "Verifying appropriate use of else..."
if grep -w -c "else" $TASK | grep -q -w 1
then
   print "  ... ok"
else
   print "  ... error"
fi
