import sys
import os

def sum_range(a, low, high):
   total = 0
   i = func_bsearch.bsearch(a, low)
   while i < len(a) and a[i] < high:
      total += a[i]
      i = i + 1
   return total

try:
   import func_sum_range
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
length = 5

for q in range(low,high):
   func_bsearch.reset()
   print "test low={} high={} expected={} actual={}".format(q, q + length, sum_range(a,q,q+length), func_sum_range.sum_range(a,q,q+length))
   if not func_bsearch.is_called():
      print "   func_bsearch.bsearch(a,q) not called the correct number of times"

   if length % 2 == 0:
      length -= 3
   else:
      length += 3
