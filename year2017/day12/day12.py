with open("input.txt") as f:
    data = f.read()

pipes = {}
for line in data.splitlines():
    start, ends = line.split(" <-> ")
    pipes[int(start)] = set(int(end) for end in ends.split(', '))


# Part 1
group = {0}
open = {0}
while open:
    next_open = set()
    for item in open:
        next_open.update(pipes[item])
    open = next_open - group
    group.update(next_open)

print(f"Part 1: {len(group)}")


# Part 2
groups = 0
remaining = set(pipes)
while remaining:
    groups += 1

    start = remaining.pop()

    group = {start}
    open = {start}
    while open:
        next_open = set()
        for item in open:
            next_open.update(pipes[item])
        open = next_open - group
        group.update(next_open)

    remaining -= group

print(f"Part 2: {groups}")
