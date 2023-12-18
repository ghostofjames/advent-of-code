from itertools import pairwise

with open("input.txt") as f:
    data = f.read()

plan = []
for line in data.splitlines():
    dir, dis, hex = line.split()
    plan.append((dir, int(dis), hex.strip("(").strip(")")))


def shoelace_formula(vert):
    area = sum(x1 * y2 - x2 * y1 for (x1, y1), (x2, y2) in pairwise(vert + [vert[0]]))
    return int(abs(area) / 2)


dirs = {"U": (0, 1), "D": (0, -1), "L": (-1, 0), "R": (1, 0)}


# Part 1

pos = (0, 0)
vertices = [pos]
parameter = 0

for line in plan:
    dir, dis, _ = line

    pos = (pos[0] + dirs[dir][0] * dis, pos[1] + dirs[dir][1] * dis)

    parameter += dis
    vertices.append(pos)

area = (shoelace_formula(vertices) - parameter // 2 + 1) + parameter

print(f"Part 1: {area}")


# Part 2

int_to_dir = ["R", "D", "L", "U"]

pos = (0, 0)
vertices = [pos]
parameter = 0

for line in plan:
    *_, hex = line
    dis = int(hex[1:-1], base=16)
    dir = int_to_dir[int(hex[-1])]

    pos = (pos[0] + dirs[dir][0] * dis, pos[1] + dirs[dir][1] * dis)

    parameter += dis
    vertices.append(pos)

area = (shoelace_formula(vertices) - parameter // 2 + 1) + parameter

print(f"Part 2: {area}")
