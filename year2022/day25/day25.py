with open("input.txt") as f:
    data = f.read()


SNAFU = {'2': 2, '1': 1, '0': 0, '-': -1, '=': -2}


# Part 1
def decode_SNAFU(s):
    value = 0
    for i, d in enumerate(s[::-1]):
        value += 5**i * SNAFU[d]
    return value


def encode_SNAFU(num):
    result = ''
    while num > 0:
        num, place = divmod(num + 2, 5)
        result += '=-012'[place]
    return result[::-1]


total = 0
for line in data.splitlines():
    total += decode_SNAFU(line)

print(f"Part 1: {encode_SNAFU(total)}")
