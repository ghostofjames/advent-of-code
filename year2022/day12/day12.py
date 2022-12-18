from collections import deque

import numpy as np

with open("input.txt") as f:
    data = f.read()

heightmap = np.array([list(line) for line in data.splitlines()])
start = np.where(heightmap == 'S')
start = (start[0][0], start[1][0])
end = np.where(heightmap == 'E')
end = (end[0][0], end[1][0])


def get_neighbours(h, c):
    y, x = c
    for n in [(y, x - 1), (y + 1, x), (y, x + 1), (y - 1, x)]:
        if 0 <= n[0] < h.shape[0] and 0 <= n[1] < h.shape[1]:
            yield n


def get_value(v):
    if v == 'S':
        return ord('a')
    if v == 'E':
        return ord('z')
    return ord(v)


# Part 1
unvisited = deque([(start, 0)])
visited = {start: 0}

while unvisited:
    curr, dist = unvisited.popleft()
    for neighbour in get_neighbours(heightmap, curr):
        if not (get_value(heightmap[neighbour]) - get_value(heightmap[curr]) <= 1):
            continue
        if neighbour not in visited:
            visited[neighbour] = dist + 1
            unvisited.append((neighbour, dist + 1))

print(f"Part 1: {visited[end]}")


# Part 2
unvisited = deque([(end, 0)])
visited = {end: 0}
while unvisited:
    curr, dist = unvisited.popleft()

    if heightmap[curr] == 'a':
        break

    for neighbour in get_neighbours(heightmap, curr):
        if not (get_value(heightmap[curr]) - get_value(heightmap[neighbour]) <= 1):
            continue
        if neighbour not in visited:
            visited[neighbour] = dist + 1
            unvisited.append((neighbour, dist + 1))

print(f"Part 2: {dist}")
