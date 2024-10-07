text = input()

# get text
# loop get target char and append to list
# loop char in text and check is in list target char

char_list = []
while True:
    x = input()

    if x == '0':
        break

    char_list.append(x)

result = ''

for char in text:
    if char in char_list:
        result += char
    else:
        result += '-'

print(result)