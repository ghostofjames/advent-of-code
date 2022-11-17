import numpy as np

with open("input.txt") as f:
    data = f.read()

dots, cmds = data.split('\n\n')

dots = [[int(i) for i in dot.split(",")] for dot in dots.splitlines()]

max_x = max(i[0] for i in dots) + 1
max_y = max(i[1] for i in dots) + 1
paper = np.zeros((max_y, max_x), dtype=bool)
for dot in dots:
    paper[dot[1], dot[0]] = 1

# Part 1
dir, pos = cmds.splitlines()[0].split(" ")[-1].split("=")
pos = int(pos)

if dir == 'x':
    paper, _, extra = np.split(paper, [pos, pos+1], axis=1)
    extra = np.flip(extra, axis=1)
elif dir == 'y':
    paper, _, extra = np.split(paper, [pos, pos+1], axis=0)
    extra = np.flip(extra, axis=0)

paper = np.logical_or(paper, extra)

print(f"Part 1: {np.count_nonzero(paper)}")


# Part 2
for cmd in cmds.splitlines()[1:]:
    dir, pos = cmd.split(" ")[-1].split("=")
    pos = int(pos)

    if dir == 'x':
        paper, _, extra = np.split(paper, [pos, pos+1], axis=1)
        extra = np.flip(extra, axis=1)
    elif dir == 'y':
        paper, _, extra = np.split(paper, [pos, pos+1], axis=0)
        extra = np.flip(extra, axis=0)

    paper = np.logical_or(paper, extra)

print(f"Part 2:")
for iy in np.ndindex(paper.shape[0]):
    for ix in np.ndindex(paper.shape[1]):
        if paper[iy[0], ix[0]]:
            print("#", end="")
        else:
            print(".", end="")
    print('')
