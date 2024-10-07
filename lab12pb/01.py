text = input()

result = ''

for char in text:
    if char in 'aeiouAEIOU':
        result += char.upper()
    else:
        result += char.lower()

print(result)