#!/usr/bin/zsh

non_empty=(
)

empty=(
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
