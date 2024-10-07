count = 0

while True:
    x = int(input('Enter number: '))

    if x < 0:
        break
    
    if x % 2 == 1:
        count += 1

print(f'Received {count} odd numbers')