from collections import defaultdict

with open("input.txt") as f:
    data = f.read()
#     data = """set a 1
# add a 2
# mul a a
# mod a 5
# snd a
# set a 0
# rcv a
# jgz a -1
# set a 1
# jgz a -2"""


def get(registers, value):
    try:
        return int(value)
    except ValueError:
        return registers[value]


instructions = [ins.split(' ') for ins in data.splitlines()]


# Part 1
sound = 0

registers = defaultdict(int)
position = 0
while 0 <= position < len(instructions):
    try:
        ins, x, y = instructions[position]
    except ValueError:
        ins, x = instructions[position]

    match ins:
        case 'snd':
            sound = get(registers, x)
            position += 1
        case 'set':
            registers[x] = get(registers, y)
            position += 1
        case 'add':
            registers[x] += get(registers, y)
            position += 1
        case 'sub':
            registers[x] -= get(registers, y)
            position += 1
        case 'mul':
            registers[x] *= get(registers, y)
            position += 1
        case 'mod':
            registers[x] %= get(registers, y)
            position += 1
        case 'rcv':
            if get(registers, x) != 0:
                break
            position += 1
        case 'jgz':
            if get(registers, x) > 0:
                position += get(registers, y)
            else:
                position += 1

print(f"Part 1: {sound}")


# Part 2

print(f"Part 2: {0}")
