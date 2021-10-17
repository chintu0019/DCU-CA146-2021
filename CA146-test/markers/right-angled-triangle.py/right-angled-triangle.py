#!/usr/bin/env python3

hypotenuse = int(input())
opposite = int(input())
adjacent = int(input())

print(hypotenuse * hypotenuse == opposite * opposite + adjacent * adjacent)

# We're using Pythagoras' Theorem, here.  There's no need to take the square
# roots, because that does not change the equality of the values.
