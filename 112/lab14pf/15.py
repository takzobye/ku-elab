ls = input().split()

for i in range(len(ls)):
    text = ls[i]

    if text not in ['for', 'and', 'with', 'of']:
        ls[i] = text.capitalize()

print(' '.join(ls))