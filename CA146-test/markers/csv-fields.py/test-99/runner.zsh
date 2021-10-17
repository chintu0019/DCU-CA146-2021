#!/usr/bin/zsh

if [[ $EINSTEIN_USER != "sblott" ]] && fgrep "." $TASK
then
   print
   print "The character '.' may not appear in your solution."
   exit 1
fi

for word in import
do
   if grep -w $word $TASK
   then
      print
      print "The word \"$word\" may not appear in your solution."
      exit 1
   fi
done

if ! grep -w "while" $TASK | wc -l | grep -q -w 2
then
   print "Your solution must involve exactly two while loops."
   exit 1
fi

print ok
