#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main()
{
    char pizza_size_str[3], is_add_pepperoni_str[3], is_add_cheese_str[3], is_add_mushroom_str[3];
    int pizza_size = 1;
    int is_add_pepperoni = 0;
    int is_add_cheese = 0;
    int is_add_mushroom = 0;

    int diameter = 10;
    float extra_cost = 0;

    printf("Welcome to My Pizza Shop!!\n");
    printf("~~~~~~~~~~~~~~~~~~~~~~~~~~\n");
    printf("Enter pizza size (1=s, 2=m, or 3=l): ");
    fgets(pizza_size_str, 3, stdin);
    pizza_size = atoi(pizza_size_str);
    printf("Extra pepperoni? (1=yes, 0=no): ");
    fgets(is_add_pepperoni_str, 3, stdin);
    is_add_pepperoni = atoi(is_add_pepperoni_str);
    printf("Extra cheese? (1=yes, 0=no): ");
    fgets(is_add_cheese_str, 3, stdin);
    is_add_cheese = atoi(is_add_cheese_str);
    printf("Extra mushroom? (1=yes, 0=no): ");
    fgets(is_add_mushroom_str, 3, stdin);
    is_add_mushroom = atoi(is_add_mushroom_str);
    printf("~~~~~~~~~~~~~~~~~~~~~~~~~~\n");

    if (pizza_size == 1)
    {
        diameter = 10;
    }
    else if (pizza_size == 2)
    {
        diameter = 16;
    }
    else if (pizza_size == 3)
    {
        diameter = 20;
    }

    if (is_add_pepperoni == 1)
    {
        extra_cost += 0.5;
    }

    if (is_add_cheese == 1)
    {
        extra_cost += 0.25;
    }

    if (is_add_mushroom == 1)
    {
        extra_cost += 0.3;
    }

    float area = M_PI * ((diameter * diameter) / 4);
    float cost = 5 + (2 * area) + (extra_cost * area);
    float price = 1.5 * cost;

    printf("Your order costs %.2f baht.\n", price);
    printf("Thank you.");

    return 0;
}