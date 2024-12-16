pokemon_level = int(input('Enter level pokemon: '))
pokeball_level = input('Enter level pokeball: ').upper()
distance = int(input('Enter distance: '))

x = 0

if pokeball_level == 'H':
    if pokemon_level <= 40:
        x = 0.01
    elif pokemon_level <= 60:
        x = 0.01
    elif pokemon_level <= 100:
        x = 0.01

elif pokeball_level == 'M':
    if pokemon_level <= 40:
        x = 0.03
    elif pokemon_level <= 60:
        x = 0.05
    elif pokemon_level <= 100:
        x = 0.08
elif pokeball_level == 'L':
    if pokemon_level <= 40:
        x = 0.05
    elif pokemon_level <= 60:
        x = 0.03
    elif pokemon_level <= 100:
        x = 0.1    

s = 100 - (pokemon_level * distance * x)

if s <= 0:
    s = 0

print(f'{s:.2f} percent.')