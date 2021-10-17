#!/usr/bin/env zsh

if grep -w True $TASK
then
   print "error: script should not contain True"
   exit 1
fi >&2

if grep -w False $TASK
then
   print "error: script should not contain False"
   exit 1
fi >&2

if grep -w bool $TASK
then
   print "it is unnecessary for your script to contain the word \"bool\""
   exit 1
fi >&2

print ok
