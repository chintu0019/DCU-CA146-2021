#!/usr/bin/env zsh

files=( fish bat ball )
dirs=( hen chicken dog roof )

touch $files
mkdir $dirs

python $TASK

rm $files
rmdir $dirs
