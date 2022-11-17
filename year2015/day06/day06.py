import re
from itertools import product

with open("input.txt") as f:
    data = f.read()

instructions = []
for line in data.splitlines():
    inst = re.findall(r'turn on|turn off|toggle', line)[0]
    nums = [int(n) for n in re.findall(r'\d+', line)]
    start, end = nums[:2], nums[2:]
    instructions.append((inst, start, end))


# Part 1
lights = [[False for _ in range(0, 1000)] for _ in range(0, 1000)]

for inst, start, end in instructions:
    if inst == "turn on":
        for i, j in product(range(start[0], end[0]+1), range(start[1], end[1]+1)):
            lights[i][j] = True

    elif inst == "turn off":
        for i, j in product(range(start[0], end[0]+1), range(start[1], end[1]+1)):
            lights[i][j] = False

    else:
        for i, j in product(range(start[0], end[0]+1), range(start[1], end[1]+1)):
            lights[i][j] = not lights[i][j]

lit = sum(x for y in lights for x in y)
print(f"Part 1: {lit}")


# Part 2
lights = [[0 for _ in range(0, 1000)] for _ in range(0, 1000)]

for inst, start, end in instructions:
    if inst == "turn on":
        for i, j in product(range(start[0], end[0]+1), range(start[1], end[1]+1)):
            lights[i][j] += 1

    elif inst == "turn off":
        for i, j in product(range(start[0], end[0]+1), range(start[1], end[1]+1)):
            lights[i][j] -= 1 if lights[i][j] > 0 else 0

    else:
        for i, j in product(range(start[0], end[0]+1), range(start[1], end[1]+1)):
            lights[i][j] += 2

brightness = sum(x for y in lights for x in y)
print(f"Part 2: {brightness}")
