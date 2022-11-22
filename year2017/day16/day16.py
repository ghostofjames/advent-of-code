with open("input.txt") as f:
    data = f.read()


def dance(programs, data):
    for move in data:
        match move[0]:
            case 's':
                x = int(move[1:])
                programs[:] = programs[-x:] + programs[:-x]
            case 'x':
                a, b = move[1:].split('/')
                a, b = int(a), int(b)
                programs[a], programs[b] = programs[b], programs[a]
            case 'p':
                a, b = move[1:].split('/')
                a, b = programs.index(a), programs.index(b)
                programs[a], programs[b] = programs[b], programs[a]


moves = data.split(',')

# Part 1
programs = list("abcdefghijklmnop")
dance(programs, moves)

print(f"Part 1: {''.join(programs)}")
assert ''.join(programs) == "hmefajngplkidocb"


# Part 2
cycle_len = 1
while programs != list("abcdefghijklmnop"):
    dance(programs, moves)
    cycle_len += 1

for _ in range(1_000_000_000 % cycle_len):
    dance(programs, moves)

print(f"Part 2: {''.join(programs)}")
assert ''.join(programs) == "fbidepghmjklcnoa"
