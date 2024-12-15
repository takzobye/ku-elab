#include <stdio.h>
#include <stdlib.h>

int main() {
    char count_str[4];
    int count;

    fgets(count_str, 4, stdin);
    count = atoi(count_str);

    for (int i = count; i >= 0; i--) {
        printf("%d\n", i);
    }

    return 0;
}