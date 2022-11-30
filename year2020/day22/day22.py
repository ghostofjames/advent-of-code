with open("input.txt") as f:
    data = f.read()


# Part 1
p1, p2 = data.split('\n\n')
p1 = [int(n) for n in p1.splitlines()[1:]]
p2 = [int(n) for n in p2.splitlines()[1:]]

round = 0
while p1 and p2:
    round += 1
    p1c = p1.pop(0)
    p2c = p2.pop(0)
    if p1c > p2c:
        p1.append(p1c)
        p1.append(p2c)
    else:
        p2.append(p2c)
        p2.append(p1c)

win_deck = p1 or p2
score = sum(a * b for a, b in zip(range(len(win_deck), 0, -1), win_deck))
print(f"Part 1: {score}")


# Part 2
def game(p1, p2):
    occur = []
    while p1 and p2:
        if p1 in occur:
            flag = True  # p1 wins
            break        # infinity
        else:
            occur.append(p1[:])
        p1c, p2c = p1.pop(0), p2.pop(0)
        if p1c <= len(p1) and p2c <= len(p2):
            _, flag = game(p1[:p1c], p2[:p2c])
            if flag:
                p1.append(p1c)
                p1.append(p2c)
            else:
                p2.append(p2c)
                p2.append(p1c)
        else:
            if p1c > p2c:
                p1.append(p1c)
                p1.append(p2c)
                flag = True
            else:
                p2.append(p2c)
                p2.append(p1c)
                flag = False
    return p1 if p1 else p2, flag


p1, p2 = data.split('\n\n')
p1 = [int(n) for n in p1.splitlines()[1:]]
p2 = [int(n) for n in p2.splitlines()[1:]]

win_deck = game(p1, p2)[0]
score = sum(a * b for a, b in zip(range(len(win_deck), 0, -1), win_deck))
print(f"Part 2: {score}")
