x = int(input())

sum = 0

while x > 0:
    sum += x % 10
    x = x // 10

if sum % 9 == 0:
    print(f'Yes {sum}')
else:
    print(f'No {sum % 9}')