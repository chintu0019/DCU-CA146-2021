#/usr/bin/env zsh

python $TASK fish dog cat fish mouse
print

python $TASK dog dog cat fish mouse
print

python $TASK flee dog cat fish mouse elephant flee
print

python $TASK moose dog cat fish mouse elephant flee
print

a=( dog cat fish mouse elephant flee )
python $TASK moose $a $a
print

python $TASK moose $a moose $a

