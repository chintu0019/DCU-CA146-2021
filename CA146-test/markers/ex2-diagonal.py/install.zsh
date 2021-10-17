#!/usr/bin/zsh

set -e

rm -vf multi-variant-task.txt

install ()
{
   local n=$argv[1]
   local ch=$argv[2]
   local boundary=$argv[3]

   local task="ex2-diagonal-$n.py"
   print $task >> multi-variant-task.txt

   mkdir -vp ../$task
   cp ./runner.zsh ../$task/
   sed "s/CHARACTER/$ch/" ./ex2-diagonal.py > ../$task/$task
   (
      cd ../$task
      env TASK=$task zsh runner.zsh > stdout.txt
      python3 $task 7 > example.txt
   )
   sed "s/X/$ch/g; s/BC/$boundary/" task-description.html > ../$task/task-description.html
}

install 0 "*" "an asterisk"
install 1 "." "a full stop character"
install 2 "#" "a hash sign"
install 3 "+" "a plus sign"
install 4 "@" "an ampersand"
