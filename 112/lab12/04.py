x = input()

lower_text = ''
upper_text = ''

for char in x:
    if char.isupper():
        upper_text += char
    elif char.islower():
        lower_text += char

print(len(lower_text))
print(len(upper_text))

x = input()

result = ''

for char in x:
    if char.isupper():
        result += char.lower()
    else:
        result += char.upper()

print(result)