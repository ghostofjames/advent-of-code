data = []
with open("input.txt") as f:
    data = f.read().splitlines()

# Part 1
position = 0
depth = 0

for i in data:
    cmd, n = i.split(" ")

    match cmd:
        case "forward":
            position += int(n)
        case "down":
            depth += int(n)
        case "up":
            depth -= int(n)

print(f"Part 1: {position * depth}")

# Part 2
position = 0
depth = 0
aim = 0

for i in data:
    cmd, n = i.split(" ")

    match cmd:
        case "forward":
            position += int(n)
            depth += aim * int(n)
        case "down":
            aim += int(n)
        case "up":
            aim -= int(n)

print(f"Part 2: {position * depth}")
