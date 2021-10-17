#!/usr/bin/zsh

set -e

M=$RANDOM$RANDOM$RANDOM$RANDOM$RANDOM$RANDOM$RANDOM
N=$RANDOM$RANDOM$RANDOM$RANDOM$RANDOM$RANDOM$RANDOM
O=$RANDOM$RANDOM$RANDOM$RANDOM$RANDOM$RANDOM$RANDOM
P=$RANDOM$RANDOM$RANDOM$RANDOM$RANDOM$RANDOM$RANDOM

M=$M[1,6]
N=$N[1,6]
O=$O[1,6]
P=$P[1,6]

sed "s/M/$M/g; s/N/$N/g; s/O/$O/g; s/P/$P/g" < ./template.py > $PWD:t
source-highlight --no-doc -s py < $PWD:t > task-description.html

python3 $PWD:t < stdin.txt > stdout.txt
cd test-1
( cd ..; python3 $PWD:t ) < stdin.txt > stdout.txt
