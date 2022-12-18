from collections import deque

with open("input.txt") as f:
    data = f.read()

cubes = set(tuple(map(int, cube.split(','))) for cube in data.splitlines())


def adjacent_cubes(cube):
    x, y, z = cube
    return [(x-1, y, z), (x+1, y, z),
            (x, y-1, z), (x, y+1, z),
            (x, y, z-1), (x, y, z+1),
            ]


# Part 1
surfaces = 0
for cube in cubes:
    for n in adjacent_cubes(cube):
        if n not in cubes:
            surfaces += 1

print(f"Part 1: {surfaces}")


# Part 2
def in_bounds(cube):
    return all(lb <= c <= ub for lb, c, ub in zip(minb, cube, maxb))


minb = (min(cubes, key=lambda x: x[0])[0] - 1,
        min(cubes, key=lambda x: x[1])[1] - 1,
        min(cubes, key=lambda x: x[2])[2] - 1)
maxb = (max(cubes, key=lambda x: x[0])[0] + 1,
        max(cubes, key=lambda x: x[1])[1] + 1,
        max(cubes, key=lambda x: x[2])[2] + 1)

surfaces = 0
seen = set()
queue = deque([minb])

while queue:
    c = queue.popleft()
    if c in seen:
        continue
    seen.add(c)
    for n in filter(in_bounds, adjacent_cubes(c)):
        if n in cubes:
            surfaces += 1
        if n not in cubes and n not in seen:
            queue.append(n)

print(f"Part 2: {surfaces}")
