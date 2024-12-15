#include <stdio.h>
#include <stdlib.h>

int main()
{
    char n_str[4];
    int n;

    fgets(n_str, 4, stdin);
    n = atoi(n_str);

    if (n <= 0 || n > 26)
    {
        printf("-");
    }
    else
    {
        for (int i = 96 + n; i >= 97; i--)
        {
            if (i == 97)
            {
                printf("%c", i);
                continue;
            }
            printf("%c-", i);
        }
        for (int i = 98; i < 97 + n; i++)
        {
            printf("-%c", i);
        }
    }

    return 0;
}