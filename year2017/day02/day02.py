from itertools import combinations

with open("input.txt") as f:
    data = f.read()

data = [[int(n) for n in line.split('\t')] for line in data.splitlines()]


# Part 1
checksum = sum(max(row) - min(row) for row in data)
print(f"Part 1: {checksum}")


# Part 2
checksum = sum(a // b
               for row in data
               for i in combinations(row, 2)
               if (a := max(i)) % (b := min(i)))
print(f"Part 2: {checksum}")
