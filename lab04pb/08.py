minute = int(input('Minutes before due: '))
temp = float(input('Temperature: '))
is_raining = input('Is it raining (y/n)? ')

day_left = minute // (60 * 24)

if minute % (60 * 24) >= 720:
    day_left += 1

if day_left == 0:
    day_left = 1

print(f'>>> {day_left} days before due.')

if day_left < 2:
    print('>>> I will do the assignment.')
elif day_left > 5: 
    print('>>> I will not do the assignment.')
elif temp > 40 or (temp > 25 and (is_raining == 'Y' or is_raining == 'y')):
    print('>>> I will not do the assignment.')
else:
    print('>>> I will do the assignment.')