x = input()

first_unit = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
second_unit_with_zero = ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
second_unit = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

if not x.isnumeric() or len(x) > 3:
    print('ERROR')
elif len(x) == 1:
    print(first_unit[int(x)])
elif len(x) == 2:
    if x[1] == '0':
        print(second_unit_with_zero[int(x[0])])
    elif x[0] == '1':
        print(second_unit[int(x[1])])
    else:
        print(second_unit_with_zero[int(x[0])] + '-' + first_unit[int(x[1])])
elif len(x) == 3:
    if x[1] == '0' and x[2] == '0':
        print(f'{first_unit[int(x[0])]}-hundred')
    elif x[1] == '0' and x[2] != '0':
        print(f'{first_unit[int(x[0])]}-hundred-{first_unit[int(x[2])]}')
    elif x[1] != '0' and x[2] == '0':
        print(f'{first_unit[int(x[0])]}-hundred-{second_unit_with_zero[int(x[1])]}')
    elif x[1] == '1' and x[2] != '0':
        print(f'{first_unit[int(x[0])]}-hundred-{second_unit[int(x[2])]}')
    else:
        print(f'{first_unit[int(x[0])]}-hundred-{second_unit_with_zero[int(x[1])]}-{first_unit[int(x[2])]}')