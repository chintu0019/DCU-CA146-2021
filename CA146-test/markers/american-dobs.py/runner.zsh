#!/usr/bin/env zsh -f

or_exit ()
{
   print -- "failed"
   exit 1
}

set -e
file="american-dobs.txt"

print "running upload..."
python ./american-dobs.py || or_exit
print "ok"

print -l "" "testing that '$file' exists..."
[[ -f $file ]] || or_exit
print "ok"

print -l "" "testing that '$file' is non-empty..."
[[ -s $file ]] || or_exit
print "ok"

print -l "" "outputing '$file' contents..."
cat $file || or_exit

rm $file

