#include <stdio.h>

int main() {
    int n;
    int is_found = 0;

    scanf("%d", & n);

    for (int a = 1; a < (n / 3); a++) {
        for (int b = a + 1; b < (n / 2); b++) {
            int c = n - a - b;

            if ( (a * a + b * b == c * c) && (a < b && b < c) ) {
                printf("(%d, %d, %d)", a, b, c);
                
                is_found = 1;
                break;
            }
        }
    }

    if (!is_found) printf("No triple found.\n");

    return 0;
}