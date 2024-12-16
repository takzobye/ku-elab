texts = []

while True:
    x = input()

    if x == '':
        break

    texts.append(x)

result = ''

i = 1
for text in texts:
    if i % 2 == 0:
        result += min(text)
    else:
        result += max(text)

    i += 1

print(result)