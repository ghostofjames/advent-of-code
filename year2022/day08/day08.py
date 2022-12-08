import numpy as np

with open("input.txt") as f:
    data = f.read()

trees = np.array([[int(i) for i in line] for line in data.splitlines()])


# Part 1
visible = np.zeros_like(trees, dtype=bool)
for iy, ix in np.ndindex(trees.shape):
    height = trees[iy, ix]

    edge = (iy == 0) or (iy == trees.shape[0]-1) or (ix == 0) or (ix == trees.shape[1]-1)
    left = all(trees[iy, x] < height for x in range(ix))
    right = all(trees[iy, x] < height for x in range(ix + 1, trees.shape[1]))
    up = all(trees[y, ix] < height for y in range(iy))
    down = all(trees[y, ix] < height for y in range(iy + 1, trees.shape[0]))

    if edge or left or right or up or down:
        visible[iy, ix] = True

print(f"Part 1: {np.count_nonzero(visible)}")

# Part 2
scenic_scores = np.zeros_like(trees)
for iy, ix in np.ndindex(trees.shape):
    height = trees[iy, ix]

    dirs = [[trees[iy, x] for x in range(ix)][::-1],
            [trees[iy, x] for x in range(ix + 1, trees.shape[1])],
            [trees[y, ix] for y in range(iy)][::-1],
            [trees[y, ix] for y in range(iy + 1, trees.shape[0])]]

    scenic_score = 1
    for dir in dirs:
        score = 0
        for tree in dir:
            score += 1
            if tree >= height:
                break
        scenic_score *= score

    scenic_scores[iy, ix] = scenic_score

print(f"Part 2: {scenic_scores.max()}")
