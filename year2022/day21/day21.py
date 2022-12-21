from operator import add, mul, sub, truediv

with open("input.txt") as f:
    data = f.read()
#     data = """root: pppw + sjmn
# dbpl: 5
# cczh: sllz + lgvd
# zczc: 2
# ptdq: humn - dvpt
# dvpt: 3
# lfqf: 4
# humn: 5
# ljgn: 2
# sjmn: drzm * dbpl
# sllz: 4
# pppw: cczh / lfqf
# lgvd: ljgn * ptdq
# drzm: hmdt - zczc
# hmdt: 32"""


ops = {'+': add, '-': sub, '*': mul, '/': truediv}

monkeys = {}
for line in data.splitlines():
    key, *line = line.replace(':', '').split(' ')

    if len(line) == 1:
        monkeys[key] = int(line[0])
    else:
        monkeys[key] = line


# Part 1
def parse(key):
    number = monkeys[key]
    if type(number) is int:
        return number
    else:
        a, op, b = number
        return ops[op](parse(a), parse(b))


print(f"Part 1: {parse('root')}")


# Part 2
monkeys['root'][1] = '-'  # = if - equals 0

lower_bound = 0
upper_bound = 1_000_000_000_000_000_000

low = lower_bound
high = upper_bound
half = (high + low) // 2
monkeys['humn'] = half
while (res := parse('root')) != 0:
    if res < 0:
        low = half
    elif res > 0:
        high = half
    if high-low == 1:
        low = upper_bound
        high = lower_bound
    half = (high + low) // 2
    monkeys['humn'] = half

print(f"Part 2: {half}")
