with open("input.txt") as f:
    data = f.read()
#     data = """nop +0
# acc +1
# jmp +4
# acc +3
# jmp -3
# acc -99
# acc +1
# jmp -4
# acc +6"""

instructions = data.splitlines()


# Part 1
line = 0
acc = 0

run_history = []
while True:
    if line in run_history:
        break

    run_history.append(line)

    ins, val = instructions[line].split(' ')
    print(ins, val)

    if ins == "acc":
        acc += int(val)
        line += 1

    elif ins == "jmp":
        line += int(val)

    elif ins == "nop":
        line += 1


print(f"Part 1: {acc}")


# Part 2

print(f"Part 2: {0}")
