import math

x = input()

text = ''
if len(x) % 2 == 0:
    center_index = int(len(x) / 2)
    text = x[:center_index][::-1] + x[center_index:][::-1]
else:
    center_index = math.ceil(len(x) / 2) - 1
    text = x[:center_index][::-1] + x[center_index] + x[center_index + 1:][::-1]

print(text)