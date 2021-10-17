#!/usr/bin/env zsh

files=( fstab passwd crontab )
dirs=( cron.d init.d )

touch $files
mkdir $dirs

python $TASK

rm $files
rmdir $dirs
