#include <stdio.h>
#include <stdlib.h>

int main() {
    char money_str[10];
    float money = 0;

    fgets(money_str, 10, stdin);
    money = atof(money_str);

    float tax = 0;

    if (money < 0) {
        printf("Error: Salary must be greater or equal to 0");
    } else {
        if (money > 300000) {
            tax += 15000;
            money -= 300000;
            tax += money * 0.1;
        } else {
            tax = money * 0.05;
        }

        printf("%.2f", tax);
    }

    return 0;
}