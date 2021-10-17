#!/usr/bin/env python
# number of non-horizonal lines that go through exactly 3 points
# Answers:
# CL1: 18
# CL2: 1223
# CL3: 28271

points = []

for i in range(3):
	points.append([(i, int(x)) for x in raw_input().split()])



# Brute force
lines = 0
for i, start in enumerate(points[0]):
	for j, mid in enumerate(points[1]):
		if (2, mid[1] + (mid[1] - start[1])) in points[2]:	# Check for existing end point
			lines += 1

print lines