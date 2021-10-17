#!/usr/bin/env zsh

python3 wrapper.py "" "" "dog" "" "" "cat" "" "" "" "mouse"
print
python3 wrapper.py "" "" "dog" "" "" "cat" "" "" "" "mouse" "elephant"
print
python3 wrapper.py "" "" "" "" "" "" "" "" "" ""
print
python3 wrapper.py
print
python3 wrapper.py "mongoose"
print
python3 wrapper.py $(seq 10)
