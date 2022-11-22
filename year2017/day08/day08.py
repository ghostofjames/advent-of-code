from collections import defaultdict


def check_condition(registers: str, condition: str):
    reg, cond, val = condition.split(" ")
    match cond:
        case '>':
            return registers[reg] > int(val)
        case '<':
            return registers[reg] < int(val)
        case '>=':
            return registers[reg] >= int(val)
        case '<=':
            return registers[reg] <= int(val)
        case '==':
            return registers[reg] == int(val)
        case '!=':
            return registers[reg] != int(val)


def execute_instruction(registers: str, instruction: str):
    reg, cmd, val = instruction.split(" ")
    match cmd:
        case "inc":
            registers[reg] += int(val)
        case "dec":
            registers[reg] -= int(val)


with open("input.txt") as f:
    data = f.read()

instructions = [x.split(" if ") for x in data.splitlines()]


# Part 1
highest_value = 0
registers = defaultdict(int)
for ins, cond in instructions:
    if check_condition(registers, cond):
        execute_instruction(registers, ins)

largest = max(registers.values())
print(f"Part 1: {largest}")


# Part 2
highest_value = 0
registers = defaultdict(int)
for ins, cond in instructions:
    if check_condition(registers, cond):
        execute_instruction(registers, ins)

    highest_value = max(highest_value, max(registers.values()))

print(f"Part 2: {highest_value}")
