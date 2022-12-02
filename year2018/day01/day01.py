from itertools import cycle

with open("input.txt") as f:
    data = f.read()

# Part 1
frequency = sum(map(int, data.splitlines()))

print(f"Part 1: {frequency}")


# Part 2
seen = set()
frequency = 0
for i in cycle(map(int, data.splitlines())):
    frequency += i
    if frequency in seen:
        break
    else:
        seen.add(frequency)
print(f"Part 2: {frequency}")
