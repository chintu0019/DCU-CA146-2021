#!/usr/bin/zsh

set -e

print python3 $TASK b.txt
python3 $TASK b.txt

print cat b.txt
cat b.txt
