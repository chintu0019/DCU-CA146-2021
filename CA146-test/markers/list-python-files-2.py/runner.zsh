#!/usr/bin/env zsh

set -e
mkdir tmp -p
cd tmp

for p in one two dog cat
do
   touch $p.py
done

for p in three four mouse elephant
do
   echo "content" > $p.py
   echo "content" > $p.yy
   echo "content" > $p.y
   echo "content" > ${p}y
done

for t in one three four mouse elephant dog
do
   echo "content" > $t.txt
done

python ../list-python-files-2.py | sort $argv
cd ..
rm -r tmp

