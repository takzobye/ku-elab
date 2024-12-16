# file name 15 char
# ext 3 char
# can dot (.) only 1
#  \ / * : | " < > can't be file name
# space ( ) can't be file name

# change space to _
# change special char to _
# change dot (.) to _
# set file name and ext length
# if file don't have ext not add dot (.)

str = input()

new_text = ''
for char in str:
    if char == ' ':
        new_text += '_'
    else:
        new_text += char

str = new_text
new_text = ''

for char in str:
    if char in '\\/*:|"<>':
        new_text += '_'
    else:
        new_text += char

str = new_text
new_text = ''

dot_count = str.count('.')
if dot_count > 1:
    count = 0 
    for char in str:
        if char == '.':
            if count == (dot_count - 1):
                new_text += '.'
            else:
                new_text += '_'
                count += 1

        else:
            new_text += char
else:
    new_text = str

str = new_text
new_text = ''

text_split_dot = str.split('.')

file_name = ''
ext = ''

file_name = text_split_dot[0]
if len(file_name) > 15:
    file_name = file_name[:15]

if len(text_split_dot) > 1:
    ext = text_split_dot[1]

if len(ext) > 3:
    ext = ext[:3]

if ext == '':
    print(file_name)
else:
    print(file_name + '.' + ext)    