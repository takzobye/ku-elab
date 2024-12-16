import math

most_length = -math.inf

while True:
    x = input()
    
    if x == '':
        break

    n = len(x)

    if n > most_length:
        most_length = n

print(most_length)

# 

import math
most_length = -math.inf
most_length_word = ''

while True:
    x = input()
    
    if x == '':
        break

    n = len(x)

    if n > most_length:
        most_length = n
        most_length_word = x

print(most_length_word)