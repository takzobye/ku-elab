x = input('Enter input: ')

string = ''

for i in range(len(x), 0, -1):
  string += x[i - 1]

print(string)