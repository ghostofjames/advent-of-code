with open("input.txt") as f:
    data = f.read().split(',')
    # data = "se,sw,se,sw,sw"

# Thanks to https://www.redblobgames.com/grids/hexagons/ for help with hexagonal grids


def cube_add(a, b):
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])


def cube_sub(a, b):
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2])


def cube_distance(a, b=(0, 0, 0)):
    vec = cube_sub(a, b)
    return (abs(vec[0]) + abs(vec[1]) + abs(vec[2])) // 2


directions = {
    #     ( q,  r,  s)
    "n":  (00, -1, +1),
    "ne": (+1, -1,  0),
    "se": (+1,  0, -1),
    "s":  (00, +1, -1),
    "sw": (-1, +1,  0),
    "nw": (-1,  0, +1),
}

# Part 1
#          (q, r, s)
position = (0, 0, 0)
for dir in data:
    position = cube_add(position, directions[dir])

steps = cube_distance(position)
print(f"Part 1: {steps}")


# Part 2
max_steps = 0
position = (0, 0, 0)
for dir in data:
    position = cube_add(position, directions[dir])

    max_steps = max(max_steps, cube_distance(position))

print(f"Part 2: {max_steps}")
