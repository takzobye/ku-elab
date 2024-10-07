x = int(input())

if x <= 0:
    print('ERROR')
else:
    while True:
        if x % 10 == 0 and x <= 0:
            break

        print(x % 10)

        x = x // 10