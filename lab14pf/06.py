text = input()
x = int(input())

x = x % len(text) if text else 0

if x == 0:
    print(text)
elif x > 0:
    print(text[len(text) - abs(x):] + text[:len(text) - abs(x)])
else:
    print(text[abs(x):] + text[:abs(x)])

"""
Hello World!
4

rld!Hello Wo

----

Python Programming
-5

n ProgrammingPytho
"""