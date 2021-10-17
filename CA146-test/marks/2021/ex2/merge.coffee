fs = require "fs"

lines = fs.readFileSync(0).toString().trim().split "\n"
marks = {}

for [user, mark] in (line.split " " for line in lines)
  marks[user] ?= 0
  marks[user] += parseInt mark

for own user, mark of marks
  console.log user, mark
