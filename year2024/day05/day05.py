with open("input.txt") as f:
    data = f.read()

rules, updates = data.split("\n\n")


# Part 1

p1 = 0
for p in updates.split():
    p = p.split(",")
    s = sorted(p, key=lambda x: -sum(x + "|" + y in rules for y in p))
    if p == s:
        p1 += int(s[len(s) // 2])

print(f"Part 1: {p1}")


# Part 2

p2 = 0
for p in updates.split():
    p = p.split(",")
    s = sorted(p, key=lambda x: -sum(x + "|" + y in rules for y in p))
    if p != s:
        p2 += int(s[len(s) // 2])

print(f"Part 2: {p2}")
