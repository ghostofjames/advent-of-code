from itertools import pairwise

with open("input.txt") as f:
    data = f.read()
#     data = """498,4 -> 498,6 -> 496,6
# 503,4 -> 502,4 -> 502,9 -> 494,9"""

rocks = set()
for path in data.splitlines():
    for a, b in pairwise(tuple(map(int, p.split(','))) for p in path.split(" -> ")):
        if a[0] == b[0]:
            for y in range(min(a[1], b[1]), max(a[1], b[1]) + 1):
                rocks.add((a[0], y))
        else:
            for x in range(min(a[0], b[0]), max(a[0], b[0]) + 1):
                rocks.add((x, a[1]))

max_ = max(rocks, key=lambda x: x[1])[1]


# Part 1
def drop_sand(max_y):
    position = (500, 0)
    while position[1] < max_y:

        next_pos = (position[0], position[1] + 1)
        if next_pos not in sand and next_pos not in rocks:
            position = next_pos
            continue

        next_pos = (position[0] - 1, position[1] + 1)
        if next_pos not in sand and next_pos not in rocks:
            position = next_pos
            continue

        next_pos = (position[0] + 1, position[1] + 1)
        if next_pos not in sand and next_pos not in rocks:
            position = next_pos
            continue

        return position

    return False


sand = set()
while True:
    new = drop_sand(max_)
    if not new:
        break
    sand.add(new)

print(f"Part 1: {len(sand)}")


# Part 2
def drop_sand_2(max_y):
    position = (500, 0)
    while position[1] < max_y:

        next_pos = (position[0], position[1] + 1)
        if next_pos not in sand and next_pos not in rocks:
            position = next_pos
            continue

        next_pos = (position[0] - 1, position[1] + 1)
        if next_pos not in sand and next_pos not in rocks:
            position = next_pos
            continue

        next_pos = (position[0] + 1, position[1] + 1)
        if next_pos not in sand and next_pos not in rocks:
            position = next_pos
            continue

        return position

    return position


sand = set()
floor = max_ + 1
while True:
    new = drop_sand_2(floor)
    sand.add(new)
    if new == (500, 0):
        break

print(f"Part 2: {len(sand)}")
