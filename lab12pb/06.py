# number can be
# 1200
# 1200.50
# 4,200,257
# 1,200.50

# check not char accept
# check is has dot (.) and split to check right text is > 2 ?
# check comma count + 3 and will comma

char_accept_list = '1234567890.,'

text = input()

is_deny_char = False
for char in text:
    if char not in char_accept_list:
        is_deny_char = True

if is_deny_char:
    print('ERROR')
else:
    number_split = text.split('.')
    integer = number_split[0]
    
    decimal = ''
    if len(number_split) > 1:
        decimal = number_split[1]

    if len(decimal) > 2:
        print('ERROR')
    else:
        integer_split = integer.split(',')

        is_skip_check_comma = len(integer_split) == 1
        is_error = False
        count = 1 

        if not is_skip_check_comma:
            for num in integer_split:
                if count != 1:
                    if len(num) != 3:
                        is_error = True

                if len(num) > 3:
                    is_error = True

                count += 1

        if is_error:
            print('ERROR')
        else:
            if decimal:
                print(str(int(integer.replace(',', '')) + 1) + '.' + decimal)
            else:
                print(str(int(integer.replace(',', '')) + 1))
