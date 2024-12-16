#include <stdio.h>
#include <stdlib.h>

int main()
{
    char x_str[5], y_str[5];
    int x, y;

    fgets(x_str, 5, stdin);
    fgets(y_str, 5, stdin);

    x = atoi(x_str);
    y = atoi(y_str);

    for (int i = 0; i < y; i++)
    {
        for (int j = 0; j < x; j++)
        {
            // Start line and end line
            if (i == 0 || i == (y - 1))
            {
                printf("*");
            }
            else
            {
                printf("%s", (j == 0 || j == (x - 1)) ? "*" : " ");
            }
        }
        if (i != (y - 1))
        {
            printf("\n");
            for (int n = 0; n <= i; n++)
            {
                printf(" ");
            }
        }
    }
}