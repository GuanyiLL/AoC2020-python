#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 11:24:26 2021

@author: ra1n
"""

from itertools import combinations
with open("src/input.txt") as file:
    data = [int(line) for line in file]

# Part 1 ===
for combo in combinations(data, 2):
    if combo[0] + combo[1] == 2020:
        part1 = combo[0] * combo[1]
        break

# Bonus one-liner
part1 = max(i*j if i + j == 2020 else 0 for i in data for j in data)


# Part 2 ===
for combo in combinations(data, 3):
    if combo[0] + combo[1] + combo[2] == 2020:
        part2 = combo[0] * combo[1] * combo[2]
        break

# Bonus one-liner
part2 = max(i*j*k if i + j + k == 2020 else 0 for i in data for j in data for k in data)

print("Part 1:", part1)
print("Part 2:", part2)