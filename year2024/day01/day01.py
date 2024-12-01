with open("input.txt") as f:
    data = f.read()

print(data)

lista, listb = [], []
for line in data.splitlines():
    a, b = line.split("   ")
    lista.append(int(a))
    listb.append(int(b))

# Part 1

total = sum(abs(a - b) for a, b in zip(sorted(lista), sorted(listb)))

print(f"Part 1: {total}")


# Part 2

score = sum(i * listb.count(i) for i in lista)

print(f"Part 2: {score}")
