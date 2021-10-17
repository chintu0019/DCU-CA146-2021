#!/usr/bin/env

if [[ -z $TASK ]]
then
   TASK=$(print *.py(N))
   if [[ -z $TASK ]]
   then
      TASK=$(print ../*.py)
   fi
fi

print "Testing unary operators..."
exec python $TASK
