import re

with open("input.txt") as f:
    data = f.read()


# Part 1
valid = 0
for line in data.splitlines():
    lb, ub, char, password = re.split(r'[- :]+', line)
    if int(lb) <= password.count(char) <= int(ub):
        valid += 1

print(f"Part 1: {valid}")


# Part 2
valid = 0
for line in data.splitlines():
    p1, p2, char, password = re.split(r'[- :]+', line)
    if (password[int(p1)-1] == char) ^ (password[int(p2)-1] == char):  # XOR
        valid += 1

print(f"Part 2: {valid}")
