#!/use/bin/env zsh

if ! sed 's:^\s*#.*$::g' $TASK | grep -w while | grep -w and | wc -l | grep -q -w 2
then
   print "Your solution must involve linear-search." >&2
   false
elif ! sed 's:^\s*#.*$::g' $TASK | grep -w while | wc -l | grep -q -w 2
then
   print "Your solution must involve exactly one while loop." >&2
else
   print ok
   true
fi
