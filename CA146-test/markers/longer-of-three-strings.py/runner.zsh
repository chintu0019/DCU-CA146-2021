#!/usr/bin/zsh

exec < words.txt

for n in $(seq 50)
do
   read a
   read b
   read c
   if [[ $#a != $#b ]] && [[ $#b != $#c ]] && [[ $#a != $#c ]]
   then
      print "testing:"
      print "   $a"
      print "   $b"
      print "   $c"
      print "   your output:"
      print -l $a $b $c | python3 $TASK | sed 's/^/      /'
   fi
done
