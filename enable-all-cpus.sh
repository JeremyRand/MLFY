#!/usr/bin/env bash

# Enables all logical CPU's.  Useful for reversing the effects of
# `disable-cpus.sh`.  Needs root privs.

for online in /sys/devices/system/cpu/cpu*/online ; do
    echo 1 > "$online"
done
