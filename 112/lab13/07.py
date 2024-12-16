"""
    เขียนฟังก์ชัน extract_string(text) ที่รับพารามิเตอร์ text เป็นสตริงที่ประกอบด้วยอักขระและตัวเลข
    แล้วคืนค่าลิสต์ที่แยกชุดอักขระกับชุดตัวเลขออกจากกันตามตัวอย่าง
"""

def extract_string(text):
    ls = []
    word = ''
    word_format = 'none' # string or number 

    for char in text:
        char_format = 'none'
        if char in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
            char_format = 'number'
        else:
            char_format = 'string'

        if word_format == char_format:
            word += char
        else:
            if word_format != 'none':
                if char_format == 'string': # check is equal string because word_format and char_format is not same
                    word = int(word)

                ls.append(word)
                
            word = char
            word_format = char_format

    if word_format == 'number':
        word = int(word)

    ls.append(word)

    if len(ls) == 1 and ls[0] == '':
        ls = []

    return ls

print(extract_string(''))