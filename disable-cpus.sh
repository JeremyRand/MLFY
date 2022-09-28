#!/usr/bin/env bash

# Pipe in a newline-delimited list of logical CPU numbers to disable.
# Needs root privs.

while read CPU; do
    echo 0 > "/sys/devices/system/cpu/cpu$CPU/online"
done
