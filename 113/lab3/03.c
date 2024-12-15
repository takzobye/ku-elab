#include <stdio.h>
#include <stdlib.h>

int gcd(int m, int n)
{
    if (m % n == 0)
    {
        return n;
    }

    return gcd(n, m % n);
}

int main()
{
    char a_str[8], b_str[8];
    int a, b;

    fgets(a_str, 8, stdin);
    fgets(b_str, 8, stdin);

    a = atoi(a_str);
    b = atoi(b_str);

    int gcd_result = gcd(a, b);

    a = a / gcd_result;
    b = b / gcd_result;

    if (b == 1)
    {
        printf("= %d", a);
    }
    else
    {
        printf("= %d/%d", a, b);
    }

    return 0;
}