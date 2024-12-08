from itertools import permutations

with open("input.txt") as f:
    data = f.read()


grid = {}
for y, line in enumerate(data.splitlines()):
    for x, char in enumerate(line):
        grid[(x, y)] = char


# Part 1


def get_antinode(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    newx = x2 + (x2 - x1)
    newy = y2 + (y2 - y1)
    return (newx, newy)


antinodes = set()
for freq in {*grid.values()} - {"."}:
    antennas = [p for p in grid if grid[p] == freq]
    antinodes |= {get_antinode(a, b) for a, b in permutations(antennas, 2)}

print(f"Part 1: {len(antinodes & set(grid))}")


# Part 2


def get_antinodes(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    for n in range(50):
        newx = x2 + (x2 - x1) * n
        newy = y2 + (y2 - y1) * n
        yield (newx, newy)


antinodes = set()
for freq in {*grid.values()} - {"."}:
    antennas = [p for p in grid if grid[p] == freq]
    antinodes |= {
        antinode
        for a, b in permutations(antennas, 2)
        for antinode in get_antinodes(a, b)
    }

print(f"Part 2: {len(antinodes & set(grid))}")
