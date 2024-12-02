#include <stdio.h>

int main()
{
    int amount = 98;

    // Start Block

    int c50 = amount / 50;
    amount = amount - (50 * c50);

    int c20 = amount / 20;
    amount = amount - (20 * c20);

    int c5 = amount / 5;
    amount = amount - (5 * c5);
    
    int c1 = amount;

    printf("1: %d\n", c1);
    printf("5: %d\n", c5);
    printf("20: %d\n", c20);
    printf("50: %d\n", c50);

    // End Block

    return 0;
}