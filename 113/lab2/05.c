#include <stdio.h>
#include <stdlib.h>

int main() {
    char side_a_str[3], side_b_str[3], side_c_str[3];
    int side_a, side_b, side_c;

    fgets(side_a_str, 3, stdin);
    fgets(side_b_str, 3, stdin);
    fgets(side_c_str, 3, stdin);

    printf("Enter length of side A: ");
    side_a = atoi(side_a_str);
    printf("Enter length of side B: ");
    side_b = atoi(side_b_str);
    printf("Enter length of side C: ");
    side_c = atoi(side_c_str);

    if ((side_a + side_b) <= side_c || (side_b + side_c) <= side_a || (side_c + side_a) <= side_b) {
        printf("Triangle type is invalid.");
    } else if (side_a <= 0 ||side_b <= 0 || side_b <= 0) {
        printf("Triangle type is invalid.");
    } else if (side_a == side_b && side_b == side_c) {
        printf("Triangle type is equilateral.");
    } else if (side_a == side_b || side_b == side_c || side_c == side_a) {
        printf("Triangle type is isosceles.");
    } else if (side_a != side_b && side_b != side_c) {
        printf("Triangle type is scalene.");
    }

    return 0;
}