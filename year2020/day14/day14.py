import re
from itertools import product

with open("input.txt") as f:
    data = f.read()


# Part 1
mask = ''
memory = dict()
for line in data.splitlines():
    cmd, val = line.split(' = ')
    if cmd == 'mask':
        mask = val
    else:
        reg = int(re.findall(r'\d+', cmd)[0])
        masked = ''
        for b, m in zip(format(int(val), '036b'), mask):
            if m == '1':
                masked += '1'
            elif m == '0':
                masked += '0'
            else:
                masked += b
        memory[reg] = int(masked, base=2)

print(f"Part 1: {sum(memory.values())}")


# Part 2
mask = ''
memory = dict()
for line in data.splitlines():
    cmd, val = line.split(' = ')
    if cmd == 'mask':
        mask = val
    else:
        reg = int(re.findall(r'\d+', cmd)[0])

        masked = ''
        for b, m in zip(format(reg, '036b'), mask):
            if m == '0':
                masked += b
            elif m == '1':
                masked += '1'
            else:
                masked += '{}'

        for bin_address in product(range(2), repeat=masked.count('{}')):
            address = int(masked.format(*bin_address), base=2)
            memory[address] = int(val)

print(f"Part 2: {sum(memory.values())}")
