#!/usr/bin/zsh

cat <<EOF
There is no unique output for this task, it depends upon the
characters from the pages which your implementation chooses
to use.

Therefore, here, the test runs your encoder, and then runs
a known-correct decoder to verify that your encoder is correct.

You will only see the output of your encoder if it is incorrect.
EOF

cat > expected.txt
python3 $TASK < expected.txt > encoded.txt
python3 ./.book-decoder.py < encoded.txt > decoded.txt

print
print "Decoded:"
sed 's/^/  /' decoded.txt

if ! cmp expected.txt decoded.txt
then
   print
   print "The original input and the decoded output do not match."
   print
   print "Here's your output:"
   sed 's/^/  /' encoded.txt
   exit 1
fi

wc -l < encoded.txt | read a
sort encoded.txt | uniq | wc -l | read b

if [[ $a != $b ]]
then
   print
   print "You appear to have re-used a triplet."
   print
   print "The first number below is a count of the number of"
   print "times which your encoder used the following triplet:"
   sort encoded.txt | sed 's/^/ - /' | uniq -c - | sort -nr | sed 's/^/  /'
fi

exit 0
