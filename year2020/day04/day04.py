from string import digits

with open("input.txt") as f:
    data = f.read()

fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']  # , 'cid']

passports = [dict(item.split(':') for item in passport.split())
             for passport in data.split('\n\n')]

# Part 1
valid = 0
for passport in passports:
    if all(field in passport for field in fields):
        valid += 1

print(f"Part 1: {valid}")


# Part 2
valid = 0
for passport in passports:
    if not all(field in passport for field in fields):
        continue

    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    if not 1920 <= int(passport['byr']) <= 2002:
        continue

    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    if not 2010 <= int(passport['iyr']) <= 2020:
        continue

    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    if not 2020 <= int(passport['eyr']) <= 2030:
        continue

    # hgt (Height) - a number followed by either cm or in:
    num, unit = passport['hgt'][:-2], passport['hgt'][-2:]
    if unit == "cm":
        # If cm, the number must be at least 150 and at most 193.
        if not 150 <= int(num) <= 193:
            continue
    elif unit == "in":
        # If in, the number must be at least 59 and at most 76.
        if not 59 <= int(num) <= 76:
            continue
    else:
        continue

    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    if not passport['hcl'].startswith('#'):
        continue
    if not all(c in digits + 'abcdef' for c in passport['hcl'][1:]):
        continue

    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    if not passport['ecl'] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        continue

    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    if not len(passport['pid']) == 9:
        continue
    if not all(c in digits for c in passport['pid']):
        continue

    # cid (Country ID) - ignored, missing or not.

    valid += 1

print(f"Part 2: {valid}")
