#!/usr/bin/zsh

mkdir tmp
cd tmp

for f in a/a/a/a/b/b/b/b/a/a/aa/b a/a/a/a/a/b/b/b/b/b/b/b/b/b/a a/a/a/a/a/b/b/b/b/b/b/b/b/b/b
do
   mkdir -p $f:h
   touch $f
done

print "here are all of the files:"
find . -type f | sort | sed 's/^/  /'

print
print "running your script..."
python ../$TASK | sort | sed 's/^/  /'

cd ..
rm -r tmp
