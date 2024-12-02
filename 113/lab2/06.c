#include <stdio.h>
#include <stdlib.h>

int main() {
    int ch = getchar();

    if (ch >= 48 && ch <= 57) {
        printf("Output: digit");
    } else if (ch >= 65 && ch <= 90) {
        printf("Output: upper case ");
    } else if (ch >= 97 && ch <= 122) {
        printf("Output: lower case ");
    } else {
        printf("Output: others");
    }

    return 0;
}