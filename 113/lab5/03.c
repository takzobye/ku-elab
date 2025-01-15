// 03
#include <stdio.h>
#include <stdlib.h>

void shift_left(char str[], int n);

int main()
{
    char str[80], *c;
    int n;

    printf("String: ");
    fgets(str, sizeof(str), stdin);
    for (c = str; *c && *c != '\n'; c++)
        ;
    *c = 0;
    printf("     n: ");
    scanf("%d", &n);
    shift_left(str, n);
    printf("Output: >>%s<<\n", str);
    return 0;
}

// ส่งเฉพาะ implementation ของฟังก์ชัน shift_left
void shift_left(char target_str[], int n)
{
    int l = 0, j = 0, k = 0;
    while (target_str[l] != '\0')
    {

        l++;
    }

    if (l == 0)
    {

        return;
    }

    char temp_str[l];

    for (int i = 0, k = 0; k < n % l; i++)
    {
        temp_str[i] = target_str[i];
        k++;
    }
    for (int i = n % l, j = 0; k < l; i++)
    {
        target_str[j] = target_str[i];
        j++;
        k++;
    }
    for (int i = l - n % l, k = 0; k < n % l; i++)
    {
        target_str[i] = temp_str[k];
        k++;
    }
}