#!/usr/bin/env python

print "This test will pass if linear search is used, but is expected to fail otherwise."

set -e

n=100000

{
   seq $n | sed 's/.*/1/'
   print end
   seq $n | sed 's/.*/1/'
   print end
} | python ex2-only-in-first.py > /dev/null
