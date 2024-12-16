str = input()

texts = []

text = ''
for char in str:
    if char == ',':
        texts.append(text)
        text = ''
    else:
        text += char

texts.append(text)

new_texts = ''
for i in range(len(texts)):
    text = ' ' + texts[i] + ' '

    first_index = -1
    last_index = -1

    for j in range(len(text)):
        char = text[j]

        if first_index == -1:
            if char != ' ':
                first_index = j

    for j in range(-1, (-len(text) - 1), -1):
        char = text[j]

        if last_index == -1:
            if char != ' ':
                last_index = j

    new_texts += '"' + text[first_index:last_index + 1] + '"'
    if i != len(texts) - 1:
        new_texts += ','

print(new_texts)