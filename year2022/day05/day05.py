import re
from copy import deepcopy

with open("input.txt") as f:
    data = f.read()

data, procedure = data.split('\n\n')

starting_stacks = {int(s): [] for s in re.findall(r'\d+', data.splitlines()[-1])}
for line in data.splitlines()[-1::-1]:
    for n, i in enumerate(range(1, len(line), 4), 1):
        if line[i] != ' ':
            starting_stacks[n].append(line[i])


# Part 1
stacks = deepcopy(starting_stacks)
for p in procedure.splitlines():
    n, s, d = [int(s) for s in re.findall(r'\d+', p)]
    for _ in range(n):
        tmp = stacks[s].pop()
        stacks[d].append(tmp)

tops = ''.join([s[-1] for s in stacks.values()])
print(f"Part 1: {tops}")

# Part 2
stacks = deepcopy(starting_stacks)
for p in procedure.splitlines():
    n, s, d = [int(s) for s in re.findall(r'\d+', p)]
    tmp = stacks[s][-n:]
    del stacks[s][-n:]
    stacks[d] += tmp

tops = ''.join([s[-1] for s in stacks.values()])
print(f"Part 2: {tops}")
