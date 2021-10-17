#!/usr/bin/zsh

while read name mark junk
do
   email=$( dcu-email-address $name)
   print $name $mark $email
   {
      cat <<EOF
Your CA116 lab exam 3 mark is $mark. This mark is out of 100.

This mark constitutes a third of your continuous assessment mark for the module, which itself constitutes 60% of your mark overall.

Overall, the marks for this lab exam were weaker than I would have hoped for.  Therefore, I reviewed all of the incorrect uploads and awarded attempt marks where merited.

I have yet to review the uploads for issues related to academic integrity, and reserve the right to pursue such matters as required.
EOF
   } | mail -s "2021/CA116, lab exam 3 mark for $name" $email

   sleep 5
done
