#!/usr/bin/env zsh

files=( main.c makefile test.py )
dirs=( src etc )

touch $files
mkdir $dirs

python $TASK

rm $files
rmdir $dirs
