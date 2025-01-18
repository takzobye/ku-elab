#include <stdio.h>

int remove_vowel(char *str) {
    char vowels[] = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'};

    for (int i = 0; str[i] != '\0'; i++) {
        char ch = str[i];

        int vowel_index = -1;

        for (int j = 0; j < 10; j++) {
            char vowel = vowels[j];

            if (vowel == ch) {  
                vowel_index = i;
                break;
            }
        }

        if (vowel_index != -1) {
            for (int j = vowel_index; str[j] != '\0'; j++) {
                str[j] = str[j + 1];
            }

            i--; // this line help to solve when vowels tid gun
        }
    }

    return 0;
}

int main() {
    char str[80];

    printf(" Input: ");
    fgets(str, 80, stdin);

    remove_vowel(str);
    printf("Output: %s\n", str);

    return 0;
}