from itertools import combinations

with open("input.txt") as f:
    data = [list(y) for y in f.read().splitlines()]


# Part 1

# Expand y
y = []
for i in data:
    y.append(i)
    if "#" not in i:
        y.append(i)

# Expand x
x = []
for i in zip(*y):
    x.append(i)
    if "#" not in i:
        x.append(i)

expanded = list(zip(*x))

galaxies = [
    (x, y) for y, row in enumerate(expanded) for x, col in enumerate(row) if col == "#"
]

part1 = sum(
    abs(ax - bx) + abs(ay - by) for (ax, ay), (bx, by) in combinations(galaxies, 2)
)

print(f"Part 1: {part1}")
assert part1 == 9639160


# Part 2


emptyrows = [y for y, row in enumerate(data) if "#" not in row]
emptycols = [x for x, col in enumerate(zip(*data)) if "#" not in col]

galaxies = [
    (x, y) for y, row in enumerate(data) for x, col in enumerate(row) if col == "#"
]

part2 = sum(
    sum(1 * (1000000 if x in emptycols else 1) for x in range(min(ax, bx), max(ax, bx)))
    + sum(
        1 * (1000000 if y in emptyrows else 1) for y in range(min(ay, by), max(ay, by))
    )
    for (ax, ay), (bx, by) in combinations(galaxies, 2)
)

print(f"Part 2: {part2}")
assert part2 == 752936133304
