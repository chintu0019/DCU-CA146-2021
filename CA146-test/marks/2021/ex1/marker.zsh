#!/usr/bin/env zsh

find uploads -type f -name '*.correct' |
   grep -v errors- |
   grep -v longes |
   cut -d/ -f 2 |
   sort |
   uniq -c |
   awk '{ print $2, $1 * 25 }'
