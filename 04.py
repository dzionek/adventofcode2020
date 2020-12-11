file = open('inputs/4.txt')
data = file.read().split('\n\n')

keys = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
eye_colors = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}

num_valid_first = num_valid_second = 0

for password in data:
    password = password.replace('\n', ' ')
    password_dict = {
        p.split(':')[0]: p.split(':')[1]
        for p in password.split(' ')
    }

    if all(key in password_dict.keys() for key in keys):
        num_valid_first += 1
        valid = True

        if not 1920 <= int(password_dict['byr']) <= 2002:
            valid = False

        if not 2010 <= int(password_dict['iyr']) <= 2020:
            valid = False

        if not 2020 <= int(password_dict['eyr']) <= 2030:
            valid = False

        weight_number = int(''.join([
            ch for ch in password_dict['hgt'] if ch.isnumeric()
        ]))
        weight_unit = ''.join([
            ch for ch in password_dict['hgt'] if not ch.isnumeric()
        ])

        if weight_unit == 'cm':
            if weight_number < 150 or weight_number > 193:
                valid = False
        elif weight_unit == 'in':
            if weight_number < 59 or weight_number > 76:
                valid = False
        else:
            valid = False

        if not valid:
            continue

        hcl = password_dict['hcl']
        valid = False
        if hcl[0] == '#':
            if len([ch for ch in hcl if ch.isdigit() or ch in 'abcdef']) == 6:
                valid = True

        if password_dict['ecl'] not in eye_colors:
            valid = False

        if len(password_dict['pid']) != 9:
            valid = False
        try:
            a = int(password_dict['pid'])
        except ValueError:
            valid = False

        if valid:
            num_valid_second += 1


# Parts A and B
print(num_valid_first)
print(num_valid_second)
