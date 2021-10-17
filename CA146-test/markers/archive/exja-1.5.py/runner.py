#!/usr/bin/env python3

import os
task = os.getenv("TASK")

s = "/hello/world"
print("s =", s)
with open(task) as f: exec(f.read())

print()
s = "//hello//world"
print("s =", s)
with open(task) as f: exec(f.read())

print()
s = ""
print("s =", s)
with open(task) as f: exec(f.read())

print()
s = "/////"
print("s =", s)
with open(task) as f: exec(f.read())
