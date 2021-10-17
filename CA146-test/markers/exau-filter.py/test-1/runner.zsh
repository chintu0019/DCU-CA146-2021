#!/usr/bin/zsh

set -e

cat <<EOF
Running your upload with various inputs...
EOF

for m in 3 5 6
do
   cat <<EOF

Testing for divisibility by $m...

EOF
   seq 1 50 | python3 exau-filter.py $m
done
