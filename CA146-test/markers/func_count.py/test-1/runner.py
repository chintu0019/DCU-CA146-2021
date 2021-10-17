import sys
import os

def count(a,q):
   x = func_bsearch.bsearch(a,q)
   y = func_bsearch.bsearch(a,q+1)

   return y - x
try:
   import func_count
   import func_bsearch
except Exception as e:
   sys.stderr.write("error: failed to import test file\n")
   sys.stderr.write(str(e))
   sys.stderr.write("\n")
   sys.exit(1)

a = map(int,sorted("-5 -8 56 56 55 56 56 57 56 56 20 89 89 89 -5 0 0 89 56 23 ".split()))

print "test list:", a

low = min(a) - 1
high = max(a) + 2

for q in range(low,high):
   func_bsearch.reset()
   print "test q={} expected={} actual={}".format(q, count(a,q), func_count.count(a,q))
   if not func_bsearch.is_called():
      print "   func_bsearch.bsearch(a,q) not called the correct number of times"
