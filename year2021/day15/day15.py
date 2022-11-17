import heapq
from collections import defaultdict

import numpy as np

with open("input.txt") as f:
    data = f.read()

cave = np.array([[int(x) for x in y] for y in data.splitlines()])


def get_neighbours(x, y, grid):
    neighbours = []

    if y > 0:
        neighbours.append((x, y - 1))
    if y < grid.shape[0] - 1:
        neighbours.append((x, y + 1))
    if x > 0:
        neighbours.append((x - 1, y))
    if x < grid.shape[1] - 1:
        neighbours.append((x + 1, y))

    return neighbours


def man_distance(a, b):
    x1, y1 = a
    x2, y2 = b
    return abs(x1 - x2) + abs(y1 - y2)


# Part 1
start = (0, 0)
target = (cave.shape[0]-1, cave.shape[1]-1)

open = []
closed = set()
parents = {}
g_score = defaultdict(lambda: np.Inf)
g_score[start] = 0

heapq.heappush(open, (man_distance(start, target), start))

while open:
    _, current = heapq.heappop(open)

    if current == target:
        break
    elif current in closed:
        continue
    else:
        for neighbour in get_neighbours(*current, cave):
            if neighbour in closed:
                continue
            cost = cave[neighbour]

            new_g = g_score[current] + cost

            if new_g <= g_score[neighbour]:
                g_score[neighbour] = new_g
                parents[neighbour] = current
                f = man_distance(neighbour, target) + new_g
                heapq.heappush(open, (f, neighbour))

        closed.add(current)

risk = 0
while current in parents:
    risk += cave[current]
    current = parents[current]

print(f"Part 1: {risk}")


# Part 2

def add(v, n):
    v += n
    if v >= 10:
        return v - 9
    return v


add_v = np.vectorize(add)

big_cave = np.concatenate([cave, *[add_v(cave, n)
                          for n in range(1, 5)]], axis=0)
big_cave = np.concatenate([big_cave, *[add_v(big_cave, n)
                          for n in range(1, 5)]], axis=1)

start = (0, 0)
target = (big_cave.shape[0]-1, big_cave.shape[1]-1)

open = []
closed = set()
parents = {}
g_score = defaultdict(lambda: np.Inf)
g_score[start] = 0

heapq.heappush(open, (man_distance(start, target), start))

while open:
    _, current = heapq.heappop(open)

    if current == target:
        break
    elif current in closed:
        continue
    else:
        for neighbour in get_neighbours(*current, big_cave):
            if neighbour in closed:
                continue
            cost = big_cave[neighbour]

            new_g = g_score[current] + cost

            if new_g <= g_score[neighbour]:
                g_score[neighbour] = new_g
                parents[neighbour] = current
                f = man_distance(neighbour, target) + new_g
                heapq.heappush(open, (f, neighbour))

        closed.add(current)

risk = 0
while current in parents:
    risk += big_cave[current]
    current = parents[current]

print(f"Part 2: {risk}")
