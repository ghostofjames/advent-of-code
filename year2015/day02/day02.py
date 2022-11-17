with open("input.txt") as f:
    data = f.read()

data = [[int(n) for n in p.split('x')] for p in data.splitlines()]


# Part 1
total = 0
for present in data:
    l, w, h = sorted(present)
    surface_area = (2 * l * w) + (2 * w * h) + (2 * h * l)
    extra = l * w
    total += surface_area + extra

print(f"Part 1: {total}")


# Part 2

total = 0
for present in data:
    l, w, h = sorted(present)
    shortest_distance = (l * 2) + (w * 2)
    volume = l * w * h
    total += shortest_distance + volume

print(f"Part 2: {total}")
