import sys
import os

try:
   import func_contains
   import func_bsearch
except Exception as e:
   sys.stderr.write("error: failed to import test file\n")
   sys.stderr.write(str(e))
   sys.stderr.write("\n")
   sys.exit(1)

a = map(int,sorted("-5 -8 20 89 89 89 -5 0 0 89 56 23 ".split()))

print "test list:", a

low = min(a) - 1
high = max(a) + 2

for q in range(low,high):
   func_bsearch.reset()
   print "test q={} expected={} actual={}".format(q, (q in a), func_contains.contains(a,q))
   if not func_bsearch.is_called():
      print "   func_bsearch.bsearch(a,q) not called"
