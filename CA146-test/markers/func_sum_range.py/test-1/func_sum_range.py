
import func_bsearch

def sum_range(a, low, high):
   total = 0
   i = func_bsearch.bsearch(a, low)
   while i < len(a) and a[i] < high:
      total += a[i]
      i = i + 1
   return total

if __name__ == "__main__":
   a = [1,2,4,4,5,5,6,7,8]
   print sum_range(a,3,7)

