#!/usr/bin/env zsh

python3 wrapper.py "cat" "elephant" "mouse" "lizard" "horse" "mongoose"
print
python3 wrapper.py a ab abc abcd abcde abcdef abcdefg
print
python3 wrapper.py 87654321 7654321 654321 54321 4321 321 21 2
print
python3 wrapper.py "" "" "" "" "" "" "" "" "" ""
print
python3 wrapper.py "mongoose"
print
python3 wrapper.py $(seq 10)
