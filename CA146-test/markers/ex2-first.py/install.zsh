#!/usr/bin/zsh

set -e

rm -vf multi-variant-task.txt

install ()
{
   local n=$argv[1]
   local start=$argv[2]
   local end=$argv[3]
   local class=$argv[4]

   local task="ex2-first-$n.py"
   print $task >> multi-variant-task.txt

   mkdir -vp ../$task
   cp ./runner.zsh ../$task/
   sed "s/START/$start/; s/END/$end/" ./ex2-first.py > ../$task/$task
   (
      cd ../$task
      env TASK=$task zsh runner.zsh > stdout.txt
   )
   # sed "s/START/$start/; s/END/$end/; s/THING/$class/" task-description.html > ../$task/task-description.html
}

install 0 "a" "g" "musical note"
install 1 "A" "Z" "capital letter"
install 2 "0" "9" "digit"
