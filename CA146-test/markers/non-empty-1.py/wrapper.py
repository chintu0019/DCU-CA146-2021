#!/usr/bin/env python3

import sys, os

a = sys.argv[1:]

__name__ = 'einstein'

print("a =", a)
exec(open(os.environ.get("TASK")).read())
