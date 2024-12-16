main_text = input().replace(' ', '')
main_code = input()
target = input()

clean_main_text = ''
for char in main_text:
    if char not in clean_main_text:
        clean_main_text += char

dc = {}

for i in range(len(main_code)):
    if i < len(clean_main_text):
        dc[main_code[i]] = clean_main_text[i]

text = ''

for char in target:
    if char == ' ':
        text += ''
    if char in dc:
        text += dc[char]
    else:
        text += char

print(text)