#include <stdio.h>
#include <stdlib.h>

int main()
{
    char goal_amount_str[100];

    printf("Enter your goal amount: ");
    fgets(goal_amount_str, sizeof(goal_amount_str), stdin);

    int day_count = 0;
    float current_amount = 0;
    float goal_amount = atof(goal_amount_str);

    while (goal_amount > 0)
    {
        char collected_amount_str[100];

        printf("Enter money collected today: ");
        fgets(collected_amount_str, sizeof(collected_amount_str), stdin);

        float collected_amount = atof(collected_amount_str);

        current_amount += collected_amount;
        goal_amount -= collected_amount;
        day_count++;

        if (goal_amount > 0)
        {
            printf("Total money collected up to day %d is %.2f. You need %.2f more.\n", day_count, current_amount, goal_amount);
        }
    }

    printf("Congratulations! You take %d %s to reach your goal.", day_count, day_count == 1 ? "day" : "days");

    return 0;
}