data = []
with open("input.txt") as f:
    data = f.read().splitlines()


# Part 1
gamma = ""
epsilon = ""
for n in range(len(data[0])):
    # bit_count = len(list(filter(lambda x: x[n] == '1', data)))
    bit_count = len([x for x in data if x[n] == '1'])

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

    # bit_count = len(list(filter(lambda x: x[i] == '1', gen_list)))
    bit_count = len([x for x in gen_list if x[i] == '1'])
    bit = '1' if bit_count >= len(gen_list) // 2 else '0'

    gen_list = list(filter(lambda z: z[i] == bit, gen_list))
gen = gen_list[0]

# CO2 scrubber rating
scrub_list = list(data)
for i in range(len(scrub_list[0])):
    if len(scrub_list) == 1:
        break

    # bit_count = len(list(filter(lambda x: x[i] == '1', scrub_l)))
    bit_count = len([x for x in scrub_list if x[i] == '1'])
    bit = '0' if bit_count >= len(scrub_list) // 2 else '1'

    scrub_list = list(filter(lambda z: z[i] == bit, scrub_list))
scrub = scrub_list[0]

print(f"Part 2: {int(gen, 2) * int(scrub, 2)}")
