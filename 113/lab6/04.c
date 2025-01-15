#include <stdio.h>
#include <stdlib.h>

#define BOARD_SIZE 8
void setPieceOnTable(int board[][BOARD_SIZE], char piece, int xPos, int yPos);

int main() {
    int n = 0;
    scanf("%d", &n);

    int board[8][8];

    for (int i = 0; i < 8; i++) {
        for (int j = 0; j < 8; j++) {
            board[i][j] = ' ';
        }
    }

    for (int i = 0; i < n; i++) {
        char c;
        int x, y;

        scanf("\n%c(%d, %d)", &c, &x, &y);

        setPieceOnTable(board, c, x, y);
    }

    printf("------------------\n");
    printf("  0 1 2 3 4 5 6 7\n");
    for (int i = 0; i < 8; i++) {
        printf("%d|", i);

        for (int j = 0; j < 8; j++) {
            printf("%c|", board[j][i]);
        }

        printf("\n");
    }

    return 0;
}

void setPieceOnTable(int board[][BOARD_SIZE], char piece, int xPos, int yPos) {
    board[xPos][yPos] = piece;
}