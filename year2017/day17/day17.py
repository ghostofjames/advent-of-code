with open("input.txt") as f:
    data = f.read()


# Part 1
spin = int(data)
buffer = [0]
position = 0
for value in range(1, 2017+1):
    position = (position + spin) % len(buffer) + 1
    buffer.insert(position, value)

print(f"Part 1: {buffer[position + 1]}")


# Part 2
spin = int(data)
buffer_len = 1
position = 0
after_0 = 0
for value in range(1, 50_000_000+1):
    position = (position + spin) % buffer_len + 1
    if position == 1:
        after_0 = value
    buffer_len += 1

print(f"Part 2: {after_0}")
