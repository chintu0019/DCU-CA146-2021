#!/usr/bin/env python3

import sys, os

a = sys.argv[1:]

s = a[0]
a = a[1:]

__name__ = 'einstein'

print("a =", a)
print("s =", s)
exec(open(os.environ.get("TASK")).read())
