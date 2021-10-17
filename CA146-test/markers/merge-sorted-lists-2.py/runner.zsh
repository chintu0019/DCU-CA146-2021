#!/usr/bin/env zsh

{
   print "It is not a good idea to merge the lists by concatenating"
   print "them and then sorting the combined list.  More specifically,"
   print "this is a BAD idea: it requires n-squared time to sort the list."
   print
   print "Whereas the previous solution for this task was O(n)."
   print
   print "This test is a trap; there is no way to pass it."
} >&2

false
