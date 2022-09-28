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
        caches.append(int(cpuset, 0))

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
