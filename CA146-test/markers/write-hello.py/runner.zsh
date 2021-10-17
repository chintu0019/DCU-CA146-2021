#!/usr/bin/env zsh -f

or_exit ()
{
   print -- "failed"
   exit 1
}

set -e
file="hello.txt"

print "running upload..."
python ./write-hello.py $argv || or_exit
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

