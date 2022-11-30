with open("input.txt") as f:
    data = f.read()

data = [int(i) for i in data.splitlines()]
print(data)


# Part 1
result = 0
for i in data:
    for j in data:
        if i + j == 2020:
            result = i * j

print(f"Part 1: {result}")


# Part 2
result = 0
for i in data:
    for j in data:
        for k in data:
            if i + j + k == 2020:
                result = i * j * k

print(f"Part 2: {result}")
