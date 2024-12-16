vars = {}
lines = []

print('Enter variables and values:')

while True:
    x = input()

    if x == '-1':
        break

    [var, value] = x.split('=')
    var = var.strip()
    value = value.strip()

    vars[var] = value

print('Enter your program:')

while True:
    x = input()

    if x == '-1':
        break

    lines.append(x)

print('Result:')

for line in lines:
    for var in vars:
        text = '{' + var + '}'
        line = line.replace(text, vars[var])
    print(line)