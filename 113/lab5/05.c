#include <stdio.h>

int main()
{
    int n = 0;

    printf("Enter n: ");
    scanf("%d", &n);

    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= i; j++)
        {
            if (j % 2 == 0)
            {
                printf("x");
            }
            else
            {
                printf("-");
            }
        }

        printf("\n");
    }

    if (n > 1)
    {
        for (int i = (n - 1); i >= 1; i--)
        {
            for (int j = 1; j <= i; j++)
            {
                if (j % 2 == 0)
                {
                    printf("x");
                }
                else
                {
                    printf("-");
                }
            }

            printf("\n");
        }
    }

    return 0;
}