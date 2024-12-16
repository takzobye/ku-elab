print('Upper left corner coordinate:')
rect_x = float(input('  << x axis: '))
rect_y = float(input('  << y axis: '))
rect_east = float(input('  << Eastern: '))
rect_south = float(input('  << Southern: '))
print('Enter a coordinate:')
target_x = float(input('  << x axis: '))
target_y = float(input('  << y axis: '))

left_x = rect_x
right_x = rect_x + rect_east
top_y = rect_y
bottom_y = rect_y - rect_south

in_x = target_x >= left_x and target_x <= right_x
in_y = target_y >= bottom_y and target_y <= top_y
in_all = in_x and in_y

if in_all:
    print(f'>>> ({target_x:.2f}, {target_y:.2f}) is inside the rectangle.')
else:
    print(f'>>> ({target_x:.2f}, {target_y:.2f}) is not inside the rectangle.')