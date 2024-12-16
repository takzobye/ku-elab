hours = int(input('Enter number of hours: '))
minutes = int(input('Enter number of minutes: '))
buyAmt = int(input('Enter shopping amount: '))

if minutes < 0 or minutes > 59 or (minutes > 0 and hours + 1 > 20 or hours < 0):
    print('Invalid time.')
else:
    price = 0

    if minutes > 0:
        hours += 1 

    # Calculate hour 3 and 4
    if buyAmt > 3000 or hours <= 2:
        pass
    elif buyAmt >= 300 and buyAmt <= 3000:
        if hours >= 4:
            hours -= 4
        elif hours >= 3:
            hours -= 3

        price += hours * 50
    else:
        if hours >= 4:
            hours -= 4
            price += 40
        elif hours >= 3:
            hours -= 3
            price += 20

        price += hours * 50

    if price > 0:
        print(f'Total amount due is {price} Baht, thank you.')
    else:
        print('No charge, thank you.')