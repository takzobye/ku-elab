import math

most_value = -math.inf
less_value = math.inf
sum_value = 0
count = 0

while True:
    x = input()
    if x == '':
        break

    x = float(x)

    if x > most_value:
        most_value = x

    if x < less_value:
        less_value = x

    sum_value += x

    count += 1

print(f'{most_value:.2f} {less_value:.2f}')
print(f'{sum_value:.2f} {(sum_value / count):.2f}')
