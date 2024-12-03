import math
import re

with open("input.txt") as f:
    data = f.read()


# Part 1

instructions = re.findall("mul\(\d+,\d+\)", data)

total = sum(math.prod(map(int, re.findall("\d+", ins))) for ins in instructions)

print(f"Part 1: {total}")


# Part 2

instructions = re.findall("mul\(\d+,\d+\)|do\(\)|don't\(\)", data)

total = 0
enabled = True
for ins in instructions:
    if ins == "don't()":
        enabled = False
    elif ins == "do()":
        enabled = True
    else:
        total += enabled * math.prod(map(int, re.findall("\d+", ins)))


print(f"Part 2: {total}")
