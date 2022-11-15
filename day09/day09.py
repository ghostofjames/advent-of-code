from math import prod

import numpy as np

data = []
with open("input.txt") as f:
    data = f.read().splitlines()


def get_neighbours(y, x, grid):
    neighbours = []

    if y > 0:
        neighbours.append(grid[y - 1, x])
    if y < grid.shape[0] - 1:
        neighbours.append(grid[y + 1, x])
    if x > 0:
        neighbours.append(grid[y, x - 1])
    if x < grid.shape[1] - 1:
        neighbours.append(grid[y, x + 1])

    return neighbours


def count_basin_neighbours(y, x, grid, visited):
    visited[y, x] = 1
    count = 0

    if y > 0:
        if grid[y - 1, x] < 9 and not visited[y - 1, x]:
            count += 1 + count_basin_neighbours(y - 1, x, grid, visited)
    if y < grid.shape[0] - 1:
        if grid[y + 1, x] < 9 and not visited[y + 1, x]:
            count += 1 + count_basin_neighbours(y + 1, x, grid, visited)
    if x > 0:
        if grid[y, x - 1] < 9 and not visited[y, x - 1]:
            count += 1 + count_basin_neighbours(y, x - 1, grid, visited)
    if x < grid.shape[1] - 1:
        if grid[y, x + 1] < 9 and not visited[y, x + 1]:
            count += 1 + count_basin_neighbours(y, x + 1, grid, visited)

    return count


def get_basin_size(y, x, heightmap):
    visited = np.zeros(heightmap.shape)
    size = 1 + count_basin_neighbours(y, x, heightmap, visited)
    return size


heightmap = np.array([[int(x) for x in y] for y in data])

# Part 1
risk_level = 0
for iy, ix in np.ndindex(heightmap.shape):
    height = heightmap[iy, ix]

    if all(height < n for n in get_neighbours(iy, ix, heightmap)):
        risk_level += (1 + height)

print(f"Part 1: {risk_level}")


# Part 2
basin_sizes = []
for iy, ix in np.ndindex(heightmap.shape):
    height = heightmap[iy, ix]

    if all(height < n for n in get_neighbours(iy, ix, heightmap)):
        basin_sizes.append(get_basin_size(iy, ix, heightmap))

print(f"Part 2: {prod(sorted(basin_sizes)[-3:])}")
