from itertools import pairwise

data = []
with open("day01_input.txt") as f:
    data = list(map(int, f.read().splitlines()))


# Part 1
count = 0
for i, j in pairwise(data):
    if j > i:
        count += 1
print(count)

# Part 2
count = 0
for i in range(0, len(data) - 3):
    if sum(data[i+1:i+4])> sum(data[i:i+3]) :
        count += 1
print(count)