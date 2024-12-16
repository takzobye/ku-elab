#include <stdio.h>
#include <stdlib.h>

int main() {
    char num_str[4];
    int num;
    fgets(num_str, 4, stdin);

    num = atoi(num_str);

    int d0 = num & 1;
    int d1 = num >> 1 & 1;
    int d2 = num >> 2 & 1;
    int d3 = num >> 3 & 1;

    printf("Binary number of %d is %d%d%d%d.", num, d3, d2, d1, d0);

    return 0;
}