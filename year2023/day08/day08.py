import itertools
import math

with open("input.txt") as f:
    data = f.read()

instructions, rawnodes = data.split("\n\n")
nodes = {}
for n in rawnodes.splitlines():
    steps, lr = n.split(" = ")
    l, r = lr[1:-1].split(", ")
    nodes[steps] = {"L": l, "R": r}


# Part 1

steps = 0
location = "AAA"
for ins in itertools.cycle(instructions):
    steps += 1
    location = nodes[location][ins]
    if location == "ZZZ":
        break

print(f"Part 1: {steps}")


# Part 2

starts = [location for location in nodes.keys() if location.endswith("A")]

stepsforstarts = []
for start in starts:
    steps = 0
    location = start
    for ins in itertools.cycle(instructions):
        steps += 1
        location = nodes[location][ins]
        if location.endswith("Z"):
            break
    stepsforstarts.append(steps)

print(f"Part 2: {math.lcm(*stepsforstarts)}")
