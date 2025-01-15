/*

ตารางหมากรุก
หมากรุกสากลเป็นเกมส์กระดานแนววางแผนสองผู้เล่น ที่เล่นบนกระดานสลับสีซึ่งมีจัตุรัส 64 ช่อง จัดเรียงแบบ 8x8 ช่อง
ประกอบด้วยตัวหมาก 6 ประเภท คือ King (ราชา), Queen (ราชินี), Knight (อัศวิน), Bishop (นักบวช), Rook (เรือ) และ Pawn (เบี้ย)

ให้เขียนโปรแกรมเพื่อแสดงตำแหน่งของตัวหมากบนตารางหมากรุกสากลในเกมหนึ่ง
โดย บรรทัดที่ 1 รับจำนวนเต็ม numPieces ที่แสดงจำนวนตัวหมากที่เหลืออยู่บนกระดาน
บรรทัดที่ 2 ถึง บรรทัดที่ numPieces + 1 รับตัวอักษร pieceChar ที่แทนตัวหมากและพิกัด x, y บนกระดาน ในรูปแบบ pieceChar(x, y) (พิกัดมุมซ้ายบนของตารางคือ 0, 0 และ พิกัดมุมขวาล่างของตารางคือ 7, 7)

ตัวอักษร pieceChar ที่แทนตัวหมากมีความหมายดังนี้

K แทน King
Q แทน Queen
N แทน Knight
B แทน Bishop
R แทน Rook
P แทน Pawn
ตัวอักษรตัวใหญ่ แทน ตัวหมากของผู้เล่น 1 และ ตัวอักษรตัวเล็ก แทน ตัวหมากของผู้เล่น 2

บรรทัดที่ numPieces + 2 เป็นต้นไป แสดงตำแหน่งของตัวหมากบนตาราง

*/

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