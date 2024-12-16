texts = []

while True:
    str = input()

    if str == '-1':
        break

    texts.append(str)

texts_splited = []
for text in texts:
    first_equal_index = text.find('=')

    left_text = text[:first_equal_index]
    right_text = text[first_equal_index + 1:]

    texts_splited.append([left_text, right_text])

texts_trimed = []
for texts in texts_splited:
    texts_trimed.append([texts[0].strip(), texts[1].strip()])

length = 0
for texts in texts_trimed:
    if len(texts[0]) > length:
        length = len(texts[0])

for texts in texts_trimed:
    text = ' ' * (length - len(texts[0])) + texts[0] + ' = ' + texts[1]
    print(text)