#!/usr/bin/env zsh

set -e
mkdir tmp -p
cd tmp

for p in one two
do
   touch $p.py
   touch $p.yy
   touch $p.y
   touch ${p}y
done

for t in one three four
do
   touch $t.txt
done

python ../list-python-files-1.py | sort $argv
cd ..
rm -r tmp

