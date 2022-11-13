import numpy as np
from math import prod

data = []
# with open("day09_input.txt") as f:
#     data = f.read().splitlines()
with open("example.txt") as f:
    data = f.read().splitlines()
heightmap = np.array([[int(x) for x in y] for y in data])


def get_neighbours(y, x, heightmap):
    neighbours = []
    if y > 0:
        neighbours.append(heightmap[y - 1, x])
    if y < heightmap.shape[0] - 1:
        neighbours.append(heightmap[y + 1, x])
    if x > 0:
        neighbours.append(heightmap[y, x - 1])
    if x < heightmap.shape[1] - 1:
        neighbours.append(heightmap[y, x + 1])
    return neighbours


# Part 1
risk_level = 0
for iy, ix in np.ndindex(heightmap.shape):
    height = heightmap[iy, ix]

    if all(height < n for n in get_neighbours(iy, ix, heightmap)):
        risk_level += (1 + height)

print(f"Part 1: {risk_level}")

# # Part 2
# basin_sizes = []
# for iy, ix in np.ndindex(heightmap.shape):
#     height = heightmap[iy, ix]
#     neighbours = []
#     if iy > 0:
#         neighbours.append(heightmap[iy - 1, ix])
#     if iy < heightmap.shape[0] - 1:
#         neighbours.append(heightmap[iy + 1, ix])
#     if ix > 0:
#         neighbours.append(heightmap[iy, ix - 1])
#     if ix < heightmap.shape[1] - 1:
#         neighbours.append(heightmap[iy, ix + 1])

#     if all(height < n for n in get_neighbours(iy, ix, heightmap)):
#         # get basin size
#         pass

# print(f"Part 2: {prod(basin_sizes[-3:])}")
