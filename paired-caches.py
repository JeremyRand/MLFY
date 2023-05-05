#!/usr/bin/env python3

# Pipe in the ouput of `lstopo --of xml`.
# Outputs a newline-delimited list of the logical CPU numbers that need to be
# disabled to avoid cache pairing.

import defusedxml.ElementTree as ET

tree = ET.parse('/dev/stdin')
root = tree.getroot()

caches = []

for element in root.iter("*"):
    objtype = element.get("type")
    if objtype is None:
        continue
    if "cache" in objtype.lower():
        cpuset = element.get("cpuset")
        if cpuset is None:
            continue

        # cpuset is an arbitrary-length integer, encoded as a big-endian
        # comma-separated list of hex-encoded 32-bit integers. Each 32-bit
        # integer has a leading "0x"; if the 32-bit integer is 0, it can be
        # encoded as an empty string. However, we take a shortcut here, because
        # on real-world Talos hardware, only the most significant 32-bit
        # integer is non-zero, so we simply take the most significant 32-bit
        # integer, and apply a bitshift based on the count of 32-bit integers.
        cpuset = cpuset.split(',')
        cpuset_shift = len(cpuset)
        cpuset_shift = cpuset_shift - 1
        cpuset_shift = cpuset_shift * 32
        cpuset = int(cpuset[0], 0)
        cpuset = cpuset << cpuset_shift

        caches.append(cpuset)

all_disable = set()

for cache in caches:
    #print(cache)
    tmp_cache = cache
    cpu = 0
    while not tmp_cache & 1:
        tmp_cache >>= 1
        cpu += 1
    cpu_enable = cpu
    cpu_disable = []
    while tmp_cache != 0:
        tmp_cache >>= 1
        cpu += 1
        if tmp_cache & 1:
            cpu_disable.append(cpu)
    #print(cpu_enable, cpu_disable)
    all_disable.update(cpu_disable)

for i in sorted(all_disable):
    print(i)
