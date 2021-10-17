#!/usr/bin/env python3

import sys, os

a = sys.argv[1:]

__name__ = 'einstein'

print("before: a =", a)
exec(open(os.environ.get("TASK")).read())
print("after: a =", a)
