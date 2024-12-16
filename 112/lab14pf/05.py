x = input()
x = x.lower()

count = 0
current_ord = 0

for char in x:
    num = ord(char)

    if num > current_ord:
        count += 1
        current_ord = num
    else:
        break

print(count)