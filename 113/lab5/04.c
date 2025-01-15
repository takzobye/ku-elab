#include <stdio.h>

int main()
{
    int n = 0;
    double result = 4;

    printf("Enter n: ");
    scanf("%d", &n);

    if (n > 1)
    {
        for (int i = 1; i < n; i++)
        {
            if (i % 2 == 0)
            {
                result += (4.0 / (i * 2 + 1));
            }
            else
            {
                result -= (4.0 / (i * 2 + 1));
            }
        }
    }

    printf("%.10f", result);

    return 0;
}