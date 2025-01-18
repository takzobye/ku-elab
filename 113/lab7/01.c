#include <stdio.h>

int main() {
    char str[1000];

    char vowels[] = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'};
    int vowels_count = 0;

    printf("String (without a space): ");
    scanf("%s", &str);

    for (int i = 0; str[i] != '\0'; i++) {
        char ch = str[i];

        for (int j = 0; j < 10; j++) {
            char vowel = vowels[j];

            if (vowel == ch) {
                printf("%c ", ch);
                vowels_count++;
            }
        };
    }

    if (vowels_count <= 1) {
        printf("\nThis string contains %d vowel.", vowels_count);
    } else {
        printf("\nThis string contains %d vowels.", vowels_count);
    }

    return 0;
}