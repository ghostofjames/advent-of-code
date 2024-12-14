import itertools
import math
import re
from collections import Counter

with open("input.txt") as f:
    data = f.read()


robots = []
for line in data.splitlines():
    robots.append(
        tuple(tuple(int(d) for d in re.findall(r"-?\d+", n)) for n in line.split())
    )


# Part 1

width = 101
height = 103
seconds = 100


def find_final_pos(robot):
    return (
        (robot[0][0] + robot[1][0] * seconds) % width,
        (robot[0][1] + robot[1][1] * seconds) % height,
    )


final_robot_pos = [find_final_pos(robot) for robot in robots]

mw, mh = width // 2, height // 2

quadrant_count = [0, 0, 0, 0]
for pos in final_robot_pos:
    if pos[0] < mw and pos[1] < mh:
        quadrant_count[0] += 1
    elif pos[0] > mw and pos[1] < mh:
        quadrant_count[1] += 1
    elif pos[0] < mw and pos[1] > mh:
        quadrant_count[2] += 1
    elif pos[0] > mw and pos[1] > mh:
        quadrant_count[3] += 1

safety_factor = math.prod(quadrant_count)

assert safety_factor == 230172768
print(f"Part 1: {safety_factor}")


# Part 2


def update_robot(robot):
    return (
        (robot[0][0] + robot[1][0]) % width,
        (robot[0][1] + robot[1][1]) % height,
    ), robot[1]


def draw_robots(robots):
    count = Counter(robot[0] for robot in robots)
    for r in range(height):
        print("".join(str(count[(r, c)] or ".") for c in range(width)))


# find when no overlapping robots
time = 0
for t in itertools.count(start=1):
    robots = list(map(update_robot, robots))
    if not (Counter(robot[0] for robot in robots).most_common(1)[0][1] > 1):
        time = t
        break


draw_robots(robots)

print(f"Part 2: {time}")
