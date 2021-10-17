#!/usr/bin/env python

import os
import sys

with open(os.environ["TASK"]) as f:
   try:
      line = f.readline().rstrip()
   except:
      line = ""
   try:
      empty = f.readline().rstrip()
   except:
      empty = "x"

print "Validating shebang..."
if line != "#!/usr/bin/env python3":
   print
   print "error: the \"#!/usr/bin/env python3\" shebang line is missing"
   print "     found \"{}\"".format(line)
   print
   sys.exit(1)

if len(empty) != 0:
   print
   print "error: always leave a blank line after the shebang"
   print
   sys.exit(1)

print
print line
print
print "ok"
print
