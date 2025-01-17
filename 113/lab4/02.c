#include <stdio.h>
#include <stdlib.h>

int is_prime(int n)
{
    int count = 0;

    for (int i = 1; i <= n; i++)
    {
        if (n % i == 0)
        {
            count++;
        }
    }

    return count == 2;
}

int main()
{
    char input[5];
    fgets(input, 5, stdin);

    int i, n;

    n = atoi(input);

    for (i = 2; i <= n; i++)
    {
        if (is_prime(i))
        {
            printf("%d is a prime number.\n", i);
        }
    }

    return 0;
}