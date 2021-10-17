#!/usr/bin/zsh

mkdir tmp
cd tmp

for f in a.txt b.t5t o/a.txt d/xt a/u/c/uuuu/e/long.txt a/b/xy/zz.tt/vry-long.txt  a/b/c/x/y/zzz.txt/a a/b/c/x/y/zzz.txt/very-long.py a/b/c/x/y/zzz.txt/very-long
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
