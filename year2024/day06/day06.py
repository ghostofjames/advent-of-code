from collections import defaultdict

with open("input.txt") as f:
    data = f.read()

grid = defaultdict(str)
for y, line in enumerate(data.splitlines()):
    for x, char in enumerate(line):
        grid[(x, y)] = char
        if char == "^":
            start = (x, y)

dirs = {"U": (0, -1), "R": (1, 0), "D": (0, 1), "L": (-1, 0)}
turn_right = {"U": "R", "R": "D", "D": "L", "L": "U"}


# Part 1

dir = "U"
pos = start
visited = set()
while grid[pos] != "":
    visited.add(pos)
    next_pos = (pos[0] + dirs[dir][0], pos[1] + dirs[dir][1])
    if grid[next_pos] == "#":
        dir = turn_right[dir]
    else:
        pos = next_pos

print(f"Part 1: {len(visited)}")


# Part 2


def walk(grid2):
    pos = start
    dir = "U"
    visited = set()
    while grid2[pos] != "" and (pos, dir) not in visited:
        visited.add((pos, dir))
        next_pos = (pos[0] + dirs[dir][0], pos[1] + dirs[dir][1])
        if grid2[next_pos] == "#":
            dir = turn_right[dir]
        else:
            pos = next_pos
    return {p for p, _ in visited}, (pos, dir) in visited


print(f"Part 2: {sum(walk(grid | {o: '#'})[1] for o in walk(grid)[0])}")
