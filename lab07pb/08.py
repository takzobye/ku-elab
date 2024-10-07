x = int(input("Enter positive integer: "))

if x < 1:
    print("Invalid number.")
else:
    factor = 2
    while x > 1:
        while x % factor == 0:
            print(factor)
            x = x // factor
        factor += 1
