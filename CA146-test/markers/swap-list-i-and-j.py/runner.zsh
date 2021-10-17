#!/usr/bin/env zsh

python3 wrapper.py 1 2 "cat" "elephant" "mouse" "lizard" "horse" "mongoose"
print
python3 wrapper.py 0 6 a ab abc abcd abcde abcdef abcdefg
print
python3 wrapper.py 3 4 87654321 7654321 654321 54321 4321 321 21 2
print
python3 wrapper.py 3 3 "" "" "" "" "" "" "" "" "" ""
print
python3 wrapper.py 0 0 "mongoose"
print
python3 wrapper.py 6 2 $(seq 10)
