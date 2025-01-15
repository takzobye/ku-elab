#include <stdio.h>
#include <math.h>

int is_automorphic(int n1)
{
    long long n2 = powl(n1, 2);

    while (n1 > 0)
    {
        if (n1 % 10 != n2 % 10)
        {
            return 0;
        }

        n1 /= 10;
        n2 /= 10;
    }

    return 1;
}

int main()
{
    int n = 0;

    printf("Input n = ");
    scanf("%d", &n);

    long long npown = powl(n, 2);

    printf("n^2 = %lld\n", npown);

    if (is_automorphic(n))
    {
        printf("Yes. %d is automorphic number.\n", n);
    }
    else
    {
        printf("No. %d is not automorphic number.\n", n);
    }

    return 0;
}