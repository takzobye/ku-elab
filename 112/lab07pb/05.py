while True:
    x = int(input('Enter a number: '))

    if x == 0:
        print('End of program, goodbye.')
        break
    elif x <= 1:
        print('Invalid input, try again.')
        continue

    if x == 2:
        print(f"{x} is a prime number.")
    else:
        is_prime = True
        i = 2
        while i ** 2 <= x:
            if x % i == 0:
                is_prime = False
            i += 1

        if is_prime:
            print(f"{x} is a prime number.")
        else:
            print(f"{x} is not a prime number.")