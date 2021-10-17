#!/usr/bin/env zsh

set -e
mkdir tmp -p
cd tmp

for p in one two three four five seven h khkh kh kjh khkj hkh
do
   touch $p.py
done

for t in one two three
do
   touch $t.txt
done

for t in one two three four five six jjjjj
do
   touch $t.py.txt
done

python ../list-python-files-1.py $argv | sort
cd ..
rm -r tmp

