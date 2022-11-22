with open("input.txt") as f:
    data = f.read()


def get(registers, value):
    try:
        return int(value)
    except ValueError:
        return registers[value]


instructions = [ins.split(' ') for ins in data.splitlines()]


# Part 1
mul_count = 0

registers = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0}
position = 0
while position < len(instructions):
    ins, x, y = instructions[position]
    match ins:
        case 'set':
            registers[x] = get(registers, y)
            position += 1
        case 'sub':
            registers[x] -= get(registers, y)
            position += 1
        case 'mul':
            mul_count += 1
            registers[x] *= get(registers, y)
            position += 1
        case 'jnz':
            if get(registers, x) != 0:
                position += get(registers, y)
            else:
                position += 1

print(f"Part 1: {mul_count}")


# Part 2

print(f"Part 2: {0}")
