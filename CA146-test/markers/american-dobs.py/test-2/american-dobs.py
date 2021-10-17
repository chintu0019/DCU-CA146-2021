
import sys

with open("irish-dobs.txt") as f_in:
   lines = f_in.readlines()

with open("american-dobs.txt", "w") as f_out:
   i = 0
   while i < len(lines):
      parse = lines[i].split()
      date = parse[0].split("/")
      f_out.write(" ".join(["/".join([date[1], date[0], date[2]]), " ".join(parse[1:])]) + "\n")
      i = i + 1
