print("---<< Main Menu >>---")
print('    <B>urger Meal')
print('    <C>hicken Meal')
print('    <P>asta Meal')

main_menu = input('Enter your choice: ').upper()

if main_menu == 'B':
    print('---<< Burger Sub Menu >>---')
    print('    <R>egular Burger')
    print('    <C>heese Burger')
    print('    <D>ouble Cheese Burger')

    sub_menu = input('Enter your choice: ').upper()
    if sub_menu == 'R':
        print('Your Regular Burger is 60 Baht.')
    elif sub_menu == 'C':
        print('Your Cheese Burger is 75 Baht.')
    elif sub_menu == 'D':
        print('Your Double Cheese Burger is 90 Baht.')
    else:
        print('Invalid sub menu choice.')

elif main_menu == 'C':
    print('---<< Chicken Sub Menu >>---')
    print('    <F>ried Chicken')
    print('    <G>rilled Chicken')
    print('    <C>hef\'s Chicken')

    sub_menu = input('Enter your choice: ').upper()
    if sub_menu == 'F':
        print('Your Fried Chicken is 120 Baht.')
    elif sub_menu == 'G':
        print('Your Grilled Chicken is 150 Baht.')
    elif sub_menu == 'C':
        print('Your Chef\'s Chicken is 180 Baht.')
    else:
        print('Invalid sub menu choice.')

elif main_menu == 'P':   
    print('---<< Pasta Sub Menu >>---')
    print('    <S>paghetti de Italiano')
    print('    <L>asagna Supreme')
    print('    <M>acaroni Special')

    sub_menu = input('Enter your choice: ').upper()
    if sub_menu == 'S':
        print('Your Spaghetti de Italiano is 90 Baht.')
    elif sub_menu == 'L':
        print('Your Lasagna Supreme is 100 Baht.')
    elif sub_menu == 'M':
        print('Your Macaroni Special is 100 Baht.')
    else:
        print('Invalid sub menu choice.')

else: 
    print('Invalid main menu choice.')


