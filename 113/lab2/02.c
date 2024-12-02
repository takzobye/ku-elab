#include <stdio.h>
#include <stdlib.h>

int main()
{
    char stamp_str[3], amount_str[9];
    int stamp = 0, stamp_left = 0;
    float amount = 0.0;

    fgets(stamp_str, 4, stdin);
    fgets(amount_str, 9, stdin);

    stamp = atoi(stamp_str);
    amount = atof(amount_str);

    int discount = 0;

    if (stamp >= 9)
    {
        discount = 40;
        stamp_left = stamp - 9;
    }
    else if (stamp >= 6)
    {
        discount = 30;
        stamp_left = stamp - 6;
    }
    else if (stamp >= 3)
    {
        discount = 20;
        stamp_left = stamp - 3;
    }
    else if (stamp >= 2)
    {
        discount = 15;
        stamp_left = stamp - 2;
    }
    else if (stamp >= 1)
    {
        discount = 10;
        stamp_left = stamp - 1;
    }

    printf("You get %d percents discount.\n", discount);
    printf("Total amount due is %.2f Baht.\n", amount * (1 - (discount / 100.0)));
    printf("And you have %d stickers left.", stamp_left);

    return 0;
}