#include <stdio.h>
#include <stdlib.h>

long long gcd(long long m, long long n)
{
    if (m % n == 0)
    {
        return n;
    }

    return gcd(n, m % n);
}

long long lcm(long long m, long long n)
{
    return (m * n) / gcd(m, n);
}

int main()
{
    char m_str[50], n_str[50];
    long long m, n;

    fgets(m_str, 50, stdin);
    fgets(n_str, 50, stdin);

    m = atoi(m_str);
    n = atoi(n_str);

    if (m < n)
    {
        int t = m;
        m = n;
        n = t;
    }

    printf("GCD: %lld\n", gcd(m, n));
    printf("LCM: %lld", lcm(m, n));

    return 0;
}