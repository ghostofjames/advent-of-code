from collections import defaultdict

with open("input.txt") as f:
    data = f.read()

grid = defaultdict(str)
for y, line in enumerate(data.splitlines()):
    for x, char in enumerate(line):
        grid[(y, x)] = char

dirs = (-1, 0, 1)


# Part 1

count = 0
for y, x in list(grid.keys()):
    for dy in dirs:
        for dx in dirs:
            count += [grid[y + dy * n, x + dx * n] for n in range(4)] == list("XMAS")

print(f"Part 1: {count}")


# Part 2

count = 0
MASSAM = (list("MAS"), list("SAM"))
for y, x in list(grid.keys()):
    count += [grid[y + d, x + d] for d in dirs] in MASSAM and [
        grid[y + d, x - d] for d in dirs
    ] in MASSAM

print(f"Part 2: {count}")
