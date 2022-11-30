with open("input.txt") as f:
    data = [int(line) for line in f.read().splitlines()]


# Part 1
pre = 25
for i in range(pre, len(data)):
    n = data[i]
    xs = data[i-pre:i]
    for x in xs:
        if (n - x) in xs:
            break
    else:
        num = n
        break

print(f"Part 1: {num}")


# Part 2
for i in range(0, len(data)):
    nums = [data[i]]
    while sum(nums) <= num:
        i += 1
        nums.append(data[i])
        if sum(nums) == num:
            break
    else:
        continue
    break

print(f"Part 2: {min(nums) + max(nums)}")
