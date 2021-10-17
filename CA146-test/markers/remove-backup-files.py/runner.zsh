#!/usr/bin/env zsh

mkdir tmp
cd tmp

touch bak

for p in one dog cat.mouse
do
   print $p > $p.py
   print $p > $p.py.bak
   print $p > $p.txt
   print $p > $p.txt.bak
   print $p > $p.txtbak
done

for p in rain snow hail thunder.lightning
do
   print $p > $p.py
   print $p > $p.txt
done

for p in mouse penguin
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
