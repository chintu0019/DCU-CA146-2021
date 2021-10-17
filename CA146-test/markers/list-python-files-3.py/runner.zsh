#!/usr/bin/env zsh

set -e
mkdir tmp -p
cd tmp

for p in one two dog
do
   touch $p.py
done

for p in three four
do
   echo "content" > $p.py
done

for t in three four mouse elephant dog
do
   echo "content" > $t.txt
done

for p in rain sun snow showers
do
   {
      print '#!/usr/bin/env python3'
      print content
   } > $p
done

for p in hail
do
   {
      print '#!/usr/bin/env Python python'
      print content
   } > $p
done

python ../list-python-files-3.py | sort $argv
cd ..
rm -r tmp

