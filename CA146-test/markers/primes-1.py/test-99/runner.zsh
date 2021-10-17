#!/use/bin/env zsh

if ! sed 's:^\s*#.*$::g' $TASK | grep -w while | wc -l | grep -q -w 2
then
   print "Your solution must involve exactly one while loop." >&2
   false
else
   print ok
   true
fi
