"""
10
5
-6
4
0

RESULT: 15
"""
"""
4
-6
7
-3
5
2
0

RESULT: 11
"""

import math

ls = []

while True:
    x = int(input())

    if x == 0:
        break

    ls.append(x)

current = -math.inf
temp = 0

for i in range(len(ls)):
    for j in range(i, len(ls)):
        temp += ls[j]

        if temp > current:
            current = temp

    temp = 0

print(current)