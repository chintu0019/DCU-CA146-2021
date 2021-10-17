#!/usr/bin/zsh

non_empty=(
   410.txt
   516.txt
   2939.txt
   3631.txt
   7289.txt
   4396.txt
   9297.txt
   2595.txt
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
