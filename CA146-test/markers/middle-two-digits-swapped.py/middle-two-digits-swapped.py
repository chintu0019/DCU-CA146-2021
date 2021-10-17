#!/usr/bin/env python3

n = int(input())

n = n // 100 % 100
d1 = n // 10
d2 = n % 10

print(d2 * 10 + d1)
