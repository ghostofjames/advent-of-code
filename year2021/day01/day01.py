with open("input.txt") as f:
    data = list(map(int, f.read().splitlines()))

# Part 1
c = 0
for i in range(0, len(data) - 1):
    if sum(data[i+1:i+2]) > sum(data[i:i+1]):
        c += 1
print(f"Part 1: {c}")

# Part 2
c = 0
for i in range(0, len(data) - 3):
    if sum(data[i+1:i+4]) > sum(data[i:i+3]):
        c += 1
print(f"Part 2: {c}")
