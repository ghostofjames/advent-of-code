from collections import defaultdict

data = []
with open("input.txt") as f:
    data = f.read().splitlines()

lines = [[[int(n) for n in point.split(",")]
          for point in line.split(" -> ")]
         for line in data]

# Part 1
areas = defaultdict(int)  # dict key: (x, y) value: n (default 0)

for line in lines:
    if (line[0][0] != line[1][0]) and (line[0][1] != line[1][1]):
        continue  # ignore non straight lines

    # Interpolate points
    start, end, mid = line[0], line[1], []
    if end[1] == start[1]:
        mid = [(x, start[1])
               for x in range(*sorted([start[0], end[0]]))][1:]
    elif end[0] == start[0]:
        mid = [(start[0], y)
               for y in range(*sorted([start[1], end[1]]))][1:]
    points = [tuple(start)] + mid + [tuple(end)]

    # Add points to area
    for point in points:
        areas[point] += 1

overlaps = sum([v >= 2 for v in areas.values()])
print(f"Part 1: {overlaps}")


# Part 2
areas2 = defaultdict(int)

for line in lines:
    start, end, mid = line[0], line[1], []
    if end[1] == start[1]:
        mid = [(x, start[1])
               for x in range(*sorted([start[0], end[0]]))][1:]
    elif end[0] == start[0]:
        mid = [(start[0], y)
               for y in range(*sorted([start[1], end[1]]))][1:]
    else:
        step_x = 1 if end[0] - start[0] > 0 else -1
        step_y = 1 if end[1] - start[1] > 0 else -1
        mid = [(start[0] + i * step_x, start[1] + i * step_y)
               for i in range(1, abs(start[0] - end[0]))]

    points = [tuple(start)] + mid + [tuple(end)]

    for point in points:
        areas2[point] += 1

overlaps = sum([v >= 2 for v in areas2.values()])
print(f"\nPart 2: {overlaps}")
