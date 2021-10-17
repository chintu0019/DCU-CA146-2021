#!/usr/bin/zsh

set -e

print python3 $TASK ab.txt
python3 $TASK ab.txt

print cat ab.txt
cat ab.txt
