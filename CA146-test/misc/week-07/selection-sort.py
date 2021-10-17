
def read_input():
   a = []
   line = raw_input()
   while line != "end":
      a.append(int(line))
      line = raw_input()
   return a

def random_input(n):
   a = []
   import random
   for i in range(n):
      a.append(random.randrange(1000))
   return a

def ssort(a):
   i = 0
   while i < len(a):
      p = i
      j = i + 1
      while j < len(a):
         if a[j] < a[p]:
            p = j
         j = j + 1

      # swap a[i] and a[p]
      tmp = a[p]
      a[p] = a[i]
      a[i] = tmp

      i = i + 1

def aprint(a):
   for v in a:
      print v

if __name__ == "__main__":
   import sys
   import getopt

   n = 0

   try:
      opts, args = getopt.getopt(sys.argv[1:], "n:r:")
      for o, a in opts:
         try:
            if o == "-n":
               n = int(a)
            if o == "-r":
               n = int(a)
         except:
            print "not an integer:", a
            sys.exit(2)

   except getopt.GetoptError as err:
      print str(err)
      sys.exit(2)

   if 0 < n:
      a = random_input(n)
      import time
      start = time.time()
      ssort(a)
      stop = time.time()
      duration = stop - start
      print int(1000 * duration), "(ms)"
   else:
      a = read_input()
      ssort(a)
      aprint(a)

