#!/usr/bin/zsh

while read name mark junk
do
   email=$( dcu-email-address $name)
   print $name $mark $email
   {
      cat <<EOF
Your CA116 lab exam 2 mark is $mark. This mark is out of 100.

This mark constitutes a third of your continuous assessment mark, which itself constitutes 60% of your mark overall.

I have yet to review the uploads for issues related to academic integrity, and reserve the right to pursue such matters as required.
EOF
   } | mail -s "2021/CA116, lab exam 2 mark for $name" $email

   sleep 5
done
