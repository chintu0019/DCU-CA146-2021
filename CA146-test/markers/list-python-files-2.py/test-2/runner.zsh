#!/usr/bin/env zsh

set -e
mkdir tmp -p
cd tmp

for p in one two
do
   touch $p.py
done

for p in three four aaa bbb hjhjd
do
   echo "content" > $p.py
done

for t in one three four
do
   echo "content" > $t.txt
done

python ../list-python-files-2.py | sort $argv
cd ..
rm -r tmp

