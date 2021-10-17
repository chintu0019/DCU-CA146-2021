#!/usr/bin/zsh

set -e

install ()
{
   local n=$argv[1]
   local ch=$argv[2]
   local boundary=$argv[3]

   local task="ex2-box-$n.py"

   mkdir -vp ../$task
   cp ./runner.zsh ../$task/
   sed "s/CHARACTER/$ch/" ./ex2-box-template.py > ../$task/$task
   (
      cd ../$task
      pwd
      ls
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
