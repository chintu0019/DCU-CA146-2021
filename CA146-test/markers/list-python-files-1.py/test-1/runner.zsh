#!/usr/bin/env zsh

set -e
mkdir tmp -p
cd tmp

for p in one two.three four.five seven
do
   touch $p.py
done

for t in one two three four.five six
do
   touch $t.txt
done

for t in one two.three four five six
do
   touch $t.py.txt
done

touch teety-py

python ../$TASK $argv | sort
cd ..
rm -r tmp

