text = input()
split_sign = ['-', '.', '=', '$', '_']

# change with same sign
# split sign
# first char upper
# other lower

change_sign_text = ''
for char in text:
    if char in split_sign:
        change_sign_text += '_'
    else:
        change_sign_text += char

word_list = change_sign_text.split('_')

clean_word_list = []
for word in word_list:
    if word != '':
        clean_word_list.append(word)

camel_case_text = ''

is_first_word = True
for word in clean_word_list:
    new_word = ''

    if is_first_word:
        new_word = word.lower()
    else:
        is_first_char = True
        for char in word:
            if is_first_char:
                new_word += char.upper()
            else:
                new_word += char.lower()

            is_first_char = False

    camel_case_text += new_word

    is_first_word = False

print(camel_case_text)