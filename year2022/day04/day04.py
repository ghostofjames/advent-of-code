with open("input.txt") as f:
    data = f.read().splitlines()

# Part 1
count = 0
for line in data:
    a, b = line.split(',')
    (a1, a2), (b1, b2) = a.split('-'), b.split('-')
    a_in_b = int(a1) >= int(b1) and int(a2) <= int(b2)
    b_in_a = int(b1) >= int(a1) and int(b2) <= int(a2)
    if a_in_b or b_in_a:
        count += 1

print(f"Part 1: {count}")


# Part 2
count = 0
for line in data:
    a, b = line.split(',')
    (a1, a2), (b1, b2) = a.split('-'), b.split('-')
    a_overlap_b = int(a1) >= int(b1) and int(a1) <= int(b2)
    b_overlap_a = int(b1) >= int(a1) and int(b1) <= int(a2)
    if a_overlap_b or b_overlap_a:
        count += 1

print(f"Part 2: {count}")
