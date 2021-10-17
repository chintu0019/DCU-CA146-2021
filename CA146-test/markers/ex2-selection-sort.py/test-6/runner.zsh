#!/usr/bin/zsh

run_test ()
{
   local -a data
   {
      seq -5 10
      seq -10 5
   } | shuf | tr "\n" " " | read -A data
   data+="end"
   print -l $data | python  ex2-selection-sort.py | md5sum - | read upload
   print -l $data | python .ex2-selection-sort.py | md5sum - | read correct
   if [[ $upload != $correct ]]
   then
      print "Incorrect output for the following input..."
      print
      print -l $data
      exit 1
   fi
}

for x in $(seq 20)
do
   run_test
done

print ok
