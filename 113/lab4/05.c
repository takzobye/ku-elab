#include <stdio.h>
#include <stdlib.h>

int main()
{
    char size_str[100];
    fgets(size_str, sizeof(size_str), stdin);

    int n = atoi(size_str);

    if (n <= 0 || n > 26)
    {
        printf("-");
        return 0;
    }

    char target_char = 'a' + n - 1;
    int dash_length = (n - 1) * 2;
    int line = 0;

    for (int i = 0; i < n * 2 - 1; i++)
    {
        for (int j = 0; j < dash_length; j++)
        {
            printf("-");
        }

        if (line == 0)
        {
            printf("%c", target_char);
        }
        else
        {
            for (int j = 0; j < line; j++)
            {
                printf("%c-", target_char - j);
            }

            for (int j = line; j >= 0; j--)
            {
                if (j == 0)
                {
                    printf("%c", target_char - j);
                }
                else
                {
                    printf("%c-", target_char - j);
                }
            }
        }

        for (int j = 0; j < dash_length; j++)
        {
            printf("-");
        }

        if (i < n - 1)
        {
            dash_length -= 2;
            line++;
        }
        else
        {
            dash_length += 2;
            line--;
        }

        printf("\n");
    }

    return 0;
}