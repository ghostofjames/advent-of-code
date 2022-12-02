from math import floor

with open("input.txt") as f:
    data = f.read()


# Part 1
fuel = sum(floor(mass / 3) - 2 for mass in map(int, data.splitlines()))

print(f"Part 1: {fuel}")


# Part 2
total_fuel = 0
for mass in map(int, data.splitlines()):
    fuel = floor(mass / 3) - 2
    while fuel > 0:
        total_fuel += fuel
        fuel = floor(fuel / 3) - 2

print(f"Part 2: {total_fuel}")
