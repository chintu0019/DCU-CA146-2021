#!/usr/bin/env python3

import os

extension = "py"
files = os.listdir(".")

i = 0
while i < len(files):
   with open(files[i]) as f:
      first_line = f.readline()

   # Accept the correct extension.
   tokens = files[i].split(".")
   is_py_file = tokens[len(tokens) - 1] == extension

   # And also accept the correct shebang.
   is_py_file = is_py_file or first_line.rstrip() == "#!/usr/bin/env python3"

   # But require the file to be non-empty, too.
   is_py_file = is_py_file and len(first_line) != 0

   if is_py_file:
      print(files[i])
   i = i + 1
