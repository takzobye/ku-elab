#include <stdio.h>

void bishopMoves(int posX, int posY) {
    char table[8][8];

    for (int i = 0; i < 8; i++) {
        for (int j = 0; j < 8; j++) {
            table[i][j] = ' ';
        }
    }

    table[posX][posY] = 'B';

    int x = posX, y = posY;

    while (x > 0 & y > 0) {
        x = x - 1;
        y = y - 1;
        table[x][y] = 'X';
    }

    x = posX, y = posY;
    while (x < 7 & y > 0) {
        x = x + 1;
        y = y - 1;
        table[x][y] = 'X';
    }

    x = posX, y = posY;
    while (x > 0 & y < 7) {
        x = x - 1;
        y = y + 1;
        table[x][y] = 'X';
    }

    x = posX, y = posY;
    while (x < 7 & y < 7) {
        x = x + 1;
        y = y + 1;
        table[x][y] = 'X';
    }

    printf("  0 1 2 3 4 5 6 7\n");
    printf("------------------\n");
    for (int i = 0; i < 8; i++) {
        printf("%d|", i);

        for (int j = 0; j < 8; j++) {
            printf("%c|", table[j][i]);
        }

        printf("\n------------------\n");
    }
}

int main() {
    int posX = 0, posY = 0;

    printf("Enter Bishop's X Y position: ");
    scanf("%d %d", &posX, &posY);

    bishopMoves(posX, posY);

    return 0;
}

/*
- make array 8x8 / arr[8][8]

1. Receive x & y / ex = 3, 4

free area is :
    left top: (2, 3), (1, 2) (0, 0) [x decrease, y decrease]            | x >= 0 & y >= 0
    right top: (4, 3), (5, 2), (6, 1), (7, 0) [x increase, y decrease]  | x <= 7 & y >= 0

    left bottom: (2, 5), (1, 6), (0, 7) [x decrease, y increase]        | x >= 0 & y <= 7
    right bottom": (4, 5), (5, 6), (6, 7) [x increase, y increase]      | x <= 7 & y <= 7

2. make 4 loop to calculate
*/