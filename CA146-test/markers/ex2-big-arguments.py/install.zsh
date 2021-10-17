#!/usr/bin/zsh

set -e

rm -vf multi-variant-task.txt

install ()
{
   local n=$argv[1]
   local NNN=$argv[2]

   local task="ex2-big-arguments-$n.py"
   print $task >> multi-variant-task.txt

   mkdir -vp ../$task
   cp ./runner.zsh ../$task/
   sed "s/NNN/$NNN/" ./ex2-big-arguments.py > ../$task/$task
   (
      cd ../$task
      env TASK=$task zsh runner.zsh > stdout.txt
   )
   # sed "s/NNN/$NNN/g" task-description.html > ../$task/task-description.html
}

install 0 50
install 1 200
install 2 500
install 3 700
