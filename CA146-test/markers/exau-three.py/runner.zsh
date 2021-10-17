#!/usr/bin/zsh

set -e

cat <<EOF
Running your upload with various inputs...

EOF

for n in $( seq 35 -1 -15 )
do
   print -n "test $n: "
   print $n | python3 exau-three.py $n
done
