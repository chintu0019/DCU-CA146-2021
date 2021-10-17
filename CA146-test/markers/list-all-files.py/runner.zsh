#!/usr/bin/zsh

mkdir tmp
cd tmp

for f in a.txt b.txt d/a.txt d/b.txt a/b/c/d/e/long.txt a/b/c/x/y/zzz.txt/very-long.txt  a/b/c/x/y/zzz.txt/a a/b/c/x/y/zzz.txt/very-long.py a/b/c/x/y/zzz.txt/very-long
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
