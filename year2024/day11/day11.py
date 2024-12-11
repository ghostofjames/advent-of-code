from functools import cache

with open("input.txt") as f:
    data = f.read()

stones = [int(stone) for stone in data.split()]


# Part 1


@cache
def apply_rules(stone):
    if stone == 0:
        return [1]
    if len(s := str(stone)) % 2 == 0:
        return int(s[: len(s) // 2]), int(s[len(s) // 2 :])
    return [stone * 2024]


new_stones = stones[:]
for _ in range(25):
    new_stones = [ns for s in new_stones for ns in apply_rules(s)]

print(f"Part 1: {len(new_stones)}")


# Part 2


@cache
def get_stone_count(stone, blinks):
    if blinks == 0:
        return 1
    return sum(get_stone_count(ns, blinks - 1) for ns in apply_rules(stone))


print(f"Part 1: {sum(get_stone_count(stone, 25) for stone in stones)}")

print(f"Part 2: {sum(get_stone_count(stone, 75) for stone in stones)}")
