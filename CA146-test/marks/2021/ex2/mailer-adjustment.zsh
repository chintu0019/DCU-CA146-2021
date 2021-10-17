#!/usr/bin/zsh

while read name mark junk
do
   email=$( dcu-email-address $name)
   print $name $mark $email
   {
      cat <<EOF
Your revised CA116 lab exam 2 mark is $mark.

You are one of five students who successfully submitted one of the lab exam's task variants (instead of completing the task which your were asked to complete).

In light of the circumstances of your submitted work, this submission is being admitted as correct.

Therefore, your mark has been adjusted up, as reflected in the mark above.
EOF
   } | mail -s "2021/CA116, lab exam 2 revised mark for $name" $email

   sleep 5
done
