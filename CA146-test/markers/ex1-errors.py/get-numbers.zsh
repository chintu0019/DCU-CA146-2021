#!/usr/bin/zsh

variants=( $( < ./multi-variant-task.txt ) )

for variant in $variants
do
   cat ../$variant/$variant |
      tr -c '0-9' "\n" |
      grep ... |
      sort |
      uniq |
      sed "s/^/$variant /"
done
