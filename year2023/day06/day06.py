import math

with open("input.txt") as f:
    data = f.read()

times, distances = data.splitlines()
times = [int(val) for val in times.split()[1:]]
distances = [int(val) for val in distances.split()[1:]]

# Part 1

total = 1
for time, distance in zip(times, distances):
    # D = (T-x) * x
    # D = T*x - x**2
    # x **2 - T*x + D = 0
    x1 = math.ceil((time - math.sqrt(time**2 - 4 * (distance + 1))) / 2)
    x2 = math.floor((time + math.sqrt(time**2 - 4 * (distance + 1))) / 2)

    total *= x2 - x1 + 1

print(f"Part 1: {total}")


# Part 2

time = int("".join(map(str, times)))
distance = int("".join(map(str, distances)))

x1 = math.ceil((time - math.sqrt(time**2 - 4 * (distance + 1))) / 2)
x2 = math.floor((time + math.sqrt(time**2 - 4 * (distance + 1))) / 2)

print(f"Part 2: {x2 - x1 + 1}")
