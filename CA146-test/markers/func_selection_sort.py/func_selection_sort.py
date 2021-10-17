#!/usr/bin/env python

def swap(a, i, j):
   tmp = a[j]
   a[j] = a[i]
   a[i] = tmp

def find_smallest_position(a, i):
   p = i
   j = i + 1
   while j < len(a):
      if a[j] < a[p]:
         p = j
      j = j + 1
   return p

def selection_sort(a):
   i = 0
   while i < len(a):
      p = find_smallest_position(a, i)
      swap(a, i, p)
      i = i + 1

def main():
   print "testing swap..."
   a = [1]
   swap(a, 0, 0)
   print a

   a = ['rock', 'scissors', 'paper']
   print a
   swap(a, 1, 2)
   print a

   a = ['rock', 'scissors', 'paper']
   print a
   swap(a, 2, 2)
   print a

   print
   print "testing find_smallest_position..."
   a = [6, 4, 7, 9, 5, 6, 9, 3, 9, 3]
   print a
   print find_smallest_position(a, 7)
   print find_smallest_position(a, 7)
   print find_smallest_position(a, 8)

   print
   print "testing selection_sort..."
   a = [6, 4, 7, 9, 5, 6, 9, 3, 9, 3]
   selection_sort(a)
   print a

   a = ["one", "two", "three", "four", "five"]
   selection_sort(a)
   print a

   a = [1]
   selection_sort(a)
   print a

   a = []
   selection_sort(a)
   print a

if __name__ == "__main__":
   main()
