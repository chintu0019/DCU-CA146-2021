#!/usr/bin/zsh

exec < words.txt

for n in $(seq 50)
do
   read a
   read b
   if [[ $#a != $#b ]]
   then
      print "testing:"
      print "   $a"
      print "   $b"
      print "   your output:"
      print -l $a $b | python3 $TASK | sed 's/^/      /'
   fi
done
