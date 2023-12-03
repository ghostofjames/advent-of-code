from collections import defaultdict

with open("input.txt") as f:
    data = f.read()

lines = data.splitlines()

# Pad grid with . on the outside
lines = (
    ["." * (len(lines[0]) + 2)]
    + ["." + line + "." for line in lines]
    + ["." * (len(lines[0]) + 2)]
)

# Part 1

sum = 0
sum2 = 0
gears = defaultdict(list)
for i, line in enumerate(lines):
    n = ""
    counts = False
    gear = False
    for j, c in enumerate(line):
        if c.isdigit():
            n += c
            for di in [-1, 0, 1]:
                for dj in [-1, 0, 1]:
                    cc = lines[i + di][j + dj]
                    if cc != "." and not cc.isdigit():
                        counts = True
                        if cc == "*":
                            gear = (i + di, j + dj)
        else:
            if counts:
                sum += int(n)
                counts = False
            if gear:
                gears[gear].append(n)
                if len(gears[gear]) == 2:
                    sum2 += int(n) * int(gears[gear][0])
                gear = False
            n = ""

print(f"Part 1: {sum}")


# Part 2

print(f"Part 2: {sum2}")
