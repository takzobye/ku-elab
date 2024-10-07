# x = input()
# ls = x.split('.')

# x = input()
# ls = x.split('.')
# ls = [ int(x) for x in ls ]

xy1 = input()
xy2 = input()

x1, y1, = xy1.split(',')
x2, y2, = xy2.split(',')

print(f'{float(x1) + float(x2)},{float(y1) + float(y2)}')