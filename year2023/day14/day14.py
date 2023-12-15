from itertools import count

with open("input.txt") as f:
    data = f.read()

rocks = [list(line) for line in data.splitlines()]


# Part 1

newrocks = []
for row in [*zip(*rocks)]:
    newrow = "".join(row)
    while ".O" in newrow:
        newrow = newrow.replace(".O", "O.")
    newrocks.append(newrow)

part1 = 0
for row in newrocks:
    load = 0
    for i, rock in enumerate(row):
        if rock == "O":
            load += len(row) - i

    part1 += load

print(f"Part 1: {part1}")
assert part1 == 113078


# Part 2


def slide(grid):
    for j in range(len(grid[0])):
        ci = 0
        for i in range(len(grid)):
            if grid[i][j] == "#":
                ci = i + 1
            if grid[i][j] == "O":
                grid[i][j] = "."
                grid[ci][j] = "O"
                ci += 1


def rotate(grid):
    new_grid = [["." for _ in range(len(grid))] for _ in range(len(grid[0]))]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            new_grid[j][len(grid) - i - 1] = grid[i][j]
    return new_grid


part2 = None

seen = {}
for cycle in count(1):
    for j in range(4):
        slide(rocks)
        rocks = rotate(rocks)

    x = "\n".join(["".join(rocks[i]) for i in range(len(rocks))])

    if x not in seen:
        seen[x] = cycle
        continue

    break

cycle_length = cycle - seen[x]
for a, b in seen.items():
    if b >= seen[x] and b % cycle_length == 1000000000 % cycle_length:
        rocks = [list(line) for line in a.split("\n")]

part2 = sum((len(rocks) - i) * rocks[i].count("O") for i in range(len(rocks)))

print(f"Part 2: {part2}")
assert part2 == 94255
