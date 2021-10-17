#!/usr/bin/env zsh

time seq 10000 | tr "\n" " " | python $TASK
