from hashlib import md5

with open("input.txt") as f:
    data = f.read()


# Part 1
number = 0
for i in range(1, 1_000_000):
    hash = md5(bytes(data + str(i), encoding='utf-8')).hexdigest()
    if hash.startswith("00000"):
        number = i
        break

print(f"Part 1: {number}")


# Part 2
number = 0
for i in range(1, 100_000_000):
    hash = md5(bytes(data + str(i), encoding='utf-8')).hexdigest()
    if hash.startswith("000000"):
        number = i
        break

print(f"Part 2: {number}")
