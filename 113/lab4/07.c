#include <stdio.h>
#include <stdlib.h>

int main()
{
    char count_str[5];

    fgets(count_str, sizeof(count_str), stdin);

    int count = atoi(count_str);

    for (int i = 1; i <= count; i++)
    {
        for (int j = 1; j <= i; j++)
        {
            printf("*");
        }
        printf("\n");
    }

    for (int i = (count - 1); i >= 1; i--)
    {
        for (int j = 1; j <= i; j++)
        {
            printf("*");
        }
        printf("\n");
    }

    return 0;
}