#include <stdio.h>

int main()
{
    int i, a[5], b[5], c[10];
    printf("Enter array a: \n");
    for (int i = 0; i < sizeof(a) / sizeof(int); i++)
    {
        printf("Please enter an integer: ");
        scanf("%d", &a[i]);
        c[i] = a[i];
    }

    printf("Enter array b: \n");
    for (int i = 0; i < sizeof(b) / sizeof(int); i++)
    {
        printf("Please enter an integer: ");
        scanf("%d", &b[i]);
        c[5 + i] = b[i];
    }

    printf("Array c: ");
    for (i = 0; i < 10; i++)
        printf("%d ", c[i]);

    printf("\n");
    return 0;
}