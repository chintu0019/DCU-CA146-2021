#!/usr/bin/env zsh

print "Validating PEP8 style..."
print

if pep8 --ignore=E111,E302,E265,E121,E114 $TASK 2>&1
then
   print "ok"
   print
else
   err="$?"
   print
   exit $err
fi
