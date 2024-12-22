#include <stdio.h>
#include <stdlib.h>

void get_binary(int num)
{
    if (num <= 0)
    {
        return;
    }

    get_binary(num / 2);
    printf("%d", num % 2);
}

int main()
{
    char num_str[100];
    fgets(num_str, sizeof(num_str), stdin);

    int num = atoi(num_str);

    if (num == 0)
    {
        printf("0");
    }
    else
    {
        get_binary(num);
    }

    return 0;
}
