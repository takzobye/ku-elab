"""
    data = {
        [name] = {
            price: 0,
            count: 0
        },
    }
"""

data = {}

while True:
    x = input()

    if x == 'end':
        break

    [name, price] = x.split()

    price = float(price)

    if name not in data:
        data[name] = {
            'price': price,
            'count': 1
        }
    else:
        if price > data[name]['price']:
            data[name]['price'] = price

        data[name]['count'] += 1

sort_data = dict(sorted(data.items()))

for name in sort_data:
    if sort_data[name]['count'] == 1:
        print(f'{name} bid at the price of {sort_data[name]['price']} baht in {sort_data[name]['count']} time.')
    else:
        print(f'{name} bid at the price of {sort_data[name]['price']} baht in {sort_data[name]['count']} times.')

most_bid_name = None
most_bid_data = None

for name in data:
    if most_bid_name == None:
        most_bid_name = name
        most_bid_data = data[name]
    else:
        if data[name]['price'] > most_bid_data['price']:
            most_bid_name = name
            most_bid_data = data[name]
           
print(f'The winner is {most_bid_name}.')