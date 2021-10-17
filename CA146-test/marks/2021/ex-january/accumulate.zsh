
grep "#smb " uploads/**/*(.) |
   tr " " "/" |
   cut -d/ -f 2,4 |
   tr "/" " " |
   {
      typeset -A marks
      while read user mark
      do
	 if [[ -z $marks[$user] ]]
	 then
	    marks[$user]=0
	 fi
	 marks[$user]=$(( marks[$user] + mark ))

      done

      for user in ${(@k)marks}
      do
	 print $user $marks[$user]
      done | sort
   }

