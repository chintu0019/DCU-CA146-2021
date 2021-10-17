#!/usr/bin/env python3

date = int(input())

year = date % 100
month = date // 100 % 100
day = date // 10000 % 100

print(month * 10000 + day * 100 + year)
