#!/usr/bin/zsh

non_empty=(
   6572.txt
   3302.txt
   8303.txt
   7067.txt
)

empty=(
   8015.txt
   7497.txt
   1637.txt
   5281.txt
   5174.txt
   6557.txt
)

print "creating non-empty files..."
for f in $non_empty
do
   print "  $f"
   echo -n "a" > $f
done

print
print "creating empty files..."
for f in $empty
do
   print "  $f"
   true > $f
done

print
files=( $( print -l $empty $non_empty | sort ) )
print "$ python3 $TASK $files"
exec python3 $TASK $files
