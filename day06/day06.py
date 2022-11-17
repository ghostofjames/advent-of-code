with open("input.txt") as f:
    data = list(map(int, f.read().split(',')))


# Part 1
lanternfish = [data.count(age) for age in range(9)]

for day in range(1, 80 + 1):
    lanternfish = lanternfish[1:] + lanternfish[:1]
    lanternfish[6] += lanternfish[8]

print(f"Part 1: {sum(lanternfish)}")


# Part 2
lanternfish = [data.count(age) for age in range(9)]

for day in range(1, 256 + 1):
    lanternfish = lanternfish[1:] + lanternfish[:1]
    lanternfish[6] += lanternfish[8]

print(f"Part 2: {sum(lanternfish)}")


# First brute force attempt, takes ages and will run out of memory
# lanternfish = list(data)
# print(f"Initial state: {lanternfish[:5]}...")
# for day in range(1, 80 + 1):
#     new_fish = []
#     for fish, timer in enumerate(lanternfish):
#         timer -= 1
#         lanternfish[fish] = timer

#         if timer == -1:
#             new_fish.append(8)
#             lanternfish[fish] = 6

#     lanternfish += new_fish

#     print(f"After {day:2} days: {len(lanternfish)} total fish")
# print(f"Part 1: {len(lanternfish)}")
