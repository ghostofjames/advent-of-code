with open("input.txt") as f:
    data = f.read()

equations = []
for line in data.splitlines():
    target, nums = line.split(": ")
    equations.append((int(target), [int(n) for n in nums.split()]))


# Part 1


def check(tar, cur, left):
    if len(left) == 0:
        return cur == tar
    return check(tar, cur + left[0], left[1:]) or check(tar, cur * left[0], left[1:])


total = sum(tar for tar, nums in equations if check(tar, nums[0], nums[1:]))

print(f"Part 1: {total} \n")


# Part 2


def check_cat(tar, cur, left):
    if len(left) == 0:
        return cur == tar
    return (
        check_cat(tar, cur + left[0], left[1:])
        or check_cat(tar, cur * left[0], left[1:])
        or check_cat(tar, int(str(cur) + str(left[0])), left[1:])
    )


total2 = sum(tar for tar, nums in equations if check_cat(tar, nums[0], nums[1:]))

print(f"Part 2: {total2}")
