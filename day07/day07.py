data = []
with open("day07_input.txt") as f:
    data = list(map(int, f.read().split(',')))

# Part 1
costs = {}
for i in range(min(data), max(data) + 1):
    cost = 0
    for crab in data:
        cost += abs(crab - i)
    costs[i] = cost

print(f"Part 1: {min(costs.values())}")


# Part 2
costs = {}
for i in range(min(data), max(data) + 1):
    cost = 0
    for crab in data:
        cost += sum(range(abs(crab - i) + 1))
    costs[i] = cost

print(f"Part 2: {min(costs.values())}")
