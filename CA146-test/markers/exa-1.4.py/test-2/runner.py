#!/usr/bin/env python

import os
task = os.environ["TASK"]

d = {}
d["fish"] = "school"
d["dogs"] = "pack"
d["sheep"] = "flock"
d["cows"] = "herd"
d["bees"] = "swarm"
d["donkeys"] = "drove"
d["geese"] = "gaggle"

print "d =", d
print "running your script..."
print

execfile(task)
