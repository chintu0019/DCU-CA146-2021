#!/usr/bin/env python3

import os

extension = ".py"
files = os.listdir(".")

i = 0
while i < len(files):
   with open(files[i]) as f:
      content = f.read()

   # Accept the correct extension.
   is_py_file = files[i][len(files[i])-len(extension):] == extension

   # Accept the correct shebang.
   is_py_file = is_py_file or content.split("\n")[0] == "#!/usr/bin/env python"

   # Require the file to be non-empty.
   is_py_file = is_py_file and len(content) != 0

   if is_py_file:
      print files[i]
   i = i + 1
