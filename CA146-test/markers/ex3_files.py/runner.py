#!/usr/bin/env python

import sys
import ex3_files

print "Contents of a.txt:"
sys.stdout.write(ex3_files.read("a.txt"))

print

print "Contents of b.txt:"
sys.stdout.write(ex3_files.read("b.txt"))

print


print "Hash of contents of c.txt:"

import hashlib
m = hashlib.md5()
m.update(ex3_files.read("c.txt"))

sys.stdout.write(m.hexdigest() + "\n")
