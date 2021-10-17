
print "Validating $MODULE Python compliance..."
print

if [[ $TASK == "count-lines.py" ]]
then
   print "ok"
   exit 0
fi

for_in_ok=()
for_in_ok+=( task-summary-1.py )
for_in_ok+=( set-union.py )
for_in_ok+=( set-intersection.py )
for_in_ok+=( set-difference.py )
for_in_ok+=( task-summary-2.py )
for_in_ok+=( singleton-words.py )
for_in_ok+=( count-lines.py )
for_in_ok+=( word-intersection.py )
for_in_ok+=( sets.py )
for_in_ok+=( book-encoder.py book-decoder.py )
for_in_ok+=( birth-month-counts.py )
for_in_ok+=( ex2-mark-lab-exam.py )
for_in_ok+=( ex3-mark-lab-exam.py )
for_in_ok+=( exj-1.4.py )
for_in_ok+=( exja-1.4.py )

if ! print -l $for_in_ok | grep -q "^"$TASK'$'
then
   if sed 's:^\s*#.*$::g' $TASK | grep -w for | grep -w in
   then
      print "error: for/in loops are not $MODULE compliant"
      exit 1
   fi
fi

sorted_ok=()
sorted_ok+=( task-summary-1.py )
sorted_ok+=( word-intersection.py )
sorted_ok+=( exj-1.4.py )
sorted_ok+=( exja-1.4.py )

if ! print -l $sorted_ok | grep -q "^"$TASK'$'
then
   for word in range max min sort sorted find insert sum eval indexOf abs exec
   do
      if sed 's:^\s*#.*$::g' $TASK | grep -e "\\<$word\\>\s*("
      then
         print "error: the $word() function or method is not $MODULE compliant"
         exit 1
      fi
   done
fi

for word in break continue
do
   if sed 's:^\s*#.*$::g' $TASK | grep -w $word
   then
      print "error: the $word statement is not $MODULE compliant"
      exit 1
   fi
done

print ok
