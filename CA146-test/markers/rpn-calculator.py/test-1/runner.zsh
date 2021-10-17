#!/usr/bin/env

if [[ -z $TASK ]]
then
   TASK=$(print *.py(N))
   if [[ -z $TASK ]]
   then
      TASK=$(print ../*.py)
   fi
fi

print "Testing binary operations..."
exec python $TASK
