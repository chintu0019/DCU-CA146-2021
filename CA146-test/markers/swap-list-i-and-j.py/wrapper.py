#!/usr/bin/env python3

import sys, os

a = sys.argv[1:]
i = int(a[0])
j = int(a[1])
a = a[2:]

__name__ = 'einstein'

print("before: a =", a)
print("        i =", i)
print("        j =", j)
exec(open(os.environ.get("TASK")).read())
print("after: a =", a)
