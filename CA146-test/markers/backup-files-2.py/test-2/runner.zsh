#!/usr/bin/env zsh

set -e
mkdir tmp -p
cd tmp

expect=()
no_expect=()

expect_dir=()
no_expect_dir=()


for p in one two dog cat
do
   print $p > $p.py
   expect+=( $p.py $p.py.bak )
done

for p in rain snow showers jhjjhjhjhjjh
do
   {
      print '#!/usr/bin/env python'
      print $p
   } > $p.txt
   expect+=( $p.txt $p.txt.bak )
done

for p in mouse elephant penguin
do
   print $p > $p.py.bak
   expect+=( $p.py.bak )
   no_expect+=( $p.py.bak.bak )
done

for d in oak maple pine jkhkhjk
do
   mkdir $d
   expect_dir+=( $d )
   no_expect_dir+=( $d.bak )
done

python ../backup-files-2.py

for f in $expect
do
   print "checking $f hashes (this verifies the file and its contents)..."
   [[ -f $f ]] && md5sum $f || print missing
done

for f in $no_expect
do
   print "checking $f does not exists..."
   [[ -e $f ]] || print ok
   [[ -e $f ]] && print "exists (incorrectly)"
done

for d in $expect_dir
do
   print "checking directory $d exists..."
   [[ -d $d ]] && print "ok" || print "missing"
done

for d in $no_expect_dir
do
   print "checking directory $d does not exists..."
   [[ -e $d ]] && print "exists (incorrectly)"
done

cd ..
rm -r tmp

