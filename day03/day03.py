data = []
with open("day03_input.txt") as f:
    data = f.read().splitlines()


# Part 1
gamma = ""
epsilon = ""
for n in range(len(data[0])):
    bit_count = len(list(filter(lambda x: x[n] == '1', data)))

    if bit_count > len(data) // 2:
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'

print(f"Part 1: {int(gamma, 2) * int(epsilon, 2)}")


# Part 2

# oxygen generator rating
gen_list = list(data)
for i in range(len(gen_list[0])):
    if len(gen_list) == 1:
        break

    bit_count = len(list(filter(lambda x: x[i] == '1', gen_list)))
    bit = '1' if bit_count >= len(gen_list) // 2 else '0'
    gen_list = list(filter(lambda z: z[i] == bit, gen_list))
gen = gen_list[0]

# CO2 scrubber rating
scrub_l = list(data)
for i in range(len(scrub_l[0])):
    if len(scrub_l) == 1:
        break

    bit_count = len(list(filter(lambda x: x[i] == '1', scrub_l)))
    bit = '0' if bit_count >= len(scrub_l) // 2 else '1'

    scrub_l = list(filter(lambda z: z[i] == bit, scrub_l))
scrub = scrub_l[0]

print(f"Part 2: {int(gen, 2) * int(scrub, 2)}")
