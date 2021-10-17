#!/usr/bin/env zsh

if [[ ${TASK##*.} != "py" ]]
then
   if test -s $TASK
   then
      print "ok (style, etc.)"
      exit 0
   else
      print "Potential error: file appears to be empty."
      exit 1
   fi
   exit 0
fi

tmp="capture-output.txt"

touch $tmp
python shebang.py > $tmp
err1="$?"

if [[ "$err1" != "0" ]]
then
   print "***************************************************"
   cat $tmp
fi >&2

python indentation.py > $tmp
err2="$?"

if [[ "$err2" != "0" ]]
then
   print "***************************************************"
   cat $tmp
fi >&2

zsh style.zsh > $tmp
err3="$?"

if [[ "$err3" != "0" ]]
then
   print "***************************************************"
   cat $tmp
fi >&2

zsh banned.zsh > $tmp
err4="$?"

if [[ "$err4" != "0" ]]
then
   print "***************************************************"
   cat $tmp
fi >&2

if [[ "$err1$err2$err3$err4" == "0000" ]]
then
   print "ok (style, etc.)"
   true
else
   print "style or validation error; see warnings (above) for details"
   false
fi
