#!/usr/bin/env zsh

set -e
mkdir tmp -p
cd tmp

expect=()
no_expect=()

for p in one two dog jkhkjhkh
do
   print $p > $p.py
   expect+=( $p.py $p.py.bak )
done

for p in rain sun snow showers jljljkjjjj
do
   {
      print '#!/usr/bin/env python'
      print $p
   } > $p.txt
   expect+=( $p.txt $p.txt.bak )
done

for p in mouse elephant hhhhh
do
   print $p > $p.py.bak
   expect+=( $p.py.bak )
   no_expect+=( $p.py.bak.bak )
done

python ../backup-files-1.py

for f in $expect
do
   print "checking $f hashes (this verifies the file and its contents)..."
   [[ -f $f ]] && md5sum $f || print missing
done

for f in $no_expect
do
   print "checking $f does not exists..."
   [[ -f $f ]] || print ok
   [[ -f $f ]] && print "exists (incorrectly)"
done

cd ..
rm -r tmp

