#!/usr/bin/env zsh

mkdir tmp
cd tmp

for p in one dog cat.mouse jglhgkjhgkhgkhg
do
   print $p > $p.py
   print $p > $p.py.bak
   print $p > $p.txt
   print $p > $p.txt.bak
done

for p in rain snow hail thunder.lightningkjh jkhkjhkkkj
do
   print $p > $p.py
   print $p > $p.txt
done

for p in mouse penguin kjhjkhkh
do
   mkdir $p.bak
done

print "before:"
ls | sort | sed 's/^/  /'

python ../$TASK

print
print "after:"
ls | sort | sed 's/^/  /'

cd ..
rm -r tmp
