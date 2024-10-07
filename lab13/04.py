ls = []

while True:
    x = input()

    if x == '':
        break

    ls.append(float(x))

ls.sort()

print(ls.count(ls[0]))