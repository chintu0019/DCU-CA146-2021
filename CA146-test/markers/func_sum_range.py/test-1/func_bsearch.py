
called = 0

def is_called():
   return called == 2

def reset():
   global called
   called = 0

def bsearch(a,q):
   global called
   called += 1
   """
   a: a sorted list
   q: a query

   If q is present in a:
      then return the *first* position at which q occurs in a.

   Otherwise:
      return the position p such that, were q inserted at position p, the list would remain sorted.
      (Note: that position could be the position *after* the end of the list.)
   """

   low = 0
   high = len(a)

   while low < high:
      mid = low + (high - low) / 2
      assert(low <= mid < high)

      if a[mid] < q:
         low = mid + 1
      else:
         high = mid

   return low

