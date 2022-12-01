with open("input.txt") as f:
    data = f.read()


# Part 1
card_public, door_public = [int(i) for i in data.splitlines()]

card_loop_size = 0
value = 1
while value != card_public:
    value *= 7
    value %= 20201227
    card_loop_size += 1

encryption_key = 1
for loop in range(card_loop_size):
    encryption_key *= door_public
    encryption_key %= 20201227

print(f"Part 1: {encryption_key}")
